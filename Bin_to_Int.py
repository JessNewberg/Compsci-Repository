"""this code converts 8 bits of binary to an integer."""
def bin_to_int(userinput:str):
    """sets up our code. we will begin by setting our number equal to 0, and saying that we
    start by observing the first digit of the binary (the first power
    of two, 2^0). Also defines length of the user's input."""
    converted = 0
    poweroftwo = 1
    i = len(userinput)

    while i>=0:
        """the number is set equal to its previous number plus either the power of two
        we are on if the digit of the binary is 1, or just the number if it is not."""
        converted += (poweroftwo * (converted[i]))
        poweroftwo * 2
        i = i- 1
    return converted
