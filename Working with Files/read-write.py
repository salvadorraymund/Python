# f = open("textfile.txt", "w+")
# two arguements by the open method
# first is the name of the file to work on
# second is the type of access you'd like to have
# w means write; + sign means create
# clears an entire file

f = open("textfile.txt", "r")
# a means append data to an existing file
# for i in range(10):
#     f.write("This is line " + str(i) + "\r\n")
# f.close()
# \n is an escape character

if f.mode == "r":
    # contents = f.read()
    # print(contents)
    fl = f.readlines()
    for x in fl:
        print(x)
