st="Hello i am Student 123 @#$"
lower_count=0
upper_count=0
digit_count=0
space_count=0
special_char_count=0
for ch in st:
    if ch.isupper():
        upper_count+=1
    elif ch.islower():
        lower_count+=1
    elif ch.isdigit():
        digit_count+=1
    elif ch.isspace():
        space_count+=1
    else:
        special_char_count+=1

print(f"lowercase:{lower_count}\nuppercase:{upper_count}\ndigit:{digit_count}\nspace:{space_count}\nspecial character:{special_char_count}\nword in string:{space_count+1}")                   