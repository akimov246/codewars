from typing import List, Tuple

example = ['###.###', '#.....#', '#.....#', '#.....#', '#######']
example2 = [' #####', ' #...#', ' ....#', ' #...#', '##...#', '#....#', '######']

def make_coord_dict(office: list[str]) -> dict:
    coords = {}
    for i, string in enumerate(office):
        for j, char in enumerate(string):
            coords.update({(j, i): char})
    return coords


def locate_entrance(office: List[str]) -> Tuple[int, int]:
    coords = make_coord_dict(office)
    for i, string in enumerate(office):
        for j, char in enumerate(string):
            if char == ".":
                # Проверка выхода
                up = coords.get((j, i - 1))
                down = coords.get((j, i + 1))
                left = coords.get((j - 1, i))
                right = coords.get((j + 1, i))
                check = [up, down, left, right]
                #print(check)
                if " " in check or None in check:
                    return j, i

def main():
    e = example2
    print(locate_entrance(e))

if __name__ == "__main__":
    main()