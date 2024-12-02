def is_safe(report):
    nums = [int(num) for num in report.split()]
    pos = nums[1] > nums[0]
    last = nums[0]
    for num in nums[1:]:
        if pos:
            if num < last:
                return False
        else:
            if num > last:
                return False
        if num == last:
            return False
        if abs(num - last) > 3:
            return False
        last = num
    return True



with open("input") as f:
    sum = 0
    for line in f.readlines():
        if is_safe(line):
            sum += 1
    print(sum)

