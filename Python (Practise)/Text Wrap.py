import textwrap

def wrap(string, max_width):
    my_list = list(string)

    i = max_width

    while(i <= len(my_list)):
        my_list.insert(i, "\n")
        i = i + max_width + 1

    result = ''.join(my_list)

    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)