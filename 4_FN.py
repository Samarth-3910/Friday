N = int(input()) # no of total sections
B = int(input()) #no of sections misbehaving
I = int(input()) # anger increase by unit per section
G = int(input()) # no of sections to be good
D = int(input()) # anger decrease by unit per section

anger_level_inc = B * I

anger_level_dec = G * D

anger_level = anger_level_inc - anger_level_dec

if anger_level > 0:
    print("Simple Questions")
elif anger_level < 0:
    print("Funny Questions")
else:
    print("God Knows")