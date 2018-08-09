#returns True if char is 'a', 'e', 'i', 'o', or 'u'
#returns False otherwise
def char_is_vowel(char):
    if char.lower() in ['a','e','i','o','u']:
        return True
    else:
        return False


#convert a word into pig latin
#if it starts with a vowel, add 'yay' to the end
#if it starts with consonants, move all consonants before first vowel
#to the end and add 'ay' to end.
#Examples: 'pig' -> 'igpay'
#          'trash' -> 'ashtray'
#          'egg' -> 'eggyay'
def convert_to_piglatin(word):
    starts_with_vowel = char_is_vowel(word[0])
    if starts_with_vowel:
        return word + "yay"
    else:
        for i in range(len(word)):
            if char_is_vowel(word[i]):
                break
            else:
                continue
        return word[i:] + word[:i] + "ay"

if __name__=="__main__":
    #TODO: write the code for char_is_vowel, causes the following print lines to test
    print("'u' is a vowel: ", char_is_vowel('u'))
    print("'z' is a vowel: ", char_is_vowel('z'))


    #TODO: replace the pass in convert_to_piglatin with the appropriate code
    #once you have written the code uncomment these lines to test code

    print("pig in piglatin is", convert_to_piglatin("pig"))
    print("trash in piglatin is", convert_to_piglatin("trash"))
    print("egg in piglatin is", convert_to_piglatin("egg"))
