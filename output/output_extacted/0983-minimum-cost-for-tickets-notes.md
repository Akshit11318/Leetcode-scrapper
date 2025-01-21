## Minimum Cost for Tickets
**Problem Link:** https://leetcode.com/problems/minimum-cost-for-tickets/description

**Problem Statement:**
- Input format and constraints: You are given an array of days representing the days on which you travel and an array of costs representing the costs of different types of tickets. Each ticket has a different validity period (1 day, 7 days, or 30 days).
- Expected output format: The minimum cost to travel on all given days.
- Key requirements and edge cases to consider: Handling edge cases such as when there are no days to travel or when the days array is empty.
- Example test cases with explanations:
    - `days = [1,4,6,7,8,20], costs = [2,7,15]`: The minimum cost to travel on all these days is `11`, achieved by buying a 7-day ticket on day 1 and another 7-day ticket on day 8.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To find the minimum cost, we could try all possible combinations of buying tickets for each day.
- Step-by-step breakdown of the solution:
    1. For each day, decide whether to buy a 1-day ticket, a 7-day ticket, or a 30-day ticket.
    2. Recursively explore all possible combinations of ticket purchases for the remaining days.
    3. Keep track of the minimum total cost found so far.
- Why this approach comes to mind first: It seems like a straightforward way to explore all possibilities, but it quickly becomes inefficient due to the large number of combinations.

```cpp
int mincostTickets(vector<int>& days, vector<int>& costs) {
    int n = days.size();
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    
    for (int i = 1; i <= n; i++) {
        // Buy a 1-day ticket
        dp[i] = min(dp[i], dp[i - 1] + costs[0]);
        
        // Buy a 7-day ticket
        int j = i - 1;
        while (j >= 0 && days[j] >= days[i - 1] - 6) j--;
        dp[i] = min(dp[i], dp[j + 1] + costs[1]);
        
        // Buy a 30-day ticket
        j = i - 1;
        while (j >= 0 && days[j] >= days[i - 1] - 29) j--;
        dp[i] = min(dp[i], dp[j + 1] + costs[2]);
    }
    
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of days and $m$ is the maximum validity period of a ticket (30 days in this case). However, this brute force approach has an exponential time complexity due to the recursive exploration of all combinations.
> - **Space Complexity:** $O(n)$, as we need to store the minimum cost for each day.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the recursive exploration of all possible combinations, and the space complexity is due to the need to store the minimum cost for each day.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use dynamic programming to find the minimum cost by considering the optimal solution for the previous days.
- Detailed breakdown of the approach:
    1. Initialize a `dp` array to store the minimum cost for each day.
    2. Iterate through each day and consider buying a 1-day ticket, a 7-day ticket, or a 30-day ticket.
    3. For each type of ticket, find the previous day that is not covered by the ticket's validity period.
    4. Update the minimum cost for the current day by considering the minimum cost of the previous days and the cost of the current ticket.
- Proof of optimality: The dynamic programming approach ensures that we consider all possible combinations of ticket purchases and find the minimum cost by breaking down the problem into smaller subproblems.

```cpp
int mincostTickets(vector<int>& days, vector<int>& costs) {
    int n = days.size();
    vector<int> dp(n + 1, INT_MAX);
    dp[0] = 0;
    
    for (int i = 1; i <= n; i++) {
        // Buy a 1-day ticket
        dp[i] = min(dp[i], dp[i - 1] + costs[0]);
        
        // Buy a 7-day ticket
        int j = i - 1;
        while (j >= 0 && days[j] >= days[i - 1] - 6) j--;
        dp[i] = min(dp[i], dp[j + 1] + costs[1]);
        
        // Buy a 30-day ticket
        j = i - 1;
        while (j >= 0 && days[j] >= days[i - 1] - 29) j--;
        dp[i] = min(dp[i], dp[j + 1] + costs[2]);
    }
    
    return dp[n];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of days and $m$ is the maximum validity period of a ticket (30 days in this case).
> - **Space Complexity:** $O(n)$, as we need to store the minimum cost for each day.
> - **Optimality proof:** The dynamic programming approach ensures that we consider all possible combinations of ticket purchases and find the minimum cost by breaking down the problem into smaller subproblems.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Dynamic programming, recursive exploration of combinations, and optimization techniques.
- Problem-solving patterns identified: Breaking down the problem into smaller subproblems and considering all possible combinations.
- Optimization techniques learned: Using dynamic programming to find the minimum cost by considering the optimal solution for the previous days.
- Similar problems to practice: Other dynamic programming problems, such as the `House Robber` problem or the `Climbing Stairs` problem.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as when there are no days to travel or when the days array is empty.
- Edge cases to watch for: Handling cases where the days array is empty or when there are no days to travel.
- Performance pitfalls: Using a brute force approach that has high time complexity due to the recursive exploration of all combinations.
- Testing considerations: Testing the solution with different input cases, including edge cases and large inputs.