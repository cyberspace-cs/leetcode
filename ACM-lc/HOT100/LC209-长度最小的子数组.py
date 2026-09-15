def min_sub_array_len(target, nums):
    """
    :type target: int
    :type nums: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    min_length=float('inf')
    left=0
    current_sum=0
    
    for right in range(len(nums)):
        current_sum+=nums[right]
        
        while current_sum>=target:
            min_length=min(min_length,right-left+1)
            current_sum-=nums[left]
            left+=1
    return min_length if min_length!=float('inf') else 0


def main():
    target = int(input())
    nums = eval(input())
    lst = min_sub_array_len(target, nums)
    print(lst)

if __name__ == "__main__":
    main()
    
    
#     209. 长度最小的子数组 Medium
# 给定一个含有 n 个正整数的数组和一个正整数 target。

# 找出该数组中满足其总和大于等于 target 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

# 示例
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下长度最小的子数组。
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 提示
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104