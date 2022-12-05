def isIsomorphic(s,t):
    if len(s) != len(t):
        return "Not same length"
    else:
        m1 = {}
        m2 = {}
        for i in range(len(s)):
            v1 = s[i]
            v2 = t[i]
            if v1 not in m1:
                m1[v1] = v2
                print(m1)
            if v2 not in m2:
                m2[v2] = v1
                print(m2)
            if m1[v1] != v2 or m2[v2] != v1:
                return False
        return True





s = "add"
t = "egd"
print(isIsomorphic(s,t))
