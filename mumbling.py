def accum(s):
    s = list(s)
    metin = ""
    for i in range(len(s)):
        metin += s[i] + (s[i] * (i))
        metin += "-"
    metin = metin[:-1].title()
    return metin



print(accum("ZpglnRxqenU"))
print(accum("NyffsGeyylB"))