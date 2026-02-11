class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res =[]
        flag = False
        x = ""
        for i in range(len(source)):
            y = source[i]
            j = 0
            if not flag :
                    x = ""
            while j < len(y):
                if not flag and j+1 < len(y) and  y[j:j+2] == "/*":
                    flag = True
                    j+=2
                elif flag and j+1 < len(y) and y[j:j+2]=="*/":
                    flag = False
                    j+=2
                elif not flag and j+1 < len(y) and y[j:j+2]=="//":
                    break
                elif not flag:
                    x += y[j]
                    j+=1
                else:
                    j+=1

            if not flag and x:
                res.append(x)
               
        return res
