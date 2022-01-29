#Random Email Generator
#3/4/21
#Inspiration from EngineerMan

import generator
import json

names = json.load(open("names.json").read())

print(names[0])

