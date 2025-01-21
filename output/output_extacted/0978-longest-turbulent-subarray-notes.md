## Longest Turbulent Subarray

**Problem Link:** [https://leetcode.com/problems/longest-turbulent-subarray/description](https://leetcode.com/problems/longest-turbulent-subarray/description)

**Problem Statement:**
- Input format: An integer array `arr` of length `n`.
- Constraints: `1 <= n <= 10^4`, `1 <= arr[i] <= 10^6`.
- Expected output format: The length of the longest turbulent subarray.
- Key requirements and edge cases to consider:
  - A subarray is turbulent if the difference between any two adjacent elements is either strictly increasing or strictly decreasing.
  - The subarray must contain at least two elements.
- Example test cases with explanations:
  - `arr = [9,4,2,10,7,8,8,1,9]`, the longest turbulent subarray is `[9, 4, 2, 10, 7, 8, 8, 1, 9]` with length 9.
  - `arr = [4,8,12,16]`, the longest turbulent subarray is `[4, 8]` or `[8, 12]` or `[12, 16]` with length 2.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every possible subarray to see if it's turbulent.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible subarrays of the given array.
  2. For each subarray, check if it's turbulent by comparing the differences between adjacent elements.
  3. Keep track of the longest turbulent subarray found.
- Why this approach comes to mind first: It's a straightforward, intuitive solution that checks all possibilities.

```cpp
#include <vector>
using namespace std;

int maxTurbulenceSize(vector<int>& arr) {
    int n = arr.size();
    int maxLength = 1;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            vector<int> subarray(arr.begin() + i, arr.begin() + j);
            if (isTurbulent(subarray)) {
                maxLength = max(maxLength, (int)subarray.size());
            }
        }
    }
    return maxLength;
}

bool isTurbulent(vector<int>& subarray) {
    if (subarray.size() < 2) return false;
    bool increasing = false, decreasing = false;
    for (int i = 1; i < subarray.size(); i++) {
        if (subarray[i] > subarray[i - 1]) {
            if (decreasing) return false;
            increasing = true;
        } else if (subarray[i] < subarray[i - 1]) {
            if (increasing) return false;
            decreasing = true;
        } else {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we're generating all possible subarrays ($O(n^2)$) and checking each one for turbulence ($O(n)$).
> - **Space Complexity:** $O(n)$, as we need to store each subarray.
> - **Why these complexities occur:** The brute force approach checks all possibilities, resulting in high time complexity. The space complexity is due to storing subarrays.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all subarrays, we can keep track of the longest turbulent subarray ending at each position.
- Detailed breakdown of the approach:
  1. Initialize two arrays, `up` and `down`, to store the length of the longest turbulent subarray ending at each position with the last difference being positive and negative, respectively.
  2. Iterate over the array, updating `up` and `down` based on the current difference.
  3. Keep track of the maximum length seen so far.
- Proof of optimality: This approach has a linear time complexity because we only need to make one pass through the array.

```cpp
int maxTurbulenceSize(vector<int>& arr) {
    int n = arr.size();
    if (n == 1) return 1;
    int up = 1, down = 1;
    int maxLength = 1;
    for (int i = 1; i < n; i++) {
        if (arr[i] > arr[i - 1]) {
            up = down + 1;
            down = 1;
        } else if (arr[i] < arr[i - 1]) {
            down = up + 1;
            up = 1;
        } else {
            up = down = 1;
        }
        maxLength = max(maxLength, max(up, down));
    }
    return maxLength;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we're making a single pass through the array.
> - **Space Complexity:** $O(1)$, as we only need a constant amount of space to store the `up`, `down`, and `maxLength` variables.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the array, resulting in the lowest possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, single-pass algorithms.
- Problem-solving patterns identified: Keeping track of the longest/shortest subarray ending at each position.
- Optimization techniques learned: Avoiding unnecessary computations by only considering the last difference.
- Similar problems to practice: Longest increasing/decreasing subsequence, longest palindromic subsequence.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases correctly (e.g., arrays of length 1).
- Edge cases to watch for: Arrays with duplicate elements, arrays with only increasing/decreasing elements.
- Performance pitfalls: Using brute force approaches for large inputs.
- Testing considerations: Test with arrays of varying lengths and patterns to ensure correctness.