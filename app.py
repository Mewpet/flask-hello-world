from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """
    <h1> Hi!!! Here's jeff! </h1>
    <img src="https://giffiles.alphacoders.com/223/223280.gif" alt="Jeff">
"""