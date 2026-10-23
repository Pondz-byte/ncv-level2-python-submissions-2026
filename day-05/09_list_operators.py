marks = []
i = 0

mark = int(input("enter mark (or -1 to stop)"))

while mark != -1:
    marks.append(mark)
    mark = int(input("enter mark (or -1 to stop)"))
    
print(f"Our list has {len(marks)} elements")
  
  
sum = 0
for x in range(len(marks)):
    mark = marks[x]
    sum = sum + mark
print(f"The sum of all marks = {sum}")

total = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total + mark
    
avg = total/len(marks)
print(f"The average of all marks = {avg}")

