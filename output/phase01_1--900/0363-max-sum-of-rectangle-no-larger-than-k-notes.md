## Max Sum of Rectangle No Larger Than K
**Problem Link:** https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description

**Problem Statement:**
- Input format: A 2D array `matrix` of integers and an integer `k`.
- Constraints: The number of rows and columns in the matrix are between 1 and 200, and all elements in the matrix are between -100 and 100.
- Expected output format: The maximum sum of a rectangle in the matrix that is no larger than `k`.
- Key requirements and edge cases to consider:
  - Handling negative numbers and zero.
  - Rectangles can be any size, including 1x1 and the entire matrix.
  - The maximum sum might be negative if all numbers are negative.
- Example test cases with explanations:
  - Example 1: `matrix = [[1,0,1],[0,-2,3]]`, `k = 2`. The answer is 2 because the sum of the rectangle `[1, 3]` is 4, which is larger than `k`. However, the sum of the rectangle `[1]` is 1, and the sum of the rectangle `[0]` is 0. The maximum sum that is no larger than `k` is 2 from the rectangle `[0, -2, 0]`.
  - Example 2: `matrix = [[2,2,-1]]`, `k = 3`. The answer is 3 because the maximum sum that is no larger than `k` is 3 from the rectangle `[2, 2, -1]`.

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible rectangle in the matrix.
- Step-by-step breakdown:
  1. Iterate over all possible top-left and bottom-right coordinates to define a rectangle.
  2. For each rectangle, calculate the sum of its elements.
  3. Check if the sum is no larger than `k`. If it is, update the maximum sum found so far.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered.

```cpp
int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int maxSum = INT_MIN;
    
    for (int rowStart = 0; rowStart < rows; ++rowStart) {
        for (int colStart = 0; colStart < cols; ++colStart) {
            for (int rowEnd = rowStart; rowEnd < rows; ++rowEnd) {
                for (int colEnd = colStart; colEnd < cols; ++colEnd) {
                    int sum = 0;
                    for (int i = rowStart; i <= rowEnd; ++i) {
                        for (int j = colStart; j <= colEnd; ++j) {
                            sum += matrix[i][j];
                        }
                    }
                    if (sum <= k && sum > maxSum) {
                        maxSum = sum;
                    }
                }
            }
        }
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^4)$ where $n$ is the number of rows or columns in the matrix, because in the worst case, we are iterating over all elements for every possible rectangle.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input, because we only use a constant amount of space to store the maximum sum and the current sum.
> - **Why these complexities occur:** The brute force approach checks every possible rectangle, leading to a high time complexity. However, it only uses a constant amount of extra space.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a prefix sum array to efficiently calculate the sum of any rectangle in the matrix.
- Detailed breakdown of the approach:
  1. Calculate the prefix sum for the entire matrix.
  2. Use the prefix sum to calculate the sum of any rectangle in $O(1)$ time.
  3. Iterate over all possible rectangles and use the prefix sum to calculate their sums.
  4. Check if the sum is no larger than `k` and update the maximum sum if necessary.
- Proof of optimality: This approach is optimal because it reduces the time complexity of calculating the sum of a rectangle from $O(n^2)$ to $O(1)$, resulting in an overall time complexity of $O(n^4)$ for the iteration over all rectangles, which is unavoidable.

```cpp
int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int maxSum = INT_MIN;
    vector<vector<int>> prefixSum(rows + 1, vector<int>(cols + 1, 0));
    
    // Calculate prefix sum
    for (int i = 1; i <= rows; ++i) {
        for (int j = 1; j <= cols; ++j) {
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + matrix[i-1][j-1];
        }
    }
    
    // Iterate over all possible rectangles
    for (int rowStart = 0; rowStart < rows; ++rowStart) {
        for (int colStart = 0; colStart < cols; ++colStart) {
            for (int rowEnd = rowStart; rowEnd < rows; ++rowEnd) {
                for (int colEnd = colStart; colEnd < cols; ++colEnd) {
                    int sum = prefixSum[rowEnd+1][colEnd+1] - prefixSum[rowStart][colEnd+1] - prefixSum[rowEnd+1][colStart] + prefixSum[rowStart][colStart];
                    if (sum <= k && sum > maxSum) {
                        maxSum = sum;
                    }
                }
            }
        }
    }
    return maxSum;
}
```

However, we can optimize this further by using a more efficient algorithm to find the maximum sum that is no larger than `k`. We can use a `multiset` to store the cumulative sums and then for each cumulative sum, we can find the maximum sum that is no larger than `k` by checking the difference between the current cumulative sum and the smallest cumulative sum that is greater than the current cumulative sum minus `k`.

```cpp
int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
    int rows = matrix.size();
    int cols = matrix[0].size();
    int maxSum = INT_MIN;
    
    for (int left = 0; left < cols; ++left) {
        vector<int> temp(rows, 0);
        for (int right = left; right < cols; ++right) {
            for (int i = 0; i < rows; ++i) {
                temp[i] += matrix[i][right];
            }
            maxSum = max(maxSum, maxSumSubarray(temp, k));
        }
    }
    return maxSum;
}

int maxSumSubarray(vector<int>& arr, int k) {
    int maxSum = INT_MIN;
    int sum = 0;
    multiset<int> cumulativeSums;
    cumulativeSums.insert(0);
    
    for (int num : arr) {
        sum += num;
        auto it = cumulativeSums.upper_bound(sum - k);
        if (it != cumulativeSums.begin()) {
            --it;
            maxSum = max(maxSum, sum - *it);
        }
        cumulativeSums.insert(sum);
    }
    return maxSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \log n)$ where $n$ is the number of rows or columns in the matrix, because we are iterating over all elements and using a `multiset` to find the maximum sum that is no larger than `k`.
> - **Space Complexity:** $O(n)$, excluding the space needed for the input, because we are using a `multiset` to store the cumulative sums.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity of finding the maximum sum that is no larger than `k` from $O(n^4)$ to $O(n^3 \log n)$, which is the best possible time complexity for this problem.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the use of prefix sums to efficiently calculate the sum of any rectangle in the matrix.
- The problem-solving pattern identified is the use of a `multiset` to find the maximum sum that is no larger than `k`.
- The optimization technique learned is the reduction of time complexity by using a more efficient algorithm.

**Mistakes to Avoid:**
- A common implementation error is not handling the edge cases correctly, such as when the matrix is empty or when `k` is negative.
- A performance pitfall is not using a `multiset` to find the maximum sum that is no larger than `k`, which can result in a higher time complexity.
- A testing consideration is to test the function with different inputs, including edge cases, to ensure that it is working correctly.