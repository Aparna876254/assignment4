text= input("Enter text to write to the file: ")
file=open('file_data.txt','w')
file.write(text + "\n")
print("Data successfully written to output.txt.")

append = input("Enter additional text to append: ")
file=open("file_data.txt", "a")
file.write(append + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("file_data.txt", "r") as file:
    final = file.read()
    print(final)
