import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Seleciona uma pasta")

archive_list = os.listdir(caminho)
print(archive_list)

locais = {
    "capturas de tela": [".png"]
}

for arquivo in archive_list:
    # 01.arquivo.pdf
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais["capturas de tela"]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{caminho}", f"{caminho}/{pasta}/{caminho}")