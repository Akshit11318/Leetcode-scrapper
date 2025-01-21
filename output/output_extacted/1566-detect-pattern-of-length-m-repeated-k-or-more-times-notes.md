## Detect Pattern of Length M Repeated K or More Times

**Problem Link:** https://leetcode.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times/description

**Problem Statement:**
- Input: `arr`, an array of integers, and two integers `m` and `k`.
- Constraints: `2 <= m <= 100`, `2 <= k <= 100`, `m` and `k` are integers, `1 <= arr.length <= 20000`, `0 <= arr[i] <= 25`.
- Expected output: `true` if the array can be partitioned into repeated patterns of length `m` repeated at least `k` times, `false` otherwise.
- Key requirements: The pattern must be repeated at least `k` times without any elements left over.
- Example test cases:
  - Input: `arr = [1,2,4], m = 1, k = 3`, Output: `true`
  - Input: `arr = [1,2], m = 2, k = 2`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible pattern of length `m` in the array and see if it can be repeated `k` times to cover the entire array.
- Step-by-step breakdown:
  1. Iterate through the array with a sliding window of size `m`.
  2. For each window, check if the pattern can be repeated `k` times to cover the rest of the array.
  3. If such a pattern is found, return `true`.
- Why this approach comes to mind first: It's the most straightforward way to check every possibility.

```cpp
bool hasPattern(int* arr, int arrSize, int m, int k) {
    for (int i = 0; i <= arrSize - m; i++) {
        bool match = true;
        for (int j = i + m; j < arrSize; j += m) {
            for (int l = 0; l < m; l++) {
                if (arr[i + l] != arr[j + l]) {
                    match = false;
                    break;
                }
            }
            if (!match) break;
        }
        if (match && (arrSize - i) / m >= k) return true;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the size of the array. This is because for each starting position, we potentially compare every element in the pattern with every element in the rest of the array.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, as we only use a constant amount of space to store the loop variables and the match flag.
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic in relation to the size of the array, and the space complexity is constant because we don't allocate any additional data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of checking every possible pattern, we can directly construct the pattern by taking the first `m` elements of the array and then check if this pattern can be repeated `k` times to cover the entire array.
- Detailed breakdown:
  1. Extract the first `m` elements as the potential pattern.
  2. Check if the array can be divided into segments of this pattern repeated `k` times.
- Proof of optimality: This approach is optimal because it directly checks if the array can be partitioned into the required pattern without unnecessary comparisons.

```cpp
bool hasPattern(int* arr, int arrSize, int m, int k) {
    if (arrSize % m != 0 || arrSize / m < k) return false;
    
    for (int i = m; i < arrSize; i += m) {
        for (int j = 0; j < m; j++) {
            if (arr[j] != arr[i + j]) return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the size of the array. This is because we potentially compare every element in the pattern with every element in the rest of the array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the loop variables.
> - **Optimality proof:** This is the best possible complexity because we must at least read the input once, and comparing each element in the pattern with each element in the array is necessary to determine if the pattern repeats.

---

### Final Notes

**Learning Points:**
- The importance of directly constructing the pattern from the given array.
- How to efficiently check for pattern repetition in an array.
- The trade-off between brute force and optimal approaches in terms of time complexity.

**Mistakes to Avoid:**
- Not checking if the array size is a multiple of the pattern length before attempting to find the pattern.
- Not validating the input constraints before proceeding with the algorithm.
- Incorrectly calculating the time and space complexities of the algorithm.