#Write a program that determines whether a given character is a vowel or consonant.



character=input("Enter any Character ")
result="character is vowel" if character in 'aeiou' else "character is consonant"
print(result)