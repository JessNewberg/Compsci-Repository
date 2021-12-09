Temp = int (input ("What temperature is it outside?"))
Unit =(input ("Is this in Fahrenheit(F) or Celsius(C)?"))

if Unit == "F":
    result = ((Temp-32)* 95/9)
    print (result)

elif Unit == "C":
    result = ((Temp * (9/5))+32)
    print (result)

else:
    print ("Uh Oh! No valid input.")




    
