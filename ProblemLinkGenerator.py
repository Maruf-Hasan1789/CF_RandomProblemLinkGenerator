import requests
from UserSubmissionGenerator import userSubmissionGeneratorFunc




def tagSpecificProblemLink(ratingsDict,userHandle,tag):
    requestpath = "https://codeforces.com/api/problemset.problems?tags="

    r = requests.get(requestpath + tag)

    jsonObject = r.json()

    allProblems = jsonObject['result']['problems']
    acceptedProblemDict = userSubmissionGeneratorFunc(userHandle)
    cnt = 0
    unsolvedProblemId = []
    for problem in allProblems:
        key = 'rating'
        if key not in problem:
            continue
        rating = problem['rating']
        ratingKey = rating
        if (ratingKey not in ratingsDict):
            continue
        problemId = str(problem['contestId']) + str(problem['index'])

        if (ratingsDict[rating] == True and problemId not in acceptedProblemDict):
            unsolvedProblemId.append(problemId)
            # print(problemId)
            cnt += 1

    return unsolvedProblemId




def problemLinkGeneratorfunc(tags,ratingsDict,userHandle):

   unsolveProblems = []
   for tag in tags:

        unsolveProblemsTagspecific=tagSpecificProblemLink(ratingsDict,userHandle,"binary search")
        unsolveProblems.extend(unsolveProblemsTagspecific)
   return unsolveProblems
