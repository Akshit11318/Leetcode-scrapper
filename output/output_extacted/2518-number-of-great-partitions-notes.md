## Number of Great Partitions
**Problem Link:** https://leetcode.com/problems/number-of-great-partitions/description

**Problem Statement:**
- Input: A string `num` consisting of digits, representing a number, and an integer `k`.
- Constraints: `1 <= num.length <= 1000`, `1 <= k <= 1000`, `num` consists only of digits.
- Expected Output: The number of great partitions of the number represented by `num` where each partition is less than or equal to `k`.
- Key Requirements: A great partition is one where the sum of the parts is equal to the original number and each part is less than or equal to `k`.
- Edge Cases: When `num` is a single digit, when `k` is greater than the maximum possible sum of `num`, when `num` starts with '0'.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all possible partitions of the number represented by `num`.
- Then, for each partition, check if the sum of the parts is equal to the original number and if each part is less than or equal to `k`.
- This approach comes to mind first because it is straightforward and does not require any complex algorithmic techniques.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int greatPartitions(string num, int k) {
    int n = num.length();
    int number = stoi(num);
    int count = 0;

    // Generate all possible partitions
    for (int mask = 0; mask < (1 << (n - 1)); mask++) {
        vector<int> parts;
        int start = 0;
        for (int i = 0; i < n - 1; i++) {
            if ((mask & (1 << i)) != 0) {
                int part = stoi(num.substr(start, i - start + 1));
                parts.push_back(part);
                start = i + 1;
            }
        }
        int lastPart = stoi(num.substr(start));
        parts.push_back(lastPart);

        // Check if the partition is great
        bool isGreat = true;
        int sum = 0;
        for (int part : parts) {
            if (part > k) {
                isGreat = false;
                break;
            }
            sum += part;
        }
        if (isGreat && sum == number) {
            count++;
        }
    }

    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n-1} \cdot n \cdot \log(n))$ where $n$ is the length of `num`. The reason for this complexity is the generation of all possible partitions and the conversion of substrings to integers.
> - **Space Complexity:** $O(n)$ for storing the parts of the partition.
> - **Why these complexities occur:** The brute force approach involves generating all possible partitions of `num`, which results in an exponential time complexity. The conversion of substrings to integers also contributes to the overall time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use dynamic programming to store the intermediate results of subproblems.
- The dynamic programming approach involves building a table where each cell represents the number of great partitions for a given prefix of `num` and a given maximum part size.
- The optimal solution is based on the principle of inclusion-exclusion, where we count the number of partitions that include each possible part size.

```cpp
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int greatPartitions(string num, int k) {
    int n = num.length();
    int number = stoi(num);
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 0));

    dp[0][0] = 1;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= k; j++) {
            int sum = 0;
            for (int l = i; l >= 1; l--) {
                sum = sum * 10 + (num[l - 1] - '0');
                if (sum > j) break;
                dp[i][j] += dp[l - 1][j];
            }
        }
    }

    return dp[n][k];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot k)$ where $n$ is the length of `num`.
> - **Space Complexity:** $O(n \cdot k)$ for storing the dynamic programming table.
> - **Optimality proof:** The dynamic programming approach ensures that we do not recalculate the same subproblems multiple times, resulting in a significant reduction in time complexity. The principle of inclusion-exclusion allows us to accurately count the number of great partitions.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: dynamic programming, principle of inclusion-exclusion.
- Problem-solving patterns identified: breaking down a problem into smaller subproblems, using a table to store intermediate results.
- Optimization techniques learned: using dynamic programming to avoid recalculating the same subproblems.
- Similar problems to practice: problems involving partitions, dynamic programming, and principle of inclusion-exclusion.

**Mistakes to Avoid:**
- Common implementation errors: incorrect initialization of the dynamic programming table, incorrect calculation of the sum of parts.
- Edge cases to watch for: when `num` is a single digit, when `k` is greater than the maximum possible sum of `num`, when `num` starts with '0'.
- Performance pitfalls: using a brute force approach instead of dynamic programming, not using a table to store intermediate results.
- Testing considerations: testing the function with different inputs, including edge cases, to ensure correctness.