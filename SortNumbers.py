def solution(nums):
    if not nums:
        return []
    else:
        return sorted(nums)


# def solution(nums):
#     return sorted(nums or [])


print(solution([]))
