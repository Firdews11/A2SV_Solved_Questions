class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        res_count = Counter()
        for day in responses:
            unique_responses = set(day) 
            for response in unique_responses:
                res_count[response] += 1
                
        best_res = ""
        max_count = -1
        for response, count in res_count.items():
            if count > max_count:
                max_count = count
                best_res = response
            elif count == max_count:
                if response < best_res:
                    best_res = response
        return best_res
