## Largest Time for Given Digits
**Problem Link:** https://leetcode.com/problems/largest-time-for-given-digits/description

**Problem Statement:**
- Input: Four digits `A = [a1, a2, a3, a4]`
- Output: The largest 24-hour time that can be formed using these digits. If no valid time can be formed, return an empty string.
- Key requirements:
  - `00 <= a1, a2, a3, a4 <= 99`
  - The time must be in the format `HHMM`
- Edge cases:
  - Invalid times (e.g., `25:00`, `00:60`)
  - No valid time can be formed

**Example Test Cases:**
- Input: `A = [1, 2, 3, 4]`
  - Output: `"23:41"`
- Input: `A = [5, 5, 5, 5]`
  - Output: `""`

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of the given digits to form a time.
- Step-by-step breakdown:
  1. Generate all permutations of the input array `A`.
  2. For each permutation, form a time string in the format `HHMM`.
  3. Validate the time string (check if `HH < 24` and `MM < 60`).
  4. Keep track of the maximum valid time found.

```cpp
#include <algorithm>
#include <string>

using namespace std;

string largestTimeFromDigits(vector<int>& A) {
    string maxTime = "";
    sort(A.begin(), A.end(), greater<int>());
    
    do {
        int h = A[0] * 10 + A[1];
        int m = A[2] * 10 + A[3];
        
        if (h < 24 && m < 60) {
            string time = to_string(h) + (m < 10 ? ":0" : ":") + to_string(m);
            if (time > maxTime) maxTime = time;
        }
    } while (next_permutation(A.begin(), A.end()));
    
    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4! \cdot 1) = O(24)$, where $4!$ is the number of permutations of the input array.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the maximum time and the current permutation.
> - **Why these complexities occur:** The time complexity is dominated by the number of permutations generated, and the space complexity is constant because we only use a fixed amount of space to store the maximum time and the current permutation.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to generate all permutations of the input array in descending order, so that we can stop as soon as we find a valid time.
- Detailed breakdown:
  1. Generate all permutations of the input array `A` in descending order.
  2. For each permutation, form a time string in the format `HHMM`.
  3. Validate the time string (check if `HH < 24` and `MM < 60`).
  4. Return the first valid time found, as it will be the maximum.

```cpp
#include <algorithm>
#include <string>

using namespace std;

string largestTimeFromDigits(vector<int>& A) {
    string maxTime = "";
    sort(A.begin(), A.end(), greater<int>());
    
    do {
        int h = A[0] * 10 + A[1];
        int m = A[2] * 10 + A[3];
        
        if (h < 24 && m < 60) {
            string time = to_string(h) + (m < 10 ? ":0" : ":") + to_string(m);
            return time;
        }
    } while (next_permutation(A.begin(), A.end()));
    
    return maxTime;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4! \cdot 1) = O(24)$, where $4!$ is the number of permutations of the input array.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the maximum time and the current permutation.
> - **Optimality proof:** This approach is optimal because we generate all permutations in descending order and return the first valid time found, which will be the maximum.

### Final Notes

**Learning Points:**
- Key algorithmic concepts: generating permutations, validating times
- Problem-solving patterns: using a brute force approach, optimizing with a more efficient algorithm
- Optimization techniques: generating permutations in descending order, stopping as soon as a valid time is found
- Similar problems to practice: generating permutations, validating inputs

**Mistakes to Avoid:**
- Not validating the input time
- Not generating all permutations
- Not stopping as soon as a valid time is found
- Not using a more efficient algorithm when possible