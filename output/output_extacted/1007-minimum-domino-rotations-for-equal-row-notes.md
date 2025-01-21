## Minimum Domino Rotations for Equal Row
**Problem Link:** [https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description)

**Problem Statement:**
- Input format: Two arrays `A` and `B`, each of length `n`, representing the two rows of dominoes.
- Constraints: `2 <= n <= 2 * 10^4`, `1 <= A[i], B[i] <= 6`, and each domino is represented by a pair of integers, with `A[i]` and `B[i]` being the numbers on the top and bottom halves of the `i`-th domino.
- Expected output format: The minimum number of rotations required to make one row equal to the other.
- Key requirements and edge cases to consider: If it's impossible to make the rows equal, return `-1`.
- Example test cases with explanations:
  - `A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]`, the output is `2`.
  - `A = [3,5,1,2,3], B = [3,6,3,3,4]`, the output is `-1`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: For each possible target number (1 to 6), calculate the minimum rotations required to make both rows equal to this number.
- Step-by-step breakdown of the solution:
  1. Initialize minimum rotations to infinity.
  2. For each possible target number (1 to 6):
    - Calculate the rotations required to make the first row equal to the target number.
    - Calculate the rotations required to make the second row equal to the target number.
    - Update the minimum rotations if the sum of rotations for both rows is less than the current minimum.
- Why this approach comes to mind first: It's a straightforward method to consider all possibilities and choose the best one.

```cpp
#include <vector>
#include <algorithm>
using namespace std;

int minDominoRotations(vector<int>& A, vector<int>& B) {
    int n = A.size();
    int minRotations = INT_MAX;
    
    // For each possible target number
    for (int target = 1; target <= 6; target++) {
        int rotationsA = 0, rotationsB = 0;
        bool possibleA = true, possibleB = true;
        
        // Calculate rotations for the first row
        for (int i = 0; i < n; i++) {
            if (A[i] != target && B[i] != target) {
                possibleA = false;
                break;
            }
            if (A[i] != target) rotationsA++;
        }
        
        // Calculate rotations for the second row
        for (int i = 0; i < n; i++) {
            if (A[i] != target && B[i] != target) {
                possibleB = false;
                break;
            }
            if (B[i] != target) rotationsB++;
        }
        
        // Update minimum rotations if possible
        if (possibleA) minRotations = min(minRotations, rotationsA);
        if (possibleB) minRotations = min(minRotations, rotationsB);
    }
    
    return minRotations == INT_MAX ? -1 : minRotations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the number of dominoes and $k$ is the number of possible target numbers (6 in this case). The reason for this complexity is that we are iterating over the dominoes for each target number.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum rotations and other variables.
> - **Why these complexities occur:** The time complexity occurs because we are considering all possible target numbers and calculating the rotations for each one. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of considering all possible target numbers, we can only consider the numbers on the first domino. This is because if the first domino does not match the target number, we would need to rotate both dominoes, which is not optimal.
- Detailed breakdown of the approach:
  1. Check if the first domino can match the target number.
  2. If it can, calculate the rotations required to make the rest of the dominoes match the target number.
- Proof of optimality: This approach is optimal because we are considering the minimum number of rotations required to make the dominoes match the target number. We are not considering any unnecessary rotations.
- Why further optimization is impossible: We are already considering the minimum number of rotations required, so further optimization is not possible.

```cpp
int minDominoRotations(vector<int>& A, vector<int>& B) {
    int n = A.size();
    int minRotations = INT_MAX;
    
    // Check for both possible target numbers
    for (int target : {A[0], B[0]}) {
        int rotationsA = 0, rotationsB = 0;
        bool possibleA = true, possibleB = true;
        
        // Calculate rotations for the first row
        for (int i = 0; i < n; i++) {
            if (A[i] != target && B[i] != target) {
                possibleA = false;
                break;
            }
            if (A[i] != target) rotationsA++;
        }
        
        // Calculate rotations for the second row
        for (int i = 0; i < n; i++) {
            if (A[i] != target && B[i] != target) {
                possibleB = false;
                break;
            }
            if (B[i] != target) rotationsB++;
        }
        
        // Update minimum rotations if possible
        if (possibleA) minRotations = min(minRotations, rotationsA);
        if (possibleB) minRotations = min(minRotations, rotationsB);
    }
    
    return minRotations == INT_MAX ? -1 : minRotations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of dominoes. The reason for this complexity is that we are iterating over the dominoes twice, once for each possible target number.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum rotations and other variables.
> - **Optimality proof:** This approach is optimal because we are considering the minimum number of rotations required to make the dominoes match the target number. We are not considering any unnecessary rotations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of considering all possible target numbers and calculating the minimum rotations required.
- Problem-solving patterns identified: The use of iteration to calculate the rotations required for each target number.
- Optimization techniques learned: The use of a constant amount of space to store the minimum rotations and other variables.
- Similar problems to practice: Other problems that involve calculating the minimum number of operations required to achieve a certain goal.

**Mistakes to Avoid:**
- Common implementation errors: Not considering all possible target numbers, not calculating the rotations required for each target number.
- Edge cases to watch for: The case where the first domino does not match the target number.
- Performance pitfalls: Using too much space to store the minimum rotations and other variables.
- Testing considerations: Testing the function with different inputs to ensure it is working correctly.