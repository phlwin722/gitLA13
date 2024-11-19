print ("A - Add Record")
print ("B - View Records")
print ("C - Clear all Records")
print ("D - Exit")

choice = "" 

while choice.upper() != 'D' :
    choice = input ("Enter Selection [A, B, C, D]: ")
    if (choice.upper() == 'A'):
        print ("Add  Record")
        addRec ()
    elif (choice.upper() == 'B'):
        print ("View Records")
        viewRec ()
    elif (choice.upper() == 'C'):
        print ("Clear Records")
        clearRec()
    elif (choice.upper() == 'D'):
        print ("Thank you! ")
def viewRec():
 file = open(filename, 'r')
 with open(filename, 'r') as read_file:
 print(read_file.read())
 read_file.close()
