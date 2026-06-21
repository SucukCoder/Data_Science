"""Dieses Modul implementiert den Merge-Sort-Algorithmus."""

from typing import List
import matplotlib.pyplot as plt


def merge_sort(items: List[int]) -> None:
    """Sortiert eine Liste von Ganzzahlen aufsteigend mittels Merge Sort."""
    if len(items) <= 1:
        return

    middle_index = len(items) // 2
    left_half = items[:middle_index]
    right_half = items[middle_index:]

    merge_sort(left_half)
    merge_sort(right_half)

    left_index = 0
    right_index = 0
    target_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            items[target_index] = left_half[left_index]
            left_index += 1
        else:
            items[target_index] = right_half[right_index]
            right_index += 1

        target_index += 1

    while left_index < len(left_half):
        items[target_index] = left_half[left_index]
        left_index += 1
        target_index += 1

    while right_index < len(right_half):
        items[target_index] = right_half[right_index]
        right_index += 1
        target_index += 1


def mergeSort(items: List[int]) -> None:
    """Kompatibilitätsfunktion für den ursprünglichen Funktionsnamen."""
    merge_sort(items)


# ==========================================
# ALTE PLOTS (Absichtlich behalten für den Konflikt!)
# ==========================================
my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

mergeSort(my_list)

x = range(len(my_list))
plt.plot(x, my_list)
plt.show()