## Minimum Impossible OR

**Problem Link:** [https://leetcode.com/problems/minimum-impossible-or/description](https://leetcode.com/problems/minimum-impossible-or/description)

**Problem Statement:**
- Input format and constraints: The input consists of an integer array `nums`.
- Expected output format: The function should return the smallest integer that cannot be represented as the bitwise OR of any subset of the given array.
- Key requirements and edge cases to consider: The array can contain duplicates, and the smallest integer that cannot be represented as the bitwise OR of any subset of the given array should be returned.
- Example test cases with explanations:
    - For `nums = [1, 2, 4, 8, 16]`, the output should be `31` because all numbers from `0` to `30` can be represented as the bitwise OR of a subset of `nums`.
    - For `nums = [1, 2]`, the output should be `3` because `3` cannot be represented as the bitwise OR of any subset of `nums`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves checking all possible subsets of the given array and calculating their bitwise OR. Then, we iterate through all integers from `0` to the maximum possible value (which is the sum of all elements in the array) and check if they can be represented as the bitwise OR of any subset.
- Step-by-step breakdown of the solution:
    1. Generate all possible subsets of the given array.
    2. Calculate the bitwise OR of each subset.
    3. Store the bitwise OR values in a set to eliminate duplicates.
    4. Iterate through all integers from `0` to the maximum possible value.
    5. For each integer, check if it is present in the set of bitwise OR values.
    6. Return the first integer that is not present in the set.

```cpp
class Solution {
public:
    int minimumImpossibleOR(vector<int>& nums) {
        int n = nums.size();
        unordered_set<int> orValues;
        for (int mask = 0; mask < (1 << n); mask++) {
            int orValue = 0;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    orValue |= nums[i];
                }
            }
            orValues.insert(orValue);
        }
        int i = 0;
        while (orValues.find(i) != orValues.end()) {
            i++;
        }
        return i;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n + m)$, where $n$ is the number of elements in the array and $m$ is the maximum possible value. The first term accounts for generating all subsets and calculating their bitwise OR, while the second term accounts for iterating through all integers.
> - **Space Complexity:** $O(2^n)$, where $n$ is the number of elements in the array. This is because we store the bitwise OR values of all subsets in a set.
> - **Why these complexities occur:** The brute force approach has an exponential time complexity due to generating all possible subsets of the given array. The space complexity is also exponential because we store the bitwise OR values of all subsets in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the smallest integer that cannot be represented as the bitwise OR of any subset. We start with an integer `i` initialized to `0` and iterate through the array. For each element `nums[j]`, we check if the `j`-th bit is set in `i`. If it is not set, we set it and update `i` to be the bitwise OR of `i` and `nums[j]`. If all bits are set in `i`, we return `i + 1` as the smallest integer that cannot be represented as the bitwise OR of any subset.
- Detailed breakdown of the approach:
    1. Initialize `i` to `0`.
    2. Iterate through the array.
    3. For each element `nums[j]`, check if the `j`-th bit is set in `i`.
    4. If it is not set, set it and update `i` to be the bitwise OR of `i` and `nums[j]`.
    5. If all bits are set in `i`, return `i + 1`.

```cpp
class Solution {
public:
    int minimumImpossibleOR(vector<int>& nums) {
        int i = 0;
        for (int num : nums) {
            i |= num;
        }
        return i + 1;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we iterate through the array once.
> - **Space Complexity:** $O(1)$, which means the space required does not change with the size of the input array. This is because we only use a constant amount of space to store the variables.
> - **Optimality proof:** The optimal approach has a linear time complexity because we only need to iterate through the array once to find the smallest integer that cannot be represented as the bitwise OR of any subset. The space complexity is constant because we only use a constant amount of space to store the variables.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, bitwise operations.
- Problem-solving patterns identified: Finding the smallest integer that cannot be represented as the bitwise OR of any subset.
- Optimization techniques learned: Using a greedy approach to reduce the time complexity.
- Similar problems to practice: Finding the smallest integer that cannot be represented as the sum of any subset, finding the smallest integer that cannot be represented as the product of any subset.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not using bitwise operations correctly.
- Edge cases to watch for: Empty array, array with duplicates.
- Performance pitfalls: Using an exponential time complexity approach, not using a greedy approach.
- Testing considerations: Testing with different input sizes, testing with different input values.