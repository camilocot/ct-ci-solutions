# Given a string and a set of delimiters, reverse the words in the string while maintaining the relative order of the delimiters.
# https://www.geeksforgeeks.org/reverse-a-string-without-affecting-special-characters/

"""
1) Let input string be 'str[]' and length of string be 'n'
2) l = 0, r = n-1
3) While l is smaller than r, do following
    a) If str[l] is not an alphabetic character, do l++
    b) Else If str[r] is not an alphabetic character, do r--
    c) Else swap str[l] and str[r]
"""


def reverseSting(text):
    index = -1

    # Loop from last index untill half of the index
    for i in range(len(text)-1, int(len(text)/2), -1):

        # match character is alphabet or not
        if text[i].isalpha():
            temp = text[i]
            while True:
                index += 1
                if text[index].isalpha():
                    text[i] = text[index]
                    text[index] = temp
                    break
    return text


# Driver code
string = "a!!!b.c.d,e'f,ghi"
print("Input string: ", string)
string = reverseSting(list(string))
print("Output string: ", "".join(string))
