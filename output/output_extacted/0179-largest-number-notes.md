## Largest Number
**Problem Link:** https://leetcode.com/problems/largest-number/description

**Problem Statement:**
- Input format: An array of non-negative integers `nums`.
- Constraints: `1 <= nums.length <= 100`, `0 <= nums[i] <= 10^9`.
- Expected output format: A string representing the largest number that can be formed by concatenating the integers in `nums`.
- Key requirements: The integers in `nums` should be concatenated in a way that maximizes the resulting number.
- Example test cases:
  - Input: `nums = [10, 7, 76, 415]`
    - Output: `"77641510"`
  - Input: `nums = [3, 6, 9]`
    - Output: `"963"`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible permutations of the integers in `nums` and concatenate them to form a number.
- Then, compare these numbers to find the largest one.
- This approach comes to mind first because it guarantees finding the optimal solution by exhaustively searching through all possibilities.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

void permute(vector<int>& nums, int start, int end, string& maxStr) {
    if (start == end) {
        string str;
        for (int i = 0; i < nums.size(); i++) {
            str += to_string(nums[i]);
        }
        if (str > maxStr) {
            maxStr = str;
        }
    } else {
        for (int i = start; i <= end; i++) {
            swap(nums[start], nums[i]);
            permute(nums, start + 1, end, maxStr);
            swap(nums[start], nums[i]); // backtrack
        }
    }
}

string largestNumber(vector<int>& nums) {
    string maxStr = "";
    permute(nums, 0, nums.size() - 1, maxStr);
    return maxStr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the number of integers in `nums`. This is because there are $n!$ permutations, and for each permutation, we concatenate the integers, which takes $O(n)$ time.
> - **Space Complexity:** $O(n)$, for the recursive call stack and the string used to store the maximum number found so far.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of the input integers, which leads to a factorial time complexity. The space complexity is linear due to the recursion stack and the space needed to store the maximum number.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to compare the integers in `nums` in a custom way: for any two integers `a` and `b`, we compare the strings `ab` and `ba` to determine which one should come first in the final concatenated number.
- This approach leads to a sorting algorithm where we sort the integers based on their string representations in descending order.
- We then concatenate the sorted integers to form the largest possible number.
- If the largest number starts with `0`, we return `"0"`, because the largest number that can be formed from zeros is `"0"`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string largestNumber(vector<int>& nums) {
    vector<string> strNums;
    for (int num : nums) {
        strNums.push_back(to_string(num));
    }
    
    // Custom comparator for sorting
    sort(strNums.begin(), strNums.end(), [](const string& a, const string& b) {
        return a + b > b + a;
    });
    
    string largestStr;
    for (const string& str : strNums) {
        largestStr += str;
    }
    
    // If the largest number starts with '0', return "0"
    if (largestStr[0] == '0') {
        return "0";
    }
    
    return largestStr;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of integers in `nums`. This is because we perform a custom sorting on the integers.
> - **Space Complexity:** $O(n)$, for storing the string representations of the integers.
> - **Optimality proof:** This approach is optimal because it avoids the need to generate all permutations of the integers, instead using a sorting algorithm to find the optimal arrangement in $O(n \log n)$ time.

---

### Final Notes
**Learning Points:**
- The importance of custom comparators in sorting algorithms.
- How to approach problems involving the concatenation of integers to form the largest possible number.
- The trade-off between brute force and optimal solutions in terms of time complexity.

**Mistakes to Avoid:**
- Not considering the custom sorting approach, which leads to a much more efficient solution.
- Failing to handle the edge case where the largest number starts with `0`.
- Not optimizing the solution to reduce time complexity from $O(n! \cdot n)$ to $O(n \log n)$.