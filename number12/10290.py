res = "1" + "8" * 80

while "18" in res or "288" in res or "3888" in res:
    if "18" in res:
        res = res.replace("18", "2", 1)
    elif "288" in res:
        res = res.replace("288", "3", 1)
    else:
        res = res.replace("3888", "1", 1)

print(res)
