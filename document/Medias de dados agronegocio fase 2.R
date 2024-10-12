# Carregando as bibliotecas necessárias
library(tidyverse)
library(dplyr)

# Carregando os dados (ajuste o caminho do arquivo)
dados <- read.csv(file.choose())
dados

#MEDIDAS DE TENDENCIA CENTRAL
# Média Valor de Produçao
media_valor_producao <- mean(dados$Valor.da.Produção.Contínua)
media_valor_producao

# Mediana do valor de Produçao
mediana_valor_producao <- median(dados$Valor.da.Produção.Contínua)
mediana_valor_producao

#MEDIDAS DE DISPERSAO
# Variância
variancia_valor_producao <- var(dados$Valor.da.Produção.Contínua)
variancia_valor_producao

# Desvio padrão
desvio_padrao_valor_producao <- sd(dados$Valor.da.Produção.Contínua)
desvio_padrao_valor_producao

# Amplitude
amplitude_valor_producao <- max(dados$Valor.da.Produção.Contínua) - min(dados$Valor.da.Produção.Contínua)
amplitude_valor_producao

#SEPARATRIZES
# Quartis
quartis_valor_producao <- quantile(dados$Valor.da.Produção.Contínua)



# GRAFICO DE ANALISE
# Histograma
hist(dados$Valor.da.Produção.Contínua, main = "Histograma do Valor da Produção", xlab = "Valor da Produção")

# Boxplot
boxplot(dados$Valor.da.Produção.Contínua, main = "Boxplot do Valor da Produção")
