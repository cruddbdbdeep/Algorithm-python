# 2018-10-23
# P1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
# input : T
#		  testCaseNum
# 		  num1 num2 ... num999 num1000
# output : #1 num

test_case = int(input())

for i in range(0, test_case):
    test_case_num = int(input())
    score_list = input().split()

    score_dict = {}
    for j in range(0, 1000):
        score = score_list[j]
        if score in score_dict:
            score_dict[score] += 1
        else:
            score_dict[score] = 1

    max = 0
    mode = ""
    for score, count in score_dict.items():
        if count > max:
            max = count
            mode = score

    print("#%s %s" %(i+1, mode))