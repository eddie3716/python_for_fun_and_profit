import os

from flask import Flask
from flask import Response

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile("config.py", silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/healthcheck")
    def hello():
        return "All good"
    
    @app.route("/")
    def art():
        acsii_art = """\

            ._ o o
            \_`-)|_
        ,""       \ 
        ,"  ## |   ಠ ಠ. 
    ," ##   ,-\__    `.
    ,"       /     `--._;)
,"     ## /
,"   ##    /

"""
       
        return  Response(status=200,
                    response=acsii_art,
                    mimetype='text/plain'
                )

    # apply the blueprints to the app
    from gitprofiles import controller

    app.register_blueprint(controller.bp)

    return app