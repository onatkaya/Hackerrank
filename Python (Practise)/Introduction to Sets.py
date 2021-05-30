def average(array):
    # your code goes here
    my_set = set(array)
    total = 0

    for a in my_set:
        total += a
    
    return(total/len(my_set))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)