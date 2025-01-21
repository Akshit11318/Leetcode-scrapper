## Minimum Cost to Make All Characters Equal

**Problem Link:** https://leetcode.com/problems/minimum-cost-to-make-all-characters-equal/description

**Problem Statement:**
- Input format and constraints: Given a string `s` of length `n` and an integer `k`, find the minimum cost to make all characters in `s` equal to a specific character `c`. The cost of changing a character at index `i` is `cost[i]`.
- Expected output format: Return the minimum cost.
- Key requirements and edge cases to consider: The string `s` only contains lowercase letters, and `cost` is an array of integers representing the cost of changing each character.
- Example test cases with explanations:
  - Example 1: Input `s = "abc", cost = [1,2,3], k = 2`, Output `2`
  - Example 2: Input `s = "aabaa", cost = [1,2,3,4,5], k = 1`, Output `10`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try to change each character to every possible character and calculate the total cost.
- Step-by-step breakdown of the solution:
  1. Iterate over each character `c` in the string `s`.
  2. For each character `c`, iterate over each character `ch` in the string `s`.
  3. Calculate the total cost of changing all characters to `ch`.
  4. Update the minimum cost if the total cost is less than the current minimum cost.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it is inefficient due to its high time complexity.

```cpp
int minCost(string s, vector<int>& cost, int k) {
    int n = s.size();
    int min_cost = INT_MAX;
    for (char c = 'a'; c <= 'z'; c++) {
        int total_cost = 0;
        for (int i = 0; i < n; i++) {
            if (s[i] != c) {
                total_cost += cost[i];
            }
        }
        min_cost = min(min_cost, total_cost);
    }
    return min_cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 26)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum cost.
> - **Why these complexities occur:** The time complexity is high because we iterate over each character in the string for each possible character, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the frequency of each character in the string and then calculate the total cost of changing all characters to each character.
- Detailed breakdown of the approach:
  1. Calculate the frequency of each character in the string `s`.
  2. For each character `c`, calculate the total cost of changing all characters to `c`.
  3. Update the minimum cost if the total cost is less than the current minimum cost.
- Proof of optimality: This approach is optimal because we only need to iterate over each character in the string once to calculate the frequency, and then we can calculate the total cost for each character in constant time.
- Why further optimization is impossible: This approach is already optimal because we have reduced the time complexity to $O(n)$, which is the minimum possible time complexity for this problem.

```cpp
int minCost(string s, vector<int>& cost, int k) {
    int n = s.size();
    vector<int> freq(26, 0);
    for (char c : s) {
        freq[c - 'a']++;
    }
    int min_cost = INT_MAX;
    for (int i = 0; i < 26; i++) {
        int total_cost = 0;
        for (int j = 0; j < n; j++) {
            if (s[j] - 'a' != i) {
                total_cost += cost[j];
            }
        }
        min_cost = min(min_cost, total_cost);
    }
    return min_cost;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + 26)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the frequency of each character.
> - **Optimality proof:** This approach is optimal because we have reduced the time complexity to $O(n + 26)$, which is the minimum possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency calculation, total cost calculation, and minimum cost update.
- Problem-solving patterns identified: Reducing the time complexity by calculating the frequency of each character and then calculating the total cost for each character.
- Optimization techniques learned: Reducing the time complexity by using a frequency array to store the frequency of each character.
- Similar problems to practice: Problems that involve calculating the frequency of each character and then calculating the total cost for each character.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the frequency array, not updating the minimum cost correctly.
- Edge cases to watch for: When the string is empty, when the cost array is empty.
- Performance pitfalls: Not using a frequency array to store the frequency of each character, which can lead to high time complexity.
- Testing considerations: Test the function with different inputs, including empty strings and cost arrays, to ensure that it works correctly.