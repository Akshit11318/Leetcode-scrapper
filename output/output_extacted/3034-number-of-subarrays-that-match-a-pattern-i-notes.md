## Number of Subarrays That Match a Pattern I
**Problem Link:** https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= k <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected Output: The number of subarrays of `nums` that match a pattern of `k` alternating odd and even numbers, starting with an odd number.
- Key Requirements: The subarray must start with an odd number, followed by an alternating sequence of odd and even numbers, and have a total length of `k`.
- Edge Cases: Handle arrays with less than `k` elements, arrays with all odd or all even numbers, and arrays with non-alternating patterns.

**Example Test Cases:**
- `nums = [2,1,2,1,2,1,1,1], k = 3`, Expected Output: `2` (Subarrays `[2,1,2]` and `[1,2,1]` do not match the pattern, but `[1,2,1]` and `[1,2,1]` do).
- `nums = [1,2,1,2,1,1,1,1], k = 4`, Expected Output: `1` (Subarray `[1,2,1,2]` matches the pattern).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check every possible subarray of `nums` with length `k`.
- For each subarray, verify if it starts with an odd number and alternates between odd and even numbers.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i <= nums.size() - k; i++) {
        bool isValid = true;
        for (int j = 0; j < k; j++) {
            if (j % 2 == 0 && nums[i + j] % 2 == 0) {
                isValid = false;
                break;
            }
            if (j % 2 == 1 && nums[i + j] % 2 == 1) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of `nums`. This is because we are iterating over every possible subarray of length `k` and checking each element within the subarray.
> - **Space Complexity:** $O(1)$, as we are not using any additional data structures that scale with the input size.
> - **Why these complexities occur:** The time complexity is high because we are checking every subarray, which results in a lot of repeated work. The space complexity is low because we only need a constant amount of space to store the count and the current subarray being checked.

---

### Optimal Approach (Required)

**Explanation:**
- Instead of checking every subarray, we can take advantage of the alternating pattern and use a sliding window approach.
- We maintain a count of the number of subarrays seen so far and extend the window to the right, checking if the new element matches the expected parity.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i <= nums.size() - k; i++) {
        bool isValid = true;
        for (int j = 0; j < k; j++) {
            if ((j % 2 == 0 && nums[i + j] % 2 == 0) || (j % 2 == 1 && nums[i + j] % 2 == 1)) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            count++;
        }
    }
    return count;
}
```

However, we can further optimize this solution by directly checking the parity of the elements in the subarray without using a separate loop for each subarray.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i <= nums.size() - k; i++) {
        bool odd = true;
        bool isValid = true;
        for (int j = 0; j < k; j++) {
            if (odd && nums[i + j] % 2 == 0) {
                isValid = false;
                break;
            }
            if (!odd && nums[i + j] % 2 == 1) {
                isValid = false;
                break;
            }
            odd = !odd;
        }
        if (isValid) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the size of `nums`. This is still the same as the brute force approach because we are checking each subarray.
> - **Space Complexity:** $O(1)$, as we are not using any additional data structures that scale with the input size.
> - **Optimality proof:** This solution is optimal because we must check each subarray at least once to determine if it matches the pattern. However, we can potentially optimize the solution by using a more efficient algorithm or data structure.

However, we can optimize it further to $O(n)$ by using a prefix sum array where `prefix[i]` stores the parity of the sum of numbers from index 0 to i.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i <= nums.size() - k; i++) {
        int oddCount = 0;
        for (int j = 0; j < k; j++) {
            if (nums[i + j] % 2 == 1) {
                oddCount++;
            }
        }
        if (oddCount == (k + 1) / 2 && (oddCount * 2 == k || (k % 2 == 1 && oddCount * 2 == k + 1))) {
            bool isValid = true;
            for (int j = 0; j < k; j++) {
                if (j % 2 == 0 && nums[i + j] % 2 == 0) {
                    isValid = false;
                    break;
                }
                if (j % 2 == 1 && nums[i + j] % 2 == 1) {
                    isValid = false;
                    break;
                }
            }
            if (isValid) {
                count++;
            }
        }
    }
    return count;
}
```

However, the above solution is still $O(n \cdot k)$.

We can further optimize the solution to $O(n)$ by using a sliding window and a hashmap to store the count of odd and even numbers in the window.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    int count = 0;
    for (int i = 0; i < nums.size(); i++) {
        int oddCount = 0;
        int evenCount = 0;
        for (int j = i; j < nums.size(); j++) {
            if (nums[j] % 2 == 1) {
                oddCount++;
            } else {
                evenCount++;
            }
            if (j - i + 1 == k) {
                if ((k % 2 == 1 && oddCount == (k + 1) / 2 && evenCount == k / 2) ||
                    (k % 2 == 0 && oddCount == k / 2 && evenCount == k / 2)) {
                    bool isValid = true;
                    int tempOddCount = 0;
                    for (int l = i; l <= j; l++) {
                        if (l - i % 2 == 0 && nums[l] % 2 == 0) {
                            isValid = false;
                            break;
                        }
                        if (l - i % 2 == 1 && nums[l] % 2 == 1) {
                            isValid = false;
                            break;
                        }
                    }
                    if (isValid) {
                        count++;
                    }
                }
                break;
            }
        }
    }
    return count;
}
```

However, the above solution is still $O(n \cdot k)$.

To optimize it further to $O(n)$, we can use a hashmap to store the count of subarrays ending at each index.

```cpp
int numberOfSubarrays(vector<int>& nums, int k) {
    unordered_map<int, int> countMap;
    countMap[0] = 1;
    int count = 0;
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (nums[i] % 2 == 1) {
            sum++;
        }
        if (i >= k) {
            if (nums[i - k] % 2 == 1) {
                sum--;
            }
        }
        if (sum % 2 == 1) {
            if (countMap.find(sum - k) != countMap.end()) {
                count += countMap[sum - k];
            }
        }
        if (countMap.find(sum) == countMap.end()) {
            countMap[sum] = 0;
        }
        countMap[sum]++;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`. This is because we are only iterating over the array once.
> - **Space Complexity:** $O(n)$, as we are using a hashmap to store the count of subarrays ending at each index.
> - **Optimality proof:** This solution is optimal because we are only iterating over the array once and using a hashmap to store the count of subarrays ending at each index. This reduces the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sliding window, hashmap, prefix sum array.
- Problem-solving patterns identified: using a hashmap to store the count of subarrays ending at each index, using a prefix sum array to store the parity of the sum of numbers.
- Optimization techniques learned: reducing the time complexity by using a hashmap and a prefix sum array.
- Similar problems to practice: problems involving subarrays, sliding window, hashmap.

**Mistakes to Avoid:**
- Common implementation errors: not checking the boundary conditions, not handling the case where the subarray has an odd length.
- Edge cases to watch for: arrays with less than `k` elements, arrays with all odd or all even numbers.
- Performance pitfalls: using a brute force approach with a high time complexity.
- Testing considerations: testing the solution with different inputs, including edge cases.