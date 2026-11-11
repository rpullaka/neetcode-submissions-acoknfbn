class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals

        s_intvls = sorted(intervals)
        m_intvls = []

        i,j = 0,1
        while j < len(s_intvls):
            l_s,l_e = s_intvls[i]
            r_s,r_e = s_intvls[j]
            if l_e >= r_s:  #overlapping
                s_intvls[i] = [l_s,max(l_e,r_e)]
            else: #non-overlapping
                m_intvls.append(s_intvls[i].copy())
                i = j
            j += 1
        m_intvls.append(s_intvls[i])
        return m_intvls
