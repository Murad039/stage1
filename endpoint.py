from flask import Flask, request, jsonify 
import datetime
import pytz

app = Flask(__name__)

@app.route('/api', methods = ['GET'])

def get_info():
    #get slackname and track
    slack_name = request.args.get('slack_name')
    track=request.args.get("track")

    #get current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime("%A")

    #get current utc time
    utc_now = datetime.datetime.now(pytz.utc)
    utc_time = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    #github repo information
    github_repo= 'https://github.com/Murad039/stage1'
    github_file = 'https://github.com/Murad039/stage1/edit/main/endpoint.py'

    #response data
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file,
        "github_repo_url": github_repo,
        "status_code": 200
    }
    return jsonify(response_data)

    if __name__ == '__main__':
        app.run(host= '0.0.0.0', debug = True, port = 5000 )
