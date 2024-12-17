def read_file():
    with open("input.txt", "r") as file:
        lines = file.readlines()

    data = []
    for line in lines:
        parts = line.strip().split()
        p = tuple(map(int, parts[0][2:].split(",")))
        v = tuple(map(int, parts[1][2:].split(",")))
        data.append((p, v))
    return data


def move_steps(robots, steps, width, height):
    pos = []
    for robot in robots:
        p, v = robot
        p_new = ((p[0] + v[0] * steps) % width, (p[1] + v[1] * steps) % height)
        pos.append(p_new)
    return pos


def print_pos(pos: list[tuple[int, int]], width: int, height: int):
    for y in range(height):
        for x in range(width):
            if (x, y) in pos:
                print("#", end="")
            else:
                print(".", end="")
        print()


HEIGHT = 103
WIDTH = 101
STEPS = 100

if __name__ == "__main__":
    print("start")

    data = read_file()

    step = 11
    while True:
        pos = move_steps(data, step, WIDTH, HEIGHT)
        print_pos(pos, WIDTH, HEIGHT)
        print(f"Step: {step}")
        print("Press enter to continue")
        input()
        step += 101
