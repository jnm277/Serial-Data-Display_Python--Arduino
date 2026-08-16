int analogPin = A0;     
int data = 0;           
char userInput;
void setup() {

  Serial.begin(9600);

}

void loop() {

  if(Serial.available()> 0){

      userInput = Serial.read();

      if(userInput == 'g'){

        data = analogRead(analogPin);
        Serial.println(data);
    }

  }

}
