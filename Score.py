grades = list(map(int, input().split()))
count = 0
minS = min(grades)
maxS = max(grades)
for grade in grades:
  if(grade<60):
    count+=1
print(f"不及格人數: {count}")
print(f"最高分: {maxS}")
print(f"最低分: {minS}")
