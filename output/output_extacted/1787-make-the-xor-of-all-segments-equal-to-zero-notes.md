## Make the XOR of All Segments Equal to Zero
**Problem Link:** https://leetcode.com/problems/make-the-xor-of-all-segments-equal-to-zero/description

**Problem Statement:**
- Input: An integer array `arr` of length `n`.
- Output: Return `true` if it is possible to divide the array into three non-empty segments with equal XOR sums.
- Key Requirements:
  - The array must be divided into exactly three segments.
  - Each segment must be non-empty.
  - The XOR sum of all elements in each segment must be equal.

**Example Test Cases:**
- Example 1: Input: `arr = [2,0,1,3]`, Output: `true`, Explanation: We can divide the array into [2,0], [1], [3].
- Example 2: Input: `arr = [0,1,2,3]`, Output: `false`, Explanation: No possible division satisfies the conditions.

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking all possible divisions of the array into three segments.
- For each division, calculate the XOR sum of each segment and check if they are equal.
- This approach comes to mind first because it systematically checks all possibilities.

```cpp
bool xorEqualSegments(vector<int>& arr) {
    int n = arr.size();
    for (int i = 1; i < n - 1; i++) {
        for (int j = i + 1; j < n; j++) {
            int xor1 = 0, xor2 = 0, xor3 = 0;
            for (int k = 0; k < i; k++) xor1 ^= arr[k];
            for (int k = i; k < j; k++) xor2 ^= arr[k];
            for (int k = j; k < n; k++) xor3 ^= arr[k];
            if (xor1 == xor2 && xor2 == xor3) return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the array. This is because for each possible division point `i` and `j`, we iterate through the array to calculate the XOR sums.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we only use a constant amount of space to store the XOR sums and indices.
> - **Why these complexities occur:** The brute force approach involves nested loops to consider all possible divisions and then another loop to calculate the XOR sums, leading to the cubic time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to first calculate the total XOR sum of the array. If the total XOR sum is not zero, it is impossible to divide the array into three segments with equal XOR sums because the sum of the XOR sums of the segments must equal the total XOR sum of the array.
- If the total XOR sum is zero, we can calculate the XOR sum of the first segment as we iterate through the array and check if we can find two more segments with the same XOR sum.

```cpp
bool xorEqualSegments(vector<int>& arr) {
    int n = arr.size();
    if (n < 3) return false;
    
    int totalXor = 0;
    for (int num : arr) totalXor ^= num;
    
    if (totalXor % 3 != 0) return false;
    
    int targetXor = totalXor / 3;
    int xor1 = 0, count = 0;
    for (int i = 0; i < n - 2; i++) {
        xor1 ^= arr[i];
        if (xor1 == targetXor) {
            int xor2 = 0;
            for (int j = i + 1; j < n - 1; j++) {
                xor2 ^= arr[j];
                if (xor2 == targetXor) {
                    int xor3 = 0;
                    for (int k = j + 1; k < n; k++) xor3 ^= arr[k];
                    if (xor3 == targetXor) return true;
                }
            }
        }
    }
    return false;
}
```

However, this can be optimized further by using a hashmap to store the XOR sums encountered so far and their counts, allowing us to find the segments with equal XOR sums more efficiently.

```cpp
bool xorEqualSegments(vector<int>& arr) {
    int n = arr.size();
    if (n < 3) return false;
    
    int totalXor = 0;
    for (int num : arr) totalXor ^= num;
    
    if (totalXor % 3 != 0) return false;
    
    int targetXor = totalXor / 3;
    int xor1 = 0, count = 0;
    unordered_map<int, int> xorCounts;
    for (int i = 0; i < n; i++) {
        xor1 ^= arr[i];
        if (xor1 == targetXor * 2 && i >= 2) return true;
        if (xorCounts.find(xor1 - targetXor) != xorCounts.end() && i >= 2) {
            return true;
        }
        xorCounts[xor1]++;
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array. This is because we make a single pass through the array.
> - **Space Complexity:** $O(n)$, for storing the XOR sums and their counts in the hashmap.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input array once, and the use of a hashmap allows us to efficiently find segments with equal XOR sums in a single pass.

---

### Final Notes

**Learning Points:**
- The importance of calculating the total XOR sum of the array to determine if it's possible to divide the array into segments with equal XOR sums.
- Using a hashmap to store XOR sums and their counts can significantly improve the efficiency of finding segments with equal XOR sums.
- Optimization techniques such as avoiding unnecessary iterations and using data structures like hashmaps can greatly reduce the time complexity of an algorithm.

**Mistakes to Avoid:**
- Not checking if the total XOR sum is zero before attempting to divide the array into segments.
- Not using a hashmap or similar data structure to efficiently store and look up XOR sums.
- Failing to consider the constraints of the problem, such as the requirement for exactly three non-empty segments.