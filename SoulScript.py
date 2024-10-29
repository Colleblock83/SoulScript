#Importing the requests module to work with API's
import requests 
fl = "Welcome to \033[0;31mSoulScript!\033[0m"
middle = fl.center(130)
print(middle)
hd2 = "Made by \033[33mColleblock83\033[0m"
middle2 = hd2.center(125)
print(middle2)
hd3 = "Donation on \033[34mPayPal\033[0m: @FabioBaensch"
middle3 = hd3.center(125)
print(middle3)
print()
print()
#List with examples
for l21 in["\033[0;31mExamples\033[0m:", "○ Psalm 145:9", "○ Genesis 1:1 ", "○ Exodus 14:14"]:
    print(l21)
print()


#Function with API by bible-api.com
#---------------------------------------------------------------------------------------
def search_verse():
    url = "https://bible-api.com/" + ip1 

    ask_permission = requests.get(url)
    if ask_permission.status_code == 200:
        bible_verse = ask_permission.json()
        verses = bible_verse.get('verses')
        verse_data = verses[0]
        print(f"\033[4m{ip1}\033[0m:")
        print(f"Book Name: {verse_data['book_name']}")
        print(f"Chapter: {verse_data['chapter']}")
        print(f"Translation Name: {bible_verse['translation_name']}")
        print()
        print("The Vers says: ")
        print(f"\033[1;34m{verse_data['text']}\033[0m")
    else:
        print(f"Bible Verse not found! API Error code: {ask_permission}")


def random_verse():
    url = "https://bible-api.com/?random=verse"

    ask_persmission2 = requests.get(url)
    if ask_persmission2.status_code == 200:
        bible_verse = ask_persmission2.json()
        verses = bible_verse.get('verses')  #important so we can use the capsuled content of the verses array
        verse_data = verses[0]  #The line `verse_data = verses[0]` accesses the first element of the `verses` array, which is returned in the JSON response of the API. 
        print(f"Your random Bible Verse is: \033[4m{bible_verse['reference']}\033[0m")
        print(f"Chapter: {verse_data['chapter']}")
        print(f"Verse: {verse_data['verse']}")
        print(f"It says: \033[1;34m{verse_data['text']}\033[0m")
    else:
        print(f"CRITICAL ERROR")

#---------------------------------------------------------------------------------

print()
print()
for list in ["What do you want to do?:", "(1) \033[1;34mSearch for a Bible Verse\033[0m", "(2) \033[1;34mGive me a random Bible Verse!\033[0m", "(3) \033[0;31mEnd the program\033[0m"]:
        print(list)
print()
choice = int(input("(Choose 1,2 or 3): "))
while True:  
    if choice == 1:
        ip1 = input("\033[1;35mPlease enter the Verse you want to check up\033[0m: ")
        search_verse()
    elif choice == 2:
        random_verse()
    elif choice == 3:
        exit()
    else: 
        print("Error, invalid input!")
    print()
    for list in ["What do you want to do?:", "(1) \033[1;34mSearch for a Bible Verse\033[0m", "(2) \033[1;34mGive me a random Bible Verse!\033[0m", "(3) \033[0;31mEnd the program\033[0m"]:
        print(list)
    choice = int(input("Option: "))
    print()
    


