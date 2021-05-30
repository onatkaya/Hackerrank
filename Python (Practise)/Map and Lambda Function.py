cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    my_list = []

    for a in range(n):
        if(a == 0):
            my_list.append(0)
        elif(a == 1):
            my_list.append(1)
        elif(a == 2):
            my_list.append(1)
        else:
            my_list.append(my_list[a-1] + my_list[a-2])

    return my_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))