## Find the Maximum Factor Score of Array

**Problem Link:** https://leetcode.com/problems/find-the-maximum-factor-score-of-array/description

**Problem Statement:**
- Input: An array of integers `nums` and an integer `k`.
- Output: The maximum factor score of the array.
- Key requirements: Calculate the score for each factor of `k` and return the maximum score.
- Edge cases: Handle cases where `k` is not a factor of any number in `nums`, and where `nums` is empty.

**Example Test Cases:**
- Input: `nums = [4,8,6,3], k = 5`
  - Output: `0` (Since none of the numbers in `nums` are divisible by `5`)
- Input: `nums = [12,18,21,10], k = 7`
  - Output: `2` (Since `21` and `7` are factors of `k` and the maximum score is `2`)

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every number in `nums` to see if it is divisible by each factor of `k`.
- For each factor, count how many numbers in `nums` are divisible by it.
- Keep track of the maximum count found.

```cpp
#include <vector>
using namespace std;

int maxScore(vector<int>& nums, int k) {
    int maxScore = 0;
    for (int i = 1; i <= k; i++) {
        if (k % i == 0) {  // Check if i is a factor of k
            int score = 0;
            for (int num : nums) {
                if (num % i == 0) {  // Check if num is divisible by i
                    score++;
                }
            }
            maxScore = max(maxScore, score);
        }
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{k})$ where $n$ is the size of `nums` and $\sqrt{k}$ represents the number of factors of $k$. This is because for each number in `nums`, we potentially check divisibility by each factor of `k`.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the maximum score and temporary variables.
> - **Why these complexities occur:** The time complexity is dominated by the nested loop structure, where for each factor of `k`, we iterate through all numbers in `nums`. The space complexity is minimal because we only need to keep track of the current and maximum scores.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach still involves checking each number in `nums` for divisibility by each factor of `k`.
- However, we can slightly optimize the factor checking by only iterating up to the square root of `k`, as any factor larger than that would have a corresponding factor smaller than the square root.
- We also keep track of the maximum score seen so far.

```cpp
#include <vector>
#include <cmath>
using namespace std;

int maxScore(vector<int>& nums, int k) {
    int maxScore = 0;
    for (int i = 1; i <= sqrt(k); i++) {
        if (k % i == 0) {  // Check if i is a factor of k
            int score = 0;
            for (int num : nums) {
                if (num % i == 0) {  // Check if num is divisible by i
                    score++;
                }
            }
            maxScore = max(maxScore, score);
            // Check the corresponding factor larger than sqrt(k)
            if (i != k / i) {
                score = 0;
                for (int num : nums) {
                    if (num % (k / i) == 0) {
                        score++;
                    }
                }
                maxScore = max(maxScore, score);
            }
        }
    }
    return maxScore;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{k})$, similar to the brute force approach, because we still potentially check each number in `nums` against each factor of `k`.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it must check each number in `nums` against each factor of `k` to ensure it finds the maximum score. Any approach that does not do this could potentially miss the maximum score.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include iterating through factors of a number and checking divisibility.
- Problem-solving patterns identified include the need to keep track of the maximum score seen so far.
- Optimization techniques learned include only iterating up to the square root of a number to find its factors.

**Mistakes to Avoid:**
- Common implementation errors include forgetting to check for the corresponding factor larger than the square root of `k`.
- Edge cases to watch for include when `k` is not a factor of any number in `nums`, and when `nums` is empty.
- Performance pitfalls include not optimizing the factor checking loop, leading to unnecessary iterations.