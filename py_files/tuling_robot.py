import requests
import json

def monitor(content, logger):
    '''
    handle the message from the eim client(eg: scratch)
    '''
    userId = 123
    apiKey = "d116ebafbaeb49a486a809ec306a6e82"
    apiUrl = "http://openapi.tuling123.com/openapi/api/v2"

    content = {
        "perception": {
            "inputText": {
                "text": content
            },
        },
        "userInfo": {
            "apiKey": apiKey,
            "userId": userId
        }
    }
    res = requests.post(url=apiUrl, data=json.dumps(content))
    r = res.json()
    return r['results'][0]['values'][r['results'][0]['resultType']]
