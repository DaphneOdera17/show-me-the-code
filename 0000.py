from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/Windows/fonts/Arial.ttf', size=100)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-120, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')

    return 0

if __name__ == '__main__':
    img = Image.open("C:\\Users\\Birdy\\Pictures\\头像.jpg")
    add_num(img)