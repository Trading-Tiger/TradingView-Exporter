

import time
from flask import Flask, request
import json



with open ('settings.json') as config_file:
    config = json.load(config_file)
    
whitelist = config['whitelist']
ip = config['IP']
port = config['PORT']


msg = 'Signal reveiced and execute!'
app = Flask(__name__)
@app.route('/webhook', methods=['POST'])
def webhook():
    timestamp = time.strftime("%Y-%m-%d %X")
    try:
        if request.method == 'POST':
            data = request.get_data(as_text=True)
            if whitelist.lower() in data.lower():
                if not "closed" in data.lower():
                    if not "ready" in data.lower():
                        import handler
                        handler.sh.onsignal(data=data)
                        print(timestamp, msg)
                        return msg, 200
                    else:
                        print('Ready in data!')
                        return 'Ready in data!', 200
                else:
                    print('Closed in data!')
                    return 'Closed in Data!', 200
            else:
                print('Not in Whitelist!')
                return 'Not in Whitlist!', 200
        else:
            return 'Refused alert', 400
    except Exception as e:
        print(e)
        return 'error', 400

if __name__ == '__main__':
    from waitress import serve
    serve(app, host=ip, port=port)
