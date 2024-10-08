import random

from flask import Flask, jsonify, redirect
from flask_cors import CORS

import main
import root

app = Flask("__name__")
CORS(app)

debug = True
if debug:
    import engine

    engine.run()


@app.route("/")
def index():
    return redirect("https://jerit.herokuapp.com")


@app.route("/api/<string:bot>/<string:user>/<string:intents>", methods=["GET"])
def bot(bot, user, intents):
    intents = str(intents).replace(bot, root.bot)
    op = main.run(intents)
    if type(op) == list:
        op = random.choice(op)
    op = op.replace(root.bot, bot)
    op = op.replace(root.name, user)
    response = jsonify(op.upper())
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response


if __name__ == "__main__":
    app.run(host="172.20.7.197", port=8000, debug=debug)
