from flask import Flask, request, send_file
from flask_cors import CORS
from mysql_DB import add_video_to_DB, get_file_path
from MY_modules import prepare_output_dir


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['POST', 'GET'])
def service_status():
    return {
        "Status": 'Alive',
        "End-points": {
            "/add_video": {
                "method": "POST",
                "parameter": "file_upload",
                "data": "video file"
            },
            "/get_video": {
                "method": "POST",
                "parameter": "file_name",
                "data": "requested video file name"
            }
        }
    }


@app.route("/get_video", methods=['POST'])
def get_video():
    if request.method == 'POST':
        file_name = request.form['file_name']
        
        try:
            DB_response = get_file_path(file_name)
            if DB_response["status"] == "SUCCESS":
                print("$$$$$$$",DB_response["file_path"])
                return send_file(DB_response["file_path"], as_attachment=False)
        except FileNotFoundError:
            return {"status":"FAILED",
                    "request_method":request.method,
                    "error":"FileNotFoundError"}


@app.route("/add_video", methods=['POST'])
def add_video():
    if request.method == 'POST':
        file = request.files['file_upload'] 
        if file:
            prepare_output_dir('videos')
            file_path = f"videos/{file.filename}"
            file.save(file_path)
            DB_response = add_video_to_DB(file_name=file.filename,dir_path="videos/")

            return {"status":"SUCCESS",
                    "request_method":request.method,
                    "response":DB_response}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004, use_reloader = True)