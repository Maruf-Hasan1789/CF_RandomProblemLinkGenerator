import requests




acceptedProblem={}

r=requests.get("https://codeforces.com/api/user.status?handle=blurryface")

userSubmissionJson=r.json()


allSubmission=userSubmissionJson['result']

print(len(allSubmission))
cnt=0




for submission in allSubmission:
    if submission['verdict']=='OK':
        problemContestIdIndex=str(submission['problem']['contestId'])+str(submission['problem']['index'])
        acceptedProblem[problemContestIdIndex]=1
        print(acceptedProblem[problemContestIdIndex])
        #print(submission['problem']['contestId']," ",submission['problem']['index'])
        cnt+=1

