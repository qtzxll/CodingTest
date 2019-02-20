# coding = utf-8

# Write a function to find all prime numbers up to a given number.


def prime(maxNumber):
    """1遍历获取小于maxNumber的所有素数"""
    lst = list()
    lst.append(2)

    # 从3开始挨个筛选
    for i in range(3, maxNumber):
        b = False

        # 用i除以小于i的质数j
        for j in lst:
            if i % j == 0:
                b = False
                break
            else:
                b = True
        if b == True:
            lst.append(i)
    return lst


def prime2(maxNumber):
    """2筛选法获取小于maxNumber的所有素数"""
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
    maxNumber = 1000

    lst = prime2(maxNumber)
    print(lst)
