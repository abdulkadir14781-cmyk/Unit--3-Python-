def count_vowels(text):
    count=0
    for ch in text:
        if ch.lower() in "aeiou":
            count+=1

    return count
text=input("Enter text: ")
print(f"Number of vowel: {count_vowels(text)}")

    