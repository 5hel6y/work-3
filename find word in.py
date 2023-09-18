file1 = open("lesson05_cats_of_ulthar.txt", "r")
word = "кошка"
words = file1.readlines()
for i in words:
    if word in i:
        print(i)
file1.close()
