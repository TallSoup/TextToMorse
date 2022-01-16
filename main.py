with open('morse.txt', 'r') as file:
    morse_list = file.readlines()

# list comp to clean up morse_list
clean_morse_list = [x.replace("\t", " ").replace("\n", "") for x in morse_list]

# dict comp to create dict from cleaned up list
morse_dict = {x.split()[0]: x.split()[1] for x in morse_list}

# request user input
string_to_convert = input("Enter your text to be converted to Morse Code:\n").upper()

# convert to and output morse code
output = ""
print(f"String entered to convert: {string_to_convert}\n")
for x in string_to_convert:
    if x == " ":
        output += "Space between words: 7 second pause\n"
    elif x not in morse_dict:
        output += f"{x}: (character not found)\n"
    else:
        output += f"{x}: {morse_dict[x]} \n"

print(output)
