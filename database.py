import sqlite3

def create_table():
    conn = sqlite3.connect("Students.db")  # To connect with database(if not exists it will create)
    cursor = conn.cursor()  # for interacting with database

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students (
        id TEXT PRIMARY KEY, 
        student_name TEXT,
        father_name TEXT,
        course_name TEXT,
        course_fee TEXT,
        course_duration TEXT,
        admission_date TEXT,
        contact TEXT,
        address TEXT)""")
    conn.commit() # commit the changes to the database
    conn.close() # close the connection


def fetch_students():
    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students") # select all records from the students table
    students = cursor.fetchall() # returns a list of tuples, where each tuple represents a single row
    conn.close()
    return students

def add_students(id, student_name, father_name, course_name, course_fee, course_duration, admission_date, contact, address):
    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (id, student_name, father_name, course_name, course_fee, course_duration, admission_date, contact, address) VALUES (?,?,?,?,?,?,?,?,?)",
                   (id, student_name, father_name, course_name, course_fee, course_duration, admission_date, contact, address))
    conn.commit()
    conn.close()


def delete_students(id):
    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update_students(u_student_name, u_father_name, u_course_name, u_course_fee, u_course_duration, u_admission_date, u_contact, u_address, id):
    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE Students SET student_name=?, father_name=?, course_name=?, course_fee=?, course_duration=?, admission_date=?, contact=?, address=? WHERE id=?",
                   (u_student_name, u_father_name, u_course_name, u_course_fee, u_course_duration, u_admission_date, u_contact, u_address, id))
    conn.commit()
    conn.close()


def id_exists(id):
    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM Students WHERE id=?", (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0  # If count > 0, ID exists, otherwise it doesn't

def search_student(student_id):
    conn = sqlite3.connect("Students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE id=?", (student_id,))
    student_row = cursor.fetchone()
    conn.close()
    return student_row

create_table()
