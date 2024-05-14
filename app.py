from flask import Flask,render_template,request,session
import sqlite3
import mysql.connector
from twilio.rest import Client
from flask import Flask
app=Flask(__name__) 
app.secret_key = 'your_secret_key' 

sid='ACb5cb03da62fc5ce8b488cd437d3e6e38'
token="61e565ee6b10513c9de53660d967017e"
mynum="+15097742361"
tonum='+919392475539'

    
@app.route('/')
def logo():
    return render_template('logo.html')
@app.route('/home')
def home():
    
    return render_template('home.html')
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
       Username=request.form["un"]
       Password=request.form["pwd"]
       print(Username)
       print(Password)
       conn=create_connection()
       cur=conn.cursor()
       cur.execute('''SELECT * FROM users WHERE Username= ? AND Password= ?''',(Username,Password))
       data= cur.fetchall()
       if data:
           session['uname']=Username
           return render_template('home.html')
           
       print(data)

       conn.commit()
       conn.close() 

    return render_template('login.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/home2')
def home2():
    return render_template('home2.html')
@app.route('/destinations')
def destination():
    return render_template('destinations.html')
@app.route('/temples',methods=['GET','POST'])
def temple():

    if request.method=='POST':

        id=request.form['imgname']
        
        print(id)
        uid=session['uname']
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO favorite_places4 (user_id, place_name) VALUES (?,?)''',(uid,id))
        conn.commit()
        conn.close()
    return render_template('temples.html')
@app.route('/waterfalls',methods=['GET','POST'])
def water():
    if request.method=='POST':

        id=request.form['imgname']
        
        print(id)
        uid=session['uname']
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO favorite_places4 (user_id, place_name) VALUES (?,?)''',(uid,id))
        conn.commit()
        conn.close()
    return render_template('waterfalls.html')
@app.route('/beaches',methods=['GET','POST'])
def beach():
    if request.method=='POST':

        id=request.form['imgname']
        
        print(id)
        uid=session['uname']
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO favorite_places4 (user_id, place_name) VALUES (?,?)''',(uid,id))
        conn.commit()
        conn.close()
    return render_template('beaches.html')
@app.route('/couplevisit',methods=['GET','POST'])
def couple():
    if request.method=='POST':

        id=request.form['imgname']
        
        print(id)
        uid=session['uname']
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO favorite_places4 (user_id, place_name) VALUES (?,?)''',(uid,id))
        conn.commit()
        conn.close()
        # return render_template('couplevisit.html')
    return render_template('couplevisit.html')
@app.route('/adventures',methods=['GET','POST'])
def adventures():
    if request.method=='POST':

        id=request.form['imgname']
        
        print(id)
        uid=session['uname']
        conn=create_connection()
        conn.cursor().execute('''INSERT INTO favorite_places4 (user_id, place_name) VALUES (?,?)''',(uid,id))
        conn.commit()
        conn.close()
    return render_template('adventures.html')
@app.route('/beachestable')
def beachestab():
    return render_template('beachestable.html')
@app.route('/couplevisittable')
def couplevisittab():
    return render_template('couplevisittable.html')
@app.route('/templestable')
def templestab():
    return render_template('templestable.html')
@app.route('/adventurestable')
def adventurestab():
    return render_template('adventurestable.html')
@app.route('/waterfallstable')
def waterfallstab():
    return render_template('waterfallstable.html')

@app.route('/favourites')
def fav():
    uid=session['uname']
    print(uid,"THIS IS IN FAV")
    conn=create_connection()
    cur=conn.cursor()
    cur.execute('''SELECT * FROM favorite_places4 WHERE user_id =?''',(uid,))
    data= cur.fetchall()
    print(data)
    return render_template('fav.html',data=data)

@app.route('/register',methods=["GET","POST"])
def register():
    if request.method=='POST':
        Username=request.form["un"]
        Password=request.form["pwd"]
        Email=request.form["email"]
        Gender=request.form["Gender"]
        Phone=request.form["phone"]
        print(Username)
        print(Password)
        print(Email) 
        print(Gender)
        print(Phone)
        conn=create_connection()
        conn.cursor().execute(''' INSERT INTO users('Username','Password','Email','Gender','Phone')VALUES(?,?,?,?,?)''',(Username,Password,Email,Gender,Phone))
        conn.commit()
        conn.close()
    return render_template('register.html')

def create_connection():
    conn=sqlite3.connect('database.db') 
    return conn

def create_table():
    conn=create_connection()
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS users (
                          id INT AUTO INCREMENT PRIMARY KEY,
                          Username CHAR NOT NULL UNIQUE,
                          Password TEXT NOT NULL,
                          Email TEXT NOT NULL,
                          Gender TEXT NOT NULL,
                          Phone INT NOT NULL)''')   

    conn.commit()
    conn.close() 


def create_connection():
    conn=sqlite3.connect('database.db') 
    return conn
def create_table():
    conn=create_connection()  
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS favorite_places4 
                          (user_id TEXT UNIQUE,
                          place_name TEXT,
                          FOREIGN KEY(user_id)REFERENCES users(id))''')
    conn.commit()
    conn.close()
    
    client=Client(sid,token)
    message=client.messages.create(
    body="BEST WISHES ON YOUR NEW ADVENTURE",
    from_=mynum,
    to=tonum)


if __name__=='__main__':
    create_table()
    app.run(debug=True)











   

