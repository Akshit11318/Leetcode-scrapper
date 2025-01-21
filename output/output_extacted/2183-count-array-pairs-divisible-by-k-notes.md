## Count Array Pairs Divisible by K

**Problem Link:** https://leetcode.com/problems/count-array-pairs-divisible-by-k/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` and an integer `k`, count the number of pairs `(nums[i], nums[j])` where `i < j` and `(nums[i] * nums[j]) % k == 0`.
- Expected output format: The number of pairs satisfying the condition.
- Key requirements and edge cases to consider: Handling large arrays, optimizing the counting process, and correctly identifying pairs that satisfy the divisibility condition.
- Example test cases with explanations:
  - For `nums = [1, 2, 3, 4, 5]` and `k = 2`, the output should be `2` because the pairs `(1, 2)` and `(3, 4)` satisfy the condition.
  - For `nums = [1, 2, 3, 4, 5]` and `k = 10`, the output should be `0` because no pairs satisfy the condition.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we can start by checking every possible pair of numbers in the array to see if their product is divisible by `k`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable to store the number of pairs that satisfy the condition.
  2. Iterate over the array for each pair of numbers `(nums[i], nums[j])` where `i < j`.
  3. For each pair, calculate the product and check if it is divisible by `k`.
  4. If the product is divisible by `k`, increment the counter.
- Why this approach comes to mind first: It's the most straightforward way to ensure all possible pairs are considered.

```cpp
int countPairs(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        for (int j = i + 1; j < nums.size(); j++) {
            if ((nums[i] * nums[j]) % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array, because we are checking every pair of numbers in the array.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the count and other variables.
> - **Why these complexities occur:** The time complexity is quadratic because of the nested loops, and the space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can optimize the counting process by using a hash map to store the frequency of each remainder when divided by `k`.
- Detailed breakdown of the approach:
  1. Initialize a hash map to store the frequency of each remainder.
  2. Iterate over the array, and for each number, calculate its remainder when divided by `k`.
  3. For each remainder, increment its frequency in the hash map.
  4. Iterate over the hash map, and for each remainder `r`, calculate the number of pairs that can be formed with numbers that have a remainder of `r` and numbers that have a remainder of `k - r`.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n^2)$ to $O(n)$ by avoiding the need to check every pair of numbers.

```cpp
int countPairs(vector<int>& nums, int k) {
    unordered_map<int, int> remainderCount;
    int count = 0;
    for (int num : nums) {
        int remainder = num % k;
        for (int i = 0; i < k; i++) {
            if ((remainder * i) % k == 0) {
                count += remainderCount[i];
            }
        }
        remainderCount[remainder]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the size of the input array and $k$ is the divisor.
> - **Space Complexity:** $O(k)$, because we are using a hash map to store the frequency of each remainder.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity by avoiding the need to check every pair of numbers, and it uses a minimal amount of space to store the frequency of each remainder.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using hash maps to optimize counting processes, and reducing time complexity by avoiding unnecessary comparisons.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems, and using data structures to store and retrieve information efficiently.
- Optimization techniques learned: Using hash maps to store frequency counts, and reducing time complexity by avoiding nested loops.
- Similar problems to practice: Counting pairs that satisfy certain conditions, and optimizing counting processes using data structures.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the remainder, or incorrectly incrementing the count.
- Edge cases to watch for: Handling large arrays, and handling cases where `k` is large.
- Performance pitfalls: Using nested loops, or using data structures that have high time complexity.
- Testing considerations: Testing with large arrays, and testing with different values of `k`.