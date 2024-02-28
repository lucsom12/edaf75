from bottle import Bottle, run, request, response
import sqlite3
import hashlib

app = Bottle()

PORT = 7007
db = sqlite3.connect('lab3.sqlite')

@app.route('/ping', method='GET')
def ping():
    return 'pong'

# def get_db_connection():
#     conn = sqlite3.connect('lab3.sqlite')
#     conn.row_factory = sqlite3.Row
#     return conn

@app.route('/empty', method='DELETE')
def empty_database():
    cursor = db.cursor()
    cursor.execute('DELETE FROM theaters')
    db.commit()
    cursor.close()
    return {'message': 'Database emptied successfully'}

@app.route('/theaters', method='POST')
def add_theaters():
    theaters_data = {"Kino": 10, "Regal": 16, "Skandia": 100}

    cursor = db.cursor()
    
    cursor.execute('DELETE FROM theaters')
    
    for theater, capacity in theaters_data.items():
        cursor.execute('INSERT INTO theaters (name, capacity) VALUES (?, ?)', (theater, capacity))
    
    db.commit()
    cursor.close()
    response.status = 201 
    return {'message': 'Theaters added successfully'}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

@app.route('/users', method='POST')
def create_user():
    user_data = request.json
    
    username = user_data.get('username')
    full_name = user_data.get('fullName')
    password = user_data.get('pwd')

    if not username or not full_name or not password:
        response.status = 400
        return {'message': 'Missing required fields'}
    
    hashed_password = hash_password(password)
    
    cursor = db.cursor()
    
    cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()
    
    if existing_user:
        cursor.close()
        response.status = 400
        return {'message': 'User with this username already exists'}
    
    cursor.execute('INSERT INTO users (username, fullname, pwd) VALUES (?, ?, ?)',
                   (username, full_name, hashed_password))
    db.commit()
    cursor.close()
    
    response.status = 201
    return {'message': f'/users/{username}'}

if __name__ == '__main__':
    # empty_database()
    #add_theaters()
    run(app, host='localhost', port=7007)
