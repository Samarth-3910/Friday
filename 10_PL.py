s = input()

if s[0] in 'aeiouAEIOU':
    print(s + "way")
else:
    for i in range(len(s)):
        if s[i] in 'aeiouAEIOU':
            print(s[i:] + s[:i] + 'ay')
            break

    else:
        print("No vowels")