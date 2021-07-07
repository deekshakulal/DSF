import functions

files=["c1.txt","c2.txt","c3.txt"]

triplets=functions.getTriplets(files)
#print(triplets)
for i,j in triplets.items():
    print("-"*100)
    print("List of triplets in ",i ,"-",j)
    
print("*"*100)
score=functions.computescore(triplets)
#print(score)
for i,j in score.items():
    print("Similarity between ",i ,"is-->",j, " %")
    print("-"*100)

search=functions.keywordsearch("diabetes",triplets)
#print(search)

for i,j in search.items():
    print(i ,"is-->",j," %")
    print("-"*100)