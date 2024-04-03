from flask import Flask, render_template, url_for, request, jsonify, redirect, flash, session
from showroom import app

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html', title='Car Showroom')