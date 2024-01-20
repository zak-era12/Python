#Python program to implement various file operations.

'''fo = open("file1.txt", "r")
print ("Name of the file: ", fo.name)
print ("Closed or not : ", fo.closed)
print ("Opening mode : ", fo.mode)'''

#WRITE A PROGRAM TO READ AN ENTIRE TEXT FILE.
'''# read the file
read_content = fo.read()
print("\n",read_content)

#WRITE A PROGRAM TO APPEND TEXT TO A FILE AND DISPLAY THE TEXT
def main():
    fo2=open("sample.txt","r+")
    rc2=fo2.read()
    print(rc2)
    fo2.write("This is the appended text")
    fo2.close()
main()'''


#WRITE A PROGRAM TO READ LAST N LINES OF A FILE.
'''import linecache
fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)


n = int(input("Enter Last n lines TO Read : "))
for i in range(num_lines,num_lines-n,-1):
	print(linecache.getline(fname,i),end="")'''


#OR
'''
with open('file1.txt', 'r') as f:
    last_line = f.readlines()[-1]
print(last_line)

'''

