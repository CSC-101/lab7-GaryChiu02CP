from convert import str_to_float

def gather_numbers() -> list[float]:
    array = []
    while True:
        userinput = input("Type 'done' to stop \nEnter Number Here: ")
        if userinput == "done":
            print(array)
            break
        else:
            tfloat = str_to_float(userinput)
            if tfloat == None:
                print()
            else:
                array.append(tfloat)
    return array

if __name__ == '__main__':
    gather_numbers()