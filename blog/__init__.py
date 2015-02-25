from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "mydb"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

def register_blueprints(app):
	#Prevents circular imports
	from blog.views import posts
	app.register_blueprint(posts)

register_blueprints(app)

if __name__ == '__main__':
	app.run()