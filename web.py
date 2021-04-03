from flask import Flask, render_template, send_from_directory
from waitress import serve as waitress_serve
from config import cfg
from glob import glob
from re import search as regex_search

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
    mlog = []
    try:
        mlog = open(cfg["motion_log"], "r").readlines()
        mlog = [l.strip() for l in mlog]
        mlog.reverse()
    except:
        mlog = []
    print(mlog)
    return render_template("motion.html", cfg=cfg, mlog=mlog)

@app.route("/captures")
def capture_view():
    fn = []
    for i in glob('static/capture/*.jpg'):
        fn.append({
            "path": i, 
            "filename": regex_search(r"(?<=static/capture\\)(.*)(?=.jpg)", i).group()
        })
    return render_template("captures.html", filenames=fn)

# Serve images in capture directory; don't know if this is necessary
@app.route('/capture/<path:path>')
def send_capture(path):
    return send_from_directory('static/capture', path)

if __name__ == "__main__":
    run_web()
