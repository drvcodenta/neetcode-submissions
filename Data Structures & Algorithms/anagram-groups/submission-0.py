class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #let's start with the brute force approach which is
        #hashmap = {}
        #key would store a-z count 26 alphabet are there so ascii and their position
        #can be used to like calculate the key values itself
        #0-a 1-b 2-c -- 26-z
        #ord(a) - 97 the ascii value, we need some array which basically denotes
        #its indexes as alphabet values but stores their occurences only inside as
        #a value placeholder
        hashmap = defaultdict(list)
        for i in strs:
            count = [0]*26
            for c in i:
                count[ord(c)-ord("a")] += 1
            hashmap[tuple(count)].append(i)
        return list(hashmap.values())