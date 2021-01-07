import flask
from flask import request, jsonify,send_file
from flask_cors import CORS, cross_origin
import os
import sys
sys.path.append("/var/www/colorPalette/colorPalette")
import tocp


app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'



    
@app.route('/', methods=['GET','POST'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/transform', methods=['GET','POST'])
@cross_origin()
def api_all():
    if request.method == 'POST':
        image = request.files['image']
        filename = image.filename
        f = open(filename, 'wb')
        f.write(image.read())
        f.close
        cp_path=tocp.transform(filename)
        return send_file(cp_path)
    else : 
        return jsonify([{"text":"fuck you"}])
if __name__ == '__main__':
    app.run()
