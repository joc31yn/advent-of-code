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


sol = GiftShop()
sol.part_1_sol()
