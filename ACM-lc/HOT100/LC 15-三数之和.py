def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res

def main():
    s = eval(input())
    lst = three_sum(s)
    print(lst)
   
if __name__=="__main__":
    main()
#     15. 三数之和 Medium
# 给你一个整数数组 nums，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k、j != k，且 nums[i] + nums[j] + nums[k] == 0。

# 请你返回所有和为 0 且不重复的三元组。

# 示例
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 输入：nums = [0,0,0,0]
# 输出：[[0,0,0]]
# 提示
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5