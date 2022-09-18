#include<Servo.h>
Servo s;
void setup()
{
pinMode(2, INPUT);
pinMode(4,INPUT);
pinMode(13,OUTPUT);  
s.attach(12);
s.write(0);
}

void loop()
{
if(digitalRead(2)==HIGH)
{
s.write(90);
delay(500);
s.write(0);
}
    digitalWrite(13,0);
  int b=digitalRead(4);
  if (b==1)
  {
    digitalWrite(13,1);
  }
}
