## Construct Smallest Number from DI String
**Problem Link:** https://leetcode.com/problems/construct-smallest-number-from-di-string/description

**Problem Statement:**
- Input format and constraints: The input is a string `s` consisting of characters 'D' and 'I', where 'D' means decreasing and 'I' means increasing. The length of `s` is between 1 and 100.
- Expected output format: The output should be the smallest number that can be constructed from the given string.
- Key requirements and edge cases to consider: The number should be as small as possible, and it should be a valid integer.
- Example test cases with explanations: 
    - Input: `s = "I"` Output: `"1"`
    - Input: `s = "D"` Output: `"21"`
    - Input: `s = "ID"` Output: `"012"`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: We can generate all possible numbers and check which one is the smallest.
- Step-by-step breakdown of the solution: 
    1. Generate all possible numbers of length `n + 1`, where `n` is the length of the input string.
    2. For each number, check if it satisfies the conditions given by the input string.
    3. If it does, add it to the list of possible numbers.
    4. Finally, return the smallest number in the list.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it is not efficient.

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string smallestNumber(string s) {
    int n = s.length();
    vector<string> nums;
    for (int i = 0; i <= n; i++) {
        string num;
        num.push_back('0' + i);
        nums.push_back(num);
    }
    for (int i = 0; i < n; i++) {
        if (s[i] == 'I') {
            for (int j = 0; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[j].back() > nums[k].back()) {
                        swap(nums[j], nums[k]);
                    }
                }
            }
        } else {
            for (int j = 0; j < nums.size(); j++) {
                for (int k = j + 1; k < nums.size(); k++) {
                    if (nums[j].back() < nums[k].back()) {
                        swap(nums[j], nums[k]);
                    }
                }
            }
        }
    }
    string res;
    for (auto& num : nums) {
        res += num.back();
    }
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 2^n \cdot n)$, where $n$ is the length of the input string. This is because we generate all possible numbers of length `n + 1`, and for each number, we check if it satisfies the conditions given by the input string.
> - **Space Complexity:** $O(2^n)$, where $n$ is the length of the input string. This is because we store all possible numbers in a vector.
> - **Why these complexities occur:** These complexities occur because we generate all possible numbers and check each one, which is not efficient.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to keep track of the digits that we have seen so far. When we encounter an 'I', we pop all the digits from the stack that are greater than the current digit and push them back onto the stack in ascending order. When we encounter a 'D', we simply push the current digit onto the stack.
- Detailed breakdown of the approach: 
    1. Initialize an empty stack and an empty string to store the result.
    2. Iterate over the input string. For each character, if it is 'I', pop all the digits from the stack that are greater than the current digit and push them back onto the stack in ascending order. Then, push the current digit onto the stack.
    3. If the character is 'D', simply push the current digit onto the stack.
    4. Finally, pop all the digits from the stack and append them to the result string.
- Proof of optimality: This approach is optimal because it uses a stack to keep track of the digits, which allows us to efficiently pop and push digits as needed. The time complexity of this approach is $O(n)$, where $n$ is the length of the input string, because we only iterate over the input string once.

```cpp
#include <iostream>
#include <string>
using namespace std;

string smallestNumber(string s) {
    string res = "";
    int num = 1;
    for (char c : s) {
        if (c == 'I') {
            res += to_string(num);
            num++;
        } else {
            res += to_string(num);
            num++;
            while (!res.empty() && res.back() > '0') {
                res += to_string(--num);
            }
        }
    }
    res += to_string(num);
    return res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input string. This is because we only iterate over the input string once.
> - **Space Complexity:** $O(n)$, where $n` is the length of the input string. This is because we store the result string.
> - **Optimality proof:** This approach is optimal because it uses a stack to keep track of the digits, which allows us to efficiently pop and push digits as needed. The time complexity of this approach is $O(n)$, where $n` is the length of the input string, because we only iterate over the input string once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to keep track of digits, iterating over the input string, and efficiently popping and pushing digits as needed.
- Problem-solving patterns identified: Using a stack to solve problems that involve iterating over a string and keeping track of digits.
- Optimization techniques learned: Using a stack to efficiently pop and push digits as needed, and iterating over the input string only once.
- Similar problems to practice: Problems that involve iterating over a string and keeping track of digits, such as constructing the smallest number from a given string.

**Mistakes to Avoid:**
- Common implementation errors: Not initializing the stack or result string correctly, not popping and pushing digits correctly, and not iterating over the input string correctly.
- Edge cases to watch for: Empty input string, input string with only 'I' or only 'D', and input string with a mix of 'I' and 'D'.
- Performance pitfalls: Using a brute force approach that generates all possible numbers and checks each one, which is not efficient.
- Testing considerations: Testing the function with different input strings, including edge cases, to ensure that it produces the correct output.