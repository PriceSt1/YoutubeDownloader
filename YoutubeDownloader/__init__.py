from pytube import *
import math
from YoutubeDownloader import Path


def direccionDescarga():
        return Path.get_download_folder()

def main():
    yt = YouTube(input("Introduce el link"))
    print("Cargando...")
    title = yt.title
    author = yt.author
    stream = yt.streams.get_highest_resolution()
    downloadPath = direccionDescarga()
    print("Cargando...")
    filesize = stream.filesize
    filesize = (filesize) / math.pow(2, 20)
    filesize = round(filesize, 2)
    print("Cargando...")




    print(f"Descargando video \n "
            f"Titulo: {title} \n "
            f"Autor: {author} \n "
            f"carpeta: {downloadPath} \n "
            f"El video ocupa {filesize} MiB")

    print("Iniciando descarga")

    stream.download(output_path=downloadPath)

    print("Descarga terminada")
if __name__ == '__main__':
        main()
