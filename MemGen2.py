from PIL import Image, ImageDraw, ImageFont
from os import path


memefolder='images'
memename='padme.png'
outputname='meme.png'
memeimage=path.join(memefolder, memename)
memeresult=path.join(memefolder, outputname)
textsize=20

texts=[
    (40,365,"Voy a prender Python", "White"),
    (430,365,"Para mejorar el mundo, ¿verdad?", "Yellow"),
    (430,750,"Para mejorar el mundo, ¿verdad?", "Yellow")
    ]

#Loads font and defines size
comicFont = ImageFont.truetype('/usr/share/fonts/opentype/comic-neue/ComicNeue_Bold.otf', textsize)


#Opens meme image
meme = Image.open(memeimage).convert('RGB')
canvas = ImageDraw.Draw(meme)

#write Text replace TODO with loop

#TODO
for text in texts:
    canvas.text((text[0],text[1]), text[2], font=comicFont, fill =text[3])

#TODO

#Show image and save it
meme.show()
meme.save(memeresult)