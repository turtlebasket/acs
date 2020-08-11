from json import load
from flask import Flask, render_template
from waitress import serve as waitress_serve

with open("config.json", "r") as cfg_file:
    cfg = load(cfg_file)

app = Flask(__name__)

def run_web_debug():
    app.run(debug=True, host='0.0.0.0:80')
    
def run_web():
    waitress_serve(app, host='0.0.0.0', port=80)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/stream")
def stream_view():
    return render_template("stream.html", cfg=cfg)

@app.route("/motion")
def motion_view():
    return render_template("motion.html", cfg=cfg)

if __name__ == "__main__":
    run_web()
