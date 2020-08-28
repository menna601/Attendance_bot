import datetime
from flask import request
from sqlalchemy import create_engine
import os
db = create_engine(os.getenv('DATABASE_URL'))

def getUsername(user):
    query = "SELECT * FROM enrolled WHERE Username = '{}'".format(user)
    r = db.execute(query,user)
    user = r.fetchone()
    return user

def saveUser(user_id):
    ip = request.remote_addr
    query = "INSERT INTO studentattendance VALUES(%s,%s,%s)"
    db.execute(query, (user_id, datetime.datetime.now(), str(ip)))
    return True

def getPassword(user):
    print("user data " + str(user[1]))
    query = "Select password From enrolled WHERE username = %s"
    r = db.execute(query, (str(user[1]),))
    password = r.fetchone()
    print("bye")
    return password

def getip():
    ip = request.remote_addr
    query = "SELECT username From studentattendance WHERE IP = %s"
    r = db.execute(query, (ip,))
    if r.fetchone() is None:
        return True
    else:
        return False
    
def checkUser(user):
    query = "SELECT * From studentattendance WHERE username = %s"
    r = db.execute(query, (user,))
    if r.fetchone() is None:
        return False
    else:
        return True
