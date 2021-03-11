import mysql.connector
from flask import request


class DatabaseHelper:

    def __init__(self):

        self.mydb = mysql.connector.connect(host='localhost', user="root", password="123", database="ToDo")




    def add_a_todo(self):
        mycursor = self.mydb.cursor()
        _json = request.get_json()
        _text = _json['text']
        _status = _json['status']

        sql = ' INSERT INTO Tasks (text,status) VALUES (%s, %s)'
        val = (_text, _status)
        mycursor.execute(sql, val)
        self.mydb.commit()


    def get_a_todo(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT text, status FROM Tasks")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)



    def update_a_to_do(self, id):
        _json = request.get_json()
        _text = _json['text']
        _status = _json['status']
        mycursor = self.mydb.cursor()
        sql = 'UPDATE Tasks SET text = %s,status = %s WHERE id ={}'.format(id)
        val = (_text, _status)
        mycursor.execute(sql,val)
        self.mydb.commit()


    def delete_a_to_do(self, id):
        mycursor = self.mydb.cursor()

        sql = "DELETE FROM Tasks  WHERE id ={}".format(id)
        mycursor.execute(sql)
        self.mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")


obj1 = DatabaseHelper()
#obj1.search_a_todo()
#obj1.update_a_to_do(17)
#obj1.add_a_todo()
#obj1.delete_a_to_do(17)
