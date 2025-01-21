## Finding 3-Digit Even Numbers
**Problem Link:** https://leetcode.com/problems/finding-3-digit-even-numbers/description

**Problem Statement:**
- Input: An array of integers `digits` where each integer is in the range `[1, 9]`.
- Constraints: The length of `digits` is between `2` and `4` (inclusive), and `2 <= digits.length <= 4`.
- Expected Output: The number of valid, 3-digit even integers that can be formed using the given digits.
- Key Requirements: 
  - Each digit can only be used once in each number.
  - The numbers must be 3 digits long and even.
  - The input array may contain duplicates, but each digit in the output numbers must be unique.
- Edge Cases: 
  - When the input array has less than 3 unique digits.
  - When the input array does not contain any even digits.
- Example Test Cases:
  - Input: `digits = [2,1,3,0]`
    - Output: `2`
    - Explanation: The valid numbers are `102` and `120`.
  - Input: `digits = [2,2,8,8,2]`
    - Output: `7`
    - Explanation: The valid numbers are `228`, `282`, `208`, `802`, `820`, `822`, and `882`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible permutations of the digits and then checking each permutation to see if it forms a valid 3-digit even number.
- This approach comes to mind first because it directly addresses the problem statement by considering all possible combinations of the digits.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findEvenNumbers(vector<int>& digits) {
    int count = 0;
    vector<bool> used(4, false);
    vector<int> path(3);
    
    // Generate all permutations
    function<void(int)> backtrack = [&](int index) {
        if (index == 3) {
            // Check if the number is valid and even
            if (path[0] != 0 && path[2] % 2 == 0) {
                count++;
            }
            return;
        }
        
        for (int i = 0; i < digits.size(); i++) {
            if (!used[i]) {
                used[i] = true;
                path[index] = digits[i];
                backtrack(index + 1);
                used[i] = false;
            }
        }
    };
    
    backtrack(0);
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot n! / (n-3)!)$ where $n$ is the number of digits. This is because in the worst case, we are generating all permutations of the digits and checking each one.
> - **Space Complexity:** $O(n)$ for the recursion stack and the `used` vector.
> - **Why these complexities occur:** The time complexity is high because we are generating all permutations, and the space complexity is due to the recursion stack and the additional data structures used.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is recognizing that we can directly count the number of valid even numbers without generating all permutations.
- We can iterate over all possible combinations of digits for the first and last positions (ensuring the last digit is even) and then count the remaining options for the middle digit.
- This approach is optimal because it directly calculates the number of valid numbers without unnecessary permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int findEvenNumbers(vector<int>& digits) {
    int count = 0;
    sort(digits.begin(), digits.end());
    
    for (int i = 0; i < digits.size(); i++) {
        for (int j = 0; j < digits.size(); j++) {
            if (i == j) continue;
            for (int k = 0; k < digits.size(); k++) {
                if (k == i || k == j) continue;
                if (digits[i] != 0 && digits[k] % 2 == 0) {
                    count++;
                }
            }
        }
    }
    
    // Since each valid number is counted 6 times (due to permutations of the same digits), we divide by 6
    return count / 6;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of digits. This is because we have three nested loops iterating over the digits.
> - **Space Complexity:** $O(1)$ since we only use a constant amount of space to store the count and indices.
> - **Optimality proof:** This approach is optimal because it directly calculates the number of valid even numbers without generating unnecessary permutations, resulting in a significant reduction in time complexity compared to the brute force approach.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the importance of **_permutation generation_** and **_direct counting_** techniques in combinatorial problems.
- It highlights the need to consider **_optimization techniques_** to reduce computational complexity.
- The problem also illustrates the concept of **_overcounting_** and how to correct for it.

**Mistakes to Avoid:**
- **_Inefficient permutation generation_**: Generating all permutations without considering the constraints of the problem can lead to high computational complexity.
- **_Not considering duplicates_**: Failing to account for duplicate digits in the input array can result in incorrect counts.
- **_Not optimizing the counting process_**: Not using direct counting methods can lead to slower algorithms.