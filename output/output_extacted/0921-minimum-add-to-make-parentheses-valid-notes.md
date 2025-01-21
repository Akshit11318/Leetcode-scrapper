## Minimum Add to Make Parentheses Valid
**Problem Link:** https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description

**Problem Statement:**
- Input: A string of parentheses `s`.
- Constraints: `1 <= s.length <= 10^4`.
- Expected Output: The minimum number of parentheses that need to be added to make the string valid.
- Key Requirements: A string of parentheses is valid if every open parenthesis can be matched with a corresponding closing parenthesis.
- Edge Cases: An empty string, a string with only one type of parenthesis, or a string with no matching parentheses.

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking every possible combination of adding parentheses to the string to make it valid.
- This involves generating all permutations of the string with additional parentheses and checking if each permutation is valid.
- Why this approach comes to mind first: It's a straightforward, albeit inefficient, way to ensure all possibilities are considered.

```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        int minAdd = INT_MAX;
        // Generate all permutations with additional parentheses
        vector<string> permutations;
        generatePermutations(s, "", permutations);
        
        // Check each permutation for validity
        for (auto perm : permutations) {
            if (isValid(perm)) {
                int addCount = perm.size() - s.size();
                minAdd = min(minAdd, addCount);
            }
        }
        return minAdd;
    }
    
    void generatePermutations(string s, string current, vector<string>& permutations) {
        if (s.empty()) {
            permutations.push_back(current);
            return;
        }
        for (int i = 0; i <= s.size(); i++) {
            string left = s.substr(0, i);
            string right = s.substr(i);
            generatePermutations(right, current + "(" + left + ")", permutations);
            generatePermutations(right, current + ")" + left, permutations);
            generatePermutations(right, current + left, permutations);
        }
    }
    
    bool isValid(string s) {
        stack<char> stack;
        for (char c : s) {
            if (c == '(') stack.push(c);
            else if (c == ')') {
                if (stack.empty()) return false;
                stack.pop();
            }
        }
        return stack.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n})$ due to generating all permutations, where $n$ is the length of the string. This is because for each character, we have the option to add an open or close parenthesis before it, effectively doubling the number of permutations.
> - **Space Complexity:** $O(2^{n})$ for storing all permutations.
> - **Why these complexities occur:** The brute force approach involves generating an exponential number of permutations and checking each one, leading to high time and space complexities.

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a stack to keep track of unmatched open parentheses.
- When a closing parenthesis is encountered, if the stack is not empty (meaning there's an unmatched open parenthesis), we pop the stack; otherwise, we increment the count of parentheses to add.
- When an open parenthesis is encountered, we push it onto the stack.
- At the end, the number of unmatched open parentheses (the size of the stack) plus the count of closing parentheses without matches gives the minimum number of parentheses to add.

```cpp
class Solution {
public:
    int minAddToMakeValid(string s) {
        stack<char> stack;
        int addCount = 0;
        for (char c : s) {
            if (c == '(') stack.push(c);
            else if (c == ')') {
                if (stack.empty()) addCount++;
                else stack.pop();
            }
        }
        return addCount + stack.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string, because we make a single pass through the string.
> - **Space Complexity:** $O(n)$ for the stack in the worst case (all characters are open parentheses).
> - **Optimality proof:** This is the best possible complexity because we must at least read the input once, and the stack allows us to keep track of the necessary information in linear space.

### Final Notes
**Learning Points:**
- Using a stack to keep track of unmatched elements.
- The importance of iterating through the input only once for optimal time complexity.
- Balancing time and space complexity for efficient solutions.

**Mistakes to Avoid:**
- Generating unnecessary permutations or combinations.
- Not considering the use of a stack for tracking unmatched elements.
- Overcomplicating the solution with unnecessary data structures or algorithms.