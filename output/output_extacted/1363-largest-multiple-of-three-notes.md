## Largest Multiple of Three

**Problem Link:** https://leetcode.com/problems/largest-multiple-of-three/description

**Problem Statement:**
- Input: A non-negative integer `num`.
- Output: The largest multiple of three that can be obtained by deleting at most one digit of `num`.
- Key requirements: The solution must handle the case where deleting one digit results in a larger multiple of three than deleting no digits.
- Example test cases:
  - Input: `num = 831`
    - Output: `6`
    - Explanation: The largest multiple of three that can be obtained by deleting at most one digit is 6 (by deleting the digits 8 and 3).
  - Input: `num = 67685`
    - Output: `67584`
    - Explanation: The largest multiple of three that can be obtained by deleting at most one digit is 67584 (by deleting the digit 6).

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible deletions of one digit and check if the resulting number is a multiple of three.
- Step-by-step breakdown:
  1. Convert the input number to a string to easily iterate over each digit.
  2. For each digit, create a new string with that digit deleted.
  3. Convert the new string back to an integer and check if it's a multiple of three.
  4. Keep track of the largest multiple of three found.

```cpp
int largestMultipleOfThree(int num) {
    string str = to_string(num);
    int maxMultiple = 0;
    
    // Try deleting each digit
    for (int i = 0; i < str.size(); i++) {
        string newStr = str.substr(0, i) + str.substr(i + 1);
        
        // Handle empty string (i.e., deleted all digits)
        if (newStr.empty()) {
            continue;
        }
        
        int newNum = stoi(newStr);
        
        // Check if new number is a multiple of three
        if (newNum % 3 == 0) {
            maxMultiple = max(maxMultiple, newNum);
        }
    }
    
    // Also check the original number
    if (num % 3 == 0) {
        maxMultiple = max(maxMultiple, num);
    }
    
    return maxMultiple;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of digits in the input number and $m$ is the time complexity of converting a string to an integer. In practice, $m$ is relatively small.
> - **Space Complexity:** $O(n)$, for storing the string representation of the input number.
> - **Why these complexities occur:** The brute force approach involves iterating over each digit in the input number and performing a constant amount of work for each digit.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the properties of modular arithmetic to reduce the problem to a simpler form.
- If the sum of the digits of the input number is a multiple of three, then the number itself is a multiple of three.
- Otherwise, we need to delete at most one digit to make the sum of the digits a multiple of three.
- We can use a greedy approach to find the smallest digit that, when deleted, results in a sum of digits that is a multiple of three.

```cpp
int largestMultipleOfThree(int num) {
    string str = to_string(num);
    int sum = 0;
    vector<int> digits;
    
    // Calculate the sum of the digits and store the digits
    for (char c : str) {
        int digit = c - '0';
        sum += digit;
        digits.push_back(digit);
    }
    
    // If the sum is already a multiple of three, return the original number
    if (sum % 3 == 0) {
        return num;
    }
    
    // Otherwise, try to delete one digit to make the sum a multiple of three
    for (int digit : digits) {
        if ((sum - digit) % 3 == 0) {
            // Create a new string with the digit deleted
            string newStr;
            for (char c : str) {
                int d = c - '0';
                if (d != digit) {
                    newStr += c;
                }
            }
            
            // Return the new number
            if (!newStr.empty()) {
                return stoi(newStr);
            }
        }
    }
    
    // If no single digit deletion results in a multiple of three, try deleting two digits
    for (int i = 0; i < digits.size(); i++) {
        for (int j = i + 1; j < digits.size(); j++) {
            if ((sum - digits[i] - digits[j]) % 3 == 0) {
                // Create a new string with the two digits deleted
                string newStr;
                for (int k = 0; k < digits.size(); k++) {
                    if (k != i && k != j) {
                        newStr += str[k];
                    }
                }
                
                // Return the new number
                if (!newStr.empty()) {
                    return stoi(newStr);
                }
            }
        }
    }
    
    // If no two-digit deletion results in a multiple of three, return 0
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of digits in the input number.
> - **Space Complexity:** $O(n)$, for storing the string representation of the input number.
> - **Optimality proof:** This approach is optimal because it tries all possible deletions of one or two digits, which is necessary to find the largest multiple of three that can be obtained by deleting at most one digit.

---

### Final Notes

**Learning Points:**
- The problem demonstrates the use of modular arithmetic to reduce a problem to a simpler form.
- The optimal approach uses a greedy strategy to find the smallest digit that, when deleted, results in a sum of digits that is a multiple of three.
- The problem also highlights the importance of considering edge cases, such as when the input number has only one digit.

**Mistakes to Avoid:**
- Not considering the case where the input number has only one digit.
- Not handling the case where deleting one digit results in a larger multiple of three than deleting no digits.
- Not using a greedy approach to find the smallest digit that, when deleted, results in a sum of digits that is a multiple of three.