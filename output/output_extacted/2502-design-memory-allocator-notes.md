## Memory Allocator
**Problem Link:** https://leetcode.com/problems/design-memory-allocator/description

**Problem Statement:**
- Input format and constraints: The problem requires designing a memory allocator with two methods: `allocate` and `free`. The `allocate` method takes an integer `size` as input and returns the starting index of the allocated memory block if possible, or -1 if not enough memory is available. The `free` method takes an integer `mID` as input and frees the memory block with the given ID if it exists.
- Expected output format: The output of the `allocate` method is the starting index of the allocated memory block or -1. The output of the `free` method is a boolean indicating whether the memory block was successfully freed.
- Key requirements and edge cases to consider: The memory allocator should handle multiple allocations and frees, and it should not allocate memory that overlaps with existing allocations.
- Example test cases with explanations:
  - `allocate(10)`: Allocate a memory block of size 10.
  - `allocate(20)`: Allocate a memory block of size 20.
  - `free(1)`: Free the memory block with ID 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over all possible memory allocations to find a block that is large enough to satisfy the request.
- Step-by-step breakdown of the solution:
  1. Initialize an array to represent the memory, where each element represents a block of memory.
  2. When `allocate` is called, iterate over the memory array to find a block that is large enough to satisfy the request.
  3. If a block is found, mark it as allocated and return its starting index.
  4. When `free` is called, iterate over the memory array to find the block with the given ID and mark it as free.
- Why this approach comes to mind first: The brute force approach is simple to understand and implement, but it is inefficient for large memory allocations.

```cpp
class MemoryAllocator {
public:
    MemoryAllocator(int n) {
        memory.resize(n, false);
        id = 1;
    }

    int allocate(int size) {
        for (int i = 0; i <= memory.size() - size; i++) {
            bool found = true;
            for (int j = i; j < i + size; j++) {
                if (memory[j]) {
                    found = false;
                    break;
                }
            }
            if (found) {
                for (int j = i; j < i + size; j++) {
                    memory[j] = true;
                }
                allocations[id] = {i, size};
                return i;
            }
        }
        return -1;
    }

    int free(int mID) {
        if (allocations.find(mID) != allocations.end()) {
            auto& allocation = allocations[mID];
            for (int i = allocation.first; i < allocation.first + allocation.second; i++) {
                memory[i] = false;
            }
            allocations.erase(mID);
            return mID;
        }
        return -1;
    }

private:
    vector<bool> memory;
    map<int, pair<int, int>> allocations;
    int id;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of the memory and $m$ is the size of the allocation request.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the memory.
> - **Why these complexities occur:** The brute force approach involves iterating over the entire memory array for each allocation request, resulting in a high time complexity. The space complexity is high because we need to store the entire memory array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of iterating over the entire memory array, we can use a data structure that allows us to efficiently find free memory blocks.
- Detailed breakdown of the approach:
  1. Use a `set` to store the free memory blocks, where each block is represented by its starting index and size.
  2. When `allocate` is called, iterate over the free memory blocks to find one that is large enough to satisfy the request.
  3. If a block is found, remove it from the `set` and return its starting index.
  4. When `free` is called, add the freed block to the `set`.
- Proof of optimality: The optimal approach has a time complexity of $O(n)$, where $n$ is the number of free memory blocks. This is because we only need to iterate over the free memory blocks to find a block that is large enough to satisfy the request.

```cpp
class MemoryAllocator {
public:
    MemoryAllocator(int n) {
        freeBlocks.insert({0, n});
        id = 1;
    }

    int allocate(int size) {
        for (auto it = freeBlocks.begin(); it != freeBlocks.end(); it++) {
            if (it->second >= size) {
                int index = it->first;
                freeBlocks.erase(it);
                if (it->second > size) {
                    freeBlocks.insert({index + size, it->second - size});
                }
                allocations[id] = {index, size};
                return index;
            }
        }
        return -1;
    }

    int free(int mID) {
        if (allocations.find(mID) != allocations.end()) {
            auto& allocation = allocations[mID];
            freeBlocks.insert({allocation.first, allocation.second});
            allocations.erase(mID);
            return mID;
        }
        return -1;
    }

private:
    set<pair<int, int>> freeBlocks;
    map<int, pair<int, int>> allocations;
    int id;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of free memory blocks.
> - **Space Complexity:** $O(n)$, where $n$ is the number of free memory blocks.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n)$, where $n$ is the number of free memory blocks. This is because we only need to iterate over the free memory blocks to find a block that is large enough to satisfy the request.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of data structures such as `set` and `map` to efficiently manage memory allocations.
- Problem-solving patterns identified: The problem requires the use of a greedy algorithm to find the largest free memory block that can satisfy the allocation request.
- Optimization techniques learned: The problem demonstrates the use of optimization techniques such as using a `set` to store free memory blocks to reduce the time complexity of the algorithm.
- Similar problems to practice: Other problems that involve managing memory allocations, such as the "Memory Allocation" problem on LeetCode.

**Mistakes to Avoid:**
- Common implementation errors: One common mistake is to forget to update the `freeBlocks` set when a block is freed.
- Edge cases to watch for: One edge case is when the memory is fully allocated and there are no free blocks available.
- Performance pitfalls: One performance pitfall is to use a brute force approach that iterates over the entire memory array for each allocation request.
- Testing considerations: The algorithm should be tested with different input scenarios, including edge cases such as a fully allocated memory and a memory with no free blocks.