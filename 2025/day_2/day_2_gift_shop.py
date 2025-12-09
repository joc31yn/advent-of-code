class GiftShop:
    """
    Day 2 GiftShop
    """

    def is_invalid(self, num: str) -> bool:
        """
        determin whether num is invalid (only even length numbers can be)
        """
        if len(num) % 2 == 1:
            return False
        left, right = 0, len(num) // 2
        while right < len(num):
            if num[left] != num[right]:
                return False
            left += 1
            right += 1
        return True

    def part_1_sol(self):
        """
        Docstring for part_1_sol
        """
        ans = 0
        with open("2025/day_2/day_2_input.txt", encoding="utf-8") as file:
            ranges = file.readline().split(",")
            invalid_nums = set()
            for r in ranges:
                low, high = r.split("-")
                for i in range(int(low), int(high) + 1):
                    if i in invalid_nums:
                        ans += i
                    elif self.is_invalid(str(i)):
                        ans += i
                        invalid_nums.add(i)
            print(ans)

    # Part 2 (very slow sol - could try to think of smt more efficient?)
    def generate_substrings(self, num, r):
        """
        Docstring for generate_substrings
        Divides the input string into even chunks. The last chunk may be
        shorter if the string length is not evenly divisible by r.
        """
        substrings = []
        length = len(num) // r + (0 if len(num) % r == 0 else 1)
        for i in range(length):
            if (i + 1) * r < len(num):
                substrings.append(num[i * r : (i + 1) * r])
            else:
                substrings.append(num[i * r : len(num)])
        return substrings

    def is_invalid_2(self, num: str, upper_bound) -> bool:
        """
        Docstring for is_invalid_2
        Determines if a number is invalid by part 2. A number is invalid if it
        is made only of some sequence of digits repeated at least twice
        """
        for i in range(1, upper_bound + 1):
            substrings = self.generate_substrings(num, i)
            invalid = True
            for s in substrings:
                if s != substrings[0]:
                    invalid = False
            if invalid:
                return True
        return False

    def part_2_sol(self):
        """
        Docstring for part_2_sol
        """
        ans = 0
        with open("2025/day_2/day_2_input.txt", encoding="utf-8") as file:
            ranges = file.readline().split(",")
            invalid_nums = set()
            for r in ranges:
                low, high = r.split("-")
                for i in range(int(low), int(high) + 1):
                    if i in invalid_nums:
                        ans += i
                    elif self.is_invalid_2(str(i), len(str(i)) // 2):
                        ans += i
                        invalid_nums.add(i)
            print(ans)


sol = GiftShop()
sol.part_1_sol()
sol.part_2_sol()
