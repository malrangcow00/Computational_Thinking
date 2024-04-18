def solution(arr):
    l = len(arr)
    stk = []
    for i in range(l):
        if not stk:
            stk.append(arr[i])
        elif stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
        i += 1
    if stk:
        return stk
    return [-1]