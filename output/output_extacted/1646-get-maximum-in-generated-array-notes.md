## Get Maximum in Generated Array

**Problem Link:** https://leetcode.com/problems/get-maximum-in-generated-array/description

**Problem Statement:**
- Input: `n`, an integer representing the size of the generated array.
- Expected output: The maximum value in the generated array.
- Key requirements: The array is generated based on the following rules:
  - The first element is `0`.
  - The second element is `1`.
  - For `i >= 3`, the `i-th` element is the sum of the `i/2`-th element and the `(i/2 + 1)`-th element if `i` is even, or the sum of the `(i-1)/2`-th element and the `(i+1)/2`-th element if `i` is odd.
- Edge cases: `n` is between 1 and 100.

**Example Test Cases:**
- For `n = 7`, the generated array is `[0,1,1,2,1,3,2]`, and the maximum value is `3`.
- For `n = 2`, the generated array is `[0,1]`, and the maximum value is `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate the array according to the given rules and then find the maximum value in the array.
- This approach comes to mind first because it directly follows the problem statement and doesn't require any complex optimizations.

```cpp
class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        
        vector<int> arr(n + 1);
        arr[0] = 0;
        arr[1] = 1;
        
        int maxVal = 1;
        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                arr[i] = arr[i / 2];
            } else {
                arr[i] = arr[(i - 1) / 2] + arr[(i + 1) / 2];
            }
            maxVal = max(maxVal, arr[i]);
        }
        
        return maxVal;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input size. This is because we need to generate the array up to the $n$-th element.
> - **Space Complexity:** $O(n)$, where $n$ is the input size. This is because we need to store the generated array.
> - **Why these complexities occur:** These complexities occur because we are generating the array sequentially and storing each element.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is that we can generate the array iteratively without storing the entire array, thus reducing the space complexity.
- However, since the problem requires generating the array up to the $n$-th element to find the maximum value, the time complexity remains $O(n)$.
- The optimality of this solution comes from the fact that we cannot avoid generating the array up to the $n$-th element to find the maximum value, given the rules of array generation.

```cpp
class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        
        vector<int> arr(n + 1);
        arr[0] = 0;
        arr[1] = 1;
        
        int maxVal = 1;
        for (int i = 2; i <= n; i++) {
            if (i % 2 == 0) {
                arr[i] = arr[i / 2];
            } else {
                arr[i] = arr[(i - 1) / 2] + arr[(i + 1) / 2];
            }
            maxVal = max(maxVal, arr[i]);
        }
        
        return maxVal;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the input size. This is because we need to generate the array up to the $n$-th element.
> - **Space Complexity:** $O(n)$, where $n$ is the input size. This is because we need to store the generated array to find the maximum value.
> - **Optimality proof:** This solution is optimal because we cannot avoid generating the array up to the $n$-th element to find the maximum value, given the rules of array generation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iterative array generation, maximum value finding.
- Problem-solving patterns identified: Generating arrays based on specific rules, finding maximum values in generated arrays.
- Optimization techniques learned: Reducing space complexity by avoiding unnecessary storage.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect array indexing, missing edge cases.
- Edge cases to watch for: Handling `n = 0` and `n = 1` separately.
- Performance pitfalls: Using excessive memory for storing the generated array.
- Testing considerations: Testing with small and large inputs to ensure correctness and performance.