# Situation: There are three building with 15 floors and 20 rooms.
rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]



# Check how many rooms are available:
vacancy = 0
for room_number in range(20):
   if not rooms[2][14][room_number]:
      vacancy += 1
print("The number of rooms available is ", vacancy)