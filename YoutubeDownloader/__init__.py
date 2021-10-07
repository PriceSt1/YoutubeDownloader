from pytube import *
import math
import os
import ctypes
from ctypes import windll, wintypes
from uuid import UUID

def main():
    salir=True
    while(salir):
        link = input("Introduce el link: ")
        yt = YouTube(link)

        print("Cargando...")
        title = yt.title
        author = yt.author
        stream = yt.streams.get_highest_resolution()
        downloadPath = get_download_folder()
        print("Cargando...")
        filesize = stream.filesize
        filesize = (filesize) / math.pow(2, 20)
        filesize = round(filesize, 2)
        print("Cargando...")
        yt.captions.all

        #en_caption = yt.captions.get_by_language_code('en')

        #en_caption_convert_to_srt = (en_caption.generate_srt_captions())

        #print(en_caption_convert_to_srt)
        #save the caption to a file named Output.txt
        #text_file = open(downloadPath,"Output.txt", "w")
        #text_file.write(en_caption_convert_to_srt)
        #text_file.close()




        print(f"Descargando video \n "
            f"Titulo: {title} \n "
            f"Autor: {author} \n "
            f"carpeta: {downloadPath} \n "
            f"El video ocupa {filesize} MiB")

        print("Iniciando descarga")

        stream.download(output_path=downloadPath)

        print("Descarga terminada")

        salida=input("Quieres salir? [Y/N]")
        if salida=="Y":
            salir=False





if os.name == 'nt':

    # ctypes GUID copied from MSDN sample code
    class GUID(ctypes.Structure):
        _fields_ = [
            ("Data1", wintypes.DWORD),
            ("Data2", wintypes.WORD),
            ("Data3", wintypes.WORD),
            ("Data4", wintypes.BYTE * 8)
        ]

        def __init__(self, uuidstr):
            uuid = UUID(uuidstr)
            ctypes.Structure.__init__(self)
            self.Data1, self.Data2, self.Data3, \
                self.Data4[0], self.Data4[1], rest = uuid.fields
            for i in range(2, 8):
                self.Data4[i] = rest>>(8-i-1)*8 & 0xff

    SHGetKnownFolderPath = windll.shell32.SHGetKnownFolderPath
    SHGetKnownFolderPath.argtypes = [
        ctypes.POINTER(GUID), wintypes.DWORD,
        wintypes.HANDLE, ctypes.POINTER(ctypes.c_wchar_p)
    ]

    def _get_known_folder_path(uuidstr):
        pathptr = ctypes.c_wchar_p()
        guid = GUID(uuidstr)
        if SHGetKnownFolderPath(ctypes.byref(guid), 0, 0, ctypes.byref(pathptr)):
            raise ctypes.WinError()
        return pathptr.value

    FOLDERID_Download = '{374DE290-123F-4565-9164-39C4925E467B}'

    def get_download_folder():
        return _get_known_folder_path(FOLDERID_Download)
else:
    def get_download_folder():
        home = os.path.expanduser("~")
        return os.path.join(home, "Downloads")

if __name__ == '__main__':
        main()
