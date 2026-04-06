class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs = [0]*k
        self.min_unfainess= float('inf')

        def BT(idx,max_so_far):
            if max_so_far > self.min_unfainess:
                return
            if idx == len(cookies):
                self.min_unfainess = min(self.min_unfainess, max(childs))
                return
            for i in range(k):
                childs[i] +=cookies[idx]
                BT(idx+1,max(self.min_unfainess,childs[i]))
                childs[i] -=cookies[idx]
                if childs[i] ==0:
                    return
        BT(0,0)
        return self.min_unfainess
        #soo this code will give TLE search for a better approch
        # the Time Complexity is k^n b/c we are making decission for each k times
        # and the space is n,and each of calling will have k so n+k
