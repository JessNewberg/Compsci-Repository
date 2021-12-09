def my_min (a:float, b:float):
    if a > b:
        return b
    else:
        return a

def temp_convert (a:float, b:str):
    if b == "F":
        result = ((a-32)* (5/9))
        print (result)
    elif b == "C":
        result = ((a * (9/5))+32)
        print (result)
    else:
        print ("Uh Oh! No valid input. a is your Temperature, b is F or C.")

def c_to_f (a:float):
    print ((a * (9/5))+32)

def f_to_c (a:float):
    print ((a-32)* (5/9))

def military_time_converter (Hours:int, Minutes:str):
    if Hours < 0:
        print ("Invalid Time: Has to be above Zero!")
    if Hours > 24:
        print ("Invalid Time: Has to be below Twenty Four!") 
    if Minutes < 0:
        print ("Invalid Time: Has to be above Zero!")
    if Minutes > 60:
        print ("Invalid Time: Has to be below Sixty!")
    if Hours > 12:
        result = Hours - 12
        print (result, ":", Minutes, "PM")
    else:
        print (Hours, ":", Minutes, "AM")

def is_divisible_by (a:float,b:float):
    c = a % b
    if c == 0:
        print ("A is divisible by B.")
    else:
        print ("A is not divisible by B.")

def pig_latin_word (W:str):
    Consonant = ("b", "c", "d", "f", "g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
    Vowel = ("a", "e", "i", "o", "u")
    Length = len(W)
    First = str (W[0])
    Word2 = (W[0:Length])
    Minus = W[1:Length]
    if First in Consonant:
        PL = Minus + First + "ay"
        print (PL)
    elif First in Vowel:
        PL = W + "way"
        print (PL)
    else:
        print ("Uh Oh! You entered either a non-letter character, or an uppercase character. Try again.")
    if " " in W:
        print ("Uh Oh! Thats more than one word. Try again.")

def star_pyramid (a:int):
    for i in range(0,a):
        print ("*"*i)
        print ("\n")

def random_list (i:int):
    while i > 0: 
        import random
        n = random.randint(0,1000)
        print(n)
        i = i-1

def starts_with_vowel (a:str):
    List = [a]
    Vowel = ("a", "e", "i", "o", "u","A", "E", "I", "O", "U")
    for a in List:
        if a[0] in Vowel:
            print ("True")
        else:
            print ("False")
    
