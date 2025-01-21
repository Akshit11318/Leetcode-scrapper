## Minimize Length of Array Using Operations
**Problem Link:** https://leetcode.com/problems/minimize-length-of-array-using-operations/description

**Problem Statement:**
- Input: An array of integers `arr`.
- Constraints: The length of the array is between $1$ and $10^5$, and each element in the array is between $1$ and $10^5$.
- Expected Output: The minimum possible length of the array after applying the given operations.
- Key Requirements: The operation can be applied to any element in the array, and the goal is to minimize the length of the array.
- Edge Cases: The array can contain duplicate elements, and the length of the array can be $1$.

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible operations on each element in the array and see which one results in the minimum length.
- Step-by-step breakdown of the solution:
  1. Initialize a variable to store the minimum length found so far.
  2. Iterate over each element in the array.
  3. For each element, try all possible operations (i.e., divide the element by $2$ if it is even).
  4. After applying the operation, check if the resulting array has a smaller length than the current minimum length.
  5. If it does, update the minimum length.
- Why this approach comes to mind first: It is a straightforward way to solve the problem, but it has an exponential time complexity due to the recursive nature of trying all possible operations.

```cpp
class Solution {
public:
    int minOperation(vector<int>& arr) {
        int n = arr.size();
        int min_len = n;
        
        // Try all possible operations
        for (int mask = 0; mask < (1 << n); mask++) {
            vector<int> temp = arr;
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) != 0) {
                    if (temp[i] % 2 == 0) {
                        temp[i] /= 2;
                    }
                }
            }
            
            // Remove duplicates and update min_len
            set<int> unique(temp.begin(), temp.end());
            min_len = min(min_len, (int)unique.size());
        }
        
        return min_len;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the array. This is because we try all possible operations for each element, resulting in $2^n$ possible combinations, and for each combination, we iterate over the array to apply the operations.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array. This is because we need to store the temporary array and the set of unique elements.
> - **Why these complexities occur:** The time complexity is exponential due to the recursive nature of trying all possible operations, and the space complexity is linear due to the need to store the temporary array and the set of unique elements.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The operation can only reduce the length of the array if it results in a duplicate element. Therefore, we can focus on finding the minimum number of unique elements that can be obtained after applying the operations.
- Detailed breakdown of the approach:
  1. Initialize a set to store the unique elements.
  2. Iterate over each element in the array.
  3. For each element, apply the operation as many times as possible (i.e., divide the element by $2$ until it is odd).
  4. Add the resulting element to the set of unique elements.
- Proof of optimality: This approach is optimal because it ensures that each element is reduced to its smallest possible value, resulting in the minimum number of unique elements.

```cpp
class Solution {
public:
    int minOperation(vector<int>& arr) {
        set<int> unique;
        
        // Apply the operation to each element and add to set
        for (int num : arr) {
            while (num % 2 == 0) {
                num /= 2;
            }
            unique.insert(num);
        }
        
        return unique.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \log n)$, where $n$ is the length of the array. This is because we iterate over each element in the array and apply the operation, resulting in a logarithmic number of divisions for each element.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the array. This is because we need to store the set of unique elements.
> - **Optimality proof:** This approach is optimal because it ensures that each element is reduced to its smallest possible value, resulting in the minimum number of unique elements.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bit manipulation, set operations, and optimization techniques.
- Problem-solving patterns identified: Focusing on the minimum number of unique elements and applying operations to reduce the length of the array.
- Optimization techniques learned: Applying operations to reduce the length of the array and using sets to store unique elements.
- Similar problems to practice: Problems involving bit manipulation, set operations, and optimization techniques.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Duplicate elements, odd elements, and elements that cannot be reduced further.
- Performance pitfalls: Using exponential time complexity algorithms or not optimizing the solution.
- Testing considerations: Testing with different input sizes, edge cases, and corner cases to ensure the solution is correct and efficient.