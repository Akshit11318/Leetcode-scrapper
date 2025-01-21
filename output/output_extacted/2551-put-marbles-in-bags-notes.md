## Put Marbles in Bags
**Problem Link:** https://leetcode.com/problems/put-marbles-in-bags/description

**Problem Statement:**
- Input format: `int n, int k, vector<int>& marbles, vector<int>& bags`
- Constraints: `1 <= n <= 10^5`, `1 <= k <= n`, `1 <= marbles[i] <= 10^6`, `1 <= bags[i] <= 10^6`
- Expected output format: The maximum number of marbles that can be put into the bags.
- Key requirements and edge cases to consider: The marbles and bags are 1-indexed, and each bag can hold a different number of marbles.
- Example test cases with explanations: 
    - `n = 3, k = 3, marbles = [1, 2, 3], bags = [1, 2, 3]` should return `6` because we can put `1` marble into the first bag, `2` marbles into the second bag, and `3` marbles into the third bag.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of marbles and bags to find the maximum number of marbles that can be put into the bags.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of marbles and bags.
    2. For each combination, calculate the total number of marbles that can be put into the bags.
    3. Keep track of the maximum number of marbles that can be put into the bags.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it's not efficient for large inputs.

```cpp
int putMarblesInBags(int n, int k, vector<int>& marbles, vector<int>& bags) {
    int maxMarbles = 0;
    for (int mask = 0; mask < (1 << n); mask++) {
        int totalMarbles = 0;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                totalMarbles += marbles[i];
            }
        }
        int totalBags = 0;
        for (int i = 0; i < k; i++) {
            if ((mask & (1 << i)) != 0) {
                totalBags += bags[i];
            }
        }
        if (totalBags >= totalMarbles) {
            maxMarbles = max(maxMarbles, totalMarbles);
        }
    }
    return maxMarbles;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ because we generate all possible combinations of marbles and bags, and for each combination, we calculate the total number of marbles that can be put into the bags.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the maximum number of marbles that can be put into the bags.
> - **Why these complexities occur:** The time complexity occurs because we use a brute force approach to generate all possible combinations of marbles and bags, and the space complexity occurs because we only use a constant amount of space to store the maximum number of marbles that can be put into the bags.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve the problem. We sort the marbles and bags in descending order, and then we try to put the largest marbles into the largest bags.
- Detailed breakdown of the approach:
    1. Sort the marbles and bags in descending order.
    2. Initialize two pointers, one for the marbles and one for the bags.
    3. While there are still marbles and bags, try to put the largest marble into the largest bag.
    4. If the bag can hold the marble, increment the pointer for the marbles and decrement the pointer for the bags.
    5. If the bag cannot hold the marble, increment the pointer for the bags.
- Proof of optimality: This approach is optimal because we always try to put the largest marbles into the largest bags, which maximizes the number of marbles that can be put into the bags.

```cpp
int putMarblesInBags(int n, int k, vector<int>& marbles, vector<int>& bags) {
    sort(marbles.begin(), marbles.end(), greater<int>());
    sort(bags.begin(), bags.end(), greater<int>());
    int maxMarbles = 0;
    int i = 0, j = 0;
    while (i < n && j < k) {
        if (bags[j] >= marbles[i]) {
            maxMarbles += marbles[i];
            i++;
        }
        j++;
    }
    return maxMarbles;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + k \log k)$ because we sort the marbles and bags in descending order.
> - **Space Complexity:** $O(1)$ because we only use a constant amount of space to store the maximum number of marbles that can be put into the bags.
> - **Optimality proof:** This approach is optimal because we always try to put the largest marbles into the largest bags, which maximizes the number of marbles that can be put into the bags.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, sorting.
- Problem-solving patterns identified: Trying to maximize the number of marbles that can be put into the bags by using a greedy approach.
- Optimization techniques learned: Using a greedy approach to solve the problem.
- Similar problems to practice: Other problems that involve maximizing or minimizing a quantity using a greedy approach.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the marbles and bags in descending order.
- Edge cases to watch for: When the number of marbles is greater than the number of bags, or when the number of bags is greater than the number of marbles.
- Performance pitfalls: Using a brute force approach to solve the problem, which can lead to a time complexity of $O(2^n \cdot n)$.
- Testing considerations: Testing the solution with different inputs, such as when the number of marbles is equal to the number of bags, or when the number of marbles is greater than the number of bags.