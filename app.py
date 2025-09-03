from flask import Flask,render_template
import requests
app = Flask(__name__)

@app.route("/")
def home():
    url="https://newsapi.org/v2/everything?q=bitcoin&apiKey=d795e8b8466949dbbdcd436eb8d2a310"
    
    r = requests.get(url).json()

    news = {
        'articles' : r['articles']
    }
    return render_template('index.html',allNews=news)