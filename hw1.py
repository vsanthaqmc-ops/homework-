habit_1 = ("Reading", (1, 1, 0, 1, 1, 0, 1))
habit_2 = ("Meditation", (1, 0, 1, 1, 1, 1, 1))

# 2. Find tuple length
print("Length of habit_1 tuple:", len(habit_1))
print("Days recorded for habit_1:", len(habit_1[1]))

# 3. Access values using indexing and slicing
print("Habit name:", habit_1[0])
print("First 3 days of completion for habit_1:", habit_1[1][:3])
print("Last day of completion for habit_1:", habit_1[1][-1])

# 4. Explore immutability
# Tuples are immutable; attempting to reassign an element causes a TypeError:
try:
    habit_1[1][0] = 0  # Tuples themselves don't support item assignment
except TypeError as e:
    print("\nError encountered:", e)
    print("Reason: Tuples are immutable and cannot be changed directly after creation.")
    