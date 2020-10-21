from flask import Flask
from datetime import datetime
import requests
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
    parameters = {
        "lat" : 48.8534,
        "lon" : 2.3488
    }
    r = requests.get("http://api.open-notify.org/iss-pass.json?", params=parameters)

    r_data = r.json()['response']

    times = []

    for d in r_data:
        timestamp = d['risetime']
        time = datetime.fromtimestamp(timestamp)
        readable_time = time.strftime("%c")
        times.append(readable_time)

    return json.dumps(times)

if __name__ == '__main__':
    app.run(host='0.0.0.0')