import json
import os.path

from flask import (Flask, abort, flash, jsonify, redirect, render_template,
                   request, session, url_for)
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/")
def home():
    return render_template("home.html", codes=session.keys())

@app.route("/your-url", methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        urls = {}
        if os.path.exists("urls.json"):
            with open("urls.json", 'r') as r_file:
                urls = json.load(r_file)
            
            if request.form["code"] in urls.keys():
                flash("Duplicate!")
                return redirect(url_for("home"))
        # print("\n" * 5, "Req", request.form, "\n" * 5)
        
        if 'url' in request.form.keys():
            urls[request.form["code"]] = {"url": request.form["url"]}
        else:
            f = request.files['file']
            full_name = request.form["code"] + secure_filename(f.filename)
            # print("\n" * 5, full_name, "\n" * 5)
            f.save("/Users/huihu/Documents/Block_Flask/static/user_files/" + full_name)
            urls[request.form["code"]] = {"file": full_name}

        with open("urls.json", 'w') as w_file:
            json.dump(urls, w_file)
            session[request.form["code"]] = True

        return render_template("your_url.html", code=urls[request.form["code"]])
    else:
        return redirect(url_for("home"))

@app.route("/<string:code>")
def redirect_to_url(code):
    urls = {}
    if os.path.exists("urls.json"):
        with open("urls.json", 'r') as r_file:
            urls = json.load(r_file)
        if code in urls.keys():
            if "url" in urls[code].keys():
                return redirect(urls[code]["url"])
            else:
                return redirect(url_for('static', filename="user_files/" + urls[code]["file"]))
        else:
            return abort(404)

        # if code in urls.keys():
        #     flash("Duplicate!")
        #     return redirect(url_for("home"))
    else:
        return abort(404)

@app.errorhandler(404)
def page_not_found(error):
    # print(type(error), error)
    return render_template("page_not_found.html"), 404


@app.route("/api")
def session_api():
    return jsonify(list(session.keys()))
