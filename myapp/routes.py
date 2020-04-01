from flask import render_template
from myapp import app
import requests

@app.route("/")
def index():
	url = "https://covid-19-data.p.rapidapi.com/country/all?format=undefined"

	querystring = {"format":"undefined"}

	headers = {
	    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
	    'x-rapidapi-key': ""
	    }

	response = requests.request("GET", url, headers=headers, params=querystring)

	return render_template("index.html", data=response.json())
