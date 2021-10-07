from YoutubeDownloader import Downloader


def main():
    link= input("Introduce el link: ")

    title = Downloader.instanciaYT(link).title
    author = Downloader.instanciaYT(link).author
    stream = Downloader.instanciaStream()
    downloadPath = Downloader.direccionDescarga()

    print("Cargando...")
    print("Cargando...")
    filesize = Downloader.Downloader.tamañoArchivo()
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
