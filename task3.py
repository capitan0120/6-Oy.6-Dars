class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        llist = []
        a = sorted(score[:], reverse=True)
        for i in score:
            index = a.index(i) + 1
            if index == 1:
                llist.append("Gold Medal")
            elif index == 2:
                llist.append("Silver Medal")
            elif index == 3:
                llist.append("Bronze Medal")
            else:
                llist.append(str(index))
        return llist