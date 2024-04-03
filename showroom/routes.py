from flask import Flask, render_template, url_for, request, jsonify, redirect, flash, session
from showroom import app
from showroom.models import Car

@app.route("/", methods=['GET', 'POST'])
def index():
    cars = Car.query.all()
    return render_template('index.html', title='Car Showroom', cars=cars)

@app.route("/car/<int:car_id>")
def car_page(car_id):
    car = Car.query.get_or_404(car_id)
    return render_template('car.html', title=car.name, car=car)