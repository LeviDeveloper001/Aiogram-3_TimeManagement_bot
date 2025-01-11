from typing import Callable, Any

import sys
import sqlite3 as sq

class Condition:
    def __call__(self, *args, **kwds):
        pass
    
    def as_str(self):
        return ''
    

class ConditionEqualsValues(Condition):
    def __init__(self, **kwds):
        self.values_dict = kwds.copy()
    
    def as_str(self):
        condition_str=''
        for field, value in self.values_dict.items():
            if condition_str: condition_str+=' AND '
            condition_str+=f'"{field}"=="{value}"'
        if condition_str: condition_str="WHERE "+condition_str
        return condition_str
        

class Manager:
    path_to_db=sys.path[0]+'\\db.sqlite3'
    
    def __init__(self):
        pass
    
    def execute_sql(self, sql:str, size:int=None):
        print(sql)
        with sq.connect(self.path_to_db) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            if size:
                if size==1: return cursor.fetchone()
                return cursor.fetchmany(size)
            return cursor.fetchall()
        
    
    
    @staticmethod
    def iter_to_sql_str(tpl:tuple):
        lst = list( map( lambda i: f'"{i}"', tpl ) )
        return ', '.join(lst)
    
    def sql_select(self, table_name, fields:tuple[str]=None, conditions_str:Condition=None, size:int=None):
        if fields!=None:
            fields_str = self.iter_to_sql_str(fields)
        else:
            fields_str = '*'
        
        sql = f"""SELECT {fields_str} FROM {table_name} """
        sql+=conditions_str if conditions_str else ''
        return self.execute_sql(sql, size=size)

    def sql_insert(self, table_name, **data):
        fields, values = data.keys(), data.values()
        sql = f'''
        INSERT INTO {table_name}
        ({self.iter_to_sql_str(fields)}) 
        VALUES({self.iter_to_sql_str(values)})
        RETURNING *
        '''
        return self.execute_sql(sql, 1)
    
    @staticmethod
    def dict_to_sql_set_string(dct:dict):
        sql_lst = []
        for key, value in dct.items():
            sql_lst.append(f'{key}=={value}')
        return ', '.join(sql_lst)
    
    def sql_update(self, table_name:str, condition:Condition, **update_data):
        sql = f"""
UPDATE {table_name}
SET {self.dict_to_sql_set_string(update_data)} 
{condition.as_str()}
RETURNING *"""
        return self.execute_sql(sql, size=1)    
        
    
        
        
    def get(self, table_name, condition:Condition) -> Any:
        return self.sql_select(table_name, conditions_str=condition.as_str(), size=1)
    
    def get_obj_or_none(self, table_name, condition:Condition):
        res = None
        try:
            res = self.get(table_name, condition)
        except:
            pass
        return res
    
    def create_user(self, tg_id:int):
        user = self.sql_insert('users', tg_id=tg_id)
        profile = self.sql_insert('profile', users_id=user[0])
        timer =self.sql_insert('timer', users_id=user[0])
        print(f'{profile=}')
        return self.sql_update('users', ConditionEqualsValues(id=user[0]), profile_id=profile[0])




        

