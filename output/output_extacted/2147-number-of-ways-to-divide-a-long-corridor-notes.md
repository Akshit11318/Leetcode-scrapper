## Number of Ways to Divide a Long Corridor

**Problem Link:** https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/description

**Problem Statement:**
- Input format and constraints: The input consists of a long corridor with `n` seats, represented by an array of integers where each integer represents the color of the seat. The task is to divide the corridor into `numOfParts` parts such that the number of seats of each color in each part is equal.
- Expected output format: The number of ways to divide the corridor.
- Key requirements and edge cases to consider: 
    - The input array `seats` is guaranteed to have at least `numOfParts` elements.
    - Each element in `seats` is either 1 or 0.
    - `numOfParts` is a positive integer.
- Example test cases with explanations:
    - For `seats = [1,1,1,1,1,1,1]` and `numOfParts = 4`, the output should be 3.
    - For `seats = [1,0,0,0,0,0,0,0]` and `numOfParts = 3`, the output should be 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To divide the corridor into `numOfParts` parts, we need to find all possible ways to split the array into `numOfParts` subarrays.
- Step-by-step breakdown of the solution:
    1. Generate all possible ways to split the array into `numOfParts` subarrays.
    2. For each split, check if the number of seats of each color in each part is equal.
    3. Count the number of valid splits.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it has a high time complexity due to the generation of all possible splits.

```cpp
class Solution {
public:
    int numberOfWays(vector<int>& seats, int numOfParts) {
        int n = seats.size();
        int count = 0;
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + seats[i];
        }
        for (int i = 1; i <= n; i++) {
            for (int j = i + 1; j <= n; j++) {
                for (int k = j + 1; k <= n; k++) {
                    // Generate all possible splits
                    vector<int> parts = {i, j, k};
                    bool valid = true;
                    int target = prefixSum[n] / numOfParts;
                    for (int part : parts) {
                        if (prefixSum[part] - prefixSum[part - 1] != target) {
                            valid = false;
                            break;
                        }
                    }
                    if (valid) {
                        count++;
                    }
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of seats. This is because we generate all possible splits of the array into `numOfParts` subarrays.
> - **Space Complexity:** $O(n)$ for the prefix sum array.
> - **Why these complexities occur:** The high time complexity occurs due to the generation of all possible splits, which results in a cubic time complexity. The space complexity occurs due to the prefix sum array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible splits, we can use a prefix sum array to count the number of seats of each color in each part.
- Detailed breakdown of the approach:
    1. Calculate the prefix sum array for the seats array.
    2. Calculate the target number of seats of each color in each part by dividing the total number of seats of each color by `numOfParts`.
    3. Initialize a variable `count` to store the number of ways to divide the corridor.
    4. Iterate over all possible start indices for the first part.
    5. For each start index, calculate the end index for the first part by finding the first index where the prefix sum equals the target.
    6. If the end index is valid, iterate over all possible start indices for the second part, and so on.
    7. For each valid split, increment the `count` variable.
- Proof of optimality: This approach is optimal because it avoids generating all possible splits and instead uses a prefix sum array to efficiently count the number of seats of each color in each part.

```cpp
class Solution {
public:
    int numberOfWays(vector<int>& seats, int numOfParts) {
        int n = seats.size();
        int count = 0;
        vector<int> prefixSum(n + 1, 0);
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + seats[i];
        }
        int target = prefixSum[n] / numOfParts;
        vector<int> splits;
        for (int i = 0; i < n; i++) {
            if (prefixSum[i + 1] - prefixSum[i] == target) {
                splits.push_back(i + 1);
            }
        }
        count = combinations(splits.size(), numOfParts - 1);
        return count;
    }
    
    int combinations(int n, int k) {
        if (k > n) return 0;
        long long result = 1;
        for (int i = 1; i <= k; i++) {
            result = result * (n - i + 1) / i;
        }
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of seats. This is because we iterate over the seats array once to calculate the prefix sum array.
> - **Space Complexity:** $O(n)$ for the prefix sum array.
> - **Optimality proof:** This approach is optimal because it uses a prefix sum array to efficiently count the number of seats of each color in each part, avoiding the generation of all possible splits. The time complexity is linear, making it much faster than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: prefix sum arrays, combinations.
- Problem-solving patterns identified: using prefix sum arrays to efficiently count the number of elements in each part.
- Optimization techniques learned: avoiding the generation of all possible splits by using a prefix sum array.
- Similar problems to practice: problems involving prefix sum arrays, combinations, and optimization techniques.

**Mistakes to Avoid:**
- Common implementation errors: incorrect calculation of the prefix sum array, incorrect calculation of the target number of seats of each color in each part.
- Edge cases to watch for: empty input array, invalid input values.
- Performance pitfalls: generating all possible splits, using inefficient algorithms.
- Testing considerations: test the solution with different input values, edge cases, and large input sizes.