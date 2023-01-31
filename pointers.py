# pointers

num1 = 11
num2 = num1  # points to num1 memory address

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

num2 = 22  # Num2 now points to a different memory address

print("After num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

print("---------------------------------")

dict1 = {
    'value': 11
}
dict2 = dict1  # dict1 and dict2 point to the same memory address

print("Before dict2 value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))


dict2['value'] = 22  # dict1 and dict2 point to the same memory address

print("After num2 value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
