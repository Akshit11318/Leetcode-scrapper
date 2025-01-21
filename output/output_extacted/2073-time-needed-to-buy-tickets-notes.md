## Time Needed to Buy Tickets
**Problem Link:** https://leetcode.com/problems/time-needed-to-buy-tickets/description

**Problem Statement:**
- Input: An array of integers `tickets` representing the number of tickets each person wants to buy and an integer `k` representing the index of the person in the queue.
- Constraints: The length of `tickets` is in the range `[1, 100]`, and `k` is in the range `[0, tickets.length - 1]`.
- Expected Output: The time needed for the person at index `k` to buy all their tickets.
- Key Requirements: Calculate the total time it takes for the person at index `k` to buy all their tickets.
- Example Test Cases:
  - Input: `tickets = [2,3,2]`, `k = 2`
    - Output: `6`
    - Explanation: Person 0 buys 2 tickets, then person 1 buys 3 tickets, then person 2 buys 2 tickets. The total time is 2 + 3 + 2 = 7. However, person 2 only needs to buy their tickets once, so the time needed for person 2 is 6.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Simulate the process of buying tickets one by one.
- Step-by-step breakdown: Iterate through the `tickets` array, decrementing the ticket count for each person until the person at index `k` has bought all their tickets.
- Why this approach comes to mind first: It directly simulates the process described in the problem.

```cpp
int timeRequiredToBuy(vector<int>& tickets, int k) {
    int time = 0;
    while (tickets[k] > 0) {
        for (int i = 0; i < tickets.size(); i++) {
            if (tickets[i] > 0) {
                tickets[i]--;
                time++;
                if (i == k && tickets[i] == 0) {
                    break;
                }
            }
        }
    }
    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of people and $m$ is the maximum number of tickets a person wants to buy.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the time.
> - **Why these complexities occur:** The brute force approach iterates through the `tickets` array for each ticket bought, resulting in a time complexity that is proportional to the number of people and the maximum number of tickets.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The person at index `k` only needs to buy their tickets once, so we can calculate the time needed by summing up the minimum between the number of tickets each person wants to buy and the number of tickets the person at index `k` wants to buy.
- Detailed breakdown: Iterate through the `tickets` array, adding the minimum between the number of tickets each person wants to buy and the number of tickets the person at index `k` wants to buy to the total time.
- Proof of optimality: This approach directly calculates the time needed for the person at index `k` to buy all their tickets, without simulating the process.

```cpp
int timeRequiredToBuy(vector<int>& tickets, int k) {
    int time = 0;
    for (int i = 0; i < tickets.size(); i++) {
        time += min(tickets[i], tickets[k] - (i > k));
    }
    return time;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of people.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the time.
> - **Optimality proof:** This approach directly calculates the time needed for the person at index `k` to buy all their tickets, without simulating the process, resulting in a time complexity that is proportional to the number of people.

---

### Final Notes
**Learning Points:**
- Key algorithmic concept: Direct calculation of the time needed for the person at index `k` to buy all their tickets.
- Problem-solving pattern: Using the minimum between the number of tickets each person wants to buy and the number of tickets the person at index `k` wants to buy to calculate the time needed.
- Optimization technique: Avoiding simulation of the process and directly calculating the time needed.

**Mistakes to Avoid:**
- Common implementation error: Simulating the process instead of directly calculating the time needed.
- Edge case to watch for: When the person at index `k` wants to buy more tickets than another person.
- Performance pitfall: Using a brute force approach that simulates the process.
- Testing consideration: Test the function with different inputs to ensure it works correctly.