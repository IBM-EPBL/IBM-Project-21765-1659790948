import time
import wiotp.sdk.application

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
    name = "Child"
    #in area location
    
    latitude = 17.4219272
    longitude = 78.5488783



    #out area location

    #latitude = 17.4219272
    #longitude = 78.5488783
    myData = {"name":name, "lat":latitude, "lon": longitude}
    client.publishEvent(eventId = "status", msgFormat = "json", data = myData, qos = 0, onPublish =None)
    print("Data published to IBM IoT Platform: ", myData)
    time.sleep(5)

client.disconnect()

