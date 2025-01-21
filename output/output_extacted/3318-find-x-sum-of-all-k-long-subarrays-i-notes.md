## Find X Sum of All K Long Subarrays I
**Problem Link:** https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/description

**Problem Statement:**
- Input: An array `arr` and integers `k` and `x`.
- Constraints: `1 <= k <= arr.length <= 10^5`, `1 <= x <= 10^6`.
- Expected output: The sum of all subarrays of length `k` that have an `XOR` of `x`.
- Key requirements: Calculate the sum of elements in all subarrays of length `k` where the bitwise XOR of the elements equals `x`.
- Example test cases:
  - `arr = [1,2,3,4,5], k = 2, x = 7` should return `10` because the subarrays `[2,5]` and `[4,3]` have an XOR of `7` and sum up to `10`.
  - `arr = [10,5,2,6], k = 3, x = 9` should return `15` because the subarray `[5,2,6]` has an XOR of `9` and sums up to `15`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves iterating over all possible subarrays of length `k` in the given array `arr`.
- For each subarray, calculate the XOR of its elements and check if it equals `x`.
- If it does, sum up the elements of this subarray.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional insights.

```cpp
int subarrayXOR(vector<int>& arr, int k, int x) {
    int n = arr.size();
    int sum = 0;
    
    for (int i = 0; i <= n - k; ++i) {
        int subarrayXor = 0;
        int subarraySum = 0;
        
        for (int j = i; j < i + k; ++j) {
            subarrayXor ^= arr[j];
            subarraySum += arr[j];
        }
        
        if (subarrayXor == x) {
            sum += subarraySum;
        }
    }
    
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of elements in the array. This is because for each starting position, we potentially iterate over `k` elements to calculate the XOR and sum.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current subarray's XOR, sum, and the total sum.
> - **Why these complexities occur:** The brute force approach involves nested loops, leading to a time complexity that depends on both the size of the array and the length of the subarrays. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to recognize that calculating the XOR and sum of each subarray separately is inefficient.
- Instead, maintain a running XOR and sum as we slide through the array with a window of size `k`.
- This approach allows us to avoid recalculating the XOR and sum for overlapping subarrays, significantly reducing the computational effort.

```cpp
int subarrayXOR(vector<int>& arr, int k, int x) {
    int n = arr.size();
    int sum = 0;
    int currentXor = 0;
    int currentSum = 0;
    
    for (int i = 0; i < n; ++i) {
        currentXor ^= arr[i];
        currentSum += arr[i];
        
        if (i >= k) {
            currentXor ^= arr[i - k];
            currentSum -= arr[i - k];
        }
        
        if (i >= k - 1 && currentXor == x) {
            sum += currentSum;
        }
    }
    
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the current XOR, sum, and the total sum.
> - **Optimality proof:** This approach is optimal because it processes each element in the array exactly once, which is the minimum required to solve the problem. By maintaining a running XOR and sum, we efficiently calculate the desired sum without unnecessary recalculations.

---

### Final Notes

**Learning Points:**
- The importance of recognizing overlapping subproblems and avoiding redundant calculations.
- The use of sliding window techniques to efficiently process arrays.
- How maintaining running sums and XORs can simplify calculations.

**Mistakes to Avoid:**
- Failing to consider the overlap between subarrays, leading to inefficient solutions.
- Not utilizing the properties of XOR to simplify calculations.
- Overlooking the possibility of using a sliding window approach for array problems.