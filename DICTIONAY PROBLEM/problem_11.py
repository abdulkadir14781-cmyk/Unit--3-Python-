department = {
    "CS Department":{"HOD Name":"Ankit","No. of Faculty":34,"No. of Student":220},
    "ECE Department":{"HOD Name":"Rahul","No. of Faculty":20,"No. of Student":100},
    "ME Department":{"HOD Name":"Shubham","No. of Faculty":40,"No. of Student":50},
}
print(department["ECE Department"]["HOD Name"])
print(department["ECE Department"]["No. of Faculty"])
print(department["ECE Department"]["No. of Student"])
print(department["CS Department"]["No. of Student"])
print(department["CS Department"]["No. of Faculty"])
print(department["CS Department"]["HOD Name"])
# department.update({"ME Department"["No. of Faculty"]:43})
department.update({"Civil Department":{"HOD Name":"Rakesh","No. of Faculty":10,"No. of Student":500},})
print(department.keys())
print(department)