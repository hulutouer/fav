from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('fav.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM favdb')
    rows = cursor.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)


@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    url = request.form['url']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO favdb (name, url) VALUES (?, ?)', (name, url))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})


@app.route('/delete', methods=['POST'])
def delete():
    data_id = request.form['id']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM favdb WHERE id = ?', (data_id,))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(debug=True)
