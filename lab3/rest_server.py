from bottle import run, request, response, get, post
import sqlite3
import hashlib
import lab3

PORT = 7007
db = sqlite3.connect('movies.sqlite')

@get('/ping')
def ping():
    return 'pong'

@post('/reset')
def reset():
    c = db.cursor()
    try:
        c.execute('DELETE FROM theaters')
        c.execute('DELETE FROM users')
        c.execute('DELETE FROM performances')
        c.execute('DELETE FROM ticket')
        c.execute('DELETE FROM movies')
        db.commit()

        #Def values
        theaters_init = [("Kino", 10), ("Regal", 16), ("Skandia", 100)]
        c.executemany("INSERT INTO theaters (theater, capacity) VALUES (?, ?)", theaters_init)

        db.commit()
        response.status = 201 
        return {'message': 'Theaters added successfully'}

    except sqlite3.Error as e:
            response.status = 500
            return f"{str(e)}"

@post('/users')
def post_user():
    user = request.json
    c = db.cursor()
    try:
        c.execute(
            """
            INSERT
            INTO   users(username, fullName, pwd)
            VALUES (?,?,?)
            RETURNING  username
            """,
            [user['username'], user['fullName'], user['pwd']]
        )
        found = c.fetchone()
        if not found:
            response.status = 400
            return "Illegal..."
        else:
            db.commit()
            response.status = 201
            username, = found
            return f"/users/{username}"
    except sqlite3.IntegrityError:
        response.status = 409
        return "Username already in use"
    
@post('/movies')
def post_movies():
    movie = request.json
    c = db.cursor()
    try:
        c.execute(
            """
            INSERT
            INTO   movies(imdbKey, title, year)
            VALUES (?,?,?)
            RETURNING  imdbKey
            """,
            [movie['imdbKey'], movie['title'], movie['year']]
        )
        found = c.fetchone()
        db.commit()
        response.status = 201
        imdbKey, = found
        return f"/movies/{imdbKey}"
    except sqlite3.IntegrityError:
        response.status = 400
        return ""
    
@post('/performances')
def post_performances():
    performance = request.json
    c = db.cursor()
    try:
        c.execute(
            """
            INSERT
            INTO   performances(imdbKey, theater, date, time)
            VALUES (?,?,?,?)
            RETURNING  screeningID
            """,
            [performance['imdbKey'], performance['theater'], performance['date'], performance['time']]
        )
        found = c.fetchone()
        db.commit()
        response.status = 201
        screeningID, = found
        return f"/performances/{screeningID}"
    except sqlite3.IntegrityError:
        response.status = 400
        return ""
    
@get('/movies')
def get_movies():
    c = db.cursor()
    return

# @get('/students')
# def get_students():
#     c = db.cursor()
#     c.execute(
#         """
#         SELECT   s_id, s_name, gpa
#         FROM     students
#         """
#     )
#     response.status = 200
#     found = [{"id": id,
#               "name": name,
#               "gpa": grade} for id, name, grade in c]
#     return {"data": found}

if __name__ == '__main__':
    run(host='localhost', port=7007)
