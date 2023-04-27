from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("controller.html", page="Home")

if __name__ == "__main__":
    app.run()