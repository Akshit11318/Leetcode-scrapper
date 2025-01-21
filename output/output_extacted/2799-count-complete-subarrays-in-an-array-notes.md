## Count Complete Subarrays in an Array
**Problem Link:** https://leetcode.com/problems/count-complete-subarrays-in-an-array/description

**Problem Statement:**
- Input format: Given an integer array `arr`.
- Constraints: The array will contain distinct integers.
- Expected output format: The number of subarrays that are complete, meaning they contain each integer from 1 to `k` at least once, where `k` is the maximum value in the subarray.
- Key requirements and edge cases to consider: Handling empty arrays, arrays with a single element, and arrays with duplicate maximum values.
- Example test cases:
  - Input: `arr = [1, 2, 3, 4, 5]`
    Output: `11`
  - Input: `arr = [1, 3, 2, 4]`
    Output: `5`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To find all possible subarrays and check each one to see if it's complete.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays from the given array.
  2. For each subarray, find the maximum value `k`.
  3. Check if all integers from 1 to `k` are present in the subarray.
  4. If the subarray is complete, increment the count.

```cpp
int countCompleteSubarrays(vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    
    // Generate all possible subarrays
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= n; j++) {
            vector<int> subarray(arr.begin() + i, arr.begin() + j);
            
            // Find the maximum value k in the subarray
            int k = *max_element(subarray.begin(), subarray.end());
            
            // Check if all integers from 1 to k are present in the subarray
            bool complete = true;
            for (int num = 1; num <= k; num++) {
                if (find(subarray.begin(), subarray.end(), num) == subarray.end()) {
                    complete = false;
                    break;
                }
            }
            
            // If the subarray is complete, increment the count
            if (complete) {
                count++;
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot k)$, where $n$ is the size of the array and $k$ is the maximum value in the subarray. The outer two loops generate all possible subarrays ($O(n^2)$), and for each subarray, we find the maximum value and check for completeness ($O(n \cdot k)$).
> - **Space Complexity:** $O(n)$, as we need to store each subarray.
> - **Why these complexities occur:** The brute force approach is inefficient because it generates all possible subarrays and checks each one individually, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a sliding window approach to efficiently generate subarrays and check for completeness.
- Detailed breakdown of the approach:
  1. Initialize a sliding window with two pointers, `left` and `right`.
  2. Expand the window to the right by incrementing `right` and adding the new element to the window.
  3. For each window, find the maximum value `k`.
  4. Check if all integers from 1 to `k` are present in the window.
  5. If the window is complete, increment the count.
  6. Shrink the window from the left by incrementing `left` and removing the leftmost element.

```cpp
int countCompleteSubarrays(vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    
    // Initialize the sliding window
    for (int left = 0; left < n; left++) {
        unordered_set<int> window;
        for (int right = left; right < n; right++) {
            window.insert(arr[right]);
            
            // Find the maximum value k in the window
            int k = *max_element(window.begin(), window.end());
            
            // Check if all integers from 1 to k are present in the window
            bool complete = true;
            for (int num = 1; num <= k; num++) {
                if (window.find(num) == window.end()) {
                    complete = false;
                    break;
                }
            }
            
            // If the window is complete, increment the count
            if (complete) {
                count++;
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$, where $n$ is the size of the array and $k$ is the maximum value in the subarray. The outer two loops generate all possible windows ($O(n^2)$), and for each window, we find the maximum value and check for completeness ($O(k)$).
> - **Space Complexity:** $O(k)$, as we need to store the elements in the window.
> - **Optimality proof:** The optimal approach is more efficient than the brute force approach because it uses a sliding window to generate subarrays, reducing the number of iterations and improving the time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window, completeness checking.
- Problem-solving patterns identified: Using a sliding window to efficiently generate subarrays.
- Optimization techniques learned: Reducing the number of iterations by using a sliding window.
- Similar problems to practice: Counting complete subarrays with additional constraints, such as a fixed window size.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly initializing the sliding window, failing to check for completeness.
- Edge cases to watch for: Handling empty arrays, arrays with a single element, and arrays with duplicate maximum values.
- Performance pitfalls: Using an inefficient algorithm, such as the brute force approach.
- Testing considerations: Thoroughly testing the implementation with various input cases, including edge cases.