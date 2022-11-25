from flask import Blueprint, render_template,jsonify, request
from datetime import datetime

todo_blueprint = Blueprint('todo',__name__)
from .models import Meters, Meter_Data
from meterapp.__init__ import db


@todo_blueprint.route('/meters/',methods=['GET'])
def meter_list():
    meters = Meters.query.all()
    return render_template('meters.html',meters=meters)


@todo_blueprint.route('/meters/<int:id>/',methods=['GET'])
def meter_details(id):
    meters_details = Meter_Data.query.get(id)
    return render_template('meter-details.html',meters=meters_details)
