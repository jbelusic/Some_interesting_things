from contextlib import suppress

def main():
    try:
        lst = [1, 2, 3, 4, 5]
        lst[10]
    except IndexError:
        #raise
        pass

    with suppress(IndexError):
        lst = [1, 2, 3, 4, 5]
        lst[10]

if __name__ == '__main__':
    main()
