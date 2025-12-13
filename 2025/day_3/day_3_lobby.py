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

    def part_2_sol(self):
        """
        Docstring for part_2_sol
        """
        with open("2025/day_3/day_3_input.txt", encoding="utf-8") as file:
            ans = 0
            for bank in file:
                final_num = 0
                formatted_bank = bank.strip()
                length = len(formatted_bank)

                # indexes represent number, array stores indexes of
                # where the number appears in the bank in reverse order
                # e.g. bank = 9583721653
                # appearances[3] = [9, 3]
                appearances = [[] for i in range(10)]
                highest_num = 1
                for i in range(len(formatted_bank) - 1, -1, -1):
                    c = int(formatted_bank[i])
                    if c > highest_num:
                        highest_num = c
                    appearances[c].append(i)

                limit = 12
                prev_index = -1
                # for each of the 12 digits, find highest available one that
                # still has [limit] digits after it to satisfy 12 digits
                while limit > 0:
                    for i in range(len(appearances) - 1, 0, -1):
                        found = False
                        for j in range(len(appearances[i]) - 1, -1, -1):
                            num = appearances[i][j]
                            if length - num >= limit and num > prev_index:
                                final_num = final_num * 10 + i
                                prev_index = num
                                limit -= 1
                                found = True
                                appearances[i].pop()
                                break
                        if found:
                            break
                ans += final_num
            print(ans)


sol = Lobby()
sol.part_1_sol()
sol.part_2_sol()
