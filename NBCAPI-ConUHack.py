import json
from time import sleep

import requests

endpoint = "https://api.powerbi.com/beta/5569f185-d22f-4e13-9850-ce5b1abcd2e8/datasets/65c10035-e0fb-4696-9531-ff23e8739d00/rows?experience=power-bi&key=DKxQGf3oQGcNxKjLiiSqW01MGB0Ler7e5QGyZm7e1TOfiO8izD9T9zDE5kPLQHPS1pRtNjwM%2B8qgrkE5ZDJmFQ%3D%3D"

if __name__ == "__main__":
    f = open('Exchange_1.json')
    data = json.load(f)
    f.close()
    f = open('Exchange_2.json')
    data.extend(json.load(f))
    f.close()
    f = open('Exchange_3.json')
    data.extend(json.load(f))
    f.close()
    sorted(data, key=lambda e: e['TimeStamp'])
    delay = 360 / len(data)

    order_queue = []
    for d in data:

        if d['MessageType'] in ("NewOrderRequest", "CancelRequest"):
            order_queue.append(d)

        elif d['MessageType'] in ("NewOrderAcknowledged", "Cancelled"):
            first_element = order_queue[0]
            if first_element['OrderID'] == d['OrderID']:
                d['ResponseTime'] = (int(d['TimeStampEpoch']) - int(first_element['TimeStampEpoch'])) / 1000000000
                print("Response Time: ", d['ResponseTime'])

            order_queue.pop(0)
        
        d['AnnotatedTime'] = d['TimeStamp'].split(" ")[1].split(".")[0]
        
        response = requests.post(endpoint, json=[d])
        if response.status_code == 200:
            print(d)
        else:
            print("Failed")
        sleep(1)
