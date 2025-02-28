from flask import Flask, request, jsonify, render_template
from collections import Counter
import re
from textblob import TextBlob

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    words = re.findall(r'\w+', text)
    word_count = len(words)
    char_count = len(text)
    most_common = Counter(words).most_common(5)

    # تحليل المشاعر (يعمل بشكل أفضل مع الإنجليزية)
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = "إيجابي 😊"
    elif sentiment_score < 0:
        sentiment = "سلبي 😞"
    else:
        sentiment = "محايد 😐"

    return jsonify({
        "word_count": word_count,
        "char_count": char_count,
        "most_common": most_common,
        "sentiment": sentiment
    })

if __name__ == "__main__":
    app.run(debug=True)
