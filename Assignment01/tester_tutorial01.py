import tutorial01 as A1

actual_answers = [9, 12, 7]
student_answers = []

test_case_1 = A1.add(4, 5)
student_answers.append(test_case_1)

test_case_2 = A1.subtract(14, 2)
student_answers.append(test_case_2)

test_case_3 = A1.subtract(15, 8)
student_answers.append(test_case_3)

print(actual_answers)
print(student_answers)

total_test_cases = len(actual_answers)
count_of_correct_test_cases = 0

for x, y in zip(actual_answers, student_answers):
    if x == y:
        count_of_correct_test_cases += 1

print(f"Test Cases Passed = '{count_of_correct_test_cases}'  / '{total_test_cases}'")

1) Goto github.com and signin and make a new repo with the name CS384_Roll_Number (all capitals please). Make sure its a pvt repo. Add mayankjoin@gmail.com as a collaborator
2) Now git clone your repo in any_folder, say on desktop git clone https://github.com/<USERNAME>/<CS384_Roll_Number>.git
3) Now clone my repo inside some other directory say Downloads : git clone https://github.com/mayankjoin/cs384_2020.git
4) Go inside the cs384_2020 folder, and copy the Assignment01 folder and paste inside the folder that was cloned in Step 2
5) Write your code and functions and then push the code on github.
#Clone that repo and go inside it 
#Copy the folder structure of https://github.com/mayankjoin/cs384_2020.git (Exclude the top level folder, "cs384_2020". Copy the content within it)
#Enter Assignment01 folder, edit the tutorial01.py 