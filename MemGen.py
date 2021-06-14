from PIL import Image, ImageDraw, ImageFont
from os import path


memefolder='images'
memename='bart-simpson.gif'
outputname='meme.png'
memeimage=path.join(memefolder, memename)
memeresult=path.join(memefolder, outputname)

text="I will not instigate revolution."
textsize=40
origen=(50, 40)

#Loads font and defines size
comicFont = ImageFont.truetype('/usr/share/fonts/opentype/comic-neue/ComicNeue_Bold.otf', textsize)


#Opens meme image
meme = Image.open(memeimage).convert('RGB')
canvas = ImageDraw.Draw(meme)

#write Text replace TODO with loop

#TODO
canvas.text(origen, text, font=comicFont, fill ="white")
#TODO

#Show image and save it
meme.show()
meme.save(memeresult)