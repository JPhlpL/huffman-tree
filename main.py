
#Create mapping from characters
"""
A -> 9
B -> 2
C -> 4
D -> 5
E -> 8
F -> 1
"""

import heapq

# Step 1: Character to number (frequency)
char_to_number = {
    'A': 9,
    'B': 2,
    'C': 4,
    'D': 5,
    'E': 8,
    'F': 1
}

# Step 2: Build initial heap with a counter to avoid comparison errors
heap = []
counter = 0  # tie-breaker for equal frequency

for char, freq in char_to_number.items():
    heap.append([freq, counter, char])  # [frequency, tie-breaker, character]
    counter += 1

heapq.heapify(heap)

# Step 3: Build Huffman Tree (no classes, no functions)
while len(heap) > 1:
    left = heapq.heappop(heap)
    right = heapq.heappop(heap)

    combined_freq = left[0] + right[0]
    new_node = [left, right]
    heapq.heappush(heap, [combined_freq, counter, new_node])
    counter += 1

# Step 4: Traverse tree to generate codes
codes = {}
stack = [(heap[0], "")]  # (node, code)

while stack:
    node, code = stack.pop()
    freq, _, value = node

    if isinstance(value, str):
        codes[value] = code  # It's a leaf node (character)
    else:
        # It's an internal node
        left, right = value
        stack.append((right, code + "1"))  # right = 1
        stack.append((left, code + "0"))   # left = 0

# Step 5: Output Huffman codes
input_char = "ABC" # Put here your mapped character from A - F

encoded = "".join(codes[ch] for ch in input_char)
print(f"{input_char}: {encoded}")






