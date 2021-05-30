def print_formatted(number):
    # your code goes here
    for i in range (1, number + 1):
        my_len = len(str(bin(number))[2:])
        
        print(str(i).rjust(my_len), str(oct(i))[2:].rjust(my_len), str(hex(i))[2:].upper().rjust(my_len), str(bin(i))[2:].rjust(my_len) )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)