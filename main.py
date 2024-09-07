import playwright.sync_api
import requests
import flask
import json
import time
import os

def setup_solver(): #please body dont sue me
    if not os.path.exists("utils"): os.mkdir("utils")
    files = ["https://raw.githubusercontent.com/Body-Alhoha/turnaround/main/utils/solver.py", "https://raw.githubusercontent.com/Body-Alhoha/turnaround/main/utils/page.html"]
    for file in files:
        r = requests.get(file).text
        with open("utils/" + file.split("/")[-1], "w") as f:
            f.write(r)

setup_solver()
app = flask.Flask(__name__)
from utils import solver

@app.route("/")
def index():
    return flask.redirect("https://github.com/Euro-pol/turnaround-api")

@app.route("/solve", methods=["POST"])
def solve():
    json_data = flask.request.json
    sitekey = json_data["sitekey"]
    invisible = json_data["invisible"]
    url = json_data["url"]
    proxy = json_data.get('proxy')
    with playwright.sync_api.sync_playwright() as p:
        s = solver.Solver(p, proxy = proxy, headless=True)
        start_time = time.time()
        print('Solving captcha with proxy: ' + str(proxy))
        token = s.solve(url, sitekey, invisible)
        print(f"took {time.time() - start_time} seconds :: " + token[:10])
        s.terminate()
        return make_response(token)

def make_response(captcha_key):
    if captcha_key == "failed":
        return flask.jsonify({"status": "error", "token": None})
    return flask.jsonify({"status": "success", "token": captcha_key})

if __name__ == "__main__":
    app.run()
