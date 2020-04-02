from PIL import Image


def make_preview(name):
    im = Image.open(name)
    im = im.resize((250, 250))
    im.save(name)


make_preview(input())
