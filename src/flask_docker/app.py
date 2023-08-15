from flask import Flask


app = Flask(__name__)


@app.route("/status")
def status():
    """Return the status/healthcheck response"""
    return {"status": "ok"}
