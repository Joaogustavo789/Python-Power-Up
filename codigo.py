# Passo a passo do projeto

#TODO Passo 1: Entrar no sistema da empresa.

import pyautogui
import time
import pandas as pd

#* pyautogui.click -> clicar com o mouse.
#* pyautogui.write -> escrever um texto.
#* pyautogui.press -> apertar 1 tecla.
#* pyautogui.hotkey -> atalho (combinação de teclas).

pyautogui.PAUSE = 1 #! Pausa para cada comando do pyautogui.

#? abrir o navegador
pyautogui.press("win")

time.sleep(2) #! Tempo de espera.

pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.hotkey("ctrl", "t") #! Abrir uma nova aba do navegador.

#? entrar no link
url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(url)
pyautogui.press("enter")

#? esperar o site carregar
time.sleep(3)

#TODO Passo 2: Fazer login.
pyautogui.click(x=1847, y=427)
pyautogui.write("testes@testando.com")
pyautogui.press("tab")
pyautogui.write("cuscuz12345")
pyautogui.press("tab")
pyautogui.press("enter")

#TODO Passo 3: Importar a base de dados de produtos.
tabela = pd.read_csv("produtos.csv")

#? Variavel criada para usar no laço for apenas 5 produtos da base de dados.
tabela2 = tabela.head(5)

#TODO Passo 4: Cadastrar todos os produtos.
time.sleep(3)

for produto in tabela2.index:
    pyautogui.click(x=1844, y=310)

    codigo = tabela.loc[produto, "codigo"]
    marca = tabela.loc[produto, "marca"]
    tipo = tabela.loc[produto, "tipo"]
    categoria = tabela.loc[produto, "categoria"]
    preco_unitario = tabela.loc[produto, "preco_unitario"]
    custo = tabela.loc[produto, "custo"]
    obs = tabela.loc[produto, "obs"]

    #? preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000) #! Ir para o topo da página.
