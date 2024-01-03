class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        y=[["".join(sorted(list(item))),item] for index,item in enumerate(strs)]
        d=dict()
        for i,j in y:
            # print(i,j,d.get(i,[]))
            d[i]=d.get(i,list())
            d[i].append(j)
            # print(d[i])
        result=list()
        print(d)
        for i in d:
            res=list()
            for j in d[i]:
                # print(j)
                res.append(j)
                # print(res)
            result.append(res.copy())
        return result