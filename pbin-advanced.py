
print("\n\n\tPoint to be noted:-\n\tDont use spaces in the text it will show error use underscore ( _ ) instead")

l = []
text  = input("\n\n\n\tEnter the text here : ")
for character in text:
    l.append(ord(character))


nl = []
for num in l:

    nl.append(bin(num))

final = " ".join(nl)


print(f"\n\n\nHere is your Binary code : {final} \n\n\n")
print("For Linux users:- To coppy the code just press ctrl + shift + c")
print("For Windows users:- To coppy the code just press ctrl + c")
print("\nMade By @Eruptedlava\n")
