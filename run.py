from groot import app, db
from groot.models import *

db.create_all()

from groot.routes import *

if __name__ == "__main__":
    app.run(host='0.0.0.0')
 
	