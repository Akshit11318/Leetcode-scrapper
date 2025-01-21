## Unique Email Addresses
**Problem Link:** https://leetcode.com/problems/unique-email-addresses/description

**Problem Statement:**
- Input format and constraints: The input is a list of email addresses. Each email address is a string consisting of lowercase English letters, digits, and special characters. The constraints are that the input list can contain duplicate email addresses, and the task is to count the number of unique email addresses.
- Expected output format: The output should be an integer representing the number of unique email addresses.
- Key requirements and edge cases to consider: The key requirement is to correctly handle the rules for determining unique email addresses. An email address is considered unique if it does not have any of the following: (1) everything after the `+` is ignored, and (2) if there is a `.`, everything after the last `.` is ignored, unless there is a `+` before the last `.`. 
- Example test cases with explanations: For example, given the email addresses `["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]`, the output should be `2`, because `testemail@leetcode.com` and `testemail@lee.tcode.com` are the unique email addresses.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The initial thought is to directly compare each email address with every other email address to determine uniqueness. However, this approach does not take into account the rules for determining unique email addresses.
- Step-by-step breakdown of the solution: 
  1. Create a function to normalize an email address based on the rules provided.
  2. Apply this function to each email address in the input list.
  3. Store the normalized email addresses in a set to eliminate duplicates.
  4. Return the size of the set as the number of unique email addresses.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement. However, it may not be the most efficient due to the potential complexity of the normalization function and the set operations.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    int numUniqueEmails(std::vector<std::string>& emails) {
        std::unordered_set<std::string> uniqueEmails;
        for (const auto& email : emails) {
            std::string normalizedEmail = normalizeEmail(email);
            uniqueEmails.insert(normalizedEmail);
        }
        return uniqueEmails.size();
    }

    std::string normalizeEmail(const std::string& email) {
        std::string normalizedEmail;
        bool foundPlus = false;
        size_t atPos = email.find('@');
        for (size_t i = 0; i < atPos; ++i) {
            if (email[i] == '+') {
                foundPlus = true;
            } else if (!foundPlus && email[i] != '.') {
                normalizedEmail += email[i];
            }
        }
        normalizedEmail += email.substr(atPos);
        return normalizedEmail;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of email addresses and $m$ is the average length of an email address. This is because for each email address, we potentially iterate over its entire length to normalize it.
> - **Space Complexity:** $O(n \cdot m)$, as in the worst case, every email address could be unique and thus stored in the set.
> - **Why these complexities occur:** These complexities occur due to the iteration over each character in each email address for normalization and the storage of all unique email addresses in a set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is to normalize each email address as we iterate through the list, applying the rules for ignoring characters after `+` and before the last `.` if there's no `+`. This approach ensures we only store unique email addresses in a set.
- Detailed breakdown of the approach: 
  1. Iterate through each email address in the input list.
  2. For each email address, find the `@` symbol to split the local name and domain.
  3. For the local name, find the `+` symbol and ignore everything after it. Also, ignore any `.` before the `+` if it exists.
  4. Normalize the local name and domain, and combine them to form the normalized email address.
  5. Add the normalized email address to a set to automatically eliminate duplicates.
  6. After iterating through all email addresses, the size of the set is the number of unique email addresses.
- Proof of optimality: This approach is optimal because it only requires a single pass through the list of email addresses and uses a set for efficient storage and lookup of unique email addresses.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

class Solution {
public:
    int numUniqueEmails(std::vector<std::string>& emails) {
        std::unordered_set<std::string> uniqueEmails;
        for (const auto& email : emails) {
            size_t atPos = email.find('@');
            std::string local = email.substr(0, atPos);
            std::string domain = email.substr(atPos);
            size_t plusPos = local.find('+');
            if (plusPos != std::string::npos) {
                local = local.substr(0, plusPos);
            }
            while (local.find('.') != std::string::npos) {
                local.erase(local.find('.'), 1);
            }
            uniqueEmails.insert(local + domain);
        }
        return uniqueEmails.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of email addresses and $m$ is the average length of an email address. This is because for each email address, we potentially iterate over its entire length to normalize it.
> - **Space Complexity:** $O(n \cdot m)$, as in the worst case, every email address could be unique and thus stored in the set.
> - **Optimality proof:** This is the optimal approach because it minimizes the number of operations required to normalize each email address and store unique ones, achieving the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Set operations for eliminating duplicates, string manipulation for normalizing email addresses.
- Problem-solving patterns identified: Normalization of data based on specific rules, use of sets for efficient storage and lookup of unique items.
- Optimization techniques learned: Minimizing unnecessary iterations and using appropriate data structures for efficient operations.
- Similar problems to practice: Problems involving data normalization, set operations, and string manipulation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly applying the rules for normalizing email addresses, not handling edge cases properly.
- Edge cases to watch for: Email addresses with multiple `+` or `.` symbols, empty strings, or strings without an `@` symbol.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the solution with a variety of input cases, including edge cases, to ensure correctness and efficiency.