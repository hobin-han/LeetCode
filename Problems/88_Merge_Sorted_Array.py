class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        total_m = 0

        i_m = m - 1
        i_n = n - 1

        i = m + n - 1
            
        while 0 <= i and 0 <= i_n < n:
            n2 = nums2[i_n]

            if i_m < 0:
                nums1[i] = n2
                i_n -= 1
            else:
                n1 = nums1[i_m]

                if n1 <= n2:
                    nums1[i] = n2
                    i_n -= 1
                else:
                    nums1[i] = n1
                    i_m -= 1
                    
            i -= 1