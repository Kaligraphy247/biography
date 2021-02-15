# Biography info
import time, os

print("I can surmarize your Biography!!")
time.sleep(1.3)
print("Fill in the data below to get started")
time.sleep(1.5)
name = input("What is your Name: ")
time.sleep(0.5)
other_names = input("Any other names? (none? type 'NO'): ")
time.sleep(0.5)
surname = input("Surname (I'm assume you have that 😉): ")
time.sleep(0.5)
dob = input("When were you born?: ")
time.sleep(0.5)
address = input("Where do you live?: ")
time.sleep(0.5)
goals = input("What are your Personal goals?: ")
time.sleep(0.5)
print("Surmarizing ...\n")
time.sleep(2)


# Displaying summary
if other_names.lower() == 'no':
    biography = (f"Name: {name.capitalize()} {surname.capitalize()}.\nDate of birth: {dob}.\nAddress: {address.capitalize()}.\nPersonal Goals: {goals.capitalize()}.\n")

else:
    biography = (f"Name: {name.capitalize()} {other_names.capitalize()} {surname.capitalize()}.\nDate of birth: {dob}.\nAddress: {address.capitalize()}.\nPersonal Goals: {goals.capitalize()}.\n")
print(biography)
time.sleep(1.5) #adjust this time

# Exporting and saving
export_biography = input("Do you wish to export this? y/n: ")
if export_biography == 'y':
    bio_export_name = input("What would you like to call this file?: ")
    with open(f'{bio_export_name}.txt', 'a') as bio_export:
        bio_export.write(biography)
    print("Exporting...")
    time.sleep(1)
    print(f"Success!!, exported to '{os.getcwd()}' as '{bio_export_name}.txt'.")
    time.sleep(1)
    print("Have a Nice day")
else:
    print("Have a Nice day")
time.sleep(2)


