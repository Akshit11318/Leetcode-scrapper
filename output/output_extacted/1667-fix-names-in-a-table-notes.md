## Fix Names in a Table

**Problem Link:** https://leetcode.com/problems/fix-names-in-a-table/description

**Problem Statement:**
- Input format and constraints: You are given a table `Names` with a column `name` containing names in lowercase.
- Expected output format: Update the table to have the names in title case.
- Key requirements and edge cases to consider: Handle names with multiple words and ensure the first letter of each word is capitalized.
- Example test cases with explanations: 
    - Input: `Names` table with `name` column containing "john smith" and "alice johnson".
    - Expected Output: `Names` table with `name` column updated to "John Smith" and "Alice Johnson".

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each character in the string to check for word boundaries.
- Step-by-step breakdown of the solution: 
    1. Select all names from the `Names` table.
    2. For each name, iterate over each character to find word boundaries (spaces).
    3. Capitalize the first letter of each word.
    4. Update the `Names` table with the formatted names.
- Why this approach comes to mind first: It's a straightforward, intuitive method for handling strings.

```cpp
#include <iostream>
#include <string>
using namespace std;

void fixNames(string& name) {
    bool capitalizeNext = true;
    for (char& c : name) {
        if (capitalizeNext) {
            c = toupper(c);
            capitalizeNext = false;
        }
        if (c == ' ') {
            capitalizeNext = true;
        } else {
            c = tolower(c);
        }
    }
}

int main() {
    string name = "john smith";
    fixNames(name);
    cout << name << endl;  // Outputs: "John Smith"
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of characters in all names. This is because we are iterating over each character once.
> - **Space Complexity:** $O(1)$, excluding the input and output, since we are modifying the string in-place.
> - **Why these complexities occur:** The linear time complexity comes from iterating over each character in the string, and the constant space complexity is due to not using any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize SQL's built-in string functions to capitalize the first letter of each word.
- Detailed breakdown of the approach: Use the `INITCAP` function in SQL to convert the first letter of each word to uppercase and the rest to lowercase.
- Proof of optimality: This is the most efficient solution as it leverages the database's native string manipulation capabilities, reducing the need for external processing.
- Why further optimization is impossible: This approach directly modifies the data within the database using optimized database functions, making it the most efficient method.

```sql
UPDATE Names
SET name = INITCAP(name);
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of rows in the table. This is because the database has to update each row.
> - **Space Complexity:** $O(1)$, since we're modifying the table in-place.
> - **Optimality proof:** This solution is optimal because it utilizes the database's optimized functions for string manipulation, minimizing the overhead of data transfer and processing.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: String manipulation and database query optimization.
- Problem-solving patterns identified: Leveraging built-in functions for efficiency.
- Optimization techniques learned: Using native database functions for data manipulation.
- Similar problems to practice: Other string manipulation and database query optimization challenges.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for null or empty strings.
- Edge cases to watch for: Handling names with punctuation or special characters.
- Performance pitfalls: Not using database indexes or optimized functions.
- Testing considerations: Ensure to test with a variety of names and edge cases.