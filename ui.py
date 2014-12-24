#!/usr/bin/env python

import pymongo
from pymongo import MongoClient

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    client = MongoClient()
    db = client.dyna_database
    clc = db.snippets_collection

    snippets = [snippet for snippet in clc.find()]

    """
    for id in db_res.keys():
        all_res += [{"score" : db_res[id]["score"],
                     "source": "Snipbase",
                     "snippet": db_res[id]["payload"]["snippet"],
                     "title": db_res[id]["payload"]["title"]}]
    """

    return render_template('index.html', snippets=snippets)

if __name__ == "__main__":
    app.run(debug=True)