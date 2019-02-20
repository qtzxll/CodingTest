# coding = utf-8

# In an array of integers, numbers 1 – 100 are stored, with at most one occurrence.
# If one number is missing, how do you find it?


class Solution:

    def miss(self, numbers):
        """
        方法1
        :param numbers: 缺失数组
        :return: none
        """
        for i in range(1, 101):
            if i not in numbers:
                print("缺失值为：", i)

    def miss_two(self, numbers):
        # 方法2：

        # sum1 = sum(range(0,101))
        n = 100
        sum1 = n * (n + 1) / 2
        sum2 = 0
        for i in range(0, len(numbers)):
            sum2 += numbers[i]

        print("缺失值为：", sum1 - sum2)


if __name__ == '__main__':

    solution = Solution()

    # 举例
    numbers = list()
    for i in range(1, 101):
        numbers.append(i)
    numbers.remove(50)

    solution.miss_two(numbers)

