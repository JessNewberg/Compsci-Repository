word1 = input ("Please input word 1.")
word2 = input ("Please input word 2.")
word3 = input ("Please input word 3.")
word4 = input ("Please input word 4.")
word5 = input ("Please input word 5.")
word6 = input ("Please input word 6.")
word7 = input ("Please input word 7.")
word8 = input ("Please input word 8.")
word9 = input ("Please input word 9.")
word10 = input ("Please input word 10.")

List = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10]
Vowel = ("a", "e", "i", "o", "u","A", "E", "I", "O", "U")
for word in List:
    if word[0] in Vowel:
        print ("True")
    else:
        print ("False")


     
     
