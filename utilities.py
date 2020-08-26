import mysql.connector as mysql
import datetime
from flask import Flask, request, jsonify

db = mysql.connect(host="localhost", user="root", password="", db="Attendance")

def getUsername(user):
    cursor = db.cursor()
    query = "SELECT * FROM enrolled WHERE Username = '{}'".format(user)
    cursor.execute(query,user)
    user = cursor.fetchone()
    return user

def saveUser(user_id):
    cursor = db.cursor()
    ip = request.remote_addr
    query = "INSERT INTO studentattendance VALUES(%s,%s,%s)"
    cursor.execute(query, (user_id, datetime.datetime.now(), str(ip)))
    db.commit()
    return True

def getPassword(user):
    cursor = db.cursor()
    print("user data " + str(user[1]))
    query = "Select password From enrolled WHERE username = %s"
    cursor.execute(query, (str(user[1]),))
    password = cursor.fetchone()
    print("bye")
    return password

def getip():
    ip = request.remote_addr
    cursor = db.cursor()
    query = "SELECT username From studentattendance WHERE IP = %s"
    cursor.execute(query, (ip,))
    if cursor.fetchone() is None:
        return True
    else:
        return False
    
    
