Hours = int (input ("What hour is it? (Military)"))
if Hours < 0:
    print ("Invalid Time: Has to be above Zero!")
if Hours > 24:
    print ("Invalid Time: Has to be below Twenty Four!") 
Minutes = int (input ("What minute of the hour is it?"))
if Minutes < 0:
    print ("Invalid Time: Has to be above Zero!")
if Minutes > 60:
    print ("Invalid Time: Has to be below Sixty!")

if Hours > 12:
    result = Hours - 12
    print (result, ":", Minutes, "PM")

else:
    print (Hours, ":", Minutes, "AM")
    
