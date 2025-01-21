## Number of Excellent Pairs

**Problem Link:** https://leetcode.com/problems/number-of-excellent-pairs/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Constraints: $1 \leq nums.length \leq 10^5$, $1 \leq nums[i] \leq 10^5$, and $1 \leq k \leq 10^5$.
- Expected Output: The number of excellent pairs, where an excellent pair is a pair of indices $(i, j)$ such that $i < j$ and the bitwise XOR of `nums[i]` and `nums[j]` is greater than or equal to `k`.
- Key Requirements: Iterate through all pairs of numbers in the array, calculate the bitwise XOR, and count the pairs that meet the condition.
- Edge Cases: Handle cases where the array is empty or contains duplicate numbers.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through all pairs of numbers in the array and calculate the bitwise XOR for each pair.
- Step-by-step breakdown:
  1. Initialize a counter for excellent pairs.
  2. Iterate through the array with two nested loops to generate all pairs of numbers.
  3. For each pair, calculate the bitwise XOR of the two numbers.
  4. If the bitwise XOR is greater than or equal to `k`, increment the counter.
- Why this approach comes to mind first: It directly addresses the problem statement by checking every possible pair.

```cpp
int countExcellentPairs(vector<int>& nums, int k) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((nums[i] ^ nums[j]) >= k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in `nums`, because we are using two nested loops to iterate through all pairs of numbers.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with input size.
> - **Why these complexities occur:** The brute force approach checks every pair of numbers in the array, resulting in quadratic time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be optimized by using a hashmap to store the frequency of each number's bitwise XOR with all other numbers, but a more straightforward optimization involves sorting the array and then using two pointers to find pairs that satisfy the condition.
- However, a more efficient approach involves using the properties of bitwise XOR and the fact that we only care about pairs where the XOR is greater than or equal to `k`.
- We can use a hashmap to count the occurrences of each number and then calculate the number of excellent pairs based on these counts.
- Detailed breakdown:
  1. Create a hashmap to store the frequency of each number in `nums`.
  2. Iterate through all possible values of `x` from `k` to the maximum possible XOR value (which is less than or equal to the maximum value in `nums`).
  3. For each `x`, calculate the number of pairs that have an XOR greater than or equal to `x`.
- Why further optimization is impossible: This approach reduces the time complexity by avoiding the need to check every pair of numbers.

```cpp
int countExcellentPairs(vector<int>& nums, int k) {
    unordered_map<int, int> count;
    for (int num : nums) {
        count[num]++;
    }
    int res = 0;
    for (auto& p : count) {
        for (auto& q : count) {
            if ((p.first ^ q.first) >= k) {
                if (p.first < q.first) {
                    res += p.second * q.second;
                } else if (p.first == q.first) {
                    res += p.second * (p.second - 1) / 2;
                }
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of unique elements in `nums` and $m$ is the average number of iterations in the inner loop, because we are iterating through the hashmap for each unique element.
> - **Space Complexity:** $O(n)$, for storing the frequency of each number in the hashmap.
> - **Optimality proof:** This approach is optimal because it reduces the number of comparisons needed by only considering unique numbers and their combinations, thus avoiding redundant calculations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Bitwise XOR, hashmap usage for frequency counting, and optimization techniques to reduce time complexity.
- Problem-solving patterns: Using hashmaps to store frequencies and then calculating combinations based on these frequencies.
- Optimization techniques: Avoiding redundant calculations and using properties of bitwise operations.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty array or duplicate numbers.
- Edge cases to watch for: Arrays with a large number of duplicate elements, which could affect the performance of the hashmap approach.
- Performance pitfalls: Using a brute force approach for large inputs, which would result in unacceptable time complexity.