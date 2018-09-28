from flask import jsonify
from flask import request
from todo import app
from todo import Db as db
import json
from todo import models
from models import Model


@app.route('/users', methods=['POST'])
def post_tasks():
    Name = request.form["Name"]
    Height = int(request.form["Height"])
    Weight = int(request.form["Weight"])
    Age = int(request.form["Age"])
    Gender = request.form["Gender"]

    user = { "Name": Name,
    "Height": Height,
    "Weight": Weight,
    "Age": Age,
    "Gender":Gender 
    }

    return jsonify(user)

@app.route('/users', methods=['GET'])
def get_users_name():
    Name = request.args.get("Name")
    return jsonify(db.get_user_info_by_name(Name))

@app.route('/users', methods=['DELETE'])
def delete_task():
    Name = request.args.get("Name")
    db.delete_task(Name)
    return jsonify("success")

@app.route('/routines', methods=['GET'])
def get_all_routines():
    db.set_up_routines()
    return jsonify(db.get_list_of_routines())