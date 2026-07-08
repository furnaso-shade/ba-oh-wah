#validating user input

username = input("username: ")

#length = len(username)
print(f"username is {len(username) - 12} characters too long" if len(username) > 12 else "")

#this part is redundant - isalpha checks for spaces too
#spaces = input.count(" ")
#print("username musnt'nt contain spaces" if spaces > 0 else "")

#digits = input.isalpha()       (redundant variable)

print("username must'nt contain digits or spaces" if not username.isalpha() else "")
