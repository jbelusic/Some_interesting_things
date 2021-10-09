
def main():
    names = ['Bob', 'Alice', 'Guido']
    for index, value in enumerate(names):
        print(f'{index}: {value}')

    for index, value in enumerate(names, 1):
        print(f'{index}: {value}')

    l = list(enumerate(names))
    print(l)

    l1 = list(enumerate(names, 1))
    print(l1)

if __name__ == '__main__':
    main()
