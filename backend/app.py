from flask import Flask

def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/xml/get', methods=['GET'])
def get_xml():
    return "get successful"

if __name__ == '__main__':
    app.run(debug=True)