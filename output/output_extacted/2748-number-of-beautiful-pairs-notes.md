## Number of Beautiful Pairs
**Problem Link:** https://leetcode.com/problems/number-of-beautiful-pairs/description

**Problem Statement:**
- Input format and constraints: Given two arrays `nums` and `n`, where `nums` contains distinct integers and `n` is the length of `nums`. The goal is to find the number of beautiful pairs, where a beautiful pair is defined as two numbers whose sum equals `n`.
- Expected output format: The number of beautiful pairs.
- Key requirements and edge cases to consider: The input arrays may contain negative numbers, and the sum `n` may not be achievable with any pair of numbers from `nums`.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1, 2, 3, 4], n = 7`. Output: `1` (The beautiful pair is `[3, 4]`).
  - Example 2: Input: `nums = [3, 2, 5], n = 6`. Output: `1` (The beautiful pair is `[2, 4]`, but `4` is not in `nums`. However, `[3, 3]` is a beautiful pair since `3 + 3 = 6`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every pair of numbers in `nums` to see if their sum equals `n`.
- Step-by-step breakdown of the solution:
  1. Initialize a variable `count` to store the number of beautiful pairs.
  2. Iterate over each number `i` in `nums`.
  3. For each `i`, iterate over each number `j` in `nums` (including `i` itself).
  4. Check if `i + j == n`. If true, increment `count`.
  5. Return `count`.
- Why this approach comes to mind first: It's a straightforward method that checks all possible pairs, ensuring no beautiful pairs are missed.

```cpp
int numBeautifulPairs(vector<int>& nums, int n) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = 0; j < nums.size(); j++) {
            if (nums[i] + nums[j] == n) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m^2)$, where $m$ is the number of elements in `nums`. This is because we have two nested loops iterating over `nums`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the `count` variable.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space complexity comes from only using a fixed amount of space regardless of the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Since `nums` contains distinct integers, we can use a hash set to store the elements we've seen so far and their complements with respect to `n`.
- Detailed breakdown of the approach:
  1. Initialize a set `seen` to store unique numbers from `nums`.
  2. Initialize a variable `count` to store the number of beautiful pairs.
  3. Iterate over each number `num` in `nums`.
  4. For each `num`, check if its complement (`n - num`) is in `seen`.
  5. If the complement is found, increment `count`.
  6. Add `num` to `seen`.
  7. Return `count`.
- Proof of optimality: This approach has a linear time complexity because we make a single pass through `nums`, and looking up an element in a set is a constant time operation.

```cpp
int numBeautifulPairs(vector<int>& nums, int n) {
    unordered_set<int> seen;
    int count = 0;
    for (int num : nums) {
        if (seen.find(n - num) != seen.end()) {
            count++;
        }
        seen.insert(num);
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of elements in `nums`. This is because we make a single pass through `nums`.
> - **Space Complexity:** $O(m)$, as in the worst case, we might store all elements from `nums` in the set.
> - **Optimality proof:** This is optimal because we reduce the time complexity from quadratic to linear by using a set for constant time lookups, and we cannot do better than linear time because we must at least examine each element once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using hash sets for efficient lookups, reducing time complexity by avoiding nested loops.
- Problem-solving patterns identified: Identifying unique elements and their complements to solve pairing problems efficiently.
- Optimization techniques learned: Using data structures like sets to reduce lookup times.
- Similar problems to practice: Other pairing problems that can be solved using hash sets or maps.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases like an empty input array or not handling duplicate pairs correctly.
- Edge cases to watch for: Handling cases where `n` is not achievable by any pair of numbers, or when `nums` contains negative numbers.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexities.
- Testing considerations: Thoroughly testing with various inputs, including edge cases, to ensure correctness and efficiency.