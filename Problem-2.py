#ODD NUMBER
def odd_num(a):
    list = []
    for i in range(a):
        list.append(2*i+1)
        print(f"Input a = {i},Then output is: {list}")
    
num = int(input("Required ODD Numbers are :"))
odd_num(num)