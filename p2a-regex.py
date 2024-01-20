#Regular Expressions

'''import re
 
Nameage = '''
#Janice is 22 and Theon is 33
#Gabriel is 44 and Joey is 21
'''
 
ages = re.findall(r'd{1,3}', Nameage)
names = re.findall(r'[A-Z][a-z]*',Nameage)
 
ageDict = {}
x = 0
for eachname in names:
    ageDict[eachname] = ages[x]
    x+=1
    print(ageDict)
'''


#RE Example 1
import re
'''
#find a word starting with a ending with s 
pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")'''

#RE Example 2

# Program to extract numbers from a string

string = 'hello 12 hi 89. Howdy 34'
pattern = '\d+'

result = re.findall(pattern, string) 
print(result)

#RE Example 3

# Program to remove all whitespaces
import re
# multiline string
string = 'abc 12\
de 23 \n f45 6'
# matches all whitespace characters
pattern = '\s+'
# empty string
replace = ''
#substitute the space with an empty string
new_string = re.sub(pattern, replace, string)
print(new_string)




