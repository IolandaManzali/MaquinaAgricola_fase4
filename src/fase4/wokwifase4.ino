# Codigo .ino 

#include <DHT.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

// DefiniÃ§Ãµes dos pinos
#define DHTPIN 15     // Pino digital conectado ao DHT22
#define LDRPIN 34     // Pino analÃ³gico conectado ao LDR
#define BOTAO_P 4     // Pino digital conectado ao botÃ£o P
#define BOTAO_K 5     // Pino digital conectado ao botÃ£o K
#define RELE_PIN 23    // Pino digital conectado ao relÃ©

// Tipo de sensor DHT
#define DHTTYPE DHT22 

// Inicializa o sensor DHT
DHT dht(DHTPIN, DHTTYPE);

// Inicializa o LCD I2C
LiquidCrystal_I2C lcd(0x27, 20, 4); // EndereÃ§o I2C 0x27, 20 colunas x 4 linhas

void setup() {
  Serial.begin(9600);      // ComunicaÃ§Ã£o serial
  dht.begin();             // Inicializa o sensor DHT22
  pinMode(BOTAO_P, INPUT_PULLUP); 
  pinMode(BOTAO_K, INPUT_PULLUP); 
  pinMode(RELE_PIN, OUTPUT);      

  // Inicializa o LCD
  lcd.init();
  lcd.backlight();
}

void loop() {
  // Leitura da umidade - Usando byte para economizar memÃ³ria, 
  // assumindo que a umidade nunca excederÃ¡ 100%
  byte h = (byte) dht.readHumidity();  
  
  // Leitura do LDR (simulando pH)
  int valorLDR = analogRead(LDRPIN);
  
  // Leitura dos botÃµes "P" e "K" 
  bool botao_p_pressionado = digitalRead(BOTAO_P) == LOW;  
  bool botao_k_pressionado = digitalRead(BOTAO_K) == LOW;
  
  // LÃ³gica de controle do relÃ© (bomba d'Ã¡gua)
  if (h < 40) {  // Se a umidade for menor que 40%
    digitalWrite(RELE_PIN, HIGH);  // Liga a Bomba 
  } else if (h > 80) {  // Se a umidade for maior que 80%
    digitalWrite(RELE_PIN, LOW);   // Desliga a bomba 
  }

  // Dados do Serial:
  Serial.print("Umidade: ");
  Serial.println(h);
  Serial.print("P: ");
  Serial.println(botao_p_pressionado);
  Serial.print("K: ");
  Serial.println(botao_k_pressionado);
  Serial.print("pH: ");
  Serial.println(valorLDR); 
  Serial.print("Rele: ");
  Serial.println(digitalRead(RELE_PIN));

  // Mostrando os dados no LCD
  lcd.setCursor(0, 0);
  lcd.print("Umid.: ");
  lcd.print(h);
  lcd.print("%");
  
  lcd.setCursor(0, 1);
  lcd.print("pH: ");
  lcd.print(valorLDR);

  lcd.setCursor(0, 2);
  lcd.print("Irrig.: ");
  // Usando operador ternÃ¡rio para simplificar e potencialmente reduzir o tamanho do cÃ³digo
  lcd.print(digitalRead(RELE_PIN) == HIGH ? "on" : "off"); 

  lcd.setCursor(0, 3); 
  lcd.print("Temp.: ");
  // Convertendo a temperatura para inteiro para economizar memÃ³ria, 
  // assumindo que a precisÃ£o de ponto flutuante nÃ£o Ã© crucial
  lcd.print((int)dht.readTemperature()); 
  lcd.print("C");

  delay(2000); // Aguarda 2 segundos
}

