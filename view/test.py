# import sys
# line = sys.stdin.readline()
# n = int(line)

# paths = ''
# for i in range(n):
#     line2 = sys.stdin.readline()
#     path = str(line2)
#     paths += path[0: len(path) - 1]


# def canEscape(paths):
#     l = 0
#     r = 0
#     straight = 0
#     across = 0
#     direction = 1
#     for step in paths:
#         if step == 'L':
#             direction += 1
#             direction %= 4
#             l += 1
#             l %= 4
#         elif step == 'R':
#             direction -= 1
#             direction %= 4
#             r += 1
#             r %= 4
#         elif step == 'S':
#             if direction == 1:
#                 straight += 1
#             elif direction == 2:
#                 across += 1
#             elif direction == 3:
#                 straight -= 1
#             else:
#                 across -= 1
    
#     flag = l == r and (abs(across) > 0 or abs(straight) > 0)
#     return 'yes' if flag else 'no'

#     # return 'yes' if (abs(l - r) % 4 == 0 and ) else 'no'

# print(canEscape(paths))


def calculator(formula):
    start, end = 0, 0
    nums, op = [], []
    for i in range(len(formula)):
        if formula[i] == '+' or formula[i] == '-':
            end = i
            num = int(formula[start: end])
            nums.append(num)
            op.append(formula[i])
            start = i + 1
    nums.append(int(formula[start:len(formula)]))
    print(nums)
    print(op)
    
    sum, subSum = nums[0], 0
    flag = False
    for i in range(len(op)):
        if op[i] == '-':
            sum -= subSum
            subSum = nums[i + 1]
            flag = True
        else:
            if flag:
                subSum += nums[i + 1]
            else:
                sum += nums[i + 1]
    return sum - subSum

print(calculator('008-9+10+007'))