## Report Spam Message

**Problem Link:** https://leetcode.com/problems/report-spam-message/description

**Problem Statement:**
- Input format: A list of `emails` where each email is a string.
- Constraints: The number of `emails` will be between 1 and 1000.
- Expected output format: The number of accounts that will report spam messages.
- Key requirements and edge cases to consider: 
  - Each email has a unique username and domain.
  - Two emails are considered to be from the same account if they have the same username and domain.
  - If two accounts have the same username and domain but different email addresses, they should be counted as one account.
- Example test cases with explanations:
  - `emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]`, the output should be `2`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves creating a set to store unique usernames and domains. We then iterate over each email, extract the username and domain, and add it to the set. If the username and domain are already in the set, we do not add it again.
- Step-by-step breakdown of the solution:
  1. Create an empty set `unique_emails` to store unique usernames and domains.
  2. Iterate over each email in the `emails` list.
  3. For each email, extract the username and domain by splitting the email at the `@` symbol.
  4. Add the username and domain to the `unique_emails` set.
  5. Return the size of the `unique_emails` set, which represents the number of unique accounts.

```cpp
#include <iostream>
#include <set>
#include <string>

int numUniqueEmails(std::vector<std::string>& emails) {
    std::set<std::string> unique_emails;
    for (const auto& email : emails) {
        std::string local_name, domain_name;
        size_t at_pos = email.find('@');
        local_name = email.substr(0, at_pos);
        domain_name = email.substr(at_pos + 1);
        
        // Remove everything after the '+' in the local name
        size_t plus_pos = local_name.find('+');
        if (plus_pos != std::string::npos) {
            local_name = local_name.substr(0, plus_pos);
        }
        
        // Remove the '.' in the local name
        local_name.erase(std::remove(local_name.begin(), local_name.end(), '.'), local_name.end());
        
        std::string normalized_email = local_name + "@" + domain_name;
        unique_emails.insert(normalized_email);
    }
    return unique_emails.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of emails and $m$ is the maximum length of an email. This is because we iterate over each email and extract the username and domain, which takes $O(m)$ time.
> - **Space Complexity:** $O(n \cdot m)$, because in the worst case, we might have to store all emails in the `unique_emails` set.
> - **Why these complexities occur:** The time complexity occurs because we iterate over each email and perform string operations, which take $O(m)$ time. The space complexity occurs because we store all unique emails in the `unique_emails` set.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution but with a few optimizations. We can use a `std::unordered_set` instead of a `std::set` to store unique emails, which has an average time complexity of $O(1)$ for insertion and lookup operations.
- Detailed breakdown of the approach:
  1. Create an empty `std::unordered_set` `unique_emails` to store unique usernames and domains.
  2. Iterate over each email in the `emails` list.
  3. For each email, extract the username and domain by splitting the email at the `@` symbol.
  4. Remove everything after the '+' in the local name and remove the '.' in the local name.
  5. Add the normalized email to the `unique_emails` set.
  6. Return the size of the `unique_emails` set, which represents the number of unique accounts.

```cpp
#include <iostream>
#include <unordered_set>
#include <string>

int numUniqueEmails(std::vector<std::string>& emails) {
    std::unordered_set<std::string> unique_emails;
    for (const auto& email : emails) {
        std::string local_name, domain_name;
        size_t at_pos = email.find('@');
        local_name = email.substr(0, at_pos);
        domain_name = email.substr(at_pos + 1);
        
        size_t plus_pos = local_name.find('+');
        if (plus_pos != std::string::npos) {
            local_name = local_name.substr(0, plus_pos);
        }
        
        local_name.erase(std::remove(local_name.begin(), local_name.end(), '.'), local_name.end());
        
        std::string normalized_email = local_name + "@" + domain_name;
        unique_emails.insert(normalized_email);
    }
    return unique_emails.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of emails and $m$ is the maximum length of an email. This is because we iterate over each email and extract the username and domain, which takes $O(m)$ time.
> - **Space Complexity:** $O(n \cdot m)$, because in the worst case, we might have to store all emails in the `unique_emails` set.
> - **Optimality proof:** This is the optimal solution because we have to iterate over each email at least once to extract the username and domain. The use of a `std::unordered_set` minimizes the time complexity of insertion and lookup operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation, set operations.
- Problem-solving patterns identified: Normalizing input data to reduce complexity.
- Optimization techniques learned: Using `std::unordered_set` instead of `std::set` for faster insertion and lookup operations.
- Similar problems to practice: Other string manipulation and set operation problems.

**Mistakes to Avoid:**
- Common implementation errors: Not removing everything after the '+' in the local name, not removing the '.' in the local name.
- Edge cases to watch for: Emails with no '@' symbol, emails with no '+' or '.' in the local name.
- Performance pitfalls: Using `std::set` instead of `std::unordered_set` for insertion and lookup operations.
- Testing considerations: Test the function with different types of input emails, including edge cases.