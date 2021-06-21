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
rep=16

#Loads font and defines size
comicFont = ImageFont.truetype('/usr/share/fonts/opentype/comic-neue/ComicNeue_Bold.otf', textsize)

#Opens meme image
meme = Image.open(memeimage).convert('RGB')
canvas = ImageDraw.Draw(meme)

#write Text replace TODO with loop

for  i in range(rep):
    canvas.text((origen[0],origen[1]+40*i), text, font=comicFont, fill ="white")


#Show image and save it
meme.show()
meme.save(memeresult)