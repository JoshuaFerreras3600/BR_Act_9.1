from flask import Flask, render_template
from requests import get
import ipaddress



app = Flask(__name__)
user = input("Enter your ip address: ")
loc = get(f'https://ipapi.co/{user}/json/')


print(loc)


# @app.route('/')
# def getipv4IP():
# return loc.json()

@app.route("/")
def main():
    return loc.json()

app.run('127.0.0.1', port = 5500)