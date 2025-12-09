class Lobby:
    """
    Day 3 Lobby
    """

    def part_1_sol(self):
        """
        Docstring for part_1_sol
        Assuming length of each bank is >= 2
        """
        with open("2025/day_3/day_3_input.txt", encoding="utf-8") as file:
            ans = 0
            for bank in file:
                tens_index = 0
                ones_index = 1
                bank = bank.strip()
                for i, c in enumerate(bank):
                    if c > bank[tens_index] and i < len(bank) - 1:
                        tens_index = i
                        ones_index = i + 1
                    if i > tens_index and c > bank[ones_index]:
                        ones_index = i
                ans += int(bank[tens_index]) * 10 + int(bank[ones_index])
            print(ans)


sol = Lobby()
sol.part_1_sol()
