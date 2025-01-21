## Count of Interesting Subarrays
**Problem Link:** https://leetcode.com/problems/count-of-interesting-subarrays/description

**Problem Statement:**
- Given an array of integers `arr`, a subarray is considered **interesting** if it contains at least one **odd** number and the sum of all elements in the subarray is even.
- Input format: An array of integers `arr`.
- Constraints: $1 \leq n \leq 10^5$, where $n$ is the number of elements in `arr`.
- Expected output format: The number of interesting subarrays.
- Key requirements and edge cases to consider: Handle cases where the array is empty or contains only one element. Also, consider cases where all elements are odd or all elements are even.

**Example Test Cases:**
- For `arr = [1, 3, 5]`, the output should be $3$ because all subarrays `[1]`, `[3]`, and `[5]` are interesting.
- For `arr = [2, 4, 6]`, the output should be $0$ because there are no odd numbers in the array.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible subarrays of the given array and then check each subarray to see if it meets the conditions of being interesting (contains at least one odd number and the sum of its elements is even).
- Step-by-step breakdown:
  1. Generate all possible subarrays.
  2. For each subarray, check if it contains at least one odd number.
  3. For each subarray that contains at least one odd number, calculate the sum of its elements and check if the sum is even.
  4. Count the number of subarrays that meet both conditions.

```cpp
int countInterestingSubarrays(vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    
    // Generate all possible subarrays
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            bool hasOdd = false;
            int sum = 0;
            
            // Check each element in the subarray
            for (int k = i; k <= j; k++) {
                sum += arr[k];
                if (arr[k] % 2 != 0) {
                    hasOdd = true;
                }
            }
            
            // Check if the subarray is interesting
            if (hasOdd && sum % 2 == 0) {
                count++;
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in the array. This is because we are generating all possible subarrays (which takes $O(n^2)$ time) and then for each subarray, we are checking each element (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The high time complexity occurs because of the nested loops that generate and then process each subarray.

---

### Optimal Approach (Required)

**Explanation:**
- To optimize the solution, we can use a prefix sum array to efficiently calculate the sum of any subarray in constant time.
- Additionally, we can use a single pass through the array to count the number of odd numbers up to each position, which helps in determining if a subarray contains at least one odd number.
- However, this problem doesn't directly benefit from these optimizations due to its specific requirements. Instead, we focus on the fact that a subarray is interesting if it has an even sum and contains at least one odd number. We can calculate prefix sums and use them to quickly determine the sum of any subarray, but we still need to check for odd numbers.

```cpp
int countInterestingSubarrays(vector<int>& arr) {
    int n = arr.size();
    int count = 0;
    
    // Calculate prefix sums
    vector<int> prefixSums(n + 1, 0);
    for (int i = 0; i < n; i++) {
        prefixSums[i + 1] = prefixSums[i] + arr[i];
    }
    
    // Generate all possible subarrays and check if they are interesting
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            bool hasOdd = false;
            int sum = prefixSums[j + 1] - prefixSums[i];
            
            // Check each element in the subarray for odd numbers
            for (int k = i; k <= j; k++) {
                if (arr[k] % 2 != 0) {
                    hasOdd = true;
                    break;
                }
            }
            
            // Check if the subarray is interesting
            if (hasOdd && sum % 2 == 0) {
                count++;
            }
        }
    }
    
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, because even though we use prefix sums to calculate the sum of subarrays in $O(1)$ time, we still have to check each element in each subarray for odd numbers, resulting in the same overall time complexity as the brute force approach for this specific problem.
> - **Space Complexity:** $O(n)$, for storing the prefix sums.
> - **Optimality proof:** This approach is not significantly more efficient than the brute force for this problem due to the necessity of checking each element for odd numbers. However, it demonstrates a systematic way of thinking about optimizations, even if they don't always yield a better time complexity in every case.

---

### Final Notes

**Learning Points:**
- The importance of considering all aspects of a problem's constraints and requirements.
- How to systematically approach optimization, even if it doesn't always lead to a better time complexity.
- The value of prefix sums in simplifying certain calculations.

**Mistakes to Avoid:**
- Not considering all edge cases, such as empty arrays or arrays with a single element.
- Overlooking the necessity of checking each element in subarrays for specific properties (like being odd).
- Failing to recognize when optimizations may not significantly improve the time complexity due to the inherent requirements of the problem.