from flask import Flask, Response
app = Flask(__name__)
@app.route("/")
def index():
    return Response("""
    <h1 style='color: red;'>HEllO WORLD!</h1>
    <p>GROOT @inc 2020</p>
    <code>Flask is <em>awesome</em></code>
    """), 200
if __name__ == "__main__":
    app.run(host='0.0.0.0')