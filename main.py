from flask import Flask
from routes.home import home_route

app = Flask(__name__, static_folder='static')
app.register_blueprint(home_route)

if __name__ == "__main__":
    app.run(debug=True)