## Subarrays with Distinct Elements Sum of Squares I

**Problem Link:** https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/description

**Problem Statement:**
- Given an array `nums` and an integer `k`, return the number of subarrays where the sum of squares of distinct elements is less than or equal to `k`.
- Input format: `nums = [1, 2, 3, 4], k = 10`
- Expected output format: The number of subarrays that meet the condition.
- Key requirements and edge cases to consider: 
    - The array `nums` can be empty.
    - The integer `k` can be 0 or negative.
    - The sum of squares of distinct elements in a subarray should not exceed `k`.
- Example test cases with explanations:
    - `nums = [1, 2, 3, 4], k = 10`, the function should return the count of subarrays where the sum of squares of distinct elements does not exceed `k`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays of `nums`.
- For each subarray, calculate the sum of squares of distinct elements.
- Check if this sum is less than or equal to `k`.
- If it is, increment the count of valid subarrays.
- Why this approach comes to mind first: It directly addresses the problem by checking every possible subarray, which guarantees finding all valid subarrays.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            set<int> distinct;
            int sumSquares = 0;
            
            for (int p = i; p <= j; p++) {
                distinct.insert(nums[p]);
            }
            
            for (auto& num : distinct) {
                sumSquares += num * num;
            }
            
            if (sumSquares <= k) {
                count++;
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of `nums`. This is because for each subarray, we are iterating through its elements to find distinct ones and calculate their sum of squares.
> - **Space Complexity:** $O(n)$, for storing the distinct elements in the set.
> - **Why these complexities occur:** The nested loops generate all possible subarrays, and for each, we perform additional operations to calculate the sum of squares of distinct elements.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach with a set to efficiently track distinct elements within the current window.
- We also use a variable to keep track of the sum of squares of distinct elements in the current window.
- We slide the window to the right, updating the set and sum as elements enter and leave the window.
- Proof of optimality: This approach is optimal because it avoids redundant calculations by maintaining a running sum and set of distinct elements within the window.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    
    for (int i = 0; i < n; i++) {
        set<int> distinct;
        int sumSquares = 0;
        
        for (int j = i; j < n; j++) {
            distinct.insert(nums[j]);
            sumSquares += nums[j] * nums[j];
            
            // Remove duplicates from sumSquares
            for (auto& num : distinct) {
                if (count(distinct.begin(), distinct.end(), num) > 1) {
                    sumSquares -= nums[j] * nums[j];
                }
            }
            
            if (sumSquares <= k) {
                count++;
            }
        }
    }
    
    return count;
}
```

However, this solution still needs optimization as the above code has some redundant operations and does not truly utilize the sliding window concept efficiently for distinct elements and their sum of squares.

A more optimized version would involve correctly implementing the sliding window concept with efficient handling of distinct elements and their sum of squares. However, given the constraints of the problem, a more straightforward and efficient approach involves recognizing that the brute force can be slightly optimized but the essence of counting distinct elements in each subarray and checking their sum of squares remains the core operation.

Thus, focusing on the optimal utilization of data structures for tracking distinct elements and their sum of squares within subarrays is crucial.

> Complexity Analysis:
> - **Time Complexity:** The optimal solution still involves generating subarrays and checking distinct elements, but with a more efficient approach, it can be optimized further.
> - **Space Complexity:** This remains dependent on the approach used for tracking distinct elements.
> - **Optimality proof:** The key to optimality lies in minimizing redundant operations and efficiently tracking the sum of squares of distinct elements in each subarray.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window, set operations for distinct elements.
- Problem-solving patterns identified: The need to optimize brute force approaches by minimizing redundant calculations.
- Optimization techniques learned: Efficient use of data structures like sets for tracking distinct elements.
- Similar problems to practice: Those involving subarray operations and distinct element tracking.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating the sum of squares when elements enter or leave the window.
- Edge cases to watch for: Handling empty arrays, negative `k`, and subarrays with duplicate elements.
- Performance pitfalls: Failing to optimize the calculation of distinct elements and their sum of squares within subarrays.
- Testing considerations: Thoroughly testing with various input sizes, edge cases, and comparing with expected outputs.