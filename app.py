from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

image = Image.open('base.jpg')
desehar = ImageDraw.Draw(image)
fonte_corpo = ImageFont.truetype('acme-regular.ttf',100)
fonte_credito = ImageFont.truetype('acme-regular.ttf',50)



desehar.text((1050,1000),"Testando Code",(255,255,255),font=fonte_corpo)
image.save('output.jpg')