from fuzzywuzzy import process
with open ("city.txt","r",encoding="utf8") as f:
    cities=f.read().split("\n")
def match(search,choice,limit=7):
    result=process.extract(search,choice,limit=limit)
    return result
search=input()
print(match(search,cities))
