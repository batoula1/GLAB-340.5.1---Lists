import random

my_list = ["apple", "banana", "cherry", "orange", "mango", "watermelon", "dragonfruit"]

#Function to create the target list randomly
def genrate_target():
    target = random.sample(my_list, random.randint(2, 5))
    return target

#Function to display the target and the current list
def display_lists(current, target):
    print("Current list:", current)
    print("Target list:", target)

#Function to allow the player to manipulate the list
def manipulte_list(current):
    print("Choose an operation:")
    print("1. Append a word to the end of the list")
    print("2. Extend the list with another list")
    print("3. Concatenate two elements in the list")
    print("4. Traverse the list and view its elements")
    print("5. Modify an element in the list")
    print("6.Insert an element at a specific index in the list")
    print("7. Pop an element from the list")
    print("8. Remove a specific element from the list")
    print("9. Sort the list in ascending or descending order")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        word = input("Enter a word to append: ")
        current.append(word)
    elif choice == 2:
        other_list = input("Enter a comma-sperated list to extend with: ").split(",")
        current.extend(other_list)
    elif choice == 3:
        index1 = int(input("Enter the index of the first element: "))
        index2 = int(input("Enter the index of the second element: "))
        if index1 >= 0 and index1 < len(current) and index2 >=0 and index2 < len(current):
            current[index1] += current[index2]
            del current[index2]
        else:
            print("Invalid index")
    elif choice == 4:
        print("List elements")
        for word in current:
            print(word)
    elif choice == 5:
        index = int(input("Enter the index of the lement to modify: "))
        if index >= 0 and index < len(current):
            word = input("Enter the new word: ")
            current[index] = word
        else:
            print("Invalid index")
    elif choice == 6:
        index = int(input("Enter the index to insert at: "))
        if index >= 0 and index <= len(current):
            word = input("Enter the new word: ")
            current.insert(word)
        else:
            print("Invalid index")
    elif choice == 7:
        if len(current) > 0:
            word = current.pop()
            print("Popped word:", word)
        else:
            print("List is empty")
    elif choice == 8:
        word = input("Enter a word to remove: ")
        if word in current:
            current.remove(word)
        else:
            print("Word not found in list")
    elif choice == 9: 
        ascending = input("Sort in ascending order? (y/n) ").lower() == "y"
        current.sort(reverse= not ascending)
    else:
        print("Invalid choice")
    
    return