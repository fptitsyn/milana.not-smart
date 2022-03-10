def solve(res, arg1, arg2):
    while arg1 in res or arg2 in res:
        if arg1 in res:
            res = res.replace(arg1, arg2[0], 1)
        else:
            res = res.replace(arg2, arg1[0], 1)

    return res


print(solve("8" * 68, "222", "888"))  # 9365
print(solve("9" * 127, "333", "999"))  # 9764
print(solve("8" * 125, "333", "888"))  # 10317
