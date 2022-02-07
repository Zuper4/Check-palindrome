print("\nThis program checks if the string is a palindrome or not.")
print("A palindrome is a word or sentence that sounds the same when you read it backwards.")
print("For example : level or radar or even racecar")

word = str(input("\nI will check if this is a palindrome :"))

word = word.lower()

rev_word = reversed(word)

if list(rev_word) == list(word):

    print(str(word)+ " is a palindrome.")

else:

     print(str(word)+ " is not a palindrome.")

