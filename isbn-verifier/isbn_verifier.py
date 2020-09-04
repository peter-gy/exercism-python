def is_valid(isbn):
    if not isbn:
        return False
    nums = [int(ch) for ch in isbn if ch.isnumeric()]
    if isbn[-1] == "X":
        nums.append(10)
    return (
        len(nums) == 10
        and sum([nums[i] * (10 - i) for i in range(len(nums))]) % 11 == 0
    )
