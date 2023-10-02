import numpy
from ProblemLinkGenerator import problemLinkGeneratorfunc

from numpy.random import default_rng






allTags=["2-sat","binary search","bitmasks","brute force","chinese remainder theorem",
      "combinatorics","constructive algorithms","data structures","dfs and similar",
      "divide and conquer","dp","dsu","expression parsing","fft","flows","games","geometry",
      "graph matchings","graphs","greedy","hashing","implementation","interactive","math","matrices",
      "meet-in-the-middle","number theory","probabilities","schedules","shortest paths","sortings",
      "string suffix structures","strings","ternary search","trees","two pointers"
]





userHandle=input("Enter your Codeforces Handle\n")
numOfTags=int(input("Enter the number of random tags\n"))
numOfProblems=int(input("Enter the number of Problems\n"))

tags=[]
rng = default_rng()
tags= rng.choice(allTags, size=numOfTags, replace=False)
tagLength=len(allTags)

#print(tags)





ratingsDict={1400:True,1500:True,1600:True,1700:True}






unsolvedProblemsId=problemLinkGeneratorfunc(tags,ratingsDict,userHandle)
#print(len(unsolvedProblemsId))

randomProblemId=rng.choice(unsolvedProblemsId, size=numOfProblems, replace=False)

print(randomProblemId)

with open("ProblemSet.txt", "w") as file:
    file.write('\n'.join(map(str, randomProblemId)))

a=input("Enter any key to exit")
