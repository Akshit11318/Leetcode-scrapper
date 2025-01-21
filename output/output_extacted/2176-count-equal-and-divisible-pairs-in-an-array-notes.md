## Count Equal and Divisible Pairs in an Array

**Problem Link:** https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Output: The number of pairs `(i, j)` where `i < j` such that `nums[i] == nums[j]` and `(nums[i] + nums[j]) % k == 0`.
- Key Requirements: 
    - The array `nums` contains only non-negative integers.
    - The integer `k` is greater than 0.
- Edge Cases: 
    - Empty array.
    - Array with a single element.
    - `k` equals 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every pair of elements in the array to see if they satisfy the given conditions.
- Step-by-step breakdown:
    1. Iterate through the array to consider each element as the first element of a potential pair.
    2. For each element, iterate through the rest of the array to consider every possible pair.
    3. Check if the current pair's elements are equal and if their sum is divisible by `k`.
    4. If both conditions are met, increment a counter to keep track of the number of such pairs.

```cpp
int countPairs(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); ++i) {
        for (int j = i + 1; j < nums.size(); ++j) {
            if (nums[i] == nums[j] && (nums[i] + nums[j]) % k == 0) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we potentially iterate through the rest of the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and indices.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, while the constant space complexity is due to not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a hashmap to store the frequency of each number in the array, and then iterate through the hashmap to count the pairs that satisfy the conditions.
- Detailed breakdown:
    1. Create a hashmap to store the frequency of each number in the array.
    2. Iterate through the array to populate the hashmap.
    3. Iterate through the hashmap to count the pairs that satisfy the conditions.
    4. For each number in the hashmap, calculate the number of pairs that can be formed with that number and add it to the count.

```cpp
int countPairs(vector<int>& nums, int k) {
    unordered_map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }
    
    int count = 0;
    for (auto& pair : freq) {
        int num = pair.first;
        int freqNum = pair.second;
        if (freqNum > 1 && (num + num) % k == 0) {
            count += freqNum * (freqNum - 1) / 2;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make two passes through the array: one to populate the hashmap and one to count the pairs.
> - **Space Complexity:** $O(n)$, as in the worst case, every element in the array could be unique and stored in the hashmap.
> - **Optimality proof:** This approach is optimal because we only make two passes through the array and use a hashmap to efficiently count the frequency of each number.

---

### Final Notes

**Learning Points:**
- The importance of using hashmaps to count frequencies and reduce time complexity.
- How to apply the formula for combinations to calculate the number of pairs that can be formed with a given number.
- The trade-off between time and space complexity in different approaches.

**Mistakes to Avoid:**
- Not considering the case where `k` equals 1, which would result in all pairs being counted.
- Not using a hashmap to store the frequency of each number, leading to inefficient counting.
- Not calculating the number of pairs correctly using the combination formula.