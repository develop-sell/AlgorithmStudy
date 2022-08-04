import collections


nums = [1,3,-1,-3,5,3,6,7]
k = int(input())
answer = []
nums_len = len(nums)
for i in range(nums_len - 2):
    current_nums = nums[i:i+k] # slice의 마지막 i+3이면 2개의 숫자가 들어감. 
    max_num = max(current_nums)
    answer.append(max_num)

print(answer)

def maxSlidingWindow(self, nums: list[int], k: int):
    results = []
    window = collections.deque()
    current_max = float('-inf') # 마이너스 무한대
    for i, v in enumerate(nums):
        window.append(v)
        if i < k - 1:
            continue

        if current_max == float('-inf'):
            current_max = max(window) # 처음 3개에 대한 max만
        elif v > current_max:
            current_max = v
        
        results.append(current_max)

        if current_max == window.popleft():
            current_max = float('-inf')

    return results