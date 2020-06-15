acti_wei=30
sports_wei=20
exam_wei=50
exam_total=200
sports_total=50
acti_total=60

exam_sc1=int(input("marks of test one"))
exam_sc2=int(input("marks of test two"))
exam_score=exam_sc1+exam_sc2

acti_sc1=int(input("marks of acti one(out of20)"))
acti_sc2=int(input("marks of acti two"))
acti_sc3=int(input("marks of acti three"))
acti_score=acti_sc1+acti_sc2+acti_sc3

sports_score=int(input("marks of sportstest one"))

exam_per=float(exam_score*exam_wei)/exam_total
acti_per=float(acti_score*acti_wei)/acti_total
sports_per=float(sports_score*sports_wei)/sports_total

total_per=exam_per+acti_per+sports_per

print(total_per)


