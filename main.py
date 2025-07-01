import os
from bible_search import get_bible_results
from flask import Flask, render_template, redirect, request, url_for

BIBLE_FOLDER = os.path.join(os.getcwd(), "source")

app = Flask(__name__,
            static_url_path='',
            static_folder='static',)

def get_bible_versions():
    versions = []
    for filename in os.listdir(BIBLE_FOLDER):
        if filename.endswith(".xml"):
            version_name = os.path.splitext(filename)[0]
            versions.append(version_name)
    return versions

@app.route('/', methods=["POST", "GET"])
def hello(query=""):
    bible_versions = get_bible_versions()

    if request.method == "POST":
        query = request.form["query"]
        bible_version = request.form["bible"]
        data = get_bible_results(query, bible_version)

        in_bible = any(info["no_hits"] > 0 for info in data.values())
        return render_template("index.html", data=data, query=query, in_bible=in_bible, versions=bible_versions)
    else:
        return render_template("index.html", data={}, versions=bible_versions)

if __name__ == "__main__":
    app.run()