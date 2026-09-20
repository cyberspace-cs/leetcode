
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: List[int]
    """
    # 在这里写你的代码（原地修改 nums1 后返回）
    p1,p2,p=m-1,n-1,m+n-1
    while p1>=0 and p2>=0:
        if nums1[p1]>nums2[p2]:
            nums1[p]=nums1[p1]
            p1-=1
        else:
            nums1[p]=nums2[p2]
            p2-=1
        p-=1
    while p2>=0:
        nums1[p]=nums2[p2]
        p2-=1
        p-=1
    return nums1

def main():
    s1 = eval(input())
    m = int(input())
    s2 = eval(input())
    n = int(input())
    lst = merge(s1, m, s2, n)
    print(lst)
   
if __name__=="__main__":
    main()
    
#     88. 合并两个有序数组 Easy
# 给你两个按非递减顺序排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n，分别表示 nums1 和 nums2 中的元素数目。

# 请你合并 nums2 到 nums1 中，使合并后的数组同样按非递减顺序排列。

# 说明：最终结果存储在数组 nums1 中。nums1 的初始长度为 m + n，后 n 个元素为 0，仅用于占位。

# 示例
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 提示
# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200

# [1,2,3,0,0,0]
# 3
# [2,5,6]
# 3
# [1, 2, 2, 3, 5, 6]