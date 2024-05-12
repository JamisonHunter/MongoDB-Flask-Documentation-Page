from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(YOUR_MONGODB_URI_HERE)
db = client["hello"]
collection = db["messages"]

@app.route("/")
def hello_world():
    result = collection.find_one()
    return render_template("index.html", message=result)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)