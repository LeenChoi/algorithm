class Solution:
    def checkValidString(self, s: str) -> bool:
        a, b = [], []
        for i in range(0, len(s)):
            k = s[i]
            if k == '(' or k == ')':
                if len(a) != 0 and a[-1]['key'] == '(' and k == ')':
                    a.pop()
                else:
                    a.append({'key': k, 'index': i})
            else:
                b.append({'key': k, 'index': i})
        
        if len(a) > len(b):
            return False
        
        _i, _j = 0, 0
        while True:
            if _i == len(a):
                return True
            if _j == len(b):
                return False

            if a[_i]['key'] == ')':
                if b[_j]['index'] > a[_i]['index']:
                    return False
                else:
                    _i += 1
                    _j += 1
                    continue
            else:
                if b[_j]['index'] < a[_i]['index']:
                    _j += 1
                    continue
                else:
                    _i += 1
                    _j += 1
                    continue

S = input()
solution = Solution()
res = solution.checkValidString(S)
print(res)

