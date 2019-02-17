from colorama import init
from colorama import Fore, Back, Style

# init colorama
init()

def report():
    print(Back.GREEN + 'mymodule.py' + Style.RESET_ALL)