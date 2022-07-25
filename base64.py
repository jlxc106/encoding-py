# converts input string to base64
# does NOT append "=" to the end of output

DEFAULT_INPUT = "Hello World!"
# expected output = SGVsbG8gV29ybGQh

sizePerEntry = 6

mapping = {
    0: "A", 1: "B", 2: "C", 3: "D",
    4: "E", 5: "F", 6: "G", 7: "H",
    8: "I", 9: "J", 10: "K", 11: "L",
    12: "M", 13: "N", 14: "O", 15: "P",
    16: "Q", 17: "R", 18: "S", 19: "T",
    20: "U", 21: "V", 22: "W", 23: "X",
    24: "Y", 25: "Z", 26: "a", 27: "b",
    28: "c", 29: "d", 30: "e", 31: "f",
    32: "g", 33: "h", 34: "i", 35: "j",
    36: "k", 37: "l", 38: "m", 39: "n",
    40: "o", 41: "p", 42: "q", 43: "r",
    44: "s", 45: "t", 46: "u", 47: "v",
    48: "w", 49: "x", 50: "y", 51: "z",
    52: "0", 53: "1", 54: "2", 55: "3",
    56: "4", 57: "5", 58: "6", 59: "7",
    60: "8", 61: "9", 62: "+", 63: "/",
}

def encode(inputStr):
    binaryString = ''.join(format(i, '08b') for i in bytearray(inputStr, encoding ='utf-8'))
    sizeOfLastEntry = len(binaryString) % sizePerEntry
    # append 0s to the last entry if len(last entry) < 6
    if sizeOfLastEntry > 0:
        binaryString += "0" * (sizePerEntry - sizeOfLastEntry)
    
    binaryArr = [binaryString[i:i+sizePerEntry] for i in range(0, len(binaryString), sizePerEntry)]

    finalAns = ''.join(list(map(lambda entry: mapping[int(entry, 2)], binaryArr)))
    print(f"given input of {inputStr} . Base64 encoded to {finalAns} .")

def main():
    userInput = input("Enter the text you want encoded to base64: ")
    if userInput is None or userInput == "":
        print(f"Using a default input of '{DEFAULT_INPUT}'")
        userInput = DEFAULT_INPUT
    encode(userInput)

if __name__ == '__main__':
    main()
