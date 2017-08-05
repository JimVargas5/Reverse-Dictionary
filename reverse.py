#Jim Vargas reverse

def reverse(dictionary):
    copy = dictionary.copy()
    keys = copy.keys()
    Nvalues = []
    for thing in keys:
        Nvalues = Nvalues + [thing]
    values = copy.values()
    Nkeys = []
    for thing in values:
        Nkeys = Nkeys + [thing]

    NewDic = {}
    for thing in range(len(Nkeys)):
        NewDic[Nkeys[thing]] = Nvalues[thing]
    return NewDic


def main():
    #AKey = input("Input a key:\n>>> ")
    InputDictionary = {}
    while True:
        Akey = input("Input a key:\n>>> ")
        if Akey == "":
            break
        else:
            AValue = input("Input a value for "+str(Akey)+":\n>>> ")
            InputDictionary[Akey] = AValue
            continue
    print("Reversed dictionary:")
    print(reverse(InputDictionary))


if __name__ == '__main__':
    main()

#print(reverse({'Dylan':'Bob', 2:1}))