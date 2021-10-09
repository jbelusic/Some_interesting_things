
def main():
    a: int = 1
    print(type(a), id(a)) # <class 'int'> 11563136

    a = "t"
    print(type(a), id(a)) # <class 'str'> 22828992"

if __name__ == '__main__':
    main()
