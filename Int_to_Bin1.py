def Int_to_Bin(num):
    converted =''
    if num==0:
        converted='0'+ converted
    else:
        while num >0:
            converted = str(num%2)+converted
            num=num//2
    print (converted)
