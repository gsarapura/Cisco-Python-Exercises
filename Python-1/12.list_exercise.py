# Step 1: Create an empty list for The Beatles' members.
Beatles = []
print("Step 1:", Beatles)

# Step 2: Use append method to add Jhon Lennon, Paul McCartney and George Harrison.
Beatles.append("Jhon Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Step 2:", Beatles)

# Step 3: Use for loop and append method to add Stu Sutcliffe and Pete Best.
for i in range(2):
    member = input("First, type in Stu Sutcliffe and, then, Pete Best: ") 
    Beatles.append(member)
    assert member == "Stu Sutcliffe" or member == "Pete Best", "Type the correct member name, please."
print("Step 3:", Beatles)

# Step 4: Use del to delete Stu Sutcliffe and Pete Best.
print(len(Beatles))
del Beatles[len(Beatles) - 1]
del Beatles[len(Beatles) - 1]
print("Step 4:", Beatles)

# Step 5: Use insert method to add Ringo Starr.
Beatles.insert(len(Beatles),"Ringo Starr")
print("Step 5:", Beatles)


# Length of the list.
print("Fav", len(Beatles))