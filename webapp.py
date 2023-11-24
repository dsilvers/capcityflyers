from flask import Flask
from flask import render_template, make_response, url_for, redirect, request

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/membership/")
def membership():
    return render_template('membership.html')

@app.route("/n271rg/")
def n271rg():
    return render_template('n271rg.html')

@app.route("/n569ds/")
def n569ds():
    return render_template('n569ds.html')

@app.route("/n8113b/")
def n8113b():
    return render_template('n8113b.html')


@app.route('/robots.txt')
def robotstxt():
    response = make_response(render_template("robots.txt"))
    response.headers['Content-Type'] = 'text/plain'
    return response


@app.route("/sitemap.xml")
def sitemap_xml():
    response = make_response(render_template("sitemap.xml"))
    response.headers['Content-Type'] = 'application/xml'
    return response