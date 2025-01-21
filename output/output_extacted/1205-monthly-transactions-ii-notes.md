## Monthly Transactions II

**Problem Link:** https://leetcode.com/problems/monthly-transactions-ii/description

**Problem Statement:**
- Input: An array of transactions where each transaction is an array of two integers, `day` and `amount`.
- Constraints: 
  - The number of transactions is between 1 and 10^5.
  - Each transaction is an array of two integers, `day` and `amount`.
  - The day of each transaction is between 1 and 30.
- Expected Output: The number of days on which the total expenditure exceeds the threshold.
- Key Requirements:
  - For each day from the 1st to the 30th, calculate the total expenditure in the last 7 days.
  - Count the days on which the total expenditure exceeds the threshold.
- Example Test Cases:
  - transactions = [[0,0],[7,1],[2,0]], threshold = 1, Output: 2

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves calculating the total expenditure for each day by summing up the amounts of all transactions that occurred in the last 7 days.
- This approach comes to mind first because it directly addresses the requirement of calculating the total expenditure for each day.
- However, this approach is inefficient because it involves redundant calculations.

```cpp
int countDays(vector<vector<int>>& transactions, int threshold) {
    int count = 0;
    for (int day = 1; day <= 30; day++) {
        int total = 0;
        for (auto& transaction : transactions) {
            if (day - transaction[0] <= 7 && day - transaction[0] >= 0) {
                total += transaction[1];
            }
        }
        if (total > threshold) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where n is the number of days (30) and m is the number of transactions.
> - **Space Complexity:** $O(1)$, as no additional space is used that scales with input size.
> - **Why these complexities occur:** The brute force approach involves nested loops, resulting in a time complexity of $O(n \times m)$. The space complexity is $O(1)$ because no additional data structures are used.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a sliding window approach to calculate the total expenditure for each day.
- This approach involves maintaining a window of the last 7 days and updating the total expenditure as the window moves.
- This is the optimal solution because it minimizes the number of calculations required to determine the total expenditure for each day.

```cpp
int countDays(vector<vector<int>>& transactions, int threshold) {
    map<int, int> dayAmounts;
    for (auto& transaction : transactions) {
        dayAmounts[transaction[0]] += transaction[1];
    }
    
    int count = 0;
    for (int day = 1; day <= 30; day++) {
        int total = 0;
        for (int i = day; i > day - 7; i--) {
            if (dayAmounts.find(i) != dayAmounts.end()) {
                total += dayAmounts[i];
            }
        }
        if (total > threshold) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where n is the number of days (30) and m is the maximum number of days in the window (7).
> - **Space Complexity:** $O(m)$, where m is the number of transactions.
> - **Optimality proof:** The optimal approach minimizes the number of calculations required to determine the total expenditure for each day, resulting in a time complexity of $O(n \times m)$.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated in this problem is the use of a sliding window approach to minimize calculations.
- The problem-solving pattern identified is the use of a map to store day-amount pairs for efficient lookup.
- The optimization technique learned is to avoid redundant calculations by maintaining a window of relevant data.

**Mistakes to Avoid:**
- A common implementation error is to use a brute force approach that results in redundant calculations.
- An edge case to watch for is when the number of transactions is large, and the brute force approach becomes inefficient.
- A performance pitfall is to use a data structure that does not support efficient lookup, such as a vector instead of a map.