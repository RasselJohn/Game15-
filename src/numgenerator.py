from random import shuffle


class NumGenerator:
    """Generator suit of numbers for Game15."""

    def __init__(self):
        self.generate_suit()

    def generate_suit(self):
        """Generate solved suit of numbers."""

        self.numbers = list(range(0, 16))
        while True:
            shuffle(self.numbers)
            check_value = 0

            for i in range(0, len(self.numbers) - 1):
                if self.numbers[i] == 0:
                    check_value += i // 4 + 1
                    continue

                for j in range(i + 1, len(self.numbers)):
                    if self.numbers[j] != 0 and self.numbers[i] > self.numbers[j]:
                        check_value += 1

            # if True - solved suit is found. Else repeat a shuffle.
            if check_value % 2 == 0:
                break

    def find_empty_element(self, current_index):
        """
        :param current_index:
        :return: index of zero(empty) element
        Find index of zero(empty) element using current element.
        If it's not  found - return -1.
        """

        # check left element
        if current_index % 4 != 0 and self.numbers[current_index - 1] == 0:
            return current_index - 1

        # check right element
        if (current_index + 1) % 4 != 0 and self.numbers[current_index + 1] == 0:
            return current_index + 1

        # check top element
        if current_index > 3 and self.numbers[current_index - 4] == 0:
            return current_index - 4

        # check bottom element
        if current_index < 12 and self.numbers[current_index + 4] == 0:
            return current_index + 4

        return -1

    def swap(self, index1, index2):
        self.numbers[index1], self.numbers[index2] = self.numbers[index2], self.numbers[index1]

    def index(self, num):
        return self.numbers.index(num)

    def is_sorted(self):
        return self.numbers[:-1] == sorted(self.numbers[:-1])
