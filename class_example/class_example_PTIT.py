class student:
    def __init__(self, name, dob, s1, s2, s3):
        self.name = name
        self.dob = dob
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.avg = 0

    def set_avg(self):
        temp = [self.s1, self.s2, self.s3]
        sorted(temp)
        self.avg = round((temp[0] * 2 + temp[1] + temp[2]) / 4, 1)
        return self.avg

if __name__ == "__main__":
    t = int(input())
    students = []
    for i in range(t):
        name = input()
        dob = input()
        s1 = float(input())
        s2 = float(input())
        s3 = float(input())
        stu = student(name, dob, s1, s2, s3)
        stu.set_avg()
        students.append(stu)
    students = sorted(students, key=lambda x: x.avg, reverse=True)
    for stu in students:
        print(stu.name, stu.dob, stu.avg)