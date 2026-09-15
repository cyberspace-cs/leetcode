def max_area(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    ans=0
    left=0
    right=len(height)-1
    while left<right:
        h=min(height[left],height[right])
        ans=max(ans,h*(right-left))
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return ans


def main():
    s = eval(input())
    lst = max_area(s)
    print(lst)
   
if __name__=="__main__":
    main()
    
#     11. 盛最多水的容器 Medium
# 给定一个长度为 n 的整数数组 height。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i])。

# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。返回容器可以储存的最大水量。

# 示例
# 输入：height = [1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：选择第 2 条线和第 9 条线，容器面积 = min(8,7) * (8-1) = 49
# 输入：height = [1,1]
# 输出：1
# 提示
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104