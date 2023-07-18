import numpy as np

print(np.cos(3))
print(np.pi)

usedspace = []

usedspace.append((1, 1))
usedspace.append((2, 2))
usedspace.append((3, 3))
usedspace.append((4, 4))
usedspace.append((5, 6))

for check in usedspace:
    if check == (6, 5):
        print("yea")

print(usedspace)
print(usedspace.__len__()-1)
len = usedspace.__len__()-1
save = usedspace[len]
print("Save = ", save[2])
