import requests
from bs4 import BeautifulSoup
from os import name,system
from time import sleep

def erroClear(Erro):
    print("Erro de ", Erro, "\nReiniciando...")
    sleep(3)

parada = False
nomeArquivo = "HTMLCopiado.html"

while(parada == False):
    system('cls' if name == 'nt' else 'clear') or None
    print("Bem-Vindo ao CopiadorAbsoluto")
    url = str(input('insira a url do site que quer copiar: \n'))

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
        erroClear("falha de acesso a URL")
        continue
    else:
        while(parada == False):
            system('cls' if name == 'nt' else 'clear') or None
            try:
                decisãoDeContiuidade = int(input('Deseja copiar mais algum site? \n1-Sim 2-Não\n'))
                if decisãoDeContiuidade == 1:
                    break
                elif decisãoDeContiuidade == 2:
                    parada = True
                    break
            except ValueError:
                erroClear("ValueError")
                continue
#
