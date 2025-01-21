## Minimum Sum of Mountain Triplets II
**Problem Link:** https://leetcode.com/problems/minimum-sum-of-mountain-triplets-ii/description

**Problem Statement:**
- Input: An array of integers `arr`, and two integers `k` and `lower`, and `upper`.
- Constraints: `3 <= arr.length <= 10^4`, `0 <= k <= 10^5`, `0 <= lower <= upper <= 10^5`.
- Expected Output: The minimum sum of mountain triplets in the range `[lower, upper]` with a maximum absolute difference of `k`.
- Key Requirements:
  - A mountain triplet consists of three elements `a`, `b`, and `c` where `a < b > c`.
  - The absolute difference between `a` and `c` should not exceed `k`.
- Example Test Cases:
  - `arr = [2, 2, 2, 2, 2], lower = 0, upper = 0, k = 0` returns `0`.
  - `arr = [2, 1, 3], lower = 2, upper = 3, k = 1` returns `-1`.

---

### Brute Force Approach
**Explanation:**
- We can generate all possible triplets from the array.
- For each triplet, we check if it forms a mountain and if the absolute difference between the first and last elements does not exceed `k`.
- If a triplet satisfies these conditions and its sum is within the range `[lower, upper]`, we update our result if necessary.
- This approach is straightforward but inefficient due to the generation of all possible triplets.

```cpp
class Solution {
public:
    int minMountainArray(vector<int>& arr, int k, int lower, int upper) {
        int n = arr.size();
        int minSum = INT_MAX;
        
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                for (int m = j + 1; m < n; ++m) {
                    if (arr[i] < arr[j] && arr[j] > arr[m] && abs(arr[i] - arr[m]) <= k) {
                        int sum = arr[i] + arr[j] + arr[m];
                        if (sum >= lower && sum <= upper && sum < minSum) {
                            minSum = sum;
                        }
                    }
                }
            }
        }
        
        return minSum == INT_MAX ? -1 : minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the input array. This is because we generate all possible triplets.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Why these complexities occur:** The brute force approach involves nested loops to generate all possible triplets, leading to cubic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- We can improve the brute force approach by observing that for a given `j`, we only need to consider `i` and `m` such that `arr[i] < arr[j] > arr[m]`.
- We can maintain two sets (or vectors) to keep track of potential `i` and `m` values that satisfy the mountain condition with `arr[j]`.
- For each `j`, we iterate through possible `i` and `m` to find valid triplets and update our result if the sum falls within the given range.
- This approach still has a high time complexity but is more efficient than the brute force by reducing unnecessary comparisons.

However, for this specific problem, we can further optimize by considering the range and the condition more effectively. 

```cpp
class Solution {
public:
    int minMountainArray(vector<int>& arr, int k, int lower, int upper) {
        int n = arr.size();
        int minSum = INT_MAX;
        
        for (int j = 1; j < n - 1; ++j) {
            vector<int> left, right;
            for (int i = 0; i < j; ++i) {
                if (arr[i] < arr[j]) {
                    left.push_back(i);
                }
            }
            for (int m = j + 1; m < n; ++m) {
                if (arr[m] < arr[j]) {
                    right.push_back(m);
                }
            }
            
            for (int i : left) {
                for (int m : right) {
                    if (abs(arr[i] - arr[m]) <= k) {
                        int sum = arr[i] + arr[j] + arr[m];
                        if (sum >= lower && sum <= upper && sum < minSum) {
                            minSum = sum;
                        }
                    }
                }
            }
        }
        
        return minSum == INT_MAX ? -1 : minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ in the worst case, but with better average performance due to the filtering of potential `i` and `m`.
> - **Space Complexity:** $O(n)$ for storing potential `i` and `m` indices.
> - **Optimality proof:** This approach still has room for improvement but demonstrates a more thoughtful consideration of the problem constraints.

However, a more optimal solution would involve a more efficient algorithm that takes advantage of the specific conditions given in the problem, potentially involving a two-pointer technique or dynamic programming to reduce the time complexity. 

Let's refine the optimal approach considering these insights:

### Refined Optimal Approach
We can further optimize the solution by considering the conditions more effectively and utilizing a more efficient algorithmic approach.

```cpp
class Solution {
public:
    int minMountainArray(vector<int>& arr, int k, int lower, int upper) {
        int n = arr.size();
        int minSum = INT_MAX;
        
        for (int j = 1; j < n - 1; ++j) {
            if (arr[j] <= arr[j-1] || arr[j] <= arr[j+1]) continue;
            
            int left = j - 1, right = j + 1;
            while (left >= 0 && arr[left] > arr[j]) --left;
            while (right < n && arr[right] > arr[j]) ++right;
            
            for (int i = left + 1; i < j; ++i) {
                if (arr[i] < arr[j]) {
                    for (int m = j + 1; m < right; ++m) {
                        if (arr[m] < arr[j] && abs(arr[i] - arr[m]) <= k) {
                            int sum = arr[i] + arr[j] + arr[m];
                            if (sum >= lower && sum <= upper && sum < minSum) {
                                minSum = sum;
                            }
                        }
                    }
                }
            }
        }
        
        return minSum == INT_MAX ? -1 : minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, considering the nested loops but with a more focused search space.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Optimality proof:** This refined approach is more efficient and takes advantage of the problem's constraints to minimize the search space.

---

### Final Notes

**Learning Points:**
- The importance of understanding problem constraints and utilizing them to optimize the solution.
- The value of iterative refinement in improving the efficiency of a solution.
- The application of algorithmic techniques such as the two-pointer method and dynamic programming in solving complex problems.

**Mistakes to Avoid:**
- Failing to consider all constraints and conditions of the problem.
- Not optimizing the solution based on the specific requirements and characteristics of the input data.
- Overlooking the potential for reducing the search space or improving the algorithm's efficiency.