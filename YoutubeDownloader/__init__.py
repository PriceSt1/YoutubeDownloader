from pytube import *


yt = YouTube(input("Introduce el link de descarga: "))
title = yt.title
author = yt.author
stream = Stream

filesize = stream.filesize



print(filesize)
print(title)
print(author)