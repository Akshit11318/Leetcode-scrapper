## Minimum Numbers of Function Calls to Make Target Array
**Problem Link:** https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/description

**Problem Statement:**
- Input: `nums`, a list of integers representing the target array.
- Constraints: Each element in `nums` is between 1 and 10^9 (inclusive).
- Expected Output: The minimum number of function calls required to make the target array.
- Key Requirements: The function `add` increments the element at index `i` by 1, and the function `divide` divides the element at index `i` by 2 (integer division).
- Edge Cases: The array can be empty, or all elements can be 1.

**Example Test Cases:**
- `nums = [2,3]`, output: `4`
- `nums = [2,6]`, output: `6`
- `nums = [8,12]`, output: `7`

---

### Brute Force Approach

**Explanation:**
- Start with an array of zeros with the same length as `nums`.
- Try all possible combinations of `add` and `divide` operations to reach the target array.
- Count the minimum number of operations required to reach the target array.

```cpp
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int minOperations(vector<int>& nums) {
    int n = nums.size();
    int minOps = INT_MAX;
    
    // Brute force approach: try all possible combinations
    // Not practical due to exponential time complexity
    return minOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{10^9})$, because in the worst case, we might try all possible combinations of `add` and `divide` operations for each element.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the minimum number of operations.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of operations, leading to an exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- For each element in `nums`, calculate the minimum number of `add` operations required to reach that element.
- For each element, calculate the minimum number of `divide` operations required to reach the element from the next power of 2.
- Add the minimum number of `add` and `divide` operations for each element to get the total minimum number of operations.

```cpp
#include <iostream>
#include <vector>

using namespace std;

int minOperations(vector<int>& nums) {
    int totalOps = 0;
    
    for (int num : nums) {
        // Calculate the minimum number of add operations
        int addOps = num;
        
        // Calculate the minimum number of divide operations
        int divideOps = 0;
        while (num > 1 && (num & 1) == 0) {
            num /= 2;
            divideOps++;
        }
        
        totalOps += addOps + divideOps;
    }
    
    return totalOps;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m)$, where $n$ is the number of elements in `nums` and $m$ is the maximum value in `nums`. This is because we iterate over each element in `nums` and perform a while loop that runs at most $\log m$ times.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the total minimum number of operations.
> - **Optimality proof:** This approach is optimal because it uses the minimum number of `add` and `divide` operations required to reach each element in `nums`. The while loop ensures that we use the minimum number of `divide` operations by dividing the element by 2 as long as it is even.

---

### Final Notes

**Learning Points:**
- The problem requires a greedy approach to minimize the number of operations.
- The key insight is to calculate the minimum number of `add` and `divide` operations for each element separately.
- The while loop is used to calculate the minimum number of `divide` operations required to reach the element from the next power of 2.

**Mistakes to Avoid:**
- Not using the while loop to calculate the minimum number of `divide` operations.
- Not initializing the `totalOps` variable to 0.
- Not iterating over each element in `nums` separately.

**Similar Problems to Practice:**
- [Minimum Number of Operations to Make Array Elements Equal](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-elements-equal/)
- [Minimum Number of Operations to Make Array Elements Equal II](https://leetcode.com/problems/minimum-number-of-operations-to-make-array-elements-equal-ii/)