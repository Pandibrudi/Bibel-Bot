from bible_search import get_bible_results
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__,
            static_url_path='',
            static_folder='static',)

@app.route('/', methods=["POST", "GET"])
def hello(query=""):
    if request.method == "POST":
        query = request.form["query"]
        data = get_bible_results(query)
        print(data)
        
        #checking if in bible at all
        in_bible = False
        for entry in data.keys():
            if data[entry]["no_hits"] > 0:
                in_bible = True

        return render_template("index.html", data=data, query=query, in_bible=in_bible)
    else:
        data={}
        return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run()