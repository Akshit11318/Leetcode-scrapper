## Distinct Numbers in Each Subarray
**Problem Link:** https://leetcode.com/problems/distinct-numbers-in-each-subarray/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` and an integer `k`, return the number of subarrays of size `k` that contain distinct elements.
- Expected output format: The number of subarrays of size `k` with distinct elements.
- Key requirements and edge cases to consider: 
  - The array `nums` contains integers.
  - The integer `k` is the size of the subarray.
  - A subarray is considered valid if it has `k` distinct elements.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1,2,1,2,3], k = 2`, Output: `7`. Explanation: The subarrays of size 2 with distinct elements are `[1,2], [1,2], [2,1], [2,3], [1,2], [2,1], [1,3]`.
  - Example 2: Input: `nums = [1,2,1,3,4], k = 3`, Output: `3`. Explanation: The subarrays of size 3 with distinct elements are `[1,2,1], [2,1,3], [1,3,4]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the array and for each starting index, generate all possible subarrays of size `k`.
- Step-by-step breakdown of the solution:
  1. Iterate through the array using a nested loop to generate all possible subarrays of size `k`.
  2. For each subarray, check if all elements are distinct.
  3. If the subarray has distinct elements, increment the count.
- Why this approach comes to mind first: This approach is straightforward and simple to understand, as it checks every possible subarray.

```cpp
int subarraysWithKDistinct(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i <= nums.size() - k; i++) {
        unordered_set<int> distinct;
        for (int j = i; j < i + k; j++) {
            distinct.insert(nums[j]);
        }
        if (distinct.size() == k) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of the array. This is because we are iterating through the array and for each starting index, we are generating a subarray of size `k`.
> - **Space Complexity:** $O(k)$, where $k$ is the size of the subarray. This is because we are using a set to store the distinct elements in the subarray.
> - **Why these complexities occur:** The time complexity is $O(n \cdot k)$ because we are iterating through the array and generating all possible subarrays of size `k`. The space complexity is $O(k)$ because we are using a set to store the distinct elements in the subarray.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to generate all possible subarrays of size `k` and use a map to store the frequency of each element in the subarray.
- Detailed breakdown of the approach:
  1. Initialize a map to store the frequency of each element in the subarray.
  2. Initialize two pointers, `left` and `right`, to represent the sliding window.
  3. Move the `right` pointer to the right and add the element to the map.
  4. If the size of the map is greater than `k`, move the `left` pointer to the right and remove the element from the map.
  5. If the size of the map is equal to `k`, increment the count.
- Proof of optimality: This approach is optimal because it generates all possible subarrays of size `k` and checks if they have distinct elements in $O(n)$ time.

```cpp
int subarraysWithKDistinct(vector<int>& nums, int k) {
    int count = 0;
    int left = 0;
    unordered_map<int, int> freq;
    for (int right = 0; right < nums.size(); right++) {
        freq[nums[right]]++;
        while (freq.size() > k) {
            freq[nums[left]]--;
            if (freq[nums[left]] == 0) {
                freq.erase(nums[left]);
            }
            left++;
        }
        if (freq.size() == k) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the array. This is because we are iterating through the array once.
> - **Space Complexity:** $O(k)$, where $k$ is the size of the subarray. This is because we are using a map to store the frequency of each element in the subarray.
> - **Optimality proof:** This approach is optimal because it generates all possible subarrays of size `k` and checks if they have distinct elements in $O(n)$ time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, using a map to store the frequency of each element.
- Problem-solving patterns identified: Using a map to store the frequency of each element, moving the `left` and `right` pointers to generate all possible subarrays.
- Optimization techniques learned: Using a sliding window approach to reduce the time complexity.
- Similar problems to practice: Problems that involve generating all possible subarrays and checking if they have certain properties.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the size of the map is greater than `k`, not moving the `left` pointer to the right when the size of the map is greater than `k`.
- Edge cases to watch for: When the array is empty, when `k` is greater than the size of the array.
- Performance pitfalls: Using a brute force approach that generates all possible subarrays and checks if they have distinct elements.
- Testing considerations: Testing the function with different inputs, including edge cases.