# It took me while to figure out how to get the height.

blocks = int(input("Type in the number of blocks: "))
blocks_needed = 1
height = 0

while blocks > blocks_needed:
    blocks -= blocks_needed
    blocks_needed += 1
    height += 1

print("Height of the pyramid:", height)
