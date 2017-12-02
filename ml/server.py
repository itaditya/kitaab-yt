import json
from flask import Flask, redirect, request, render_template, jsonify
from search import search

app = Flask(__name__)



@app.route('/api/search_key', methods=['POST'])
def searchKeyWord():
    
    name = request.form["name"]
    keyword = request.form["keyword"]

    result = search(name, keyword)

    if not result:
        return jsonify(dict())

    return jsonify(timeStamp(result))


def timeStamp(list_time):

    format_time = dict()
    i = 0
    for time in list_time:
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        format_time[str(i)] = {"%dh%02dm%02ds" % (h, m, s): time}
        i += 1
    return format_time


if __name__ == '__main__':
    app.run()
