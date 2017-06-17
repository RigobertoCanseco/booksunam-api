from flask import render_template, send_from_directory

from v1 import app, db

#######################################################################################################################
## APP
app.config.from_pyfile( "flaskapp.cfg" )
########################################################################################################################
## FLASK
db.init_app(app)
########################################################################################################################


@app.route( '/' )
def index():
    return render_template( 'index.html' )


@app.route( '/<path:resource>' )
def serve_static_resource( resource ):
    return send_from_directory( 'static/', resource )


@app.route( "/test" )
def test():
    return "<strong>It's Alive!</strong>"


if __name__ == '__main__':
    app.run( app.config[ 'IP' ], app.config[ 'PORT' ] )
