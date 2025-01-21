## Biggest Single Number

**Problem Link:** [https://leetcode.com/problems/biggest-single-number/description](https://leetcode.com/problems/biggest-single-number/description)

**Problem Statement:**
- Input: A list of integers `nums`.
- Constraints: The input list contains only integers.
- Expected Output: The largest number that appears only once in the list.
- Key Requirements: The solution should handle cases where there are multiple single numbers, and the output should be the largest among them.
- Edge Cases: If there are no single numbers, the solution should return -1.

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over the list and count the occurrence of each number. Then, we can find the largest number that appears only once.
- Step-by-step breakdown of the solution:
  1. Create a map to store the frequency of each number.
  2. Iterate over the list to count the frequency of each number.
  3. Iterate over the map to find the largest number that appears only once.
- Why this approach comes to mind first: It's straightforward and easy to understand, but it may not be efficient for large lists.

```cpp
int largestUniqueNumber(vector<int>& nums) {
    unordered_map<int, int> count;
    for (int num : nums) {
        count[num]++;
    }
    int maxUnique = -1;
    for (auto& pair : count) {
        if (pair.second == 1) {
            maxUnique = max(maxUnique, pair.first);
        }
    }
    return maxUnique;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the list. This is because we iterate over the list twice: once to count the frequency and once to find the largest unique number.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique elements in the list. This is because we use a map to store the frequency of each number.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the list twice, and the space complexity occurs because we use a map to store the frequency of each number.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal in terms of time complexity, but we can make some minor improvements by using a single pass through the list.
- Detailed breakdown of the approach:
  1. Create a map to store the frequency of each number.
  2. Iterate over the list to count the frequency of each number and keep track of the largest unique number.
- Proof of optimality: The time complexity is still $O(n)$, but we reduce the number of iterations by half.
- Why further optimization is impossible: We must iterate over the list at least once to count the frequency of each number, so the time complexity cannot be improved further.

```cpp
int largestUniqueNumber(vector<int>& nums) {
    unordered_map<int, int> count;
    int maxUnique = -1;
    for (int num : nums) {
        count[num]++;
        if (count[num] == 1) {
            maxUnique = max(maxUnique, num);
        } else if (count[num] == 2) {
            maxUnique = max(maxUnique, -1);
        }
    }
    return maxUnique;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the list. This is because we iterate over the list only once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique elements in the list. This is because we use a map to store the frequency of each number.
> - **Optimality proof:** The time complexity is optimal because we must iterate over the list at least once to count the frequency of each number.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, frequency counting, and iteration.
- Problem-solving patterns identified: Using a map to store frequency and iterating over the list to find the largest unique number.
- Optimization techniques learned: Reducing the number of iterations by half.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the map or maxUnique variable.
- Edge cases to watch for: Handling cases where there are no single numbers.
- Performance pitfalls: Using inefficient data structures or algorithms.
- Testing considerations: Testing with large lists and edge cases.