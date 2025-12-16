import pyautogui
import time
import pandas

# Nada foi feito com IA, eu faço comentários apenas para organizar cada passo do meu código.

# Passo 1: Abrir o site https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Fazer login
# Passo 3: Importar a base de dados
# Passo 4: Cadastrar um produto
# Passo 5: Loop com o resto dos produtos

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

# Passo 1
pyautogui.press("win")
pyautogui.write("edge")
time.sleep(0.5)
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=147, y=50)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# Passo 2
pyautogui.click(x=418, y=391)
pyautogui.write("emailAleatorio@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhaAleatoria")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# Passo 3
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4
for linha in tabela.index:
    pyautogui.click(x=409, y=269)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
    
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
    
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.scroll(10000)