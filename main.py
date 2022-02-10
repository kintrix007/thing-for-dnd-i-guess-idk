#!/usr/bin/python3

from itertools import permutations


def main() -> None:
    dice_values = [int(i) for i in input().strip().split() if i != ""]
    assert len(dice_values) == 9
    tables_values: dict[int, list[int]] = {}

    for throws in set(permutations(dice_values)):
        table = list(throws)
        table_value = get_table_value(table)
        tables_values[table_value] = table
    
    best_value, best_table = sorted(tables_values.items())[-1]
    
    print(best_table[:3])
    print(best_table[3:6])
    print(best_table[6:])
    print(best_value)

def get_table_value(table: list[int]) -> int:
    def sum_indeces(*indeces: list[int]) -> int:
        return sum(table[i] for i in indeces)

    sums = [
        sum_indeces(0,1,2),
        sum_indeces(3,4,5),
        sum_indeces(6,7,8),
        sum_indeces(0,3,6),
        sum_indeces(1,4,7),
        sum_indeces(2,5,8),
        sum_indeces(0,4,8),
        sum_indeces(2,4,6),
    ]

    return sum(sorted(sums)[:-2])


if __name__ == "__main__":
    main()
