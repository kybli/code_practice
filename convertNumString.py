def convertString (input_string):
    output = 0
    input_string = input_string.strip()
    neg = 1
    start_index = 0

    if(ord(input_string[0]) == 45 and len(input_string) > 1):
            neg = -1
            start_index = 1

    for i in range(start_index, len(input_string)):
        output *= 10
        current = ord(input_string[i]) - 48
        
        if(current >= 0 and current <= 9):
            output += current
        else:
            return None    

    return neg * output




# first line
a = "-192837404851"
result = convertString(a)

f = open("convertNumString_Output.txt","w+")
f.write(str(result))
f.close