""" Specifies routing for the application"""
from flask import render_template, request, jsonify
from app import app
from app import database as db_helper

@app.route("/delete/<Instructor>", methods=['POST'])
def delete(Instructor):
    """ recieved post requests for entry delete """

    try:
        db_helper.delete(Instructor)
        result = {'success': True, 'response': 'Removed Instructor'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/edit/<Instructor>", methods=['POST'])   
def update(Instructor):
    """ recieved post requests for entry updates """
    data = request.get_json()
    try:
        db_helper.update(data['Instructor'], data["Rating"], data['Password'])
        result = {'success': True, 'response': 'Status Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)


@app.route("/insert", methods=['POST'])
def insert():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert(data['Instructor'], data["Rating"], data['Password'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


@app.route("/")
def homepage():
    """ returns rendered homepage """
    items = db_helper.fetch_todo()
    return render_template("index.html", items=items)

@app.route("/search_instructor", methods=['POST','GET'])
def search_instructor():
    data = request.get_json()
    try:
        global items
        items = db_helper.search_instructor(data['Instructor'])
        return render_template("instructor.html", items=items)
    except:
        return render_template("instructor.html", items=items)

@app.route("/search_course", methods=['POST','GET'])
def search_course():
    data = request.get_json()
    try:
        global items
        items = db_helper.search_course(data['Subject'], data['Number'])
        return render_template("course.html", items=items)
    except:
        return render_template("course.html", items=items)

@app.route("/search", methods=['POST','GET'])
def search():
    data = request.get_json()
    global items
    try:
        items = db_helper.search(data['Instructor'])
        return render_template("index.html", items=items)
    except:
        return render_template("index.html", items=items)

@app.route("/search_ge", methods=['POST','GET'])
def search_ge():
    data = request.get_json()
    try:
        global items
        items = db_helper.searchGE(data['ge_type'])
        return render_template("ge.html", items=items)
    except:
        return render_template("ge.html", items=items)