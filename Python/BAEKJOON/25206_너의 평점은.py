total = 0
cnt = 0

mark = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

for tc in range(20):
    subject, credit, grade = map(str, input().split())
    if grade == 'P':
        continue
    else:
        score = mark.get(grade)
        total += float(credit) * score
        cnt += float(credit)
print(total/cnt)