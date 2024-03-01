base = "abcdefghijklmnopqrstuvwxyz"
print("here are some slices")
print(base[0:3])
print(base[10:])  # all the way till the end
print(base[:10])  # all the way from the beginning
print(base[:])  # the whole string

print(base[::2])  # every other letter
print(base[5:15:3])  # from 5th character to the 14th, in steps of 3
print(base[::-1])  # the whole string backwards
