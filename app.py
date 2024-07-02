......

from auth import jwt, auth_bp, bcrypt

# used on the on file we have the routes
from flask_jwt_extended import jwt_required

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///school.db'
......

# secret key
app.config['SECRET_KEY'] = '584e2ad25ba2d9101c1107ace0ca8a'

....
app.register_blueprint(auth_bp)
db.init_app(app)
jwt.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app=app, db=db)

.....


# protecting our data
@app.route('/students')
@jwt_required()
def students():
    pass