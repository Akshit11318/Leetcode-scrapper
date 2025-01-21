## Successful Pairs of Spells and Potions
**Problem Link:** https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description

**Problem Statement:**
- Input: `success` (the success threshold), `spells` (a list of spell costs), and `potions` (a list of potion strengths).
- Constraints: 
  - `1 <= success <= 10^6`
  - `1 <= spells.length, potions.length <= 500`
  - `1 <= spells[i], potions[i] <= 10^6`
- Output: A list of successful spell pairs for each spell, where a spell is successful if its cost multiplied by a potion's strength is greater than or equal to the success threshold.
- Key requirements: Calculate the successful pairs for each spell.
- Example test cases:
  - `success = 5`, `spells = [5, 1, 3]`, `potions = [1, 2, 3, 4, 5]`
  - Expected output: For each spell, find the number of potions that make the spell successful.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each spell and for each spell, iterate over each potion to check if the product of the spell's cost and the potion's strength is greater than or equal to the success threshold.
- Step-by-step breakdown of the solution:
  1. For each spell in the `spells` list, initialize a counter for successful pairs.
  2. For each potion in the `potions` list, check if the product of the spell's cost and the potion's strength is greater than or equal to the `success` threshold.
  3. If the condition is met, increment the counter for the current spell.
  4. After checking all potions for a spell, add the count of successful pairs to the result list.

```cpp
vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
    vector<int> result;
    for (int spell : spells) {
        int count = 0;
        for (int potion : potions) {
            if ((long long)spell * potion >= success) {
                count++;
            }
        }
        result.push_back(count);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of spells and $m$ is the number of potions, because for each spell, we iterate over all potions.
> - **Space Complexity:** $O(n)$, because we store the count of successful pairs for each spell in the result list.
> - **Why these complexities occur:** The brute force approach involves nested loops over the spells and potions, leading to the time complexity. The space complexity is due to storing the results for each spell.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can sort the potions in descending order and then for each spell, use a binary search to find the first potion that makes the spell successful. This reduces the number of iterations significantly.
- Detailed breakdown of the approach:
  1. Sort the `potions` list in descending order.
  2. For each spell in the `spells` list, perform a binary search in the sorted `potions` list to find the first potion that makes the spell successful.
  3. The index of this potion (or the length of the potions list if no such potion is found) gives us the count of successful pairs for the spell.

```cpp
vector<int> successfulPairs(vector<int>& spells, vector<int>& potions, long long success) {
    sort(potions.rbegin(), potions.rend());
    vector<int> result;
    for (int spell : spells) {
        int left = 0, right = potions.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if ((long long)spell * potions[mid] < success) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        result.push_back(potions.size() - left);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log m + m \log m)$, where $n$ is the number of spells and $m$ is the number of potions. The $m \log m$ term comes from sorting the potions, and the $n \log m$ term comes from performing binary search for each spell.
> - **Space Complexity:** $O(n)$, because we store the count of successful pairs for each spell in the result list.
> - **Optimality proof:** This approach is optimal because it reduces the number of comparisons needed to find successful pairs for each spell, leveraging the fact that the potions are sorted and that we can stop searching once we find the first successful potion for a spell.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search and sorting.
- Problem-solving patterns identified: Using sorting and binary search to reduce the time complexity of finding successful pairs.
- Optimization techniques learned: Leveraging the properties of sorted lists to reduce the number of comparisons needed.
- Similar problems to practice: Problems involving finding pairs or elements in sorted lists.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where no potion makes a spell successful.
- Edge cases to watch for: Empty input lists, or lists containing a single element.
- Performance pitfalls: Not using binary search after sorting, leading to higher time complexity.
- Testing considerations: Testing with edge cases, such as empty lists or lists with a single element, and with large inputs to ensure performance.