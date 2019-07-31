import json

start = '''On today's survey, you will be asked various questions
to determine based on your eye color if you are more
likely to be an introvert or an extrovert.
'''

print(start)
human = {}

def idea():
    for i in range(0,1):
        thoughts = input("do you think that you are an extrovert or an introvert?")
        if thoughts == "extrovert":
            return thoughts

        if thoughts == "introvert":
            return thoughts



def rather():
    fame = input('''Would you rather be famous when you are alive
    and forgotten when you die or unknown when you are alive but famous
    after you die?(Type forgotten or unknown)\n''')
    if fame == "forgotten":
        return fame
    if fame == "unknown":
        return fame


def hippl():
    print("Hi", user_input)
    eyecolor = input("What is your eye color?\n")
    if eyecolor == "blue":
        rather()
        idea()
        return eyecolor
    if eyecolor == "brown":
        rather()
        idea()
        return eyecolor
    if eyecolor == "green":
        rather()
        idea()
        return eyecolor
    if eyecolor == "hazel":
        rather()
        idea()
        return eyecolor
    if eyecolor == "black":
        rather()
        idea()
        return eyecolor

user_input = input("What is your name?\n")
#hippl()

color = hippl()
guess = idea()
would = rather()

human["name"] = user_input
human["eyecolor"] = color
human["try"] = guess
human["response"] = would


print(human)

with open("survey.json", "w") as json_file:
    json.dump(human, json_file)

myFile = open("data.json", "r")
human = json.load(myFile)
myFile.close()
