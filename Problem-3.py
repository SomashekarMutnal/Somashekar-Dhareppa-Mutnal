#ODD NUMBERS
def odd_num(a):
    list = []
    nxt_odd = 1  
    for i in range(1, a + 1):
        if i % 2 != 0:  
            while len(list) < i: 
                list.append(nxt_odd)
                nxt_odd = nxt_odd + 2

        print(f"Input a = {i}, Then output is: {list}")
    
num = int(input("Required ODD Numbers are: "))
odd_num(num)


