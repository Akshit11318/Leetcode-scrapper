## Find X Sum of All K-Long Subarrays II

**Problem Link:** https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-ii/description

**Problem Statement:**
- Input: An integer array `arr` and two integers `k` and `x`.
- Output: Return the sum of all subarray sums of length `k` that add up to `x`.
- Key Requirements:
  - `1 <= k <= arr.length <= 1000`
  - `-10^5 <= arr[i] <= 10^5`
  - `-10^5 <= x <= 10^5`
- Edge Cases:
  - Empty array
  - `k` larger than the array length
  - `x` is out of the possible sum range

**Example Test Cases:**
- `arr = [1,2,3,4], k = 2, x = 3` should return `0` because no subarray sums up to `3`.
- `arr = [1,1,1], k = 3, x = 3` should return `3` because there is one subarray that sums up to `3`.

---

### Brute Force Approach

**Explanation:**
- The initial thought is to generate all possible subarrays of length `k` and check if their sum equals `x`.
- This approach involves iterating through the array with a sliding window of size `k` to generate all subarrays.

```cpp
int kSum(vector<int>& arr, int k, int x) {
    int sum = 0;
    for (int i = 0; i <= arr.size() - k; i++) {
        int subarraySum = 0;
        for (int j = i; j < i + k; j++) {
            subarraySum += arr[j];
        }
        if (subarraySum == x) {
            sum += subarraySum;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ where $n$ is the size of the array, because for each starting position, we sum `k` elements.
> - **Space Complexity:** $O(1)$ as we use a constant amount of space.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic in terms of the array size and linear in terms of `k`, while the space complexity remains constant as we only use a fixed amount of space to store the sum and the subarray sum.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal insight is to still use a sliding window approach but calculate the sum of the subarray in constant time by maintaining a running sum of the current window.
- This approach avoids recalculating the sum of the subarray for each position, reducing the time complexity.

```cpp
int kSum(vector<int>& arr, int k, int x) {
    int sum = 0;
    for (int i = 0; i <= arr.size() - k; i++) {
        int windowSum = 0;
        for (int j = i; j < i + k; j++) {
            windowSum += arr[j];
        }
        if (windowSum == x) {
            sum += windowSum;
        }
    }
    return sum;
}
```
However, the above solution can be optimized further by using a single pass through the array and maintaining a running sum of the current window, thus avoiding the nested loop structure.

```cpp
int kSum(vector<int>& arr, int k, int x) {
    int sum = 0, windowSum = 0;
    for (int i = 0; i < arr.size(); i++) {
        windowSum += arr[i];
        if (i >= k) {
            windowSum -= arr[i - k];
        }
        if (i >= k - 1 && windowSum == x) {
            sum += windowSum;
        }
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the size of the array, because we make a single pass through the array.
> - **Space Complexity:** $O(1)$ as we use a constant amount of space.
> - **Optimality proof:** This is optimal because we must at least look at each element once to determine if it's part of a subarray that sums to `x`, and we do this in a single pass.

---

### Final Notes

**Learning Points:**
- The importance of maintaining a running sum or using a sliding window to reduce computational complexity.
- How to optimize a brute force approach by reducing unnecessary calculations.

**Mistakes to Avoid:**
- Not considering the possibility of optimizing the calculation of subarray sums.
- Failing to recognize the opportunity to use a single pass through the data to achieve the desired result.