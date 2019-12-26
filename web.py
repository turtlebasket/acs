from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/stream")
def stream_view():
    return render_template("stream.html")

@app.route("/motion")
def motion_view():
    return render_template("motion.html")

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
