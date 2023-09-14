class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # dict 선언
        anagrams = collections.defaultdict(list)
        
        # 애너그램끼리 같은 key 값을 갖는다. 
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return sorted(list(anagrams.values()), key = lambda x : len(x))