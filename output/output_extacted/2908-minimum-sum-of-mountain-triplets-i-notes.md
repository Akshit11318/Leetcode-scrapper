## Minimum Sum of Mountain Triplet
**Problem Link:** https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/description

**Problem Statement:**
- Input: An integer array `arr`.
- Constraints: The array `arr` has at least 3 elements.
- Expected output: The minimum sum of a mountain triplet if it exists; otherwise, -1.
- Key requirements: A mountain triplet is defined as a triplet `(i, j, k)` where `i < j < k` and `arr[i] < arr[j] > arr[k]`. The sum of the triplet is `arr[i] + arr[j] + arr[k]`.
- Example test cases:
  - `arr = [2,2,2,2,2]`, output: -1 (no mountain triplet exists)
  - `arr = [2,1,3]`, output: 6 (triplet (0,1,2) is a mountain triplet with sum 2+1+3=6)

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to check every possible triplet in the array to see if it forms a mountain triplet.
- Step-by-step breakdown:
  1. Generate all possible triplets from the array.
  2. For each triplet, check if it satisfies the mountain condition (`arr[i] < arr[j] > arr[k]`).
  3. If a mountain triplet is found, calculate its sum.
  4. Keep track of the minimum sum found among all mountain triplets.

```cpp
class Solution {
public:
    int minimumMountainSum(vector<int>& arr) {
        int n = arr.size();
        int minSum = INT_MAX; // Initialize minSum to a large value
        for (int i = 0; i < n - 2; ++i) {
            for (int j = i + 1; j < n - 1; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    if (arr[i] < arr[j] && arr[j] > arr[k]) {
                        int sum = arr[i] + arr[j] + arr[k];
                        minSum = min(minSum, sum);
                    }
                }
            }
        }
        return minSum == INT_MAX ? -1 : minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the array. This is because we are generating all possible triplets, which involves three nested loops.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum sum and indices.
> - **Why these complexities occur:** The brute force approach involves checking every possible triplet, leading to cubic time complexity. The space complexity is constant because we only need to keep track of a fixed amount of information.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a more efficient algorithm that takes advantage of the mountain triplet property.
- Step-by-step breakdown:
  1. Initialize variables to keep track of the minimum sum and whether a mountain triplet is found.
  2. Iterate through the array, maintaining two pointers, one starting from the left and one from the right, both moving towards the center.
  3. For each pair of pointers, check if there exists an element in between that satisfies the mountain condition.
  4. If such an element is found, update the minimum sum if necessary.

However, the optimal solution involves recognizing that for each element, we need to find the maximum element to its left that is smaller than it and the maximum element to its right that is smaller than it. This can be efficiently done by maintaining two arrays that store the maximum smaller element to the left and right of each element, respectively.

```cpp
class Solution {
public:
    int minimumMountainSum(vector<int>& arr) {
        int n = arr.size();
        vector<int> leftMax(n, 0), rightMax(n, 0);
        leftMax[0] = arr[0];
        rightMax[n-1] = arr[n-1];
        
        for (int i = 1; i < n; ++i) {
            leftMax[i] = max(leftMax[i-1], arr[i]);
        }
        for (int i = n - 2; i >= 0; --i) {
            rightMax[i] = max(rightMax[i+1], arr[i]);
        }
        
        int minSum = INT_MAX;
        for (int i = 1; i < n - 1; ++i) {
            if (arr[i] > leftMax[i-1] && arr[i] > rightMax[i+1]) {
                minSum = min(minSum, arr[i-1] + arr[i] + arr[i+1]);
            }
        }
        return minSum == INT_MAX ? -1 : minSum;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make two passes through the array to compute the `leftMax` and `rightMax` arrays, and then one more pass to find the minimum sum.
> - **Space Complexity:** $O(n)$, as we need to store the `leftMax` and `rightMax` arrays.
> - **Optimality proof:** This solution is optimal because it only requires a constant number of passes through the array, and each pass involves a linear number of operations. The use of the `leftMax` and `rightMax` arrays allows us to efficiently find the maximum smaller elements to the left and right of each element, which is necessary for identifying mountain triplets.

---

### Final Notes

**Learning Points:**
- The importance of recognizing patterns and properties of the problem that can lead to more efficient algorithms.
- The use of auxiliary arrays to store information that can be used to avoid redundant computations.
- The trade-off between time and space complexity in algorithm design.

**Mistakes to Avoid:**
- Not considering the properties of the problem that can lead to more efficient solutions.
- Failing to optimize the algorithm by reducing the number of redundant computations.
- Not properly handling edge cases, such as when no mountain triplet exists.