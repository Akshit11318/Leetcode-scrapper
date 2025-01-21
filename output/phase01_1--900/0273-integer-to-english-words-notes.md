## Integer to English Words

**Problem Link:** https://leetcode.com/problems/integer-to-english-words/description

**Problem Statement:**
- Input: An integer `num` between 0 and $2^{31}-1$.
- Output: The English words representation of `num`.
- Key requirements and edge cases:
  - Handle numbers in the range $[0, 2^{31}-1]$.
  - Convert numbers to their English word equivalents, considering ones, tens, hundreds, thousands, millions, and billions places.
- Example test cases:
  - `num = 123` -> "One Hundred Twenty Three"
  - `num = 12345` -> "Twelve Thousand Three Hundred Forty Five"
  - `num = 1234567` -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves creating a mapping of numbers to their English word equivalents for ones, tens, and thousands places.
- We then iterate through the number from right to left, converting each set of three digits (hundreds place) to English words and appending the corresponding thousands place word if applicable.
- This approach comes to mind first because it directly addresses the conversion of numbers to words without considering efficiency.

```cpp
class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        
        vector<string> ones = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        vector<string> teens = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        vector<string> tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        vector<string> thousands = {"", "Thousand", "Million", "Billion"};
        
        string result = "";
        int i = 0;
        
        while (num > 0) {
            if (num % 1000 != 0) {
                result = helper(num % 1000, ones, teens, tens) + " " + thousands[i] + " " + result;
            }
            num /= 1000;
            i++;
        }
        
        return result.substr(1); // Remove the trailing space
    }
    
    string helper(int num, vector<string>& ones, vector<string>& teens, vector<string>& tens) {
        if (num == 0) return "";
        
        if (num < 10) return ones[num];
        else if (num < 20) return teens[num - 10];
        else if (num < 100) return tens[num / 10] + (num % 10 == 0 ? "" : " " + ones[num % 10]);
        else return ones[num / 100] + " Hundred" + (num % 100 == 0 ? "" : " " + helper(num % 100, ones, teens, tens));
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input number, because we process the number digit by digit.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the word mappings and the result.
> - **Why these complexities occur:** The time complexity is due to the iterative processing of the number, and the space complexity is due to the use of constant space for the word mappings and the result.

---

### Optimal Approach (Required)

The provided brute force approach is already quite efficient and optimal for this problem. It correctly handles the conversion of numbers to English words and uses a reasonable amount of space. The time complexity of $O(\log n)$ is optimal because we must process each digit of the input number at least once.

However, we can make some minor adjustments to improve readability and maintainability:

```cpp
class Solution {
public:
    string numberToWords(int num) {
        if (num == 0) return "Zero";
        
        vector<string> ones = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        vector<string> teens = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
        vector<string> tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
        vector<string> thousands = {"", "Thousand", "Million", "Billion"};
        
        string result = "";
        int i = 0;
        
        while (num > 0) {
            if (num % 1000 != 0) {
                result = helper(num % 1000, ones, teens, tens) + " " + thousands[i] + " " + result;
            }
            num /= 1000;
            i++;
        }
        
        return result.substr(1); // Remove the trailing space
    }
    
    string helper(int num, vector<string>& ones, vector<string>& teens, vector<string>& tens) {
        if (num == 0) return "";
        
        string result = "";
        
        if (num >= 100) {
            result += ones[num / 100] + " Hundred";
            num %= 100;
        }
        
        if (num >= 20) {
            result += (result.empty() ? "" : " ") + tens[num / 10];
            num %= 10;
        }
        
        if (num >= 10) {
            result += (result.empty() ? "" : " ") + teens[num - 10];
            num = 0;
        }
        
        if (num > 0) {
            result += (result.empty() ? "" : " ") + ones[num];
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the input number.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space.
> - **Optimality proof:** This approach is optimal because we must process each digit of the input number at least once, and the used space is constant.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iterative processing, word mapping, and recursive helper functions.
- Problem-solving patterns identified: breaking down complex problems into smaller sub-problems and using helper functions.
- Optimization techniques learned: using constant space and minimizing the number of operations.
- Similar problems to practice: other problems involving number-to-word conversions or similar iterative processing.

**Mistakes to Avoid:**
- Common implementation errors: incorrect handling of edge cases (e.g., numbers less than 10 or greater than or equal to 1000).
- Edge cases to watch for: numbers with trailing zeros, numbers greater than $2^{31}-1$, and negative numbers.
- Performance pitfalls: using excessive space or unnecessary operations.
- Testing considerations: thoroughly testing the function with various input values, including edge cases.