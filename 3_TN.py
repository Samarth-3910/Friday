N = int(input()) #no of days left in exam
S = int(input()) #no of subjects
C = int(input()) #no of chapter in that subject
H = int(input()) # each chapter will take this much time to complete chapter
L = int(input()) # it is long days trip
T = int(input()) # time to study daily

total_hours_required = S * C * H

study_days = N - L

total_study_hours_available = study_days * T

if total_study_hours_available >= total_hours_required:
    print("Goa Jaayenge")
else:
    print("Padhai Karenge")


    # first calculate total hors left
    # study days left
    # total hours available