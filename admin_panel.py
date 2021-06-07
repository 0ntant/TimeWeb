from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

import sqlite3

@app.route('/')
def index():
    con = sqlite3.connect('webdata.sqlite3')
    cur = con.cursor()
    del_id = request.args.get("delete")
    if del_id != None:
        sql_q = f'DELETE FROM data WHERE id = {del_id}'
        cur.execute(sql_q)
        con.commit()    
    sql_q = "SELECT * FROM data"
    cur.execute(sql_q)
    data = cur.fetchall()
    
    cur.close()
    con.close()
    return render_template('index.html', data=data)
 
@app.route('/addForm')
def add_form():
    return render_template('addForm.html')

@app.route('/editForm')
def edit_form():
    edit_id = request.args.get("edit")
    con = sqlite3.connect('webdata.sqlite3')
    cur = con.cursor()
    
    sql_q = f"SELECT * FROM data WHERE id = {edit_id}"
    cur.execute(sql_q)
    data = cur.fetchall()
    
    cur.close()
    con.close()
    return render_template('editForm.html' , data = data)


@app.route('/add', methods=['POST'])
def add_action():
    con = sqlite3.connect('webdata.sqlite3')
    cur = con.cursor()    
   
    post = request.form
    
    sql_q = f'INSERT INTO data (field1, field2, field3 , filed) VALUES ("{request.form.get("field_1")}", "{request.form.get("field_2")}", "{request.form.get("field_3")}","{request.form.get("field_4")}")'
    print(sql_q)
    cur.execute(sql_q)
    con.commit()
    
    sql_q = "SELECT * FROM data"
    cur.execute(sql_q)
    data = cur.fetchall()   
    
    cur.close()
    con.close()
    return render_template('index.html', data = data)
    
@app.route('/edit', methods = ['POST'])
def edit_action():
    id = request.form.get("field_id")
    field_1 = request.form.get("field_1")
    field_3 = request.form.get("field_2")
    field_2 = request.form.get("field_3")
    field_4 = request.form.get("field_4")
    
    con = sqlite3.connect('webdata.sqlite3')
    cur = con.cursor() 
    
    sql_q = f'UPDATE data SET field1 = "{field_1}", field2 = "{field_2}", field3 = "{field_3}", filed = "{field_4}" WHERE id = {id}'
    cur.execute(sql_q)
    con.commit()
    
    sql_q = "SELECT * FROM data"
    cur.execute(sql_q)
    data = cur.fetchall()   
    
    cur.close()
    con.close()
    return render_template('index.html', data = data)
    

app.run()    