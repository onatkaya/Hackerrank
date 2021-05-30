def minion_game(string):
    total_subtr_num = (len(string) * (len(string)+1))// 2
    
    vowels = 'AEIOU'

    kevin_score = 0 # (Team Vowels)
    
    # Instead of running a nested loop, we are going to look iterate the string once. 
    # If our string length is k, there are k different substrings for that.
    # So, keeping that in mind we, will look at all substrings (including multiples).
    # len(s) - i means there are that many substrings in the string of string[i:]
    # If we collect these len(s) - i collectively, it will equal to total_subtr_num
    # However, we want to distinguish them whether the first the letter is a vowel or
    # not, so we put a if statement as well. 

    for i in range(len(string)):
        if(string[i] in vowels):
            kevin_score += len(s) - i
        else:
            continue

    # total_substr_num = kevin_score + stuart_score
    stuart_score = total_subtr_num - kevin_score 

    #printing the winner
    if(stuart_score > kevin_score):
        print("Stuart", stuart_score)
    elif(kevin_score > stuart_score):
        print("Kevin", kevin_score)
    elif(stuart_score == kevin_score):
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)