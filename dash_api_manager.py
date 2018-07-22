import json
import requests
import time

def exec():
    response = requests.get("https://notify.run/VM3CtOHiizyyy6ZL") #personal
    response = json.loads(response.text)
    # print(response)
    last_message_details = (response['messages'][0])
    last_message = last_message_details['message']
    # print(last_message)
    notification_time = last_message_details['time']
    notification_time = notification_time.split(" ")[-2]
    # print(notification_time)
    time_since_last_notif = 0
    print(last_message)
    if(last_message != '"SAFE"'):
        from datetime import datetime
        FMT = '%H:%M:%S'
        current_time = str(datetime.utcnow()).split(" ")[-1].split(".")[0]
        notification_time = datetime.strptime(notification_time, FMT)
        current_time = datetime.strptime(current_time, FMT)
        tdelta = current_time - notification_time
        time_split = str(tdelta).split(":")
        # print(int(time_split[0]) and int(time_split[2]))
        if((int(time_split[0])<1) and (int(time_split[2]) > 30)):
            tdelta = current_time - notification_time
            time_split = str(tdelta).split(":")
            # print(f"time elapsed:{time_split}")
            if(int(time_split[0])<1 and int(time_split[1]) < 2 and int(time_split[2]) > 30):
                requests.post("https://notify.run/e9xzTNsDtJKDKCBW", data="Help!") #inform public
            elif (int(time_split[1]) > 2):
                requests.post("https://notify.run/e9xzTNsDtJKDKCBW", data='"SAFE"')
                time.sleep(30)
                exec()

while True:
    time.sleep(5)
    exec()

    
    