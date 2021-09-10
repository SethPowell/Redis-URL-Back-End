import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from rq import Queue
from rq.job import Job
from worker import conn

from models import *


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

q = Queue(connection=conn)
db = SQLAlchemy(app)
ma = Marshmallow(app)
CORS(app)

def urlShorten(r: redis.Redis, myurl: str) -> None:
    with r.pipeline() as pipe:
        error_count = 0
        while True:
            try:
                pipe.watch(myurl)
                storing = r.hset(myurl, )



if __name__ == "__main__":
    app.run(debug=True)