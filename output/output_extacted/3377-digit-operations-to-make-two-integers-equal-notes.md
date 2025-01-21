## Digit Operations to Make Two Integers Equal
**Problem Link:** https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/description

**Problem Statement:**
- Input format and constraints: The problem takes two integers `num1` and `num2` as input, where $1 \leq num1, num2 \leq 10^9$. The goal is to find the minimum number of operations required to make `num1` and `num2` equal. 
- Expected output format: The minimum number of operations required.
- Key requirements and edge cases to consider: Operations allowed are adding 1 to a digit, subtracting 1 from a digit, or multiplying a digit by 2.
- Example test cases with explanations: For example, if `num1 = 601` and `num2 = 664`, the minimum number of operations would be 3, as we can change `num1` to `num2` by applying the operations to the digits.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can start by considering all possible operations on each digit of `num1` and then check if we can reach `num2` after applying these operations.
- Step-by-step breakdown of the solution:
  1. Convert both numbers to strings to easily access each digit.
  2. For each digit in `num1`, try all possible operations (add 1, subtract 1, multiply by 2).
  3. Check if the resulting number is equal to `num2`.
  4. If yes, count the number of operations applied and update the minimum count if necessary.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, but it is not efficient due to the large number of possible operations.

```cpp
#include <iostream>
#include <string>
#include <climits>

using namespace std;

int minOperations(string num1, string num2) {
    int minCount = INT_MAX;
    // Try all possible operations
    for (int i = 0; i < num1.size(); i++) {
        for (int j = -1; j <= 1; j += 2) { // -1 for subtract, 1 for add
            for (int k = 0; k < 2; k++) { // 0 for no multiply, 1 for multiply by 2
                string temp = num1;
                int count = 0;
                temp[i] = (temp[i] - '0' + j) + '0';
                if (k == 1) {
                    temp[i] = (temp[i] - '0') * 2 + '0';
                    count++;
                }
                count++;
                if (temp == num2) {
                    minCount = min(minCount, count);
                }
            }
        }
    }
    return minCount == INT_MAX ? -1 : minCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the number of digits in `num1`, because we try all possible operations for each digit.
> - **Space Complexity:** $O(n)$, as we need to store the temporary string.
> - **Why these complexities occur:** The brute force approach tries all possible operations, resulting in exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a breadth-first search (BFS) to find the minimum number of operations.
- Detailed breakdown of the approach:
  1. Convert both numbers to strings and calculate the difference in digits.
  2. Create a queue for BFS, where each element is a pair of the current number and the number of operations.
  3. For each number in the queue, try all possible operations (add 1, subtract 1, multiply by 2) and add the resulting numbers to the queue if they are not visited before.
  4. Continue the BFS until we find `num2` or the queue is empty.
- Proof of optimality: BFS guarantees that we find the minimum number of operations because it explores all possible numbers in the order of their distance from the starting number.

```cpp
#include <iostream>
#include <string>
#include <queue>
#include <unordered_set>

using namespace std;

int minOperations(string num1, string num2) {
    int minCount = INT_MAX;
    queue<pair<string, int>> q;
    unordered_set<string> visited;
    q.push({num1, 0});
    visited.insert(num1);
    while (!q.empty()) {
        string curr = q.front().first;
        int count = q.front().second;
        q.pop();
        if (curr == num2) {
            return count;
        }
        for (int i = 0; i < curr.size(); i++) {
            string temp = curr;
            // Try add 1
            temp[i] = (temp[i] - '0' + 1) + '0';
            if (temp != num2 && visited.find(temp) == visited.end()) {
                q.push({temp, count + 1});
                visited.insert(temp);
            }
            // Try subtract 1
            temp = curr;
            temp[i] = (temp[i] - '0' - 1) + '0';
            if (temp != num2 && visited.find(temp) == visited.end()) {
                q.push({temp, count + 1});
                visited.insert(temp);
            }
            // Try multiply by 2
            temp = curr;
            temp[i] = ((temp[i] - '0') * 2) + '0';
            if (temp != num2 && visited.find(temp) == visited.end()) {
                q.push({temp, count + 1});
                visited.insert(temp);
            }
        }
    }
    return -1;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10^n)$, where $n$ is the number of digits in `num1`, because in the worst case, we need to explore all possible numbers.
> - **Space Complexity:** $O(10^n)$, as we need to store all visited numbers.
> - **Optimality proof:** BFS guarantees that we find the minimum number of operations because it explores all possible numbers in the order of their distance from the starting number.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: BFS, queue data structure.
- Problem-solving patterns identified: Using BFS to find the minimum number of operations.
- Optimization techniques learned: Using a visited set to avoid exploring the same number multiple times.
- Similar problems to practice: Other problems that involve finding the minimum number of operations to reach a target state.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for visited numbers, not handling edge cases correctly.
- Edge cases to watch for: Handling cases where `num1` is equal to `num2`, or where `num2` is not reachable from `num1`.
- Performance pitfalls: Not using a visited set, resulting in exponential time complexity.
- Testing considerations: Testing the function with different inputs, including edge cases.