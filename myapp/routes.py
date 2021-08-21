from flask import render_template, jsonify
from myapp import app
import json
from .scraper import scrape_all
import requests

@app.route("/")
def index():
	data = scrape_all()
	return render_template("index.html", data=data)


