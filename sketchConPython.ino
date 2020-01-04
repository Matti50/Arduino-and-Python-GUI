int pin = 13;
char dato;
void setup() {
  // put your setup code here, to run once:
  pinMode(pin,OUTPUT);
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    dato = Serial.read();
  
    if(dato == '0'){
      digitalWrite(pin,LOW);
      }
    else if(dato == '1'){
      digitalWrite(pin,HIGH);
      } 
  }
  
  
}
