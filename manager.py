import sys
from main import run
from testing import apps



def init_test() -> None:
    for command in sys.argv:
        try:
            if command != 'manager.py':
                run(apps[command])
        except Exception as error:
            print(error)

if __name__ == '__main__':
    init_test()