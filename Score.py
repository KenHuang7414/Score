grades = list(map(int, input().split()))
count = 0
for grade in grades:
  if(grade<60):
    count+=1
print(count)