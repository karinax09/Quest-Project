from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/levels")
def levels():
    return render_template("levels.html")


@app.route("/actors")
def actors():
    return render_template("actors.html")






if __name__ == "__main__":
    app.run(debug=True)