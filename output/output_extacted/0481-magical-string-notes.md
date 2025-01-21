## Magical String

**Problem Link:** https://leetcode.com/problems/magical-string/description

**Problem Statement:**
- The input is a string `s` which represents a magical string.
- The task is to find the number of `1`s in the string up to the `n`-th position.
- The string is generated based on a specific rule.
- The string starts with "1" and each subsequent character is determined by the previous characters.
- The string is considered magical because it has a special property: it is generated based on the previous characters.
- The key requirements are to find the number of `1`s in the string up to the `n`-th position.

**Example Test Cases:**
- Input: `n = 6`
  Output: `3`
  Explanation: The first 6 numbers in the magical string are "1 1 2 2 1 1" so the first 6 magical string is "112221".
- Input: `n = 1`
  Output: `1`
  Explanation: The first number is 1.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate the magical string up to the `n`-th position and then count the number of `1`s.
- This approach involves creating a loop to generate the string and another loop to count the `1`s.

```cpp
class Solution {
public:
    int magicalString(int n) {
        if (n == 1) return 1;
        vector<int> magical(n + 1, 0);
        magical[0] = 1;
        magical[1] = 1;
        int head = 2, tail = 2, num = 2;
        while (tail < n) {
            int count = magical[head];
            while (tail < n && count > 0) {
                magical[tail] = num;
                tail++;
                count--;
            }
            num = (num == 1) ? 2 : 1;
            head++;
        }
        int countOnes = 0;
        for (int i = 0; i < n; i++) {
            if (magical[i] == 1) countOnes++;
        }
        return countOnes;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we need to generate the magical string up to the `n`-th position and then count the `1`s.
> - **Space Complexity:** $O(n)$ because we need to store the magical string up to the `n`-th position.
> - **Why these complexities occur:** These complexities occur because we need to generate the magical string and then count the `1`s, which requires iterating over the string.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to generate the magical string up to the `n`-th position and count the `1`s in a single pass.
- We can do this by maintaining a count of `1`s as we generate the string.

```cpp
class Solution {
public:
    int magicalString(int n) {
        if (n == 1) return 1;
        vector<int> magical(n + 1, 0);
        magical[0] = 1;
        magical[1] = 1;
        int head = 2, tail = 2, num = 2, countOnes = 1;
        while (tail < n) {
            int count = magical[head];
            while (tail < n && count > 0) {
                magical[tail] = num;
                if (num == 1) countOnes++;
                tail++;
                count--;
            }
            num = (num == 1) ? 2 : 1;
            head++;
        }
        return countOnes;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we need to generate the magical string up to the `n`-th position.
> - **Space Complexity:** $O(n)$ because we need to store the magical string up to the `n`-th position.
> - **Optimality proof:** This is the optimal solution because we are generating the magical string and counting the `1`s in a single pass, which requires a minimum of $O(n)$ time and space.

---

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is generating a magical string and counting the `1`s in a single pass.
- The problem-solving pattern identified is maintaining a count of `1`s as we generate the string.
- The optimization technique learned is to generate the string and count the `1`s in a single pass.

**Mistakes to Avoid:**
- A common implementation error is to generate the magical string and then count the `1`s in two separate passes.
- An edge case to watch for is when `n` is 1.
- A performance pitfall is to use unnecessary loops or recursive calls.
- A testing consideration is to test the function with different values of `n`.