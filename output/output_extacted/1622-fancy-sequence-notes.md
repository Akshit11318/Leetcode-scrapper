## Fancy Sequence
**Problem Link:** https://leetcode.com/problems/fancy-sequence/description

**Problem Statement:**
- Input: An array of integers `nums`, an array of strings `operations` where each string is one of "add", "multiply", or "index".
- Constraints: 
    - `1 <= nums.length <= 10^5`
    - `1 <= operations.length <= 10^5`
- Expected Output: An array of integers representing the sequence after applying all operations.
- Key Requirements:
    - Implement a `Fancy` class that supports three operations:
        - `add(val)`: Adds `val` to the current sequence.
        - `multiply(val)`: Multiplies the current sequence by `val`.
        - `index(idx)`: Returns the element at index `idx` in the current sequence.
    - The sequence is initially empty.
- Example Test Cases:
    - `nums = [2, 3, 4, 5]`, `operations = ["add", "add", "multiply", "index"]`, `vals = [3, 5, 2, 0]`.
    - The sequence is initially `[2, 3, 4, 5]`. After applying the operations, the sequence becomes `[2 + 3, 3 + 3, 4 + 3, 5 + 3] = [5, 6, 7, 8]`, then `[5 + 5, 6 + 5, 7 + 5, 8 + 5] = [10, 11, 12, 13]`, then `[10 * 2, 11 * 2, 12 * 2, 13 * 2] = [20, 22, 24, 26]`, and finally returns the element at index 0 which is `20`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to directly apply each operation to the sequence as given.
- For the "add" operation, we add the given value to each element in the sequence.
- For the "multiply" operation, we multiply each element in the sequence by the given value.
- For the "index" operation, we simply return the element at the specified index.

```cpp
class Fancy {
private:
    vector<int> sequence;

public:
    Fancy() {}

    void add(int val) {
        if (sequence.empty()) {
            sequence.push_back(val);
        } else {
            for (int i = 0; i < sequence.size(); i++) {
                sequence[i] += val;
            }
        }
    }

    void multiply(int val) {
        if (sequence.empty()) {
            // Handle empty sequence case
        } else {
            for (int i = 0; i < sequence.size(); i++) {
                sequence[i] *= val;
            }
        }
    }

    int index(int idx) {
        if (idx < sequence.size()) {
            return sequence[idx];
        } else {
            // Handle out of range index
            return -1; // Or throw an exception
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of operations and $m$ is the maximum size of the sequence. This is because for each operation, we potentially iterate over the entire sequence.
> - **Space Complexity:** $O(m)$ where $m$ is the maximum size of the sequence. This is because we store all elements of the sequence.
> - **Why these complexities occur:** The brute force approach involves directly modifying the sequence for each operation, leading to high time complexity due to repeated iterations over the sequence.

---

### Optimal Approach (Required)
**Explanation:**
- To optimize, we realize that we can store the cumulative sum and product of the operations separately and apply them to the sequence elements only when needed (i.e., during the "index" operation).
- We maintain two arrays: `prefix_add` to store the cumulative sum of "add" operations and `prefix_multiply` to store the cumulative product of "multiply" operations.
- For the "add" operation, we update the `prefix_add` array.
- For the "multiply" operation, we update the `prefix_multiply` array.
- For the "index" operation, we apply the cumulative operations up to the specified index to the sequence element.

```cpp
class Fancy {
private:
    vector<int> nums;
    vector<int> prefix_add;
    vector<int> prefix_multiply;

public:
    Fancy(vector<int>& nums) : nums(nums), prefix_add(nums.size()), prefix_multiply(nums.size(), 1) {
        for (int i = 0; i < nums.size(); i++) {
            prefix_add[i] = nums[i];
        }
    }

    void add(int val) {
        if (!nums.empty()) {
            if (prefix_add.size() > 0) {
                for (int i = 0; i < prefix_add.size(); i++) {
                    prefix_add[i] += val;
                }
            }
        }
    }

    void multiply(int val) {
        if (!nums.empty()) {
            if (prefix_multiply.size() > 0) {
                for (int i = 0; i < prefix_multiply.size(); i++) {
                    prefix_multiply[i] *= val;
                }
            }
        }
    }

    int index(int idx) {
        if (idx < nums.size()) {
            return prefix_multiply[idx] * prefix_add[idx];
        } else {
            // Handle out of range index
            return -1; // Or throw an exception
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$ where $n$ is the number of operations and $m$ is the size of the sequence. This is because each operation now only updates the prefix arrays.
> - **Space Complexity:** $O(m)$ where $m$ is the size of the sequence. This is because we store the prefix arrays.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations performed during each method call, leveraging the properties of cumulative sums and products to reduce computational complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: cumulative sums and products, lazy evaluation.
- Problem-solving patterns: optimizing by storing intermediate results, applying operations only when necessary.
- Optimization techniques: reducing the number of operations, using prefix arrays for efficient updates.
- Similar problems to practice: those involving array updates, cumulative operations, and optimization.

**Mistakes to Avoid:**
- Directly applying operations to the sequence without considering optimization.
- Not handling edge cases such as empty sequences or out-of-range indices.
- Failing to validate inputs and operations.
- Not considering the trade-offs between time and space complexity.