#!/usr/bin/python3
"""Flask api application"""
import os
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def shutdown_everything(exception):
    """Closes and clears everything"""
    storage.close()

if __name__ == "__main__":
    port = int(os.getenv("HBNB_API_PORT", 5000))
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    app.run(host=host, port=port, threaded=True)