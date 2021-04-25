input_file = open("Input Text File", "r")
print(input_file.read())

output_file = open("Compressed version", "w+")
for i in range(10):
    output_file.write("This is line %d\r\n" % (i + 1))

input_file.close()
output_file.close()
