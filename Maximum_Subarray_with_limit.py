"""
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum. But the sum must not exceed B.
"""
class Solution:
    """
    Approach : Calculate  current sum ,find the maximum Subarray sum
    if it goes maximum subtract the array element from beginning ,To ensure contigous sum
    
    """
    @staticmethod
    def Maximum_Subarray(array, B):
        res, cur_sum, j = 0, 0, 0

        for i in range(len(array)):
            cur_sum += array[i]
            while cur_sum > B:
                cur_sum -= array[j]
                j += 1
            res = max(cur_sum, res)
        return res


if __name__ == '__main__':
    A,B=map(int,input().split())
    array=list(map(int,input().split()))
    print(Solution().Maximum_Subarray(array,B))
