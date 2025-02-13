def say_s():
    n = int(input("Input n:"))
    if n < 0:
        print("Error")
    else:
        for i in range(n):
            print('*' * (n-i))


say_s()
