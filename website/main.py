from flask import Flask, render_template
import sqlite3
import pathlib

base_path = pathlib.Path().cwd()
db_name = "../database/dealers.db"
db_path = base_path / db_name
table_name = "ford_dealers"

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/data")
def data():
    conn = sqlite3.connect(db_name)
    print(conn)
    cursor = conn.cursor()
    ford_dealers = cursor.execute(f"SELECT * from {table_name}").fetchall()
    print(ford_dealers)
    return render_template("data_table_fillin.html", ford_dealers=ford_dealers)

if __name__ == "__main__":
    app.run(debug=True)