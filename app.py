from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """_summary_
    """
    return {'status': 'OK'}


if __name__ == "__main__":
    app.run()
