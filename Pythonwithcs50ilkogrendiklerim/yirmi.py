import csv

name=input("Whats ur name?")
home=input("Wheres ur home?")

with open("students.csv","a")as file:
    writer=csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"home":home,"name":name})
