print ("A - Add Record")
print ("B - View Records")
print ("C - Clear all Records")
print ("D - Exit")

choice = "" 

while choice.upper() != 'D' :
    choice = input ("Enter Selection [A, B, C, D]: ")
    if (choice.upper() == 'A'):
        print ("Add  Record")
        addRec()
    elif (choice.upper() == 'B'):
        print ("View Records")
        viewRec ()
    elif (choice.upper() == 'C'):
        print ("Clear Records")
    elif (choice.upper() == 'D'):
        print ("Thank you! ")