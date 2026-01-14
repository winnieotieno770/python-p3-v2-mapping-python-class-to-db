from __init__ import CURSOR, CONN


class Department:

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location
    
    @classmethod
    def create(cls,name,location):
        department = cls(name,location)
        department.save()
        return department
    
    def update(self):
        '''update record'''
        sql = '''
            UPDATE departments
            SET name = ? ,location = ?
            WHERE id = ?
        '''
        CURSOR.execute(sql,(self.name, self.location, self.id))
        CONN.commit()

    def delete(self):
        '''delete a record'''
        sql = '''
                DELETE FROM departments
                WHERE id = ?
        '''

        CURSOR.execute(sql, (self.id,))
        CONN.commit()
    
    @classmethod
    def create_table(cls):
      """CREATING A TABLE"""
      sql = """ CREATE TABLE IF NOT EXISTS departments (
         id INTEGER PRIMARY KEY,
         name TEXT, 
         location TEXT
        )
      """
      CURSOR.execute(sql)
      CONN.commit()

    @classmethod
    def drop_table(cls):
        "DELETING A TABLE"
        sql = """
               DROP TABLE IF  EXISTS departments;
               """
        CURSOR.execute(sql)
        CONN.commit()
    
    def save(self):
        '''saving instance/object to a row in our company database'''
        sql ="""
            INSERT INTO departments (name, location) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()
        self.id = CURSOR.lastrowid

    def __repr__(self):
        return f"<Department {self.id}: {self.name}, {self.location}>"
