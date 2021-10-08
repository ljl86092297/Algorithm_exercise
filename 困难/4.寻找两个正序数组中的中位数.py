from heapq import heappush, heappop

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums1_l = len(nums1)
        nums2_l = len(nums2)
        d = []
        if nums1_l + nums2_l == 0:
            return 0
        elif (nums1_l + nums2_l) % 2 == 0:
            for i in range((nums2_l + nums1_l)//2+1):
                if nums1 != [] and nums2 != []:
                    if nums1[0] <= nums2[0]:
                        heappush(d, -nums1.pop(0))
                    else:
                        heappush(d, -nums2.pop(0))
                elif nums1 != [] and nums2 == []:
                    heappush(d, -nums1.pop(0))
                else:
                    heappush(d, -nums2.pop(0))
            print(d)
            return  -(heappop(d)+heappop(d))/2
        else:
            for i in range((nums2_l + nums1_l)//2+1):
                if nums1 != [] and nums2 != []:
                    if nums1[0] <= nums2[0]:
                        heappush(d, -nums1.pop(0))
                    else:
                        heappush(d, -nums2.pop(0))
                elif nums1 != [] and nums2 == []:
                    heappush(d, -nums1.pop(0))
                else:
                    heappush(d, -nums2.pop(0))
            return  -d[0]



S = Solution()
nums1 = [1,2]
nums2 = [3,4]
x = S.findMedianSortedArrays(nums1, nums2)
print(x)