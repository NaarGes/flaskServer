from flask import Flask, request

app = Flask(__name__)


@app.route('/files/', methods=['POST'])
def files():
    with open('file.png', 'wb') as f:
        f.write(request.files['myFile'].read())
    return ''

# Run the app :)
if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int("5000")
    )
