# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

    word = str(input("Enter word: \n").casefold())
    anagram = str(input("Enter anagram: \n").casefold())

 # To remove spaces, ",", ".", " ' "
    rearrWord = ''.join(sorted(word)).strip().replace(".", "").replace(",", "").replace(" ", "").replace("'", "")     # rearranging the word
    rearrAnag = ''.join(sorted(anagram)).strip().replace(".", "").replace(",", "").replace(" ", "").replace("'", "")     #  rearranging the anagram
    # print(rearrWord, rearrAnag)
   
    if rearrWord == rearrAnag:
        return True
    else:
        return False

print(find_anagram("word", "anagram"))

startFinding = True
while startFinding:
    
    find_again = str(input("Would you like to try something else? type (y or n) :  \n"))
    if find_again == "n": 
        startFinding = False 
        print("Bye...")
    elif find_again == "y": 
         print(find_anagram("word", "anagram"))       
    else:
        startFinding = False
        print("Wrong Input")
   
