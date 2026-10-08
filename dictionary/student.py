students= {
    101: {"name" : "aditi" , "scores" :[75,85,90]},
    102: {"name" : "rahul" , "scores" :[45,60,50]},
    103: {"name" : "sneha" , "scores" :[90,88,95]},
    104: {"name" : "karan" , "scores" :[55,72,68]},
    105: {"name" : "priya" , "scores" :[49,51,47]},
    }
for sid ,details in students.items():
    avg = sum(details["scores"])/len(details["scores"])
    details["avrage"] = avg
    details["passed"] = avg >=50

print(" who passed :")
for sid , details in students.items():
    if details["passed"]:
     print(details["name"]) 

