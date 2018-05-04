


word = input("Enter a word to test if its a palindrome: ")

#for c in test_string:
#    print(c)

#above is a for each loop. 
#either of these solutions work
#bellow is a for loop
#for index in range(0, len(word)):
#    print(word[index])
#def is_palindrome():
#    for index in range(len(word)-1,-1,-1):
#        print(f"reversed_word = {reversed_word} and word[index] = {word[index]}")
#        reversed_word += word[index]
#
#    if word == reversed_word:
#        print("palindrome")
#    else:
#        print:("Not a Palindrome")
#is_palindrome()

#alternate way of doing the same thing
for index in range(len(word)-1,-1,-1):
    reversed_word += word[index]
return word == reversed_word

if is_palindrome(word):
    print("palindrom")
else:
    print("not a palindrome")