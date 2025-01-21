## Subarrays with K Different Integers
**Problem Link:** [https://leetcode.com/problems/subarrays-with-k-different-integers/description](https://leetcode.com/problems/subarrays-with-k-different-integers/description)

**Problem Statement:**
- Given an array of integers `nums` and an integer `k`, return the number of good subarrays of length at least 2 where there are at least `k` different integers.
- Input format and constraints: `nums` is an array of integers with length `n`, and `k` is an integer between 1 and `n`.
- Expected output format: The number of good subarrays.
- Key requirements and edge cases to consider: Empty arrays, arrays with a single element, and arrays where `k` is larger than the number of unique elements.

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to consider every possible subarray of `nums` and count the number of different integers in each subarray.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, count the number of different integers.
  3. If the number of different integers is at least `k` and the length of the subarray is at least 2, increment the count of good subarrays.
- Why this approach comes to mind first: It's a straightforward approach that considers all possibilities, making it easy to understand and implement.

```cpp
int subarraysWithKDistinct(int* nums, int numsSize, int k) {
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        unordered_map<int, int> freq;
        for (int j = i; j < numsSize; j++) {
            freq[nums[j]]++;
            if (freq.size() >= k && j - i + 1 >= 2) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the length of `nums`, because for each element, we potentially iterate through the rest of the array.
> - **Space Complexity:** $O(n)$ for storing the frequency of each integer in the subarray.
> - **Why these complexities occur:** The nested loops over the array elements lead to the quadratic time complexity, and the map used to store frequencies contributes to the linear space complexity.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of counting all subarrays and checking their diversity, we can use a sliding window approach to efficiently count subarrays with at least `k` distinct elements.
- Detailed breakdown of the approach:
  1. Initialize two pointers, `left` and `right`, to represent the sliding window.
  2. Use an unordered map to store the frequency of each integer within the current window.
  3. Expand the window to the right by moving `right`, and for each new element, update the frequency map.
  4. When the window contains at least `k` distinct elements, start moving `left` to the right, shrinking the window, and update the count of good subarrays accordingly.
- Proof of optimality: This approach ensures that we only consider subarrays with at least `k` distinct integers and do so in a way that avoids redundant computations, leading to a significant improvement in efficiency over the brute force method.

```cpp
int subarraysWithKDistinct(int* nums, int numsSize, int k) {
    int count = 0;
    for (int i = 0; i < numsSize; i++) {
        unordered_map<int, int> freq;
        for (int j = i; j < numsSize; j++) {
            freq[nums[j]]++;
            if (freq.size() == k) {
                int right = j;
                while (right < numsSize) {
                    freq[nums[right]]++;
                    right++;
                    if (freq.size() > k) {
                        break;
                    }
                }
                right--;
                count += right - j + 1;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ in the worst case, but significantly improved over the brute force due to the efficient use of the sliding window and frequency map.
> - **Space Complexity:** $O(n)$ for the frequency map.
> - **Optimality proof:** While the time complexity remains quadratic, the practical performance is improved due to the reduced number of operations within the loops, making this approach more efficient for large inputs.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, use of frequency maps for counting distinct elements.
- Problem-solving patterns identified: Reducing computational complexity by avoiding redundant operations.
- Optimization techniques learned: Efficient use of data structures like maps to store and update frequencies.
- Similar problems to practice: Other problems involving subarrays and diversity, such as finding the longest subarray with `k` distinct elements.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the frequency map or miscounting the number of good subarrays.
- Edge cases to watch for: Handling arrays with fewer than `k` distinct elements or arrays with a length less than 2.
- Performance pitfalls: Failing to optimize the solution, leading to inefficient performance on large inputs.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases, to ensure correctness and efficiency.