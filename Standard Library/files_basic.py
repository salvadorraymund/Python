"""Basic file operations in Python"""

# Open a file for writing data
# "w" means write
# open is a built-in function that has a required argument - the path to the file
# fp = open("textfile.txt", "r+")
# fp.write("{my_list = [i*2 for i in range(1,4)]}")
# fp.close()

# with open("textfile.txt", "r+") as reader:
#     reader.write("Hello, world! \n")
#     reader.write("test \n")

f = open('textfile.txt', 'w')
f.write('Hello, world!')
f.close()
with open('textfile.txt', 'r') as f:
    f2 = f.readlines()
    print(f2)
with open('textfile.txt', 'a') as f:
    # f.write('\nHappy campers!')
    line_number = 0
    favorite_names = ['Dora', 'Ethan', 'Wesley', 'Lizzie', 'Alex']
    for name in favorite_names:
        line_number += 1
        f.write("\n")
        f.write(name)
        print('{}. {}'.format(line_number, name))
with open('new_textfile.txt', 'w') as f:
    my_pets = ['Pug', 'Jack Russell', 'Spaniel',
               'German Shepherd', 'Bull Terrier', 'Golden Retriever']
    for pet in my_pets:
        f.write(pet)
        f.write('\n')
with open('new_textfile.txt', 'r') as f:
    line = f.readline()
    while line != '':
        print(line, end='')
        # if you are not going to include the next line, condition will always be set to True
        line = f.readline()

# using 'write' as the mode will not let you use readlines function
with open('new_textfile.txt', 'r+') as writer:
    dog_breeds = writer.readlines()
    for breed in reversed(dog_breeds):
        writer.write(breed)

with open('new_textfile.txt', 'r') as a_reader, open('textfile.txt', 'a') as a_writer:
    dog_breeds = a_reader.readlines()
    for breed in dog_breeds:
        a_writer.write(breed)

birthday_celebrants = open('employee_birthday.txt', 'w')
birthday_celebrants.write('name, departments, birthday month')
birthday_celebrants.write('\nJohn Smith, Accounting, November')
birthday_celebrants.write('\nErica Meyers, IT, March')
birthday_celebrants.close()

with open('employee_address.txt', 'w') as a_writer:
    a_writer.write('name, address, date joined')
    a_writer.write('\njohn smith;1132 Anywhere Lane Hoboken NJ, 07030;Jan 4')
    a_writer.write('\nerica meyers;1234 Smith Lane Hoboken NJ, 07030;xMarch 2')
