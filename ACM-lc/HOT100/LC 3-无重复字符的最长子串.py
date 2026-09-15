def lengthOfLongestSubstring(s: str) -> int:
        char_index={}
        left=0
        max_length=0
        
        for right, char in enumerate(s):
            if char in char_index and char_index[char]>=left:
            # 如果字符在当前窗口内重复，移动左指针到重复字符上一次位置的下一位
                left=char_index[char]+1
            char_index[char]=right
            max_length=max(max_length,right-left+1)
        return max_length
                
                
def main():
    s = input()
    length = lengthOfLongestSubstring(s)
    print(length)
   
if __name__=="__main__":
    main()
    
    
#     3. 无重复字符的最长子串
# 已解答
# 中等
# 相关标签
# premium lock icon
# 相关企业
# 提示
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

 

# 示例 1:

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
# 示例 2:

# 输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
