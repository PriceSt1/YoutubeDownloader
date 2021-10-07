from pytube import *


yt = YouTube(input("Introduce el link de descarga: "))
title = yt.title
author = yt.author
stream = StreamQuery.get_highest_resolution()



stream.download(yt)


filesize = stream.filesize



print(filesize)
print(title)
print(author)
