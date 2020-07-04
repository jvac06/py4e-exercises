import json
import sqlite3

conn = sqlite3.connect('coursesDB.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User ( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    name TEXT UNIQUE
);

CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                    title TEXT UNIQUE
);

CREATE TABLE Member (user_id INTEGER,
                    course_id INTEGER,
                    role INTEGER,
                    PRIMARY KEY (user_id, course_id))''')

fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'roster_data.json'

data = open(fname).read()
js = json.loads(data)

for entry in js:
    name = entry[0]
    course = entry[1]
    role = entry[2]

    print(name, course, role)

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (name,))
    cur.execute('SELECT id FROM User WHERE name = ?', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course,))
    cur.execute('SELECT id FROM Course WHERE title = ?', (course,))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, role))

    conn.commit()

cur.close()

