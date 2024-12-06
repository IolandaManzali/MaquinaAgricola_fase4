# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto - Automação e inteligência na FarmTech Solutions

![Designer.jpeg](https://github.com/IolandaManzali/MaquinaAgricola_fase4/blob/main/assets/assetsfase4/CAP1FASE4.png)

Na Fase 3 (atividade: Construindo uma máquina agrícola) foi desenvolvido um projeto de um sistema de irrigação automatizado e inteligente para monitoramento da umidade, PK e  pH do solo em tempo real  e com ajuste de irrigação, utilizando as tecnologias Python, Oracle e a plataforma Wokwi. Utilizamos dados ficticios para mostrar o acionamento de  uma bomba de água (representada no modelo por um relé). Esse modelo se encontra disponivel atraves do link <https://wokwi.com/projects/414296192887361537>.

Para a Fase 4 foi lançado o desafio de otimizar o projeto anterior adicionando novas funcionalidades e incorporando novas tecnologias ao adicionar uma interface gráfica mais amigável com o Scikit-learn e o Streamlit, além das melhorias no banco de dados e no próprio código, que foi revisado para ser mais eficiente e mais econômico (utiliza uma memoria menor) sem comprometer sua qualidade. Esse modelo se encontra disponível através do link abaixo: <https://wokwi.com/projects/416358079505406977> 


## Nome do grupo - Grupo 38

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/guilherme-dos-santos-barbosa-58397b176">Guilherme dos Santos Barbosa</a>
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
Sk-learn - falta
streamlit - falta

Modelo Wokwi versão 1.2

<p align="justify">
 
Este projeto implementa um sistema de irrigação automatizado utilizando um microcontrolador ESP32, um sensor de umidade DHT22, um sensor de luminosidade (LDR) para simular níveis de nutrientes e um display LCD para monitoramento. O sistema controla uma bomba d'água através de um relé, ligando-a quando a umidade do solo estiver abaixo de 40% e desligando-a quando a umidade ultrapassar 80%. 
Na versao atualizada, o projeto conta com um banco de dados mais robusto do que o anterior e, alem de exibir os dados coletados em tempo real no display, apresenta interface grafica amigável para facilitar o monitoramento e compreensão dos dados analisados.


 Funcionalidades:
 
 * Monitoramento da umidade do solo: Utiliza um sensor DHT22 para medir a umidade do solo.
 * Simulação de níveis de nutrientes: Utiliza um LDR para simular a leitura de níveis de nutrientes no solo pH
 * Controle automático da irrigação: Liga e desliga a bomba d'água automaticamente com base na umidade do solo.
 * Interface de usuário: Exibe informações relevantes em um display LCD 20x4, incluindo umidade, níveis de nutrientes simulados, status da irrigação e temperatura.
 * Comunicação serial: Envia dados do sistema para o monitor serial para depuração e monitoramento.
 * Serial plotter : Exibe as informaçoes do sensor LRD (pH) do solo

Atualizações no codigo c++:

 * inclusao do codigo para utilização do LCD

 * troca de float por byte para leitura de umidade, com o objetivo de economizar memoria

 * codificação para parametrizar a visualização dos dados na tela LCD 





</p>

Integração do Serial Plotter: faça a demonstração do uso do Serial Plotter usando prints da sua tela do Wokwi para monitoramento de variáveis e poste no REDME, e explique os prints inseridos;



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
