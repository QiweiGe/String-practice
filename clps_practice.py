#!/usr/bin/python3

def practice():
	rawString = input("Please enter your string: \n")
	findPosition = False
	position = 0
	outputNum = ""
	while findPosition == False:
		if rawString[position].isdigit():
			findPosition = True
			convertNum = rawString[position:].split(".")
			if len(convertNum) == 1: # deal with integer nums
				outputNum = convertNum[0]+".00"
			else:
				if len(convertNum[1]) == 1: # deal with only one decimal
					outputNum = convertNum[0]+"."+convertNum[1][:2]+"0"
				else: # deal with more than one decimal
					outputNum = convertNum[0]+"."+convertNum[1][:2]
		else:
			position+=1
	print(outputNum)

practice()