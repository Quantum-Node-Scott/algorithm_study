class Student:
    def __init__(self, age, height):
        self.age = age
        self.height = height
    def __lt(self,other):
        if self.age == other.age:
            return self.height < other.height
        return self.age < other.age

def divide(students, start, end):
    if start >= end:
        return
    mid = (start + end) // 2
    divide(students, start, mid)
    divide(students, mid + 1, end)
    merge(student, start, end)

def merge(students, start, end):
    temp = []
    mid = (start + end) // 2
    left = start
    right = mid + 1

    while left <= mid and right <= end:
        if students[left] < students[right]:
            temp.append(students[left])
            left += 1
        else:
            temp.append(students[right])
            right += 1
    
    while left <= mid:
        temp.append(students[left])
        left += 1

    while left <= mid:
        temp.append(students[right])
        right += 1

    for i in range(len(temp)):
        students[start + i] = temp[i]

if __name__ == "__main__":
    n = int(input())
    students = []
    for _ in range(n):
        age, height = map(int, input().split())
        students.append(Student(age, height))

    divide(students, 0, n-1)
    for student in students:
        print(student.age, student.height)