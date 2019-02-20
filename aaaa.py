import time
start=time.clock()

def primes2(maxNumber):
    '''筛选法获取小于maxNumber的所有素数'''
    # 待判断整数
    lst = list(range(3, maxNumber, 2))
    # 最大整数的平方根
    m = int(maxNumber ** 0.5)
    for index in range(m):
        current = lst[index]
        # 如果当前数字已大于最大整数的平方根，结束判断
        if current > m:
            break
        # 对该位置之后的元素进行过滤
        lst[index + 1:] = list(
            filter(
                lambda x: 0 if not x % current else x,
                lst[index + 1:]))
    # 2也是素数
    return [2] + lst



if __name__ == '__main__':
    maxnumber = 500000
    list = primes2(maxnumber)
    print(list)
    t = (time.clock() - start)
    print(t)
