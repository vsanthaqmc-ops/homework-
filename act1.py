from array import array


box_a = {"apple", "pretzels", "popcorn"}
box_b = {"banana", "pretzels", "crackers"}


box_a.add("grapes")
box_b.add("apple")


shared_snacks = box_a.intersection(box_b)
print(f"Shared snacks: {shared_snacks}")


snack_counts = array("i", [len(box_a), len(box_b)])


snack_counts.append(len(shared_snacks))


print(f"Count of boxes/groups with 3 items: {snack_counts.count(3)}")


snack_counts.reverse()
print(f"Reversed snack counts array: {snack_counts.tolist()}")