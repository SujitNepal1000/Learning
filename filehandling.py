# file = open('C:\\Users\\HP\\Desktop\\myfile.txt', 'w')


# file.write('Hello World\n')
# file.write('This is my first file')

# file.close()

# #reading file content
# file = open('C:\\Users\\HP\\Desktop\\myfile.txt', 'r')
# print(file.read())

# file.close()

# file = open('C:\\Users\\HP\\Desktop\\myfile.txt', 'r')
# print(file.readlines())

# file.close()

# appending data

# file = open('C:\\Users\\HP\\Desktop\\myfile.txt', 'a')

# file.write('This is append mode\n')
# file.close()
# file = open('C:\\Users\\HP\\Desktop\\myfile.txt', 'r')
# print(file.read())

# file.close()

# reading data through loop

file = open('C:\\Users\\HP\\Desktop\\myfile.txt', 'r')

for i in file:
    print(i)


