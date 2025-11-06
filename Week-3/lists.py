# List
# ['item1', 'item2', 'item3']


shopping_list = ['milk', 'eggs', 'bread', 'butter']
print(shopping_list)
print(type(shopping_list))
print(len(shopping_list))

nums = [1, 2, 3, 4, 5]
print(nums)

names = ['Alice', 'Bob', 'Charlie']
print(names)

mixed_list = [1, 'two', 3.0, True]
print(mixed_list)

# Accessing list items
print(shopping_list[0])  # First item
print(shopping_list[2])  # Third item

# Modifying list items
shopping_list[1] = 'organic eggs'
print(shopping_list)

# Mixed data types
data = [42, 'hello', 3.14, False, [1, 2, 3]]

num= [1, 2, 12]
print(num[0])  # Accessing first item
print(len(num))  # Length of the list

last_index = len(num) - 1
print(num[last_index])  # Accessing last item using length

print(num[-1])  # Accessing last item using negative index
print(num[-2])  # Accessing second last item using negative index
print(num[-3])  # Accessing third last item using negative index
#print(num[-4])  # This will raise an IndexError

#sclicing
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[0:3]) 
print(fruits[2:5]) 
print(fruits[2:])
print(fruits[::-1])  # Reversing the list
print(fruits[-3:])  # Last three items
print(fruits[:3])  # First three items
print(fruits[:])  # Entire list
print(fruits[3:])
print(fruits[-3:])
print(fruits[-3::])

# Modifying lists
numbers = [1, 2, 3, 4, 5]
numbers[0] = 10  
print(numbers)

numbers[2] = 33
print(numbers)

# Removing items
numb = [10, 20, 30, 40, 50]
numb.pop()  # Removes last item
print(numb)

nmb = [1, 2, 3, 4, 5]
nmb.pop(0)  # Removes item at index 0
print(nmb)


nmb = [1, 2, 3, 4, 5]
nmb.pop(1)  # Removes item at index 1
print(nmb)

# insert
colors = ['red', 'green', 'blue']
colors.insert(1, 'yellow')  # Insert 'yellow' at index 1
print(colors) 

colors.insert(2, 100)  
print(colors) 
