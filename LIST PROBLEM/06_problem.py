fruits=["apple","banana","grapes","guavava","lichi","watermelon"]
fruits.append("mango")
fruits[1]="pink"
print(fruits)

longest_element=fruits[0]
for item in fruits:
    if len(item)>(len(longest_element)):
        longest_element =item                         
print(longest_element)