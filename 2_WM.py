# hours = int(input())
# minutes = int(input())
#
# if (4 <= hours < 12) or (hours == 12 and minutes == 0):
#     print("Good Morning")
# elif (12 <= hours < 16) or (hours == 16 and minutes == 0):
#     print("Good Afternoon")
# elif (16 <= hours < 21) or (hours == 21 and minutes == 0):
#     print("Good Evening")
# else:
#     print("Good Night")
#
#
#
#
hours = int(input())
minutes = int(input())

if (4 <= hours < 12) or (hours == 12 and minutes == 0):
    print("Good Morning")
elif (12 <= hours < 16) or (hours == 16 and minutes == 0):
    print("Good Afternoon")
elif (16 <= hours < 21) or (hours == 21 and minutes == 0):
    print("Good Evening")
elif hours >= 22 or (0 <= hours < 4):
    print("Good Night")
else:
    print("Invalid time entered")
