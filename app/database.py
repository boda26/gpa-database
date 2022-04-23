"""Defines all the functions related to the database"""
from app import db

def fetch_todo() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Rating limit 20;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "Instructor": result[0],
            "Rating": result[1],
            "Tag": result[2]
        }
        todo_list.append(item)
    
    return todo_list


def update(instructor_name, rating, pwd):
    if pwd != "root":
        return False
    conn = db.connect()
    query = 'Update Rating set Rating = {} where Instructor = "{}";'.format(rating, instructor_name)
    conn.execute(query)
    conn.close()
    return True


def insert(instructor_name, rating,pwd):
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """
    if pwd != "root":
        return False
    conn = db.connect()
    query = 'Insert Ignore Into Rating VALUES ("{}", {}, "placeholder");'.format(
        instructor_name, rating)
    conn.execute(query)
    conn.close()
    return True


def delete(instructor_name):
    """ remove entries based on task ID """
    conn = db.connect()
    query = 'Delete From Rating where Instructor= "{}";'.format(instructor_name)
    conn.execute(query)
    conn.close()

def search_course(Subject, Number):
    conn = db.connect()
    query = """
    SELECT c.Instructor, ROUND((SUM(c.A_plus)*4 + SUM(A)*4 + SUM(A_minus) * 3.67 + 
    SUM(B_plus) * 3.33 + SUM(B) * 3 + SUM(B_minus) * 2.67 + 
    SUM(C_plus) * 2.33 + SUM(C) * 2 + SUM(C_minus) * 1.67 +
    SUM(D_plus) * 1.33 + SUM(D) * 1 + SUM(D_minus) * 0.67) / 
    (SUM(c.A_plus) + SUM(A) + SUM(A_minus) + 
    SUM(B_plus) + SUM(B) + SUM(B_minus) + 
    SUM(C_plus) + SUM(C) + SUM(C_minus) +
    SUM(D_plus) + SUM(D) + SUM(D_minus) +SUM(F)),3) AS avg_gpa, R.Rating
    FROM Course c NATURAL JOIN Rating R
    WHERE c.Subject = "{}" AND c.Number = "{}"
    GROUP BY c.Instructor
    ORDER BY avg_gpa DESC, R.Rating DESC;
    """.format(Subject, Number)
    query_results = conn.execute(query).fetchall()

    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "Instructor": result[0],
            "AVG_GPA": result[1],
            "Rating":result[2]
        }
        todo_list.append(item)
    
    return todo_list

def search_instructor(instructor_name):
    conn = db.connect()
    query = """
    SELECT c.Subject, c.Number, ROUND((SUM(c.A_plus)*4 + SUM(A)*4 + SUM(A_minus) * 3.67 + 
    SUM(B_plus) * 3.33 + SUM(B) * 3 + SUM(B_minus) * 2.67 + 
    SUM(C_plus) * 2.33 + SUM(C) * 2 + SUM(C_minus) * 1.67 +
    SUM(D_plus) * 1.33 + SUM(D) * 1 + SUM(D_minus) * 0.67) / 
    (SUM(c.A_plus) + SUM(A) + SUM(A_minus) + 
    SUM(B_plus) + SUM(B) + SUM(B_minus) + 
    SUM(C_plus) + SUM(C) + SUM(C_minus) +
    SUM(D_plus) + SUM(D) + SUM(D_minus) +SUM(F)),3) AS avg_gpa,left(d.Description,40) AS Description, d.CreditHours
    FROM Course c 
        JOIN Description d USING (Title)
    WHERE c.Instructor = "{}"
    GROUP BY c.Instructor, c.Subject, c.Number, d.Title
    ORDER BY avg_gpa;
    """.format(instructor_name)

    query_results = conn.execute(query).fetchall()

    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "Subject": result[0],
            "Number": str(result[1]),
            "AVG_GPA":str(result[2]),
            "Description":result[3],
            "Credit":str(result[4])
        }
        todo_list.append(item)
    
    return todo_list

def search(Instructor):
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query = 'Select * from Rating where Instructor LIKE "%%{}%%";'.format(Instructor)
    query_results = conn.execute(query).fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "Instructor": result[0],
            "Rating": result[1]
        }
        todo_list.append(item)
    
    return todo_list

def searchGE(ge_type):
    conn = db.connect()
    query = 'CALL result("{}");'.format(ge_type)

    query_results = conn.execute(query).fetchall()

    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "Subject": result[0],
            "Number": str(result[1]),
            "AVG_GPA":str(result[2]),
            "AVG_GRADE": str(result[3]),
            "Description":result[4],
            "Credit":str(result[5])
        }
        todo_list.append(item)
    
    return todo_list
