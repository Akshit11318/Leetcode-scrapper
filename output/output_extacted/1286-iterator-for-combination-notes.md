## Iterator for Combination

**Problem Link:** https://leetcode.com/problems/iterator-for-combination/description

**Problem Statement:**
- Input format and constraints: The problem takes a string `characters` and an integer `combinationLength` as input. The goal is to create an iterator that generates all possible combinations of `combinationLength` characters from the `characters` string.
- Expected output format: The iterator should yield each combination as a string, and it should be possible to iterate over all combinations using the `next()` method.
- Key requirements and edge cases to consider:
  - The input string `characters` can contain duplicate characters.
  - The `combinationLength` can be greater than the length of the `characters` string.
  - The iterator should yield combinations in lexicographical order.
- Example test cases with explanations:
  - Input: `characters = "abc", combinationLength = 2`
    Output: `["ab", "ac", "bc"]`
  - Input: `characters = "aaa", combinationLength = 2`
    Output: `["aa"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible combinations of characters and then filter out the ones that have the correct length.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of characters using a recursive function or a loop.
  2. Check each combination to see if it has the correct length.
  3. If it does, add it to the result list.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that does not require any advanced algorithms or data structures.

```cpp
class CombinationIterator {
public:
    vector<string> combinations;
    int index = 0;
    CombinationIterator(string characters, int combinationLength) {
        vector<string> temp;
        backtrack(characters, "", combinationLength, temp);
        combinations = temp;
    }
    string next() {
        return combinations[index++];
    }
    bool hasNext() {
        return index < combinations.size();
    }
    void backtrack(string characters, string current, int combinationLength, vector<string>& temp) {
        if (current.size() == combinationLength) {
            temp.push_back(current);
            return;
        }
        for (int i = 0; i < characters.size(); i++) {
            current.push_back(characters[i]);
            backtrack(characters.substr(i + 1), current, combinationLength, temp);
            current.pop_back();
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the `characters` string. This is because in the worst case, we have to generate all possible combinations of characters.
> - **Space Complexity:** $O(2^n)$, because we store all combinations in the `combinations` vector.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of characters, which results in exponential time and space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a technique called "backtracking" to generate combinations on the fly, without storing them all in memory at once.
- Detailed breakdown of the approach:
  1. Initialize an array of indices, where each index corresponds to a character in the `characters` string.
  2. Use a recursive function to generate combinations by incrementing the indices and adding characters to the current combination.
  3. When the current combination reaches the correct length, yield it and backtrack to generate the next combination.
- Proof of optimality: This approach has a time complexity of $O(\frac{n!}{(n-k)!k!})$, where $n$ is the length of the `characters` string and $k$ is the `combinationLength`. This is because we only generate combinations that have the correct length, and we do not store all combinations in memory at once.

```cpp
class CombinationIterator {
public:
    string characters;
    int combinationLength;
    vector<int> indices;
    CombinationIterator(string characters, int combinationLength) : characters(characters), combinationLength(combinationLength) {
        indices.resize(combinationLength);
        for (int i = 0; i < combinationLength; i++) {
            indices[i] = i;
        }
    }
    string next() {
        string result;
        for (int i = 0; i < combinationLength; i++) {
            result.push_back(characters[indices[i]]);
        }
        // increment indices
        for (int i = combinationLength - 1; i >= 0; i--) {
            if (indices[i] < characters.size() - combinationLength + i) {
                indices[i]++;
                for (int j = i + 1; j < combinationLength; j++) {
                    indices[j] = indices[j - 1] + 1;
                }
                break;
            }
        }
        return result;
    }
    bool hasNext() {
        for (int i = combinationLength - 1; i >= 0; i--) {
            if (indices[i] < characters.size() - combinationLength + i) {
                return true;
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\frac{n!}{(n-k)!k!})$, where $n$ is the length of the `characters` string and $k$ is the `combinationLength`. This is because we only generate combinations that have the correct length.
> - **Space Complexity:** $O(k)$, where $k$ is the `combinationLength`. This is because we only store the current combination and the indices array.
> - **Optimality proof:** This approach is optimal because it generates combinations on the fly, without storing them all in memory at once. It also has a time complexity that is proportional to the number of combinations, which is the minimum possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Backtracking, recursion, and iteration.
- Problem-solving patterns identified: Using indices to generate combinations, and incrementing indices to generate the next combination.
- Optimization techniques learned: Generating combinations on the fly, without storing them all in memory at once.
- Similar problems to practice: Permutations, subsets, and other combinatorial problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty `characters` string or a `combinationLength` that is greater than the length of the `characters` string.
- Edge cases to watch for: Duplicate characters in the `characters` string, and a `combinationLength` that is equal to the length of the `characters` string.
- Performance pitfalls: Storing all combinations in memory at once, which can lead to high memory usage and slow performance.
- Testing considerations: Testing the iterator with different inputs, such as an empty `characters` string, a `combinationLength` of 1, and a `combinationLength` that is greater than the length of the `characters` string.