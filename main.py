#Random Email Generator
#3/4/21
#Inspiration from EngineerMan

import random

while True:
    numbers = random.randint(0, 17)

    names = ["Olivia", "Emma", "Ava", "Sophia", "Isabella", "Charlotte", "Amelia", "Mia", "Willow", "Ariana", "Aaliyah", "Cora", "Clara", "Vivian", "Madeline", "Peyton", "Julia", "Rylee"]
    name = names[numbers]

    emails = ["aol.com", "att.net", "comcast.net", "facebook.com", "gmail.com", "gmx.com", "googlemail.com", "google.com",
              "hotmail.com", "hotmail.co.uk", "mac.com", "me.com", "mail.com",
              "msn.com", "live.com", "sbcglobal.net", "verizon.net", "yahoo.com"]
    email = emails[numbers]

    print(name+str(numbers)+"@"+email)