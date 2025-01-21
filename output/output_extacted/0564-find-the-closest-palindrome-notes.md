## Find the Closest Palindrome

**Problem Link:** https://leetcode.com/problems/find-the-closest-palindrome/description

**Problem Statement:**
- Input: A string `n` representing a positive integer.
- Output: The closest palindrome number to the input number `n`.
- Key requirements: The input number `n` has a fixed length, and we need to find the closest palindrome number.
- Edge cases: If there are two closest palindrome numbers, we should return the smaller one.

**Example Test Cases:**
- Input: `n = "123"`
  - Expected output: `"121"`
- Input: `n = "1"`
  - Expected output: `"0"`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can start by checking all numbers less than or equal to the input number `n` to find the closest palindrome number.
- Step-by-step breakdown:
  1. Convert the input string `n` to an integer `num`.
  2. Initialize a variable `closest` to store the closest palindrome number.
  3. Iterate over all numbers from `num` to 0 (inclusive) to find the closest palindrome number.
  4. For each number, check if it is a palindrome by converting it to a string and comparing it with its reverse.
  5. If the number is a palindrome, update the `closest` variable with the current number.
  6. Return the `closest` palindrome number.

```cpp
class Solution {
public:
    string nearestPalindromic(string n) {
        long long num = stoll(n);
        long long closest = LLONG_MAX;
        long long diff = LLONG_MAX;
        
        for (long long i = num; i >= 0; i--) {
            string str = to_string(i);
            string rev = str;
            reverse(rev.begin(), rev.end());
            if (str == rev) {
                long long currDiff = abs(num - i);
                if (currDiff < diff) {
                    diff = currDiff;
                    closest = i;
                } else if (currDiff == diff) {
                    closest = min(closest, i);
                }
            }
        }
        
        return to_string(closest);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times 10^n)$, where $n$ is the number of digits in the input number. This is because we are iterating over all numbers from `num` to 0 and checking if each number is a palindrome.
> - **Space Complexity:** $O(n)$, where $n$ is the number of digits in the input number. This is because we are storing the input number as a string and its reverse.
> - **Why these complexities occur:** The brute force approach has high time complexity because it involves iterating over all numbers and checking if each number is a palindrome. The space complexity is relatively low because we are only storing a few variables.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can generate all possible palindrome numbers with the same number of digits as the input number `n` and compare them with the input number.
- Detailed breakdown:
  1. Convert the input string `n` to an integer `num`.
  2. Generate all possible palindrome numbers with the same number of digits as `num`.
  3. Compare each generated palindrome number with `num` and find the closest one.
  4. Return the closest palindrome number.

```cpp
class Solution {
public:
    string nearestPalindromic(string n) {
        long long num = stoll(n);
        long long nDigits = n.size();
        
        // Generate all possible palindrome numbers with the same number of digits
        vector<long long> candidates;
        if (nDigits == 1) {
            candidates = {0, 1};
        } else {
            long long firstHalf = pow(10, nDigits / 2);
            for (long long i = firstHalf; i < firstHalf * 10; i++) {
                string str = to_string(i);
                string rev = str;
                reverse(rev.begin(), rev.end());
                if (nDigits % 2 == 0) {
                    candidates.push_back(stoll(str + rev));
                } else {
                    candidates.push_back(stoll(str + rev.substr(0, rev.size() - 1)));
                }
            }
        }
        
        long long closest = LLONG_MAX;
        long long diff = LLONG_MAX;
        
        for (long long candidate : candidates) {
            long long currDiff = abs(num - candidate);
            if (currDiff < diff) {
                diff = currDiff;
                closest = candidate;
            } else if (currDiff == diff) {
                closest = min(closest, candidate);
            }
        }
        
        return to_string(closest);
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(10^{n/2})$, where $n$ is the number of digits in the input number. This is because we are generating all possible palindrome numbers with the same number of digits as the input number.
> - **Space Complexity:** $O(10^{n/2})$, where $n$ is the number of digits in the input number. This is because we are storing all generated palindrome numbers.
> - **Optimality proof:** The optimal approach is more efficient than the brute force approach because it generates only palindrome numbers with the same number of digits as the input number, reducing the search space significantly.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: generating palindrome numbers, comparing numbers, and finding the closest number.
- Problem-solving patterns identified: reducing the search space by generating only relevant candidates.
- Optimization techniques learned: using mathematical insights to reduce the time complexity.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as when the input number has only one digit.
- Edge cases to watch for: when the input number is a palindrome itself.
- Performance pitfalls: using the brute force approach, which has high time complexity.
- Testing considerations: testing the solution with different input numbers, including edge cases.