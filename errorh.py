import flask
from __init__ import app


@app.errorhandler(401)
def page_not_found(e):
    return flask.Response("<p>Sorry,Login failed</p>")


@app.errorhandler(402)
def page_not_found(e):
    return flask.Response("<p>Sorry, Signup failed</p>")


@app.errorhandler(404)
def page_not_found(e):
    return flask.Response("<p>Unable to fulfil search request</p>")
