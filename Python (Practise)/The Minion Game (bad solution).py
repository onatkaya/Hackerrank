def occurrence_score(sub_str, string): # calculates the time of occurrences of a substring inside the main string
    count = 0
    for a in range(0, len(string)): 
        if(string[a:a+len(sub_str)] == sub_str):
            count = count + 1
        else:
            continue
    return count

def minion_game(string):
    # finding all substrings in the given string

    sub_list = []

    for a in range(0,len(string)):
        for b in range(0,len(string)+1):
            if(string[a:a+b] not in sub_list):
                sub_list.append(string[a:a+b])
            else:
                continue


    sub_list.pop(0) # this is unnecessary ('')

    vowel_words = [word for word in sub_list if word[0] in 'AEIOU'] # substrings that start with a vowel
    #print(vowel_words)

    consonant_words = [word for word in sub_list if word[0] not in 'AEIOU'] # substrings that start with a consonant
    #print(consonant_words)

    # calculating Stuart's score (Team Consonants)
    stuart_score = 0

    for i in consonant_words:
        stuart_score = stuart_score + occurrence_score(i, string)
    
    # calculating Kevin's score (Team Vowels)
    kevin_score = 0

    for i in vowel_words:
        kevin_score = kevin_score + occurrence_score(i, string)

    #printing the winner
    if(stuart_score > kevin_score):
        print("Stuart", stuart_score)
    elif(kevin_score > stuart_score):
        print("Kevin", kevin_score)
    elif(stuart_score == kevin_score):
        print("Draw")



if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)