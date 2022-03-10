res = "5" * 54 + "7"

while "722" in res or "557" in res:
    if "722" in res:
        res = res.replace("722", "57", 1)
    else:
        res = res.replace("557", "72", 1)

print(res)
