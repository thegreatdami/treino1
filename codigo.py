import pyautogui
import time

pyautogui.PAUSE = 0.5

# Abrir navegador (Chrome)
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

# Entrar no site do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Uma espera maior para carregar o site
time.sleep(2)

# Fazendo login
pyautogui.click(x=818, y=372)
pyautogui.write("damiaorochaduda@gmail.com")
pyautogui.press("tab")
pyautogui.write("1q2w3e4r5t")
pyautogui.press("enter")

# Importando a base de dados para o cadastro dos produtos
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Cadastrar um produto

for  linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])

    # Clicar no campo do código do produto
    pyautogui.click(x=782, y=256)

    # Preencher codigo
    pyautogui.write(codigo)

    # Passar para o próximo campo
    pyautogui.press("tab")

    # Passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))

    # Passar para o próximo campo
    pyautogui.press("tab")

    # Passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))

    # Passar para o próximo campo
    pyautogui.press("tab")

    # Passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "categoria"])) 

    # Passar para o próximo campo
    pyautogui.press("tab")

    # Passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

    # Passar para o próximo campo
    pyautogui.press("tab")

    # Passar para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "custo"]))

    # Passar para o próximo campo
    pyautogui.press("tab")

    # Passar para o próximo campo
    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)

    # Passar para o próximo campo
    pyautogui.press("tab")

    # Apertar o botão de enviar
    pyautogui.press("enter")
    
    # Voltar ao inicio da tela
    pyautogui.scroll(500)
