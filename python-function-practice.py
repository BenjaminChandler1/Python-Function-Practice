def max_num(x, y, z):
    list = [x, y, z]
    return max(list)

def mult_list(thisList):
    result = 1
    for x in thisList:
        result = result * x
    return result

def rev_string(word):
    txt = word [::-1]
    print(txt)

def num_within(num, b, e):
    if (b <= num <= e):
        print("True")
    print("False")

def pascal(n):
    for i in range(1, n+1):
        for j in range(0, n-i+1):
            print(' ', end='')
            C = 1
        for j in range(1, i+1):
            print(' ', C, sep='', end='')
            C = C * (i - j) // j
        print()

max_num(1,8,2)
mult_list([4, 8, 5])
rev_string("string")
num_within(5, 1, 10)
pascal(5)