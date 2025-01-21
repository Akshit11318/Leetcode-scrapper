## Find Users With Valid E-mails
**Problem Link:** https://leetcode.com/problems/find-users-with-valid-e-mails/description

**Problem Statement:**
- Input format and constraints: The problem requires writing a SQL query to find users with valid e-mails from a given table `Users`.
- Expected output format: The output should be a list of user IDs with valid e-mails.
- Key requirements and edge cases to consider: A valid e-mail address consists of the local part and the domain, separated by '@'. The local part can contain alphanumeric characters, '.', '_', and '-'. The domain can contain alphanumeric characters, '.', and '-'.
- Example test cases with explanations: For example, 'example@gmail.com' is a valid e-mail address, while 'example@gmail' is not.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first step is to understand the structure of a valid e-mail address and how to check for it in a string.
- Step-by-step breakdown of the solution: We can use a regular expression to match the pattern of a valid e-mail address.
- Why this approach comes to mind first: This approach is straightforward and uses a well-known technique for pattern matching.

```cpp
// This problem requires a SQL query, not C++ code. However, for the sake of following instructions, let's consider a hypothetical C++ function that takes a string as input and returns true if it's a valid e-mail, false otherwise.
#include <regex>
#include <string>

bool isValidEmail(const std::string& email) {
    // Regular expression pattern for a valid e-mail
    std::regex pattern("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$");
    return std::regex_match(email, pattern);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the length of the input string, because `std::regex_match` needs to iterate over the entire string in the worst case.
> - **Space Complexity:** $O(n)$, because the regular expression engine may need to create temporary match results that scale with the input size.
> - **Why these complexities occur:** The complexities are due to the nature of regular expression matching, which can involve backtracking and creating temporary data structures.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a SQL query with a regular expression to filter out invalid e-mail addresses directly in the database.
- Detailed breakdown of the approach: We use the `REGEXP` function in SQL to match the pattern of valid e-mail addresses.
- Proof of optimality: This approach is optimal because it minimizes the amount of data transferred and processed by only selecting valid e-mails directly in the database query.

```sql
SELECT id
FROM Users
WHERE email REGEXP '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$';
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where n is the number of rows in the `Users` table, because the database needs to scan each row to apply the regular expression filter.
> - **Space Complexity:** $O(1)$, assuming the database can filter rows without creating additional temporary storage that scales with the input size.
> - **Optimality proof:** This approach is optimal because it leverages the database's ability to filter data efficiently, minimizing the amount of data that needs to be processed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Regular expression pattern matching.
- Problem-solving patterns identified: Using database queries to filter data efficiently.
- Optimization techniques learned: Minimizing data transfer and processing by filtering data at the source (in this case, the database).
- Similar problems to practice: Other problems involving data filtering and validation.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly specifying the regular expression pattern.
- Edge cases to watch for: E-mail addresses with non-ASCII characters or very long local parts.
- Performance pitfalls: Transferring all data to the application layer for filtering instead of using database queries.
- Testing considerations: Ensuring the regular expression pattern correctly matches all valid e-mail formats and rejects all invalid ones.