# Dictionaries are used to store data values in kry:value pairs.
# A dictionaries is a collection which is orderd, changeable and not allow duplicates.

thisdict = {
    1:"one",
    2: "two",
    3:"three"
}

print(thisdict)
print(thisdict[1])
for key in thisdict:
    print(key)

for value in thisdict.values():
    print(value)