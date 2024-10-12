import requests
from bs4 import BeautifulSoup
from os import name,system
from time import sleep

def erroClear(Erro):
    print("Error: ", erro, "\nrestarting...")
    sleep(3)
    system('cls' if name == 'nt' else 'clear') or None

parada = False
nomeArquivo = "HTMLCopy.html"

while(parada == False):
    system('cls' if name == 'nt' else 'clear') or None
    print("Welcome to CopiadorAbsoluto")
    url = str(input('Enter the url of the website you want to copy the html \n'))

    try:
        htmlSite = requests.get(url)
        arquivohtml = BeautifulSoup(htmlSite.text, 'lxml')

        with open(nomeArquivo, "a", encoding="utf-8") as file:
            file.write("\n<!--website copied using CopiadorAbsoluto made by Biks-->")
            file.write("\n<!--for more information visit:https://github.com/IAmBiks-->\n")
            file.write(str(arquivohtml))


    except ValueError:
        erroClear("valueError")
        continue
    except requests.exceptions.RequestException:
        erroClear("URL access failure")
        continue
    else:
        while(parada == False):
            system('cls' if name == 'nt' else 'clear') or None
            try:
                decisãoDeContiuidade = int(input('Do you want to copy another website? \n1-Yes 2-No\n'))
                if decisãoDeContiuidade == 1:
                    break
                elif decisãoDeContiuidade == 2:
                    parada = True
                    break
            except ValueError:
                erroClear("ValueError")
                continue
