def detect(temperature,humidity):
    if(humidity<30):
        if(temperature>30):
            print("Humidity : ",humidity,"Temperature : ",temperature,"ALARM TURNED ON !!")
            
for i in range(0,15):
    temperature = random.randint(15,50)
    humidity = random.randint(15,50)
    detect(temperature,humidity)
