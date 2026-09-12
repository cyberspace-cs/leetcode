
def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    # 在这里写你的代码
    if not height:
        return 0
    
    n=len(height)
    left_max=[0]*n
    right_max=[0]*n
    result=0
    
    #计算每个位置左边的最大高度
    left_max[0]=height[0]
    for i in range(1,n):
        left_max[i]=max(left_max[i-1],height[i])
    #计算每个位置右边的最大高度
    right_max[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        right_max[i]=max(right_max[i+1],height[i])
        
    for i in range(n):
        result+=min(left_max[i],right_max[i])-height[i]
    return result
        

def main():
    s = eval(input())
    lst = trap(s)
    print(lst)
   
if __name__=="__main__":
    main()
    
    
# 42. 接雨水 Hard
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

# 示例
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 输入：height = [4,2,0,3,2,5]
# 输出：9
# 提示
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5