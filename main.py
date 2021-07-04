import functions

files=["a.txt","a.txt",'c.txt']

triplets=functions.getTriplets(files)
print(triplets)
score=functions.computescore(triplets)
print(score)
search=functions.keywordsearch("quarantined",triplets)
print(search)