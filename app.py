from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>My First Web Application 🚀</h1>
    <p>Hello! My app is working.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)