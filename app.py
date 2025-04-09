from flask import Flask
from flask import render_template

path_of_templates = "/home/ojw/flask/my_web_server/my_web_server/templates"

app = Flask(__name__, template_folder=path_of_templates)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)