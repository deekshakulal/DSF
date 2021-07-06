import functions

files=["c1.txt","c2.txt","c3.txt"]

triplets=functions.getTriplets(files)
print(triplets)
score=functions.computescore(triplets)
print(score)
search=functions.keywordsearch("diabetes",triplets)
print(search)