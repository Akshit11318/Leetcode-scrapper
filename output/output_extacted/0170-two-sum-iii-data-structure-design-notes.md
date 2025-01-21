## Two Sum III - Data Structure Design
**Problem Link:** https://leetcode.com/problems/two-sum-iii-data-structure-design/description

**Problem Statement:**
- Design a data structure to handle two operations:
  - `void add(int num)`: Add the number to the data structure.
  - `bool find(int num)`: Return `true` if any `x` and `y` exist in the data structure such that `x + y == num`, otherwise return `false`.
- Input format and constraints: Numbers added are integers, and the data structure should efficiently handle both operations.
- Expected output format: `bool` for the `find` operation.
- Key requirements and edge cases to consider: Handling duplicates, negative numbers, and zero.
- Example test cases with explanations:
  - Adding numbers and then checking for sums.
  - Handling edge cases like adding zero or negative numbers.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Store all numbers in a list and for each `find` operation, check every pair of numbers to see if their sum matches the target.
- Step-by-step breakdown of the solution:
  1. Create a list to store all numbers.
  2. For the `add` operation, append the number to the list.
  3. For the `find` operation, iterate through all pairs of numbers in the list and check if any pair sums up to the target number.
- Why this approach comes to mind first: It's the most straightforward way to ensure that we consider all possible pairs of numbers.

```cpp
class TwoSum {
public:
    vector<int> nums;
    void add(int num) {
        nums.push_back(num);
    }
    bool find(int num) {
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == num) return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ for the `add` operation and $O(n^2)$ for the `find` operation, where $n$ is the number of elements in the data structure.
> - **Space Complexity:** $O(n)$, as we store all numbers in the list.
> - **Why these complexities occur:** The `add` operation is linear because we simply append to the list, while the `find` operation is quadratic due to checking all pairs of numbers.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a `unordered_set` (hash set) to store the numbers allows for constant time lookup, which can significantly speed up the `find` operation.
- Detailed breakdown of the approach:
  1. Create an `unordered_set` to store all numbers.
  2. For the `add` operation, insert the number into the set.
  3. For the `find` operation, for each number in the set, check if the difference between the target number and the current number exists in the set.
- Proof of optimality: This approach ensures that both operations are efficient, with the `add` operation being $O(1)$ on average and the `find` operation being $O(n)$ in the worst case, where $n$ is the number of elements in the data structure.

```cpp
class TwoSum {
public:
    unordered_set<int> nums;
    void add(int num) {
        nums.insert(num);
    }
    bool find(int num) {
        for (auto n : nums) {
            if (nums.find(num - n) != nums.end() && num - n != n) return true;
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `add` operation and $O(n)$ for the `find` operation, where $n$ is the number of elements in the data structure.
> - **Space Complexity:** $O(n)$, as we store all numbers in the set.
> - **Optimality proof:** The use of an `unordered_set` minimizes the time complexity for both operations, making this approach optimal for the given problem constraints.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using data structures like `unordered_set` for efficient lookup and insertion.
- Problem-solving patterns identified: Breaking down problems into operations and optimizing each operation separately.
- Optimization techniques learned: Choosing the right data structure based on the operations required.
- Similar problems to practice: Other problems involving efficient insertion and lookup, such as implementing a hash table.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like duplicates or negative numbers.
- Edge cases to watch for: Ensuring that the solution correctly handles all possible inputs, including zero and negative numbers.
- Performance pitfalls: Using data structures that lead to inefficient operations, such as using a list for lookup-heavy operations.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases.