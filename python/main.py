# how to import module
from mymodule import report

# how to import package
from MyPackage import myscript
from MyPackage.SubPackage import mysubscript

def main():
    report()
    myscript.report()
    mysubscript.report()

if __name__ == '__main__':
    main()