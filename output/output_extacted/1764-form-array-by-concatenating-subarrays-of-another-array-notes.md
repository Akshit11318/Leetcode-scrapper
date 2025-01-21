## Form Array by Concatenating Subarrays of Another Array

**Problem Link:** https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/description

**Problem Statement:**
- Input: Two arrays, `s` and `rollMax`.
- Constraints: `1 <= s.length <= 10^5`, `s.length == rollMax.length`, `1 <= rollMax[i] <= 15`.
- Expected Output: A boolean indicating whether it's possible to form the array `s` by concatenating subarrays of another array.
- Key Requirements: Determine if the array can be formed by concatenating subarrays.
- Edge Cases: Empty input arrays, arrays with a single element, arrays with all elements being the same.

**Example Test Cases:**
- Input: `s = [1,2,3,4,5,6], rollMax = [1,1,1,1,1,1]`
  Output: `true`
- Input: `s = [1,1,2,2,3,3], rollMax = [1,1,1,1,1,1]`
  Output: `false`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible subarrays and checking if they can be concatenated to form the array `s`.
- This approach involves nested loops to generate subarrays and then checking if these subarrays can be concatenated to form `s`.

```cpp
bool canFormArray(vector<int>& s, vector<int>& rollMax) {
    int n = s.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            vector<int> subarray(s.begin() + i, s.begin() + j);
            // Check if subarray can be concatenated to form s
            bool isValid = true;
            int k = 0;
            while (k < n) {
                bool found = false;
                for (int len = 1; len <= rollMax[k]; len++) {
                    if (k + len > n) break;
                    vector<int> currSubarray(s.begin() + k, s.begin() + k + len);
                    if (currSubarray == subarray) {
                        found = true;
                        k += len;
                        break;
                    }
                }
                if (!found) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot rollMax_{max})$ where $n$ is the size of the array `s` and $rollMax_{max}$ is the maximum value in `rollMax`.
> - **Space Complexity:** $O(n)$ for storing the subarray.
> - **Why these complexities occur:** The brute force approach involves generating all possible subarrays (resulting in $O(n^2)$ complexity) and then checking if each subarray can be concatenated to form `s` (resulting in an additional $O(n \cdot rollMax_{max})$ complexity).

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a sliding window technique to generate subarrays and then checking if these subarrays can be concatenated to form `s`.
- We maintain a window of size `rollMax[i]` and check if the subarray within this window can be concatenated to form `s`.

```cpp
bool canFormArray(vector<int>& s, vector<int>& rollMax) {
    int n = s.size();
    for (int i = 0; i < n; i++) {
        int windowSize = rollMax[i];
        vector<int> subarray(s.begin() + i, s.begin() + min(i + windowSize, n));
        bool isValid = true;
        int k = 0;
        while (k < n) {
            bool found = false;
            for (int len = 1; len <= rollMax[k]; len++) {
                if (k + len > n) break;
                vector<int> currSubarray(s.begin() + k, s.begin() + k + len);
                if (currSubarray == subarray) {
                    found = true;
                    k += len;
                    break;
                }
            }
            if (!found) {
                isValid = false;
                break;
            }
        }
        if (isValid) return true;
    }
    return false;
}
```

However, the optimal approach can be further improved using a more efficient algorithm.

```cpp
bool canFormArray(vector<int>& s, vector<int>& rollMax) {
    int n = s.size();
    unordered_map<int, vector<int>> freq;
    for (int i = 0; i < n; i++) {
        freq[s[i]].push_back(i);
    }
    for (int i = 0; i < n; i++) {
        int windowSize = rollMax[i];
        int count = 0;
        for (int j = i; j < min(i + windowSize, n); j++) {
            if (freq[s[j]].size() > 0) {
                count++;
                freq[s[j]].erase(freq[s[j]].begin());
            }
        }
        if (count == windowSize) {
            return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot rollMax_{max})$ where $n$ is the size of the array `s` and $rollMax_{max}$ is the maximum value in `rollMax`.
> - **Space Complexity:** $O(n)$ for storing the frequency of each element.
> - **Optimality proof:** This is the optimal solution because we are using a sliding window technique to generate subarrays and then checking if these subarrays can be concatenated to form `s`. This approach has a linear time complexity with respect to the size of the input array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, frequency counting.
- Problem-solving patterns identified: Using a window to generate subarrays and checking if these subarrays can be concatenated to form the target array.
- Optimization techniques learned: Using a frequency map to count the occurrences of each element.
- Similar problems to practice: Problems involving sliding window techniques and frequency counting.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not checking for invalid input.
- Edge cases to watch for: Empty input arrays, arrays with a single element, arrays with all elements being the same.
- Performance pitfalls: Using inefficient algorithms, not optimizing the solution for large input sizes.
- Testing considerations: Testing the solution with different input sizes, testing the solution with edge cases.