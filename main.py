import flask
import requests
import os
import json

app = flask.Flask(__name__)

def download_solver(): #please body dont sue me
    if not os.path.exists("utils"): os.mkdir("utils")
    files = ["https://raw.githubusercontent.com/Body-Alhoha/turnaround/main/utils/solver.py", "https://raw.githubusercontent.com/Body-Alhoha/turnaround/main/utils/page.html"]
    for file in files:
        r = requests.get(file).text
        with open("utils/" + file.split("/")[-1], "w") as f:
            f.write(r)        