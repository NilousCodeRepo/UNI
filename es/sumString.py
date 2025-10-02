def main():
    string = "12345"
    a = 0

    for i in string:
        a += int(i) # a = a + 1
    print(a)

    sum(map(int, string))

main()
