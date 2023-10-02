import requests

tags=["2-sat","binary search","bitmasks","brute force","chinese remainder theorem",
      "combinatorics","constructive algorithms","data structures","dfs and similar",
      "divide and conquer","dp","dsu","expression parsing","fft","flows","games","geometry",
      "graph matchings","graphs","greedy","hashing","implementation","interactive","math","matrices",
      "meet-in-the-middle","number theory","probabilities","schedules","shortest paths","sortings",
      "string suffix structures","strings","ternary search","trees","two pointers"
]

ratingsDict={1400:True,1500:True,1600:True,1700:True}


requestpath="https://codeforces.com/api/problemset.problems?tags="



#print(requestpath)
r=requests.get(requestpath+"binary search")


jsonObject=r.json()
#print(jsonObject['result']['problems'])

allProblems=jsonObject['result']['problems']

cnt=0
for problem in allProblems:
    key='rating'
    if key not in problem:
        continue
    rating=problem['rating']
    ratingKey=rating
    if(ratingKey not in ratingsDict):
            continue
    if(ratingsDict[rating]==True):
        print(problem['contestId']," ",problem['index'])
        cnt+=1


