with open("index.html","r+",encoding="utf8") as p:
    pp=p.read()
with open("index.html","w+",encoding="utf8") as p:
    p.write(pp.replace(".下载",""))
