def Hello(name):
    number = 0
    if name == "Jack":
        number = 2
        return print(f"Hello {name}, you have {number} apples")
    else:
        return print(f"Hey {name}, you don't have any apples")
    

Hello("Jack")
Hello("Jill")