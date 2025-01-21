## Lemonade Change
**Problem Link:** https://leetcode.com/problems/lemonade-change/description

**Problem Statement:**
- Input format and constraints: The problem provides a list of transactions where each transaction is the amount of money a customer pays for a lemonade.
- Expected output format: The function should return `true` if it is possible to make change for every customer, and `false` otherwise.
- Key requirements and edge cases to consider: The initial stock of lemonades is 0, and each lemonade costs 5 dollars.
- Example test cases with explanations:
  - For the transactions `[5,5,5,10,20]`, the function should return `true` because we can give 5 dollars in change for the 10 dollar bill and 15 dollars in change for the 20 dollar bill.
  - For the transactions `[5,5,10]`, the function should return `true` because we can give 5 dollars in change for the 10 dollar bill.
  - For the transactions `[10,10]`, the function should return `false` because we cannot give change for the first 10 dollar bill.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first idea is to simulate each transaction and try to make change for each customer.
- Step-by-step breakdown of the solution:
  1. Initialize variables to keep track of the number of 5 dollar and 10 dollar bills we have.
  2. For each transaction, check if we can make change.
  3. If the transaction is a 5 dollar bill, increment the count of 5 dollar bills.
  4. If the transaction is a 10 dollar bill, try to make change by using a 5 dollar bill.
  5. If the transaction is a 20 dollar bill, try to make change by using two 5 dollar bills or one 10 dollar bill and one 5 dollar bill.
- Why this approach comes to mind first: This approach is straightforward and directly simulates the process of making change for each customer.

```cpp
bool lemonadeChange(vector<int>& transactions) {
    int five = 0, ten = 0;
    for (int transaction : transactions) {
        if (transaction == 5) {
            five++;
        } else if (transaction == 10) {
            if (five == 0) return false;
            five--;
            ten++;
        } else {
            if (five >= 3) {
                five -= 3;
            } else if (five >= 1 && ten >= 1) {
                five--;
                ten--;
            } else {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions, because we process each transaction once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the counts of 5 dollar and 10 dollar bills.
> - **Why these complexities occur:** The time complexity is linear because we make a single pass through the transactions, and the space complexity is constant because we only use a fixed amount of space to store the counts of bills.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The same insight as the brute force approach, but we can implement it more efficiently by directly using the counts of bills to make change.
- Detailed breakdown of the approach: The approach is the same as the brute force approach, but we can simplify the code by directly using the counts of bills.
- Proof of optimality: This approach is optimal because we must process each transaction at least once to determine if we can make change, and we use a constant amount of space to store the counts of bills.
- Why further optimization is impossible: We cannot further optimize the time complexity because we must process each transaction, and we cannot further optimize the space complexity because we only use a constant amount of space.

```cpp
bool lemonadeChange(vector<int>& transactions) {
    int five = 0, ten = 0;
    for (int transaction : transactions) {
        if (transaction == 5) {
            five++;
        } else if (transaction == 10) {
            if (five == 0) return false;
            five--;
            ten++;
        } else {
            if (five >= 3) {
                five -= 3;
            } else if (five >= 1 && ten >= 1) {
                five--;
                ten--;
            } else {
                return false;
            }
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of transactions, because we process each transaction once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the counts of bills.
> - **Optimality proof:** This approach is optimal because we must process each transaction at least once to determine if we can make change, and we use a constant amount of space to store the counts of bills.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Simulation, counting, and making change.
- Problem-solving patterns identified: Using counts of bills to make change, and checking for sufficient bills to make change.
- Optimization techniques learned: Using a constant amount of space to store counts of bills.
- Similar problems to practice: Other problems involving simulation, counting, and making change.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for sufficient bills to make change, and not updating the counts of bills correctly.
- Edge cases to watch for: Transactions that are not 5 dollar or 10 dollar bills, and not having sufficient bills to make change.
- Performance pitfalls: Using too much space to store counts of bills, and not processing each transaction efficiently.
- Testing considerations: Testing with different transactions, and checking for correct output for each test case.