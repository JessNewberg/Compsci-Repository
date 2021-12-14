""" this code converts an integer of any length to binary. """
def Int_to_Bin(num):
    converted =''
    if num==0:
        converted='0'+ converted
        """When the number is , a 0 is added and the code moves onto
            the next character of the binary. """
    else:
        while num >0:
            converted = str(num%2)+converted
            num=num//2
            """While a number isnt equal to 0, it keeps being divided by 2. Every time it is divisible, a 1 is added."""
    print (converted)
""" this is the only way to get this to work in Visual Studio. Haven't quite figured it out yet."""
def main():
    Int_to_Bin (10)

main()