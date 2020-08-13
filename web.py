from flask import Flask, render_template
from waitress import serve as waitress_serve
from config import cfg

app = Flask(__name__)

def run_web_debug():
    app.run(debug=True, host='0.0.0.0:{}'.format(cfg["host_port"]))
    
def run_web():
    waitress_serve(app, host='0.0.0.0', port=cfg["host_port"])

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/stream")
def stream_view():
    return render_template("stream.html", cfg=cfg)

@app.route("/motion")
def motion_view():
    mlog = open(cfg["motion_log"], "r").readlines()
    mlog = [l.strip() for l in mlog]
    mlog.reverse()
    print(mlog)
    return render_template("motion.html", cfg=cfg, mlog=mlog)

if __name__ == "__main__":
    run_web()
