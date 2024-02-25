#!/usr/bin/env python
# coding: utf-8

# # Part 1

# In[1]:


class Chocolate: #identify a chocolate class with attributes
    def __init__(self, chocolate_id, weight, price, chocolate_type): #initialize the chocolate object attributes
        self.ID = chocolate_id #chocolate ID
        self.weight = weight #weight of the chocolate in grams
        self.price = price #price of the chocolate (float)
        self.type = chocolate_type #chocolate flavor
        self.distributed = False  # Flag to track if the chocolate is distributed

class Student: #create a student class
    def __init__(self, name):
        self.name = name #name of the student

# define a recursive function to distribute chocolates
def distribute_chocolates_recursive(chocolates, students, index=0, distributed_chocolates=None): #takes the chocolate and studnet object as an input
    # Initialize the distributed_chocolates dictionary if not provided
    if distributed_chocolates is None:
        distributed_chocolates = {}

    # If there are more students to distribute chocolates to
    if index < len(students):# It keeps track of how many students still haven't got a chocolate yet
        # Iterate through each chocolate
        for chocolate in chocolates:
            # Check if the chocolate is not already assigned to a student
            if not chocolate.distributed:
                # Assign the chocolate to the current student and flag the chocolate is distributed
                distributed_chocolates[students[index]] = chocolate
                chocolate.distributed = True 

                # Recursively call the function for the next student
                distribute_chocolates_recursive(chocolates, students, index + 1, distributed_chocolates)

                # Reset the distributed flag after the recursive call
                chocolate.distributed = False
                break

    return distributed_chocolates

# Test case with 5 chocolates and 5 students assuming we got enough chocolates for the students
chocolates = [
    Chocolate("001", 52, 5.25, "dark"),
    Chocolate("002", 33, 3, "milk"),
    Chocolate("003", 41, 4.9, "white"),
    Chocolate("004", 50, 5.5, "caramel"),
    Chocolate("005", 21, 3.2, "peanut"),
]

students = [Student("Aisha"), Student("Amna"), Student("Hessa"),Student("Shamsa"),Student("Hind")]

# Test the recursive function
result_recursive = distribute_chocolates_recursive(chocolates, students) 

# Print the recursive result
print("Recursive result:")
for student, chocolate in result_recursive.items():
    print(f"{student.name} gets Chocolate(ID={chocolate.ID}, weight={chocolate.weight}, price={chocolate.price}, type={chocolate.type})")


# In[2]:


class Chocolate: #identify a chocolate class with attributes
    def __init__(self, chocolate_id, weight, price, chocolate_type): #initialize the chocolate object attributes
        self.ID = chocolate_id #chocolate ID
        self.weight = weight #weight of the chocolate in grams
        self.price = price #price of the chocolate (float)
        self.type = chocolate_type #chocolate flavor
        self.distributed = False  # Flag to track if the chocolate is distributed

class Student: #create a student class
    def __init__(self, name):
        self.name = name #name of the student

# define an iterative function to distribute chocolates
def distribute_chocolates_iterative(chocolates, students): #takes the chocolate and studnets objects as inputs
    # Dictionary to store the distributed chocolates with students (keys) and chocolate objects (values)
    distributed_chocolates = {}

    # Iterate through each student
    for student in students:
        # Iterate through each chocolate
        for chocolate in chocolates:
            # Check if the chocolate is not already assigned to a student
            if not chocolate.distributed:
                distributed_chocolates[student] = chocolate # Assign the chocolate to the current student
                chocolate.distributed = True
                break

    return distributed_chocolates

# Test cases with no two choclates having the same ID
chocolates = [
    Chocolate("001", 52, 5.25, "dark"),
    Chocolate("002", 33, 3, "milk"),
    Chocolate("003", 41, 4.9, "white"),
    Chocolate("004", 50, 5.5, "caramel"),
    Chocolate("005", 21, 3.2, "peanut"),
]

students = [Student("Aisha"), Student("Amna"), Student("Hessa"),Student("Shamsa"),Student("Hind")]

# Test the iterative function
distribute_chocolates = distribute_chocolates_iterative(chocolates, students)

# Print the iterative result
print("Iterative result:")
for student, chocolate in distribute_chocolates.items():
    print(f"{student.name} gets Chocolate(ID={chocolate.ID}, weight={chocolate.weight}, price={chocolate.price}, type={chocolate.type})")


# # Part 2

# In[3]:


def merge_sort(chocolates, key):
    # make sure the list has more than one element
    if len(chocolates) > 1:
        # Find the middle index of the list
        mid = len(chocolates) // 2
        
        # Split the list into two halves
        left_side = chocolates[:mid]
        right_side = chocolates[mid:]

        # Recursively call merge_sort on both halves to further divide the list
        merge_sort(left_side, key)
        merge_sort(right_side, key)

        # Initialize indices for left_side (i), right_side (j), and merged list (k)
        i, j, k = 0, 0, 0

        # Merge the two halves into a sorted list
        while i < len(left_side) and j < len(right_side):
            # Compare elements based on the specified key attribute
            if getattr(left_side[i], key) < getattr(right_side[j], key):
                # If the left element is smaller, update the original list with it
                chocolates[k] = left_side[i]
                i += 1
            else:
                # If the right element is smaller or equal, update the original list with it
                chocolates[k] = right_side[j]
                j += 1
            k += 1

        # Check if there are any remaining elements in left_side and add them to the merged list
        while i < len(left_side):
            chocolates[k] = left_side[i]
            i += 1
            k += 1

        # Check if there are any remaining elements in right_side and add them to the merged list
        while j < len(right_side):
            chocolates[k] = right_side[j]
            j += 1
            k += 1


# Using the output from the iterative chocolate distribution from part 1
# Sort chocolates by weight using Merge Sort function
merge_sort_chocolates_by_weight = list(distribute_chocolates.values())
merge_sort(merge_sort_chocolates_by_weight, key="weight")

# Sort chocolates by price using Merge Sort function
merge_sort_chocolates_by_price = list(distribute_chocolates.values())
merge_sort(merge_sort_chocolates_by_price, key="price")

# Display results
print("\nChocolates sorted by weight using Merge Sort:")
for chocolate in merge_sort_chocolates_by_weight:
    print(f"ID: {chocolate.ID}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")

print("\nChocolates sorted by price using Merge Sort:")
for chocolate in merge_sort_chocolates_by_price:
    print(f"ID: {chocolate.ID}, Weight: {chocolate.weight}, Price: {chocolate.price}, Type: {chocolate.type}")


# # Part 3

# In[4]:


def find_student_by_chocolate_property(chocolates, students, property_value, property_type):
    """
    Find the student holding a chocolate with a specified price or weight.

    Parameters:
    - chocolates: List of Chocolate objects
    - students: List of Student objects
    - property_value: The specified price or weight to search for
    - property_type: The type of property to search ('price' or 'weight')

    Returns:
    - Student object if a match is found, None otherwise
    """


    # Perform binary search to find the chocolate with the specified property value
    left, right = 0, len(chocolates) - 1

    while left <= right:
        mid = (left + right) // 2
        current_chocolate = chocolates[mid]

        if getattr(current_chocolate, property_type) == property_value:
            # Match found, retrieve the student holding this chocolate
            for student, chocolate in distribute_chocolates.items():
                if chocolate == current_chocolate:
                    return student
        elif getattr(current_chocolate, property_type) < property_value:
            left = mid + 1
        else:
            right = mid - 1

    # If no match is found
    return None

# Test Cases
# Test 1: Find student holding a chocolate with weight 50
weight_50_student = find_student_by_chocolate_property(chocolates, students, property_value=33, property_type="weight")
print("\nTest 1:")
if weight_50_student:
    print(f"Student holding chocolate with weight 50: {weight_50_student.name}")
else:
    print("No student found for chocolate with weight 50")

    

    
# Test 2: Find student holding a chocolate with price 4.9
price_4_student = find_student_by_chocolate_property(chocolates, students, property_value=4.9, property_type="price")
print("\nTest 2:")
if price_4_student:
    print(f"Student holding chocolate with price 4.9: {price_4_student.name}")
else:
    print("No student found for chocolate with price 4.9")

    
    
# Test 3: Find student holding a chocolate with weight 25 (non-existent)
weight_25_student = find_student_by_chocolate_property(chocolates, students, property_value=25, property_type="weight")
print("\nTest 3:")
if weight_25_student:
    print(f"Student holding chocolate with weight 25: {weight_25_student.name}")
else:
    print("No student found for chocolate with weight 25")

