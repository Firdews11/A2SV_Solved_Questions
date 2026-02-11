class Solution:
    def findRestaurant(self, list1, list2):
        index_map = {}
        for i in range(len(list1)):
            index_map[list1[i]] = i

        min_sum = float('inf')
        result = []

        for j in range(len(list2)):
            if list2[j] in index_map:
                s = index_map[list2[j]] + j

                if s < min_sum:
                    min_sum = s
                    result = [list2[j]]
                elif s == min_sum:
                    result.append(list2[j])

        return result
