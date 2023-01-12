
#교재 dictionary
subjects = {"의영": "A+",
             "전산제도": "B+",
             "유체역학": "A0"
             }
student = input("이름 : ")
subject = "유체역학"
print(student,"학생의 ",subject,"성적은",subjects["유체역학"],"입니다")
#old style
print('%s학생의 %s 과목 성적은 %s입니다' % (student, subject, subjects[subject]))
#modern style
print("{0}학생의 {1} 과목 성적은 {2}입니다".format(student, subject, subjects[subject]))
#f스트링
print(f'{student}학생의 {subject} 과목 성적은 {subjects[subject]}입니다')
