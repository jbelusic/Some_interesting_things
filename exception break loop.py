
from time import sleep

class GenericError(Exception):
    pass

def test(test_var):
    if test_var == 5:
        raise GenericError()
    return test_var


def main():
    print("Start")
    var = 0
    try:
        while True:
            var += 1
            sleep(1)
            a = test(var)
            print(a)
    except Exception as e:
        print("exception",str(e))

    print("End")

if __name__ == '__main__':
    main()
