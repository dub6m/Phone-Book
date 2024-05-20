import PhoneBook

PhoneBook.createDB()  
choice = 0
PhoneBook.menu()
while choice !=7:
    choice = PhoneBook.getChoice() 
    PhoneBook.execute(choice)
    
