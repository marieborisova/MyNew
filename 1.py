def squared():
    for i in range(1, 10):
        for j in range(1, 10):
            a = (i * 10 + j) ** 2
            if j != 9:
                if a < 1000:
                    print(a, end='  ')
                else:
                    print(a, end=' ')
            else:
                print(a, end='')
        print()


squared()
