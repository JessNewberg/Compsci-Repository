
Word = input(str("What word should be translated into Pig Latin? Start with a lowercase letter!"))
Consonant = ("b", "c", "d", "f", "g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
Vowel = ("a", "e", "i", "o", "u")
Length = len(Word)
First = str (Word[0])
Word2 = (Word[0:Length])
Minus = Word[1:Length]

if First in Consonant:
    PL = Minus + First + "ay"
    print (PL)

elif First in Vowel:
    PL = Word + "way"
    print (PL)

else:
    print ("Uh Oh! You entered either a non-letter character, or an uppercase character. Try again.")
    
if " " in Word:
    print ("Uh Oh! Thats more than one word. Try again.")
