class Solution(object):
    def isMatch(self, s, p):
        p = re.sub("\*+", "*", p)
        while(len(p) != 0):
            next = p.find("*", p.find("*") + 1)
            if(p[0] == "*"):
                if(next == -1):
                    if(len(p) == 1):#1
                        return True
                    else:#2
                        ret = match_from_back(s, p[1:])
                else: #3
                    ret = match_from_front_with_star(s, p[1:next])
            else:
                next = p.find("*")
                if(next == -1): #4
                    ret = match_fully(s, p)
                else: #5
                    ret = match_fully_from_front(s, p[:next])
            
            #print(ret)
            if(ret == "success"):
                return True
            elif(ret == -1):
                return False
            else:
                s = s[ret:]
                p = p[next:]
        if(len(s) == 0):
            return True
        else:
            return False
                
                
def match_from_back(txt, pat):
    pat = pat[::-1]
    txt = txt[::-1]
    ret = match_fully_from_front(txt, pat)
    print(ret)
    if(ret == len(pat)):
        return "success"
    else:
        return -1

def match_from_front_with_star(txt, pat):
    M = len(pat)
    N = len(txt)

    lps = [0] * M
    j = 0

    computeLPSArray(pat, M, lps)

    i = 0
    while i < N:
        if pat[j] == txt[i] or pat[j] == '?':
            i += 1
            j += 1

        if j == M:
            return i
            j = lps[j - 1]
        elif i < N and ( pat[j] != txt[i] and pat[j] != '?'):
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def computeLPSArray(pat, M, lps):
    len = 0
    lps[0]
    i = 1

    while i < M:
        if pat[i] == pat[len] or pat[len] == '?':
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1


def match_fully(txt, pat):
    ret = match_from_front_with_star(txt, pat)
    if(len(pat) == len(txt) and ret == len(pat)):
        return "success"
    else:
        return -1
    
def match_fully_from_front(txt, pat):
    ret = match_from_front_with_star(txt, pat)
    if(ret != len(pat)):
        return -1
    else:
        return ret