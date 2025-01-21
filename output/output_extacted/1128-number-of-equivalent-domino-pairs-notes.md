## Number of Equivalent Domino Pairs

**Problem Link:** https://leetcode.com/problems/number-of-equivalent-domino-pairs/description

**Problem Statement:**
- Input: An array of pairs `dominoes` where each pair is represented as `[a, b]`.
- Constraints: Each domino is represented as a pair of integers, `1 <= a, b <= 6`.
- Expected output: The number of pairs that are equivalent.
- Key requirements: Two dominoes are equivalent if they have the same numbers, regardless of order.
- Example test cases:
  - Input: `[[1,2],[2,1],[3,4],[5,6]]`, Output: `1`
  - Input: `[[1,2],[1,2],[1,1],[1,2],[3,4]]`, Output: `3`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each pair with every other pair to check for equivalence.
- Step-by-step breakdown:
  1. Initialize a counter for equivalent pairs.
  2. Iterate through each pair in the array.
  3. For each pair, iterate through the remaining pairs.
  4. Check if the current pair is equivalent to the compared pair (i.e., `a == b' && b == a'` or `a == a' && b == b'`).
  5. If equivalent, increment the counter.
- Why this approach comes to mind first: It's a straightforward, intuitive approach to solving the problem by comparing each pair with every other pair.

```cpp
int numEquivDominoPairs(vector<vector<int>>& dominoes) {
    int count = 0;
    for (int i = 0; i < dominoes.size(); i++) {
        for (int j = i + 1; j < dominoes.size(); j++) {
            if ((dominoes[i][0] == dominoes[j][0] && dominoes[i][1] == dominoes[j][1]) ||
                (dominoes[i][0] == dominoes[j][1] && dominoes[i][1] == dominoes[j][0])) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of pairs. This is because we're using nested loops to compare each pair with every other pair.
> - **Space Complexity:** $O(1)$, as we're only using a constant amount of space to store the count of equivalent pairs.
> - **Why these complexities occur:** The time complexity is quadratic due to the nested loops, and the space complexity is constant because we're not using any data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of comparing each pair with every other pair, we can use a hashmap to store the frequency of each unique pair (where `a <= b` to ensure consistency).
- Detailed breakdown:
  1. Initialize a hashmap to store the frequency of each unique pair.
  2. Iterate through each pair in the array.
  3. For each pair, sort the numbers in ascending order (to ensure `a <= b`).
  4. Increment the frequency of the sorted pair in the hashmap.
  5. Calculate the number of equivalent pairs by summing the combinations of each frequency `n` choose 2, where `n` is the frequency of a pair.
- Proof of optimality: This approach reduces the time complexity to linear because we're only iterating through the pairs once and using a hashmap for constant-time lookups.

```cpp
int numEquivDominoPairs(vector<vector<int>>& dominoes) {
    unordered_map<string, int> freq;
    for (auto& pair : dominoes) {
        string key = to_string(min(pair[0], pair[1])) + "," + to_string(max(pair[0], pair[1]));
        freq[key]++;
    }
    int count = 0;
    for (auto& [key, value] : freq) {
        count += value * (value - 1) / 2;
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of pairs. This is because we're iterating through the pairs once and using a hashmap for constant-time lookups.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every pair in the hashmap.
> - **Optimality proof:** This is the optimal solution because we're minimizing the number of operations by using a hashmap and only iterating through the pairs once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts: Hashmaps, frequency counting, combinations.
- Problem-solving patterns: Reducing time complexity by using data structures for efficient lookups.
- Optimization techniques: Minimizing the number of operations by iterating through the input only once.

**Mistakes to Avoid:**
- Not considering the case where `a > b`.
- Not using a hashmap to store frequencies.
- Not calculating combinations correctly.

**Similar Problems to Practice:**
- Other problems involving frequency counting and combinations, such as counting the number of anagrams in a list of strings.