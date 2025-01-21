## Equal Sum Arrays With Minimum Number of Operations

**Problem Link:** https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/description

**Problem Statement:**
- Input: Two integer arrays `nums1` and `nums2`.
- Constraints: Both arrays are non-empty and have the same length.
- Expected Output: The minimum number of operations required to make the sum of elements in `nums1` equal to the sum of elements in `nums2`.
- Key Requirements:
  - An operation is defined as adding `1` to an element in `nums1` or subtracting `1` from an element in `nums2`.
  - The goal is to find the minimum number of such operations.
- Edge Cases:
  - If the sums of `nums1` and `nums2` are already equal, return `0`.
  - If one array is longer than the other, the problem statement does not apply.
- Example Test Cases:
  - Input: `nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]`
    - Output: `3`
    - Explanation: You can add `1` to the elements of `nums1` to make them equal to the sum of `nums2`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying to adjust each element in `nums1` and `nums2` to make their sums equal.
- This involves calculating the difference in sums between the two arrays and then trying to distribute this difference across the elements of the arrays.
- However, this approach quickly becomes complex as it involves considering all possible combinations of adjustments.

```cpp
int minOperations(vector<int>& nums1, vector<int>& nums2) {
    int sum1 = accumulate(nums1.begin(), nums1.end(), 0);
    int sum2 = accumulate(nums2.begin(), nums2.end(), 0);
    int diff = abs(sum1 - sum2);
    int operations = 0;
    
    if (sum1 > sum2) {
        for (int i = 0; i < nums1.size(); i++) {
            if (diff == 0) break;
            if (nums1[i] > 1) {
                int decrease = min(diff, nums1[i] - 1);
                nums1[i] -= decrease;
                diff -= decrease;
                operations += decrease;
            }
        }
    } else {
        for (int i = 0; i < nums2.size(); i++) {
            if (diff == 0) break;
            if (nums2[i] < 6) {
                int increase = min(diff, 6 - nums2[i]);
                nums2[i] += increase;
                diff -= increase;
                operations += increase;
            }
        }
    }
    
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the size of the arrays and $m$ is the maximum possible value in the arrays (in this case, $6$), because in the worst case, we might need to adjust every element in the arrays.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the sums and the difference.
> - **Why these complexities occur:** The brute force approach considers adjusting every element in the worst case, leading to a high time complexity. However, it only uses a fixed amount of space to store the necessary variables.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight to the optimal solution is recognizing that we should prioritize adjustments that result in the largest reduction of the difference in sums.
- Since the values in `nums1` and `nums2` are between `1` and `6`, the maximum reduction in the difference per operation is achieved by either subtracting `1` from a `6` in `nums1` or adding `1` to a `1` in `nums2`.
- This approach ensures that we minimize the number of operations required to equalize the sums.

```cpp
int minOperations(vector<int>& nums1, vector<int>& nums2) {
    if (nums1.size() > 6 * nums2.size() || nums2.size() > 6 * nums1.size()) {
        return -1; // Impossible to make sums equal
    }
    
    int sum1 = accumulate(nums1.begin(), nums1.end(), 0);
    int sum2 = accumulate(nums2.begin(), nums2.end(), 0);
    int diff = abs(sum1 - sum2);
    int operations = 0;
    vector<int> freq1(7), freq2(7);
    
    for (int num : nums1) freq1[num]++;
    for (int num : nums2) freq2[num]++;
    
    if (sum1 > sum2) {
        for (int i = 6; i > 0; i--) {
            if (freq1[i] > 0) {
                int ops = min(diff, freq1[i]);
                diff -= ops;
                operations += ops;
                if (diff == 0) break;
            }
        }
    } else {
        for (int i = 1; i <= 6; i++) {
            if (freq2[i] > 0) {
                int ops = min(diff, freq2[i]);
                diff -= ops;
                operations += ops;
                if (diff == 0) break;
            }
        }
    }
    
    return operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the arrays, because we iterate through the arrays to calculate frequencies and then iterate through the frequencies to calculate the operations.
> - **Space Complexity:** $O(1)$, because we use a fixed amount of space to store the frequencies of the numbers in the arrays.
> - **Optimality proof:** This approach is optimal because it prioritizes the operations that result in the largest reduction of the difference in sums, ensuring the minimum number of operations are used.

---

### Final Notes

**Learning Points:**
- The importance of prioritizing operations based on their impact on the problem.
- How to approach problems that require minimizing a certain metric (in this case, the number of operations).
- The use of frequency arrays to efficiently calculate the number of operations.

**Mistakes to Avoid:**
- Not considering the constraints of the problem (e.g., the range of values in the arrays).
- Not prioritizing operations based on their impact.
- Not using efficient data structures (e.g., frequency arrays) to simplify the solution.