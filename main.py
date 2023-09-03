import os
import time

import playwright.sync_api
import requests
from flask import Flask, jsonify, redirect, request

from utils.utils import solver

app = Flask(__name__)


@app.route("/")
def index():
    return redirect("https://github.com/Euro-pol/turnaround-api")


@app.route("/solve", methods=["POST"])
def solve():
    json_data = request.json
    sitekey = json_data.get("sitekey")
    invisible = json_data.get("invisible")
    url = json_data.get("url")

    if not all([sitekey, invisible, url]):
        return make_response("error", None)

    with playwright.sync_api.sync_playwright() as p:
        s = solver.Solver(p)
        # start_time = time.time()
        token = s.solve(url, sitekey, invisible)
        # print(f"took {time.time() - start_time} seconds")
        return make_response("success", token)


def make_response(status, token):
    if status == "error" or token == "failed":
        return jsonify({"status": "error", "token": None})
    return jsonify({"status": "success", "token": token})


if __name__ == "__main__":
    app.run()
