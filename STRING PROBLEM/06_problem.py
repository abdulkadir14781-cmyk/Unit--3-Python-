s1 = input('enter  first string: ')
s2 = input('enter  second string: ')

if sorted(s1.lower()) == sorted(s2.lower()) :
    print("String are Anagram")
else:
    print("not Anagram")