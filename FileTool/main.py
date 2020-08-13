from FileTool import File

file_1 = File("sperma")
file_2 = File("semen")

file_3 = file_1 + file_2
print(file_3.read())

for i in file_3:
    print(i)

print(file_3[1])
print(file_3)