
#include <Servo.h>

Servo myservo;
int openingPos = 180;
int normalPos = 0;
void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  myservo.attach(9);
}

void loop() {
  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    String readString;
    String Q;
    
    
     while (Serial.available()){
      delay(1);
      if(Serial.available()>0){
      char c = Serial.read();
       if (isControl(c)){
      break;
      }
      readString += c;    
      }
     }
    
    Q = readString;

    // say what you got:
    Serial.print(Q);

    if(Q == "open"){
      Serial.print("it is working");
      myservo.write(openingPos);
      delay(1000);
      myservo.write(normalPos);
    }
  }
}
