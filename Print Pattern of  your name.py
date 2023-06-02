# Python3 code to print input in your own font

# To take input from User
name = input("Enter your name: ")

length = len(name)
l = ""

for x in range(0, length):
	c = name[x]
	c = c.upper()
	
	if (c == "A"):
		print("..######..\n..#....#..\n..######..", end = " ")
		print("\n..#....#..\n..#....#..\n\n")
		
	elif (c == "B"):
		print("..######..\n..#....#..\n..#####...", end = " ")
		print("\n..#....#..\n..######..\n\n")
		
	elif (c == "C"):
		print("..######..\n..#.......\n..#.......", end = " ")
		print("\n..#.......\n..######..\n\n")
		
	elif (c == "D"):
		print("..#####...\n..#....#..\n..#....#..", end = " ")
		print("\n..#....#..\n..#####...\n\n")
		
	elif (c == "E"):
		print("..######..\n..#.......\n..#####...", end = " ")
		print("\n..#.......\n..######..\n\n")
		
	elif (c == "F"):
		print("..######..\n..#.......\n..#####...", end = " ")
		print("\n..#.......\n..#.......\n\n")
		
	elif (c == "G"):
		print("..######..\n..#.......\n..#.####..", end = " ")
		print("\n..#....#..\n..#####...\n\n")
		
	elif (c == "H"):
		print("..#....#..\n..#....#..\n..######..", end = " ")
		print("\n..#....#..\n..#....#..\n\n")
		
	elif (c == "I"):
		print("..######..\n....##....\n....##....", end = " ")
		print("\n....##....\n..######..\n\n")
		
	elif (c == "J"):
		print("..######..\n....##....\n....##....", end = " ")
		print("\n..#.##....\n..####....\n\n")
		
	elif (c == "K"):
		print("..#...#...\n..#..#....\n..##......", end = " ")
		print("\n..#..#....\n..#...#...\n\n")
		
	elif (c == "L"):
		print("..#.......\n..#.......\n..#.......", end = " ")
		print("\n..#.......\n..######..\n\n")
		
	elif (c == "M"):
		print("..#....#..\n..##..##..\n..#.##.#..", end = " ")
		print("\n..#....#..\n..#....#..\n\n")
		
	elif (c == "N"):
		print("..#....#..\n..##...#..\n..#.#..#..", end = " ")
		print("\n..#..#.#..\n..#...##..\n\n")
		
	elif (c == "O"):
		print("..######..\n..#....#..\n..#....#..", end = " ")
		print("\n..#....#..\n..######..\n\n")
		
	elif (c == "P"):
		print("..######..\n..#....#..\n..######..", end = " ")
		print("\n..#.......\n..#.......\n\n")
		
	elif (c == "Q"):
		print("..######..\n..#....#..\n..#.#..#..", end = " ")
		print("\n..#..#.#..\n..######..\n\n")
		
	elif (c == "R"):
		print("..######..\n..#....#..\n..#.##...", end = " ")
		print("\n..#...#...\n..#....#..\n\n")
		
	elif (c == "S"):
		print("..######..\n..#.......\n..######..", end = " ")
		print("\n.......#..\n..######..\n\n")
		
	elif (c == "T"):
		print("..######..\n....##....\n....##....", end = " ")
		print("\n....##....\n....##....\n\n")
		
	elif (c == "U"):
		print("..#....#..\n..#....#..\n..#....#..", end = " ")
		print("\n..#....#..\n..######..\n\n")
		
	elif (c == "V"):
		print("..#....#..\n..#....#..\n..#....#..", end = " ")
		print("\n...#..#...\n....##....\n\n")
		
	elif (c == "W"):
		print("..#....#..\n..#....#..\n..#.##.#..", end = " ")
		print("\n..##..##..\n..#....#..\n\n")
		
	elif (c == "X"):
		print("..#....#..\n...#..#...\n....##....", end = " ")
		print("\n...#..#...\n..#....#..\n\n")
		
	elif (c == "Y"):
		print("..#....#..\n...#..#...\n....##....", end = " ")
		print("\n....##....\n....##....\n\n")
		
	elif (c == "Z"):
		print("..######..\n......#...\n.....#....", end = " ")
		print("\n....#.....\n..######..\n\n")
		
	elif (c == " "):
		print("..........\n..........\n..........", end = " ")
		print("\n..........\n\n")
		
	elif (c == "."):
		print("----..----\n\n")



# Output
'''
 .######..
..#....#..
..######..
..#....#..
..#....#..


..#...#...
..#..#....
..##......
..#..#....
..#...#...


..######..
..#....#..
..######..
..#....#..
..#....#..


..######..
..#.......
..######..
.......#..
..######..


..#....#..
..#....#..
..######..
..#....#..
..#....#..
'''


