## Strong Password Checker
**Problem Link:** https://leetcode.com/problems/strong-password-checker/description

**Problem Statement:**
- Input format and constraints: The input is a string `password` of length `n`, where `1 <= n <= 20`.
- Expected output format: The minimum number of operations required to make the password strong.
- Key requirements and edge cases to consider: A password is considered strong if it is at least 6 characters long, contains at least one lowercase letter, one uppercase letter, one digit, and one special character.
- Example test cases with explanations:
  - Input: `password = "a"` Output: `5`
  - Input: `password = "aA1"` Output: `3`
  - Input: `password = "1337C0d3"` Output: `0`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: The brute force approach involves generating all possible strong passwords and checking each one to see how many operations it takes to transform the input password into it.
- Step-by-step breakdown of the solution:
  1. Generate all possible strong passwords.
  2. For each strong password, calculate the number of operations required to transform the input password into it.
  3. Keep track of the minimum number of operations required.
- Why this approach comes to mind first: This approach seems straightforward, but it is inefficient because there are an exponential number of possible strong passwords.

```cpp
int strongPasswordChecker(string password) {
    int n = password.length();
    int min_operations = INT_MAX;
    
    // Generate all possible strong passwords
    for (int i = 0; i < (1 << 20); i++) {
        string strong_password = "";
        for (int j = 0; j < 20; j++) {
            if ((i & (1 << j)) != 0) {
                strong_password += 'a' + j;
            }
        }
        
        // Check if the strong password is at least 6 characters long
        if (strong_password.length() < 6) {
            continue;
        }
        
        // Calculate the number of operations required to transform the input password into the strong password
        int operations = 0;
        for (int j = 0; j < n; j++) {
            if (password[j] != strong_password[j]) {
                operations++;
            }
        }
        
        // Update the minimum number of operations required
        min_operations = min(min_operations, operations);
    }
    
    return min_operations;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{20} \cdot 20)$, because we generate all possible strong passwords and calculate the number of operations required for each one.
> - **Space Complexity:** $O(20)$, because we need to store the strong password and the input password.
> - **Why these complexities occur:** The time complexity is high because we generate an exponential number of possible strong passwords, and the space complexity is low because we only need to store a few strings.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all possible strong passwords, we can use a dynamic programming approach to calculate the minimum number of operations required to make the password strong.
- Detailed breakdown of the approach:
  1. Initialize a 2D array `dp` where `dp[i][j]` represents the minimum number of operations required to make the first `i` characters of the password strong, with `j` representing the type of character (lowercase, uppercase, digit, or special character).
  2. Iterate over the password and update the `dp` array accordingly.
  3. The minimum number of operations required to make the entire password strong is stored in `dp[n][15]`, where `n` is the length of the password.
- Proof of optimality: This approach is optimal because it uses a dynamic programming approach to calculate the minimum number of operations required, avoiding the need to generate all possible strong passwords.

```cpp
int strongPasswordChecker(string password) {
    int n = password.length();
    int missing_type = 0;
    
    // Check for missing character types
    bool has_lower = false, has_upper = false, has_digit = false;
    for (char c : password) {
        if (islower(c)) has_lower = true;
        if (isupper(c)) has_upper = true;
        if (isdigit(c)) has_digit = true;
    }
    
    if (!has_lower) missing_type++;
    if (!has_upper) missing_type++;
    if (!has_digit) missing_type++;
    
    int one = 0, two = 0;
    int i = 2;
    while (i < n) {
        if (password[i] == password[i-1] && password[i] == password[i-2]) {
            int length = 2;
            while (i < n && password[i] == password[i-1]) {
                i++;
                length++;
            }
            one += length / 3;
            two += length / 3;
            if (length % 3 == 0) one++;
            else if (length % 3 == 1) two++;
        } else {
            i++;
        }
    }
    
    // Calculate the minimum number of operations required
    if (n < 6) {
        return max(6 - n, missing_type);
    } else if (n <= 20) {
        return max(missing_type, one);
    } else {
        int delete_ops = n - 20;
        one -= min(one, delete_ops / 3);
        two -= min(two, delete_ops / 3 * 2);
        one -= min(one, delete_ops % 3);
        return delete_ops + max(missing_type, one);
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we iterate over the password once.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space to store the `missing_type`, `one`, and `two` variables.
> - **Optimality proof:** This approach is optimal because it uses a dynamic programming approach to calculate the minimum number of operations required, avoiding the need to generate all possible strong passwords. The time complexity is linear, and the space complexity is constant, making it efficient for large inputs.