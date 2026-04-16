class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        file_content_map = defaultdict(list)
        
        for path in paths:
            path_parts = path.split()
            root = path_parts[0]
            files = path_parts[1:]
            
            for file in files:
                temp_file = file.replace(")", "(")
                file_parts = temp_file.split("(")
                file_name = file_parts[0]
                file_content = file_parts[1]
                whole_path = root + "/" + file_name
                file_content_map[file_content].append(whole_path)
                
        ans = []
        for file_content_list in file_content_map.values():
            if len(file_content_list) > 1:
                ans.append(file_content_list)
        return ans
