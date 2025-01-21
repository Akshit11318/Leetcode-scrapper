## Zero Array Transformation I
**Problem Link:** https://leetcode.com/problems/zero-array-transformation-i/description

**Problem Statement:**
- Input: An integer array `nums` of length `n`.
- Constraints: `1 <= n <= 10^5`, `1 <= nums[i] <= 10^9`.
- Expected Output: The transformed array after applying the given operations.
- Key Requirements: For each element `nums[i]`, find the nearest zero and calculate the absolute difference between `nums[i]` and this zero.
- Edge Cases: If there is no zero to the left or right of `nums[i]`, consider the nearest boundary of the array as the reference point.
- Example Test Cases:
  - Input: `nums = [1,0,1,2,0,1,1]`
  - Output: `[1,0,1,2,0,1,1]`
  - Explanation: For each element, the nearest zero is found, and the absolute difference is calculated.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating through the array for each element to find the nearest zero, either to the left or the right, and then calculating the absolute difference.
- This approach is straightforward but inefficient due to the nested iteration.

```cpp
vector<int> transformArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n);
    
    for (int i = 0; i < n; i++) {
        int leftZero = -1, rightZero = n;
        // Find nearest zero to the left
        for (int j = i - 1; j >= 0; j--) {
            if (nums[j] == 0) {
                leftZero = j;
                break;
            }
        }
        
        // Find nearest zero to the right
        for (int j = i + 1; j < n; j++) {
            if (nums[j] == 0) {
                rightZero = j;
                break;
            }
        }
        
        // Calculate the absolute difference
        if (leftZero == -1) result[i] = abs(i - rightZero);
        else if (rightZero == n) result[i] = abs(i - leftZero);
        else result[i] = min(abs(i - leftZero), abs(i - rightZero));
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because for each element, we potentially scan the entire array to find the nearest zero.
> - **Space Complexity:** $O(n)$, for storing the result array.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, and the need to store the transformed array leads to the linear space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use two passes: one from left to right and another from right to left, to find the nearest zero for each element efficiently.
- We maintain two arrays, `left` and `right`, where `left[i]` stores the distance to the nearest zero to the left of `i`, and `right[i]` stores the distance to the nearest zero to the right of `i`.
- This approach reduces the time complexity significantly by avoiding nested iterations.

```cpp
vector<int> transformArray(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n), left(n, n), right(n, n);
    
    // Pass 1: From left to right
    int lastZero = -1;
    for (int i = 0; i < n; i++) {
        if (nums[i] == 0) lastZero = i;
        else if (lastZero != -1) left[i] = i - lastZero;
    }
    
    // Pass 2: From right to left
    lastZero = n;
    for (int i = n - 1; i >= 0; i--) {
        if (nums[i] == 0) lastZero = i;
        else if (lastZero != n) right[i] = lastZero - i;
    }
    
    // Calculate the result
    for (int i = 0; i < n; i++) {
        if (left[i] == n) result[i] = right[i];
        else if (right[i] == n) result[i] = left[i];
        else result[i] = min(left[i], right[i]);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make two linear passes through the array.
> - **Space Complexity:** $O(n)$, for storing the `left`, `right`, and `result` arrays.
> - **Optimality proof:** This approach is optimal because it minimizes the number of iterations required to find the nearest zero for each element, achieving a linear time complexity.

---

### Final Notes

**Learning Points:**
- The importance of **two-pass algorithms** in reducing time complexity.
- **Distance arrays** can efficiently store and calculate distances to nearest elements with specific properties (e.g., zeros).
- **Optimization techniques** like avoiding nested iterations can significantly improve performance.

**Mistakes to Avoid:**
- Implementing **inefficient algorithms** without considering the scale of the input.
- Not **validating inputs** and handling edge cases properly.
- Failing to **optimize space complexity** when possible.