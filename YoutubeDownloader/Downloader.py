from pytube import *
from pytube.cli import on_progress
import math
from YoutubeDownloader import Path



def instanciaYT(link):
    return YouTube(link)

def instanciaStream():
    return instanciaYT().streams.get_highest_resolution()

def direccionDescarga():
    return Path.get_download_folder()

def tamañoArchivo():
    filesize = instanciaStream().filesize
    filesize = (filesize) / math.pow(2, 20)
    filesize = round(filesize, 2)
    return filesize