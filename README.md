# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto - Construindo uma Máquina Agrícola

![Designer.jpeg](https://github.com/IolandaManzali/Construindo_maquina_agicola_fase3fiap/blob/main/assets/maquinaagricola.jpeg)

Este projeto é composto por um código em python que consulta os valores do sensores no banco de dados(SQL). Os sensores abordados são Ph, K, P e Umidade, os valores dos sensores são fictícios, visando fins acadêmicos. Objetivo do projeto é realizar uma integração entre o banco de dados e o código em python, assim como os valores fornecidos pelo monitor serial do simulador, para podermos simular um início de um sistema de irrigação.

Funcionalidades
Umidade: Código analisa o valor da variável umidade que é retirado do banco e informa ao usuário, se é necessário ligar a bomba ou não e por qual motivo, esta função foi elaborada por meio dos comando if, elif e else, que são comandos condicionais
Ph: Código analisa o valor da variável ph que é retirado do banco, classificando o ph em três níveis conforme o valor, sendo eles nível ácido, básico e neutro 
Fósforo e Potássio: Ambos foram representados por botões no sistema eletrônico, e o botão informa se está ligado ou não, por isso o código analisa o valor que foi retirado do banco, retornando True, ou seja, não necessita de nem um tipo de correção e retornando False, ou seja, necessita de algum tipo de correção.

![Figura1.jpeg](https://github.com/HilmarMarques/MaquinaAgricola/main/assets/codigo1.jpeg)


![Figura2.jpeg](https://github.com/HilmarMarques/MaquinaAgricola/main/assets/codigo2.jpeg)



![circuito.jpeg](https://github.com/HilmarMarques/MaquinaAgricola/main/assets/circuito.jpeg)

Projeto de Automação de Irrigação com ESP32 e Wokwi
Este projeto utiliza um ESP32 para automatizar um sistema de irrigação, controlando uma bomba d'água com base na umidade do solo. Ele também inclui um sensor de luminosidade (LDR) para simular a leitura de pH e botões para controle manual da bomba. O projeto é simulado na plataforma Wokwi, que permite a prototipagem e visualização do circuito de forma online.

Funcionalidades
Monitoramento da umidade do solo: O sensor DHT22 mede a umidade do ar, que neste projeto representa a umidade do solo.
Simulação de leitura de pH: Um sensor de luminosidade (LDR) simula a leitura do pH do solo.
Controle automático da bomba d'água: A bomba d'água é ligada quando a umidade do solo (simulada pela umidade do ar) está abaixo de 40% e desligada quando está acima de 80%.
Controle manual da bomba d'água: Botões P e K permitem ligar e desligar a bomba manualmente, independentemente da umidade do solo.
Monitoramento via comunicação serial: Os valores da umidade, pH (simulado) e estado da bomba são enviados pela porta serial para monitoramento.
Hardware
ESP32: Placa microcontroladora com Wi-Fi e Bluetooth integrado, que processa os dados dos sensores e controla a bomba d'água.
Sensor DHT22: Sensor de temperatura e umidade.
Sensor de luminosidade (LDR): Simula o sensor de pH.
Botão P: Representando sensor de nutrientes Fósforo (P). monitore a umidade do solo em tempo real e os níveis dos nutrientes. Ajustando a irrigação conforme o necessário
Botão K: como sensor de nutrientes de Potássio (K). monitore a umidade do solo em tempo real e os níveis dos nutrientes. Ajustando a irrigação conforme o necessário

Software
Arduino IDE: Ambiente de desenvolvimento para programar o ESP32 (configurado para ESP32).
Biblioteca DHT: Biblioteca para o sensor DHT22.
Detalhes das conexões:
DHT22:
Pino de dados (sinal) conectado ao pino digital 15 do ESP32.
Pino VCC conectado ao pino 5V do ESP32.
Pino GND conectado ao pino GND do ESP32.
Sensor de luminosidade (LDR):
Um dos pinos do LDR conectado ao pino analógico 34 do ESP32.
O outro pino do LDR conectado ao pino GND do ESP32.
Pino VCC conectado ao pino 5V do ESP32.
Botão P:
Um pino do botão conectado ao pino digital 4 do ESP32.
O outro pino do botão conectado ao pino GND do ESP32.
Botão K:
Um pino do botão conectado ao pino digital 5 do ESP32.
O outro pino do botão conectado ao pino GND do ESP32.
Relé:
Pino de controle do relé conectado ao pino digital 23 do ESP32.
Pino VCC conetado na da fonte externa
Pino GND do Relé conectado no GND da placa
Pino de saída do relé NC conectado no LED para mostrar que esta energizado.
Pino CO do Relé conectado no 5v da placa  ESP32.
bomba d’água representado por um relé.
Led:
Pino positivo (anodo) do LED conectado ao NO do Relé( bomba da agua).
Pino negativo (catodo) do LED conectado ao pino GND do ESP32, através de um resistor de 220Ω para regular a tensão.
O led representando quando a bomba está energizada.

https://wokwi.com/projects/414296192887361537


## Nome do grupo - Grupo 07

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/hilmar-marques-358672161">Hilmar Gomes Marques da Silva</a>
- <a href="https://www.linkedin.com/in/iolanda-helena-fabbrini-manzali-de-oliveira-14ab8ab0">Iolanda Helena Fabbrini Manzali de Oliveira</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Murilo Carone Nasser</a> 
- <a href="https://www.linkedin.com/in/pedro-eduardo-soares-de-sousa-439552309">Pedro Eduardo Soares de Sousa</a> 
- <a href="https://www.linkedin.com/company/inova-fusca">Yago Brendon Iama</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Andre Godoi Chaviato</a>


## 📜 Descrição
falta

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: imagens utilizadas no projeto

- <b>config</b>: arquivos de configuração para definir parâmetros e ajustes do projeto.

- <b>document</b>: documentos complementares do projeto

- <b>scripts</b>: scripts auxiliares

- <b>src</b>: código fonte principal

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código
 falta 






## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - 13/11/2024
    *
  
## Desenvolvedores

![Designer.jpeg](https://github.com/IolandaManzali/decolando_com-_ciencia_de_dados_grupo21/blob/main/assets/grupo_fiap.jpg)


## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
