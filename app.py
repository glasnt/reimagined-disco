from flask import Flask, Response, request
from colorama import Fore, Back, Style
from PIL import Image
from ih.chart import preprocess_image
from ih.palette import *

app = Flask(__name__)

def answer_html():
    if "text/html" not in request.headers.get("Accept", ""):
        return False
    return True


def c(text, bg=None, fg=None):
    def color(rgb, code):
        if not rgb:
            return ""
        R, G, B = rgb
        return f"\033[{code};2;{R};{G};{B}m"
        
    def foreground(rgb=None):
        return color(rgb, "38")

    def background(rgb=None):
        return color(rgb, "48")

    def reset():
        return "\033[0;00m"

    result = foreground(fg) + background(bg) + text + reset()
    return result


@app.route("/")
def base():
    if answer_html(): 
        return "<body>Hello!</body>"
    else:
        resp = f'This is a {c("test", fg=(45,26,68))} of the {c("colorisation options", bg=(255,0,0))}'
        return Response(resp, mimetype="text/plain; charset=utf-8")
    
@app.route("/img/<img>")
def img(img):
    im = Image.open(img)
    res = ""
    render = request.args.get("render", False)
    if render:
        im = im.resize((im.height * 2, im.width), Image.NEAREST)

    im = preprocess_image(im, palette=get_palette("wool"), colorlimit=16)
    for x in range(0, im.width):
        for y in range(0, im.height):
            rgb = im.getpixel((x,y))
            if render:
                res += c(" ", bg=rgb[:3])
            else:
                res += c("*", fg=rgb[:3])+ " "
        res += "\n"
    return Response(res, mimetype="text/plain; charset=utf-8")

if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
