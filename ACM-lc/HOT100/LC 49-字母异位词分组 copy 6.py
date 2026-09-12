
def group_anagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    # 在这里写你的代码
    from collections import defaultdict
    groups=defaultdict(list)
    for s in strs:
        key=''.join(sorted(s))
        groups[key].append(s)
    return list(groups.values())
def main():
    s = eval(input())
    lst = group_anagrams(s)
    print(lst)
   
if __name__=="__main__":
    main()