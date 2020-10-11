import random

nouns = open("nouns.txt","r").readline().split(",")
verbs = open("verbs.txt","r").readline().split(",")
adjectives = open("adjectives.txt","r").readline().split(",")
intensifiers = open("intensifiers.txt","r").readline().split(",")
numbers = open("numbers.txt","r").readline().split(",")
text = "piss egg"
mad = random.choice(["Mad", "Chad", "Dab", "Sad", "Bad", "Nap", "Rad", "Vlad", "Glad", "Whap", "Jank"])
lib = random.choice(["Lib", "Lip", "Leg", "Dip", "Pip", "Bup", "Pis", "Lick", "Derp", "Slip", "Nip"])
if mad == "Mad" and lib == "Lib":
    mad = "Ponk"
    lib = "Bean"
print("Welcome to " + mad + " " + lib + "s!")
print("Glossary:\nNOUN- noun\nVERB- verb\nADJ- adjective\nINT- intensifier\nNUM- number")
if lib == "Pis":
    lib = "Piss"
while text != "":
    print("Enter a " + mad + " " + lib + ", or hit 'enter' to exit.")
    text = input()
    random.shuffle(nouns)
    nountimes = text.count("NOUN")
    verbtimes = text.count("VERB")
    adjtimes = text.count("ADJ")
    inttimes = text.count("INT")
    numtimes = text.count("NUM")
    for x in range (0, nountimes):
        text = text.replace("NOUN", random.choice(nouns), 1)
    for x in range (0, verbtimes):
        text = text.replace("VERB", random.choice(verbs), 1)
    for x in range (0, adjtimes):
        text = text.replace("ADJ", random.choice(adjectives), 1)
    for x in range (0, inttimes):
        text = text.replace("INT", random.choice(intensifiers), 1)
    for x in range (0, numtimes):
        text = text.replace("NUM", random.choice(numbers), 1)
    print(text)
