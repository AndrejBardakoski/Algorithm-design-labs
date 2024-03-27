nTests = int(input())

for testIter in range(nTests):

    n = int(input())
    string1 = input()

    if 'B' not in string1 and 'R' not in string1:
        string1 = 'B' + string1[1:]

    while '?' in string1:
        string1 = string1.replace('?B', 'RB').replace('?R', 'BR').replace('B?', 'BR').replace('R?', 'RB')

    print(string1)
