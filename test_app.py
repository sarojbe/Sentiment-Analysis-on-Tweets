from flask import Flask, render_template, url_for
import nlp_controller

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("base.html", title="home")


@app.route("/about")
def about():
    return render_template("base.html", title="about")


@app.route("/analyzer")
def analyzer():
    filterdata = nlp_controller.sampleDataParse()
    return render_template("parsed_data.html", filterdata=filterdata)


if __name__ == "__main__":
    app.run()
