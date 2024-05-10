class Solution:
    def countStudents(self, st: List[int], sa: List[int]) -> int:
        count = 0
        while len(st) > count:
            if st[0] == sa[0]:
                st.pop(0)
                sa.pop(0)
                count=0
            else:
                count+=1
                st.append(st.pop(0))
        return len(st)