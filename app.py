from flask import Flask, Response, request
from colorama import Fore, Back, Style

app = Flask(__name__)

def answer_html():
    if "text/html" not in request.headers.get("Accept", ""):
        return False
    return True

def simple():
    print(Fore.RED + 'some red text')
    print(Back.GREEN + 'and with a green background')
    print(Style.DIM + 'and in dim text')
    print(Style.RESET_ALL)
    print('back to normal now')


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
    print(result)
    return result


@app.route("/")
def base():
    if answer_html(): 
        return "<body>Hello!</body>"
    else:
        resp = f'This is a {c("test", fg=(45,26,68))} of the {c("colorisation options", bg=(255,0,0))}'
        return Response(resp, mimetype="text/plain; charset=utf-8")
    


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
