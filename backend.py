import sqlite3
def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TAbLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title text,author text,year INTEGER,isbn INTEGER)")
    conn.commit()
    conn.close()
def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES(NUll,?,?,?,?)",(title,author,year,isbn))
    conn.commit()
    conn.close()
def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(title="",author="",year="",isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? or isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()
    return rows
def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book where id=?",(id,))
    conn.commit()
    conn.close()
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?,author=?,year=?,isbn=? where id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()
connect()
# print(view())
