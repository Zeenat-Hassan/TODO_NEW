import mysql.connector
from flask import request
from flask import jsonify


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

    def get_a_todo_by_status(self,status):
        mycursor = self.mydb.cursor(buffered=True)
        sql = "Select text,status FROM Tasks  WHERE status=%s"
        val=(status,)
        mycursor.execute(sql,val)
        self.mydb.commit()
        myresult = mycursor.fetchall()

        for x in myresult:
            print (x)
       # return {"message": "inside put method"}, 200


    def  get_a_todo_by_id(self,id):
        mycursor = self.mydb.cursor(buffered=True)

        sql = "Select text,status FROM Tasks  WHERE id ={}".format(id)
        mycursor.execute(sql)
        self.mydb.commit()
        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
