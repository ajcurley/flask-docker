import random

from flask import Flask, request


app = Flask(__name__)


@app.route("/status", methods=["GET"])
def status():
    """Return the status/healthcheck response"""
    return {"status": "ok"}


@app.route("/randomize", methods=["GET"])
def randomize():
    """Return a randomized integer value (default between 0 and 100)"""
    lower = request.args.get("lower", 0)
    upper = request.args.get("upper", 100)

    try:
        lower = int(lower)
    except ValueError:
        return {"detail": "'lower' must be an integer"}, 400

    try:
        upper = int(upper)
    except ValueError:
        return {"detail": "'upper' must be an integer"}, 400

    if upper < lower:
        return {"detail": "'upper' must be greater than or equal to 'lower'"}, 400

    return {"detail": random.randint(lower, upper)}
