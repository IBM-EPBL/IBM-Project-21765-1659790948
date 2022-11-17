import time
import wiotp.sdk.application
from twilio.rest import Client
import twilio_keys

myConfig = {
    "identity" : {
        "orgId" : "fjde2i",
        "typeId": "Tracker",
        "deviceId":"28",
    },
    "auth": {
        "token": "123456789"
    }
}
client = wiotp.sdk.device.DeviceClient(config = myConfig, logHandlers = None)
client.connect()

while True:
    name = "Shyrin"
    #in area location
    
    #latitude = 17.4219272
    #longitude = 78.5488783



    #out area location

    latitude = 30.4219272
    longitude = 108.5488783

    if (latitude != 17.4219272) and (longitude != 78.5488783):
        client1 = Client(twilio_keys.account_sid, twilio_keys.auth_token)
        message = client1.messages.create(
            body="Dear Parent/Guardian,"
                 "\nShyrin is not within the geofence!!!",
            from_=twilio_keys.twilio_number,
            to=twilio_keys.target_number
        )

    myData = {"name":name, "lat":latitude, "lon": longitude}
    client.publishEvent(eventId = "status", msgFormat = "json", data = myData, qos = 0, onPublish =None)
    print("Data published to IBM IoT Platform: ", myData)
    time.sleep(5)


client.disconnect()


