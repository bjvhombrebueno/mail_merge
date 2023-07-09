#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as letter:
    my_letter = letter.read()

with open ("./Input/Names/invited_names.txt") as invited:
    newguest = []
    guests = invited.readlines()
    for guest in guests:
        guest = guest.strip()
        newguest.append(guest)
    print(newguest)

for guest in newguest:
    rev_letter = my_letter.replace("[name]",guest)
    with open(f"./Output/ReadyToSend/{guest}.txt", mode="w") as new_letter:
        new_letter.writelines(rev_letter)
    #my_letter = orig
