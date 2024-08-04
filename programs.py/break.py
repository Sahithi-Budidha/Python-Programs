dumb=(1,2,2,3,2,6,5,2)
count=0
index = 0

while index < len(dumb):
    if dumb[index] == 2:
        count += 1
    index += 1

print("The number of 2kg dumbbells in the list is: {}".format(count))

