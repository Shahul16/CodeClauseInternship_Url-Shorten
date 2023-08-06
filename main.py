from flask import Flask, render_template, request
import pyshorteners

app = Flask(__name__)

def shorten_url(url):
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(url)
        return short_url
    except pyshorteners.exceptions.ShorteningErrorException as e:
        return None

@app.route("/", methods=["GET", "POST"])
def home():
    shortened_url = None

    if request.method == "POST":
        long_url = request.form["long_url"]
        shortened_url = shorten_url(long_url)

    return render_template("index.html", shortened_url=shortened_url)

if __name__ == "__main__":
    app.run(debug=True)
