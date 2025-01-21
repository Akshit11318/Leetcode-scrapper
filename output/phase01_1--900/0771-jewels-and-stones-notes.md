## Jewels and Stones
**Problem Link:** https://leetcode.com/problems/jewels-and-stones/description

**Problem Statement:**
- Input format and constraints: The function takes two strings `J` and `S` as input, where `J` represents the types of stones that are jewels and `S` represents the stones you have. 
- Expected output format: The function should return the number of stones you have that are also jewels.
- Key requirements and edge cases to consider: The input strings only contain English letters (both lowercase and uppercase), and the length of both strings is between 1 and 50.
- Example test cases with explanations: 
  - Input: `J = "aA", S = "aAAbbbb"` Output: `3`
  - Input: `J = "z", S = "ZZ"` Output: `0`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each character in `S` and check if it exists in `J`.
- Step-by-step breakdown of the solution: 
  1. Initialize a counter variable to 0.
  2. Iterate through each character in `S`.
  3. For each character in `S`, iterate through each character in `J` to check if they match.
  4. If a match is found, increment the counter.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem, checking each stone against each jewel type.

```cpp
int numJewelsInStones(string J, string S) {
    int count = 0;
    for (char s : S) {
        for (char j : J) {
            if (s == j) {
                count++;
                break;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of `S` and $m$ is the length of `J`. This is because for each character in `S`, we potentially check all characters in `J`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count.
> - **Why these complexities occur:** The nested loop structure causes the time complexity to be the product of the lengths of the two input strings, while the space complexity remains constant because we do not allocate any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking each stone against each jewel type, we can create a `set` or use an array to keep track of the jewel types we've seen. This allows us to check if a stone is a jewel in constant time.
- Detailed breakdown of the approach: 
  1. Create a `set` of jewel types from `J`.
  2. Iterate through each stone in `S`.
  3. For each stone, check if it exists in the `set` of jewel types.
  4. If it does, increment the count.
- Proof of optimality: This approach is optimal because it reduces the time complexity of checking each stone from $O(m)$ to $O(1)$, resulting in an overall time complexity of $O(n + m)$, where $n$ is the length of `S` and $m` is the length of `J`.

```cpp
int numJewelsInStones(string J, string S) {
    unordered_set<char> jewels(J.begin(), J.end());
    int count = 0;
    for (char s : S) {
        if (jewels.find(s) != jewels.end()) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of `S` and $m` is the length of `J`. This is because creating the `set` of jewel types takes $O(m)$ time, and then checking each stone in `S` against this `set` takes $O(n)$ time.
> - **Space Complexity:** $O(m)$, as we store all unique jewel types in the `set`.
> - **Optimality proof:** This is the best possible time complexity because we must at least read the input strings once, and the use of a `set` for lookup allows us to do so in linear time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The importance of data structures like `sets` for efficient lookup, and how to optimize nested loops by reducing the complexity of the inner loop.
- Problem-solving patterns identified: Recognizing when a problem can be simplified by pre-processing data into a more efficient form.
- Optimization techniques learned: Using a `set` for constant time lookup instead of linear search.
- Similar problems to practice: Other string or array problems where lookup efficiency is key.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like empty input strings.
- Edge cases to watch for: Ensuring the solution works correctly for inputs with repeating characters or when one string is much longer than the other.
- Performance pitfalls: Failing to recognize the potential for optimization, leading to inefficient solutions.
- Testing considerations: Thoroughly testing the function with a variety of inputs, including edge cases, to ensure correctness and efficiency.