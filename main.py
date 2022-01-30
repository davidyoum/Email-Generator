#Random Email Generator made by David Youm
#3/4/21

import json
import random

how_many_emails = 10

names = json.loads(open("Email-Generator\\names.json").read())
domains = json.loads(open("Email-Generator\domains.json").read())
lastnames = json.loads(open("Email-Generator\lastnames.json").read())

for i in range(how_many_emails):
    random_numbers = random.randint(0, 999)

    print(random.choice(names) + random.choice(lastnames) + (str)(random_numbers) + random.choice(domains))

