word=input()
total=0

if "c=" in word:
  total+=word.count("c=")
  word=word.replace('c=',' ')
if "c-" in word:
  total+=word.count("c-")
  word=word.replace("c-"," ")
if "dz=" in word:
  total+=word.count("dz=")
  word=word.replace("dz="," ")
if "d-" in word:
  total+=word.count("d-")
  word=word.replace("d-"," ")
if "lj" in word:
    total+=word.count("lj")
    word=word.replace("lj"," ")
if "nj" in word:
    total+=word.count("nj")
    word=word.replace("nj"," ")
if "s=" in word:
  total+=word.count("s=")
  word=word.replace("s="," ")
if "z=" in word:
    total+=word.count("z=")
    word=word.replace("z="," ")

print(total+len(word.replace(" ","")))










