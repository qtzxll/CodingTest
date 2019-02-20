# coding = utf-8

# In an array of integers, numbers 1 – 100 are stored,
# and multiple numbers are duplicated. How do you find the duplicated numbers?


class Solution:
    # 找到重复的值并赋值到duplication

    def duplicate(self, numbers, duplication):
        """
        方案1,时间复杂度O(nlogn)
        :param numbers: 传入重复数组
        :param duplication: 保存重复值
        """
        numbers = sorted(numbers)
        for i in range(1, len(numbers)):
            if numbers[i] == numbers[i - 1]:
                duplication.append(numbers[i])

    def duplicate_two(self, numbers, duplication):
        # 时间复杂度O(n)，空间复杂度O(n)

        hash_table = [None] * len(numbers)
        for i in range(len(numbers)):
            hash_value = numbers[i]
            if hash_table[hash_value]:
                duplication.append(hash_table[hash_value])
            else:
                hash_table[hash_value] = hash_value

    def duplicate_three(self, numbers, duplication):
        # 时间复杂度O(n^2)

        for i in range(0, len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] == numbers[j]:
                    duplication.append(numbers[i])

    def duplicate_four(self, numbers, duplication):
        # 时间复杂度O(n)，空间复杂度O(1)

        for i in range(len(numbers)):
            while numbers[i] != i:
                if numbers[numbers[i]] == numbers[i]:
                    duplication.append(numbers[i])
                    break
                else:
                    numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]


if __name__ == '__main__':

    solution = Solution()

    # 定义一个重复数组
    numbers = list()
    for i in range(1, 101):
        numbers.append(i)
    numbers.append(51)
    numbers.append(88)

    duplication = list()
    solution.duplicate_four(numbers, duplication)
    print("重复数值为:", duplication)
