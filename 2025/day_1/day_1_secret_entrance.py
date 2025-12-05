# Part 1
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
