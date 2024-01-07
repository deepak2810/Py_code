#program to enter a title and the print the number of characters in the given title.

title_name = input()

count = 0

for i in title_name:
    if i == " ":
        continue
        
    count += 1



print(count)





