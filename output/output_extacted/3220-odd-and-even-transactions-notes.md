## Odd and Even Transactions
**Problem Link:** https://leetcode.com/problems/odd-and-even-transactions/description

**Problem Statement:**
- Input: An array of integers `transactions` representing transaction amounts.
- Constraints: `1 <= transactions.length <= 10^5`, `1 <= transactions[i] <= 10^9`.
- Expected Output: The minimum number of transactions required to make all transactions even.
- Key Requirements and Edge Cases: All transactions must be even at the end, and the minimum number of transactions should be achieved.

**Example Test Cases:**
- `transactions = [1, 2, 3, 4]`, output: `2`.
- `transactions = [1, 2, 3, 4, 5]`, output: `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of adding or subtracting `1` from each transaction until all transactions are even.
- Step-by-step breakdown:
  1. Initialize a counter for the number of transactions.
  2. Loop through each transaction.
  3. If the transaction is odd, add or subtract `1` to make it even and increment the counter.
  4. Repeat until all transactions are even.

```cpp
#include <vector>
using namespace std;

int minTransactions(vector<int>& transactions) {
    int count = 0;
    for (int i = 0; i < transactions.size(); i++) {
        if (transactions[i] % 2 != 0) {
            transactions[i] += 1;
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions. This is because we only need to loop through each transaction once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counter.
> - **Why these complexities occur:** The brute force approach is straightforward but not optimal because it doesn't consider the possibility of combining transactions to reduce the total count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Count the number of odd transactions, as each odd transaction requires one operation to become even.
- Detailed breakdown:
  1. Initialize a counter for the number of odd transactions.
  2. Loop through each transaction and increment the counter if the transaction is odd.
  3. The minimum number of transactions is equal to the number of odd transactions.

```cpp
#include <vector>
using namespace std;

int minTransactions(vector<int>& transactions) {
    int oddCount = 0;
    for (int transaction : transactions) {
        if (transaction % 2 != 0) {
            oddCount++;
        }
    }
    return oddCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the counter.
> - **Optimality proof:** This approach is optimal because it directly counts the minimum number of operations required to make all transactions even, without considering unnecessary combinations or permutations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Counting, basic arithmetic operations.
- Problem-solving patterns: Identifying the minimum number of operations required to achieve a certain state.
- Optimization techniques: Direct counting, avoiding unnecessary iterations.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as an empty input array.
- Performance pitfalls: Using inefficient data structures or algorithms.
- Testing considerations: Verifying the correctness of the solution with various input scenarios.