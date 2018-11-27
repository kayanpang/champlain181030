# multidimensional list

students = [[88,99,100],[90,60,77],[80,90,90],[12,13,14]]
# 1st quiz for 2nd student
print(students[1][0])

# what is the max value of the quizzes for for student #2
print(max(students[1]))

# what is the average of quizzes for students #3
print(sum(students[2])/len(students[2]))

# 3 dimensional (scenario: two students' 2 quiz that each has 2 sections)
students2 = [[[40,50],[55,30]],[[30,40],[22,10]]]
#what is the score of section1 of quiz1 for student1
print(students2[0][0][0])

# print the score of 4th student,for loop
students3 = [[88,99,100],[90,60,77],[80,90,90],[12,13,14]]
for q in students3[3]:
    print(q)