class SecretEntrance:
    def part_1_sol(self):
        """
        Docstring for part_1_sol
        """
        current = 50
        ans = 0
        with open("2025/day_1/day_1_input.txt") as file:
            for rotation in file:
                dir = rotation[:1]
                num = int(rotation[1:])
                if dir == "L":
                    current = (current - num) % 100
                else:
                    current = (current + num) % 100
                if current == 0:
                    ans += 1
        print(ans)

    def part_2_sol(self):
        """
        Docstring for part_2_sol
        """
        current = 50
        ans = 0
        with open("2025/day_1/day_1_input.txt") as file:
            for rotation in file:
                dir = rotation[:1]
                num = int(rotation[1:])
                if dir == "L":
                    if num >= current:
                        temp = num - current
                        whole = temp // 100
                        ans += whole
                        if current != 0:
                            ans += 1
                    current = (current - num) % 100
                else:
                    if num + current > 99:
                        temp = num - (100 - current)
                        whole = temp // 100
                        ans += whole
                        # add 1 even if current is 0 because subtracted 100
                        # incorrectly if current was 0 on line 40
                        ans += 1
                    current = (current + num) % 100
        print(ans)


sol = SecretEntrance()
sol.part_2_sol()
