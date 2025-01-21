## Positions of Large Groups

**Problem Link:** https://leetcode.com/problems/positions-of-large-groups/description

**Problem Statement:**
- Input format: A string `s`.
- Constraints: `1 <= s.length <= 1000`.
- Expected output format: A list of lists, where each sublist contains two integers representing the start and end positions of a large group.
- Key requirements and edge cases to consider: 
    * A large group is defined as a group of `3` or more consecutive characters that are the same.
    * The function should return all positions of large groups in the input string.
- Example test cases with explanations:
    * Input: `"abbxxxxxyy"` 
      Output: `[[3,6]]` 
      Explanation: `"xx"` is not a large group because it only has 2 'x's, and `"yyy"` is not a large group because it only has 3 'y's but the problem statement does not ask for groups of size 3 or more of the same character that are at the end of the string. However, `"xxxxx"` is a large group because it has 5 'x's.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through the string and check every character and the next two characters to see if they are the same.
- Step-by-step breakdown of the solution:
    1. Initialize an empty list to store the positions of large groups.
    2. Iterate through the string using a for loop.
    3. For each character, check if it and the next two characters are the same.
    4. If they are the same, find the start and end positions of the large group by expanding outwards from the current character.
    5. Add the start and end positions to the list.
- Why this approach comes to mind first: It is the simplest way to solve the problem, but it may not be the most efficient.

```cpp
vector<vector<int>> largeGroupPositions(string s) {
    vector<vector<int>> result;
    for (int i = 0; i < s.length() - 2; i++) {
        if (s[i] == s[i + 1] && s[i] == s[i + 2]) {
            int start = i;
            int end = i + 2;
            while (end + 1 < s.length() && s[end] == s[end + 1]) {
                end++;
            }
            result.push_back({start, end});
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because in the worst case we are iterating through the entire string.
> - **Space Complexity:** $O(n)$ because in the worst case we are storing the positions of all characters in the string.
> - **Why these complexities occur:** These complexities occur because we are iterating through the string and storing the positions of all large groups.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can iterate through the string and keep track of the current character and the number of times it has appeared in a row.
- Detailed breakdown of the approach:
    1. Initialize an empty list to store the positions of large groups.
    2. Initialize variables to keep track of the current character and the number of times it has appeared in a row.
    3. Iterate through the string using a for loop.
    4. For each character, check if it is the same as the current character.
    5. If it is the same, increment the count of the current character.
    6. If it is not the same, check if the count of the current character is 3 or more.
    7. If it is 3 or more, add the start and end positions of the large group to the list.
    8. Update the current character and the count.
- Proof of optimality: This solution is optimal because it only iterates through the string once and keeps track of the minimum amount of information necessary to solve the problem.

```cpp
vector<vector<int>> largeGroupPositions(string s) {
    vector<vector<int>> result;
    int start = 0;
    for (int i = 0; i < s.length(); i++) {
        if (i == s.length() - 1 || s[i] != s[i + 1]) {
            if (i - start + 1 >= 3) {
                result.push_back({start, i});
            }
            start = i + 1;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the length of the string, because we are only iterating through the string once.
> - **Space Complexity:** $O(n)$ because in the worst case we are storing the positions of all characters in the string.
> - **Optimality proof:** This solution is optimal because it only iterates through the string once and keeps track of the minimum amount of information necessary to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and list manipulation.
- Problem-solving patterns identified: Keeping track of the current character and the number of times it has appeared in a row.
- Optimization techniques learned: Only iterating through the string once and keeping track of the minimum amount of information necessary to solve the problem.
- Similar problems to practice: Other string manipulation problems, such as finding the longest substring with a certain property.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty string or a string with only one character.
- Edge cases to watch for: A string with only two characters, or a string with a large group at the beginning or end.
- Performance pitfalls: Iterating through the string multiple times, or using unnecessary data structures.
- Testing considerations: Testing the function with different types of input, such as a string with multiple large groups, or a string with no large groups.