from flask import Flask, render_template

app = Flask(__name__)

#www.mojastrona.pl/
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/reservation")
def reservation():
    return render_template("reservation.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

#Jinja2

if __name__ == "__main__":
    app.run()