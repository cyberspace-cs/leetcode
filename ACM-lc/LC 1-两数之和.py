

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 在这里写你的代码
    hashmap=dict()
    for id,num in enumerate(nums):
        if target-num in hashmap:
            return [hashmap[target-num],id]
        hashmap[num]=id
        
    return []

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    target=int(input())
    lst = two_sum(nums,target)
    print(lst)
   
if __name__=="__main__":
    main()