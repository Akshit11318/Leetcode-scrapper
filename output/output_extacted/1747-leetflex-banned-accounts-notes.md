## Leetflex Banned Accounts
**Problem Link:** https://leetcode.com/problems/leetflex-banned-accounts/description

**Problem Statement:**
- Input format: A list of strings representing the accounts, where each string contains two space-separated values: the username and the email.
- Constraints: Each account is represented as a string in the format "username email".
- Expected output format: The number of banned accounts.
- Key requirements and edge cases to consider: 
    - A banned account is one that shares the same username or email with another account.
    - The accounts list can contain duplicate accounts.
- Example test cases with explanations:
    - Example 1:
        - Input: ["john smith", "john newyork", "john newyork"]
        - Output: 2
        - Explanation: The accounts with usernames "john" and emails "smith" and "newyork" are banned because they share the same username.
    - Example 2:
        - Input: ["mary key", "mary key", "john key"]
        - Output: 2
        - Explanation: The accounts with usernames "mary" and emails "key" are banned because they share the same email.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each account with every other account to check for shared usernames or emails.
- Step-by-step breakdown of the solution:
    1. Iterate through each account in the list.
    2. For each account, iterate through the remaining accounts in the list.
    3. Check if the usernames or emails of the two accounts are the same.
    4. If they are the same, increment the count of banned accounts.
- Why this approach comes to mind first: It is a straightforward and intuitive approach to compare each account with every other account.

```cpp
int countBannedAccounts(vector<string>& accounts) {
    int bannedCount = 0;
    unordered_set<string> bannedUsernames;
    unordered_set<string> bannedEmails;

    for (int i = 0; i < accounts.size(); i++) {
        string username, email;
        stringstream ss(accounts[i]);
        ss >> username >> email;

        if (bannedUsernames.find(username) != bannedUsernames.end() || 
            bannedEmails.find(email) != bannedEmails.end()) {
            bannedCount++;
        } else {
            bannedUsernames.insert(username);
            bannedEmails.insert(email);
        }
    }

    return bannedCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of accounts. This is because we are iterating through each account and then iterating through the remaining accounts.
> - **Space Complexity:** $O(n)$, where $n$ is the number of accounts. This is because we are storing the banned usernames and emails in sets.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops, and the space complexity occurs because of the sets used to store the banned usernames and emails.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a set to store the banned usernames and emails, and then iterate through the accounts only once.
- Detailed breakdown of the approach:
    1. Initialize two sets to store the banned usernames and emails.
    2. Iterate through each account in the list.
    3. For each account, check if the username or email is already in the sets of banned usernames or emails.
    4. If it is, increment the count of banned accounts.
    5. Otherwise, add the username and email to the sets of banned usernames and emails.
- Proof of optimality: This approach is optimal because it only requires a single pass through the list of accounts, resulting in a time complexity of $O(n)$.

```cpp
int countBannedAccounts(vector<string>& accounts) {
    int bannedCount = 0;
    unordered_set<string> bannedUsernames;
    unordered_set<string> bannedEmails;

    for (int i = 0; i < accounts.size(); i++) {
        string username, email;
        stringstream ss(accounts[i]);
        ss >> username >> email;

        if (bannedUsernames.find(username) != bannedUsernames.end() || 
            bannedEmails.find(email) != bannedEmails.end()) {
            bannedCount++;
        } else {
            bannedUsernames.insert(username);
            bannedEmails.insert(email);
        }
    }

    return bannedCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of accounts. This is because we are iterating through each account only once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of accounts. This is because we are storing the banned usernames and emails in sets.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the list of accounts, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using sets to store banned usernames and emails, and iterating through the accounts only once.
- Problem-solving patterns identified: Checking for shared usernames or emails, and using sets to keep track of banned accounts.
- Optimization techniques learned: Reducing the time complexity from $O(n^2)$ to $O(n)$ by iterating through the accounts only once.
- Similar problems to practice: Other problems that involve checking for shared values or using sets to keep track of banned items.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for shared usernames or emails correctly, or not using sets to keep track of banned accounts.
- Edge cases to watch for: Duplicate accounts, or accounts with the same username or email.
- Performance pitfalls: Using nested loops to iterate through the accounts, resulting in a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different inputs, including edge cases and large inputs.