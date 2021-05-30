alp = list(map(chr, range(97, 123))) # list of the alphabet

def print_rangoli(size):
    str_len = (4 * size) - 3 # length of string to be printed for each line
    middle_letter = alp[size-1] # the letter that is going to be in the middle for each line

    alp_str = ""

    solution_list = [] # keeping all the upper-lines

    for k in range(1, size+1): # set-back
        alp_str = ""
        for i in range(1, k+1): # constructing loop, little-incerement
            alp_str = alp_str + alp[size-1-k+i] # building the right part of the string

        alp_str = alp_str[len(alp_str)-1:0:-1] + alp_str # added the left part of the string (the symmetrical part)

        temp_list = list(alp_str) # distributing the letters of alp_str to a string

        new_alp_str = '-'.join(alp_str) # concatenating the letters with '-'

        # print(new_alp_str.center(str_len, '-'))
        temp_line = (new_alp_str.center(str_len, '-'))

        solution_list.append(temp_line)

    solution_list_rev = solution_list[::-1] # keeping all the lower lines
    solution_list.pop() # popping the longest line, we don't want to print that twice

    #printing all the lines
    for i in solution_list:
        print(i)
    for n in solution_list_rev:
        print(n)
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)