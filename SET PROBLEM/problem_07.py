science_club = {"Aman","Riya","Rahul","Priya","Ankit"}
coding_club = {"Rahul","Ankit","Simran","Rohit","Riya"}

print(science_club | coding_club)
print(science_club & coding_club)
print(science_club - coding_club)
print(coding_club - science_club)
print(coding_club - science_club)
print(science_club.isdisjoint(coding_club))
science_club.add("Abdul")
science_club.remove("Aman")
print(science_club)
    