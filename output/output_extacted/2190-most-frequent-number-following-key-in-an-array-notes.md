## Most Frequent Number Following Key in an Array
**Problem Link:** https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/description

**Problem Statement:**
- Input format: An array of integers `arr` and a key `k`.
- Constraints: `1 <= arr.length <= 1000` and `0 <= arr[i] <= 1000`.
- Expected output format: The most frequent number following the key `k` in the array.
- Key requirements and edge cases to consider:
  - If there are multiple numbers with the same maximum frequency, return the smallest one.
  - If the key `k` does not exist in the array, return `-1`.
- Example test cases with explanations:
  - Example 1: `arr = [2,2,2,3,3], k = 2`, output: `2`.
  - Example 2: `arr = [1,1000,1000,1000], k = 1000`, output: `1000`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through the array to find all occurrences of the key `k`, then count the frequency of each number following `k`.
- Step-by-step breakdown of the solution:
  1. Initialize a hashmap to store the frequency of each number following `k`.
  2. Iterate through the array, and for each occurrence of `k`, increment the frequency of the next number in the hashmap.
  3. Find the maximum frequency and the corresponding number(s).
  4. If there are multiple numbers with the same maximum frequency, return the smallest one.
- Why this approach comes to mind first: It directly addresses the problem statement and is easy to understand.

```cpp
int mostFrequent(int arr[], int arrSize, int k) {
    unordered_map<int, int> freq;
    for (int i = 0; i < arrSize - 1; i++) {
        if (arr[i] == k) {
            freq[arr[i + 1]]++;
        }
    }
    if (freq.empty()) return -1; // key k not found
    int maxFreq = 0, res = INT_MAX;
    for (auto& it : freq) {
        if (it.second > maxFreq) {
            maxFreq = it.second;
            res = it.first;
        } else if (it.second == maxFreq) {
            res = min(res, it.first);
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array, because we iterate through the array once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every number in the hashmap.
> - **Why these complexities occur:** The iteration through the array and the use of a hashmap to store frequencies cause these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The same as the brute force approach, but with a more efficient way to find the maximum frequency and the corresponding number.
- Detailed breakdown of the approach:
  1. Initialize a hashmap to store the frequency of each number following `k`.
  2. Iterate through the array, and for each occurrence of `k`, increment the frequency of the next number in the hashmap.
  3. Keep track of the maximum frequency and the corresponding number(s) during the iteration.
- Proof of optimality: This approach still has a time complexity of $O(n)$, but it reduces the space complexity and improves the constant factor by avoiding the extra iteration through the hashmap.

```cpp
int mostFrequent(int arr[], int arrSize, int k) {
    unordered_map<int, int> freq;
    int maxFreq = 0, res = -1;
    for (int i = 0; i < arrSize - 1; i++) {
        if (arr[i] == k) {
            freq[arr[i + 1]]++;
            if (freq[arr[i + 1]] > maxFreq) {
                maxFreq = freq[arr[i + 1]];
                res = arr[i + 1];
            } else if (freq[arr[i + 1]] == maxFreq) {
                res = min(res, arr[i + 1]);
            }
        }
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the array, because we iterate through the array once.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every number in the hashmap.
> - **Optimality proof:** This is the optimal solution because we must iterate through the array at least once to find the frequencies, and using a hashmap allows us to do so in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashmap usage, frequency counting, and optimization techniques.
- Problem-solving patterns identified: Directly addressing the problem statement and optimizing the solution.
- Optimization techniques learned: Reducing the number of iterations and improving the constant factor.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as the key `k` not existing in the array.
- Edge cases to watch for: The key `k` not existing in the array, and multiple numbers having the same maximum frequency.
- Performance pitfalls: Using inefficient data structures or algorithms, such as sorting the array instead of using a hashmap.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure correctness.