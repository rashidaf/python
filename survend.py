import json

myFile = open("data.json", "r")
human = json.load(myFile)
myFile.close()

while True:
 x = human.get("eyecolor")
 y = human.get("try")
print("Wow. other people with",x, "eyecolor are also", y)
