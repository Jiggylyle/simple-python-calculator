# Collection = A container that can hold multiple values of different types
#   List[] = A collection which is ordered and changeable. Allows duplicate members.
#   Tuple() = A collection which is ordered and unchangeable. Allows duplicate members.(faster than list)
#   Set{} = A collection which is unordered, unchangeable*, and unindexed. No duplicate members.

fruits = {"Apple", "Banana", "Cherry", "Orange"}
print("Strawberry" in fruits)
fruits.add("apple")  # Add an item to the set
fruits.discard("Banana")  # Remove an item from the set
print(fruits)
