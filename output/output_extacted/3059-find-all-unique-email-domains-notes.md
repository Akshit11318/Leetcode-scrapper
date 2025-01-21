## Find All Unique Email Domains
**Problem Link:** https://leetcode.com/problems/find-all-unique-email-domains/description

**Problem Statement:**
- Input: A list of email addresses.
- Constraints: The input list is non-empty and contains only strings representing email addresses.
- Expected Output: A list of unique email domains.
- Key Requirements: Extract the domain from each email address and return a list of unique domains.
- Edge Cases: Consider email addresses with subdomains, local parts with special characters, and varying domain extensions.

**Example Test Cases:**
- Input: `["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]`
- Output: `["leetcode.com","lee.tcode.com","gmail.com"]`
- Explanation: Extract the domain from each email address and return a list of unique domains.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate over each email address, extract the domain, and add it to a list if it's not already present.
- This approach involves string manipulation to extract the domain from each email address.
- It comes to mind first because it's straightforward and easy to implement.

```cpp
vector<string> uniqueEmailDomains(vector<string>& emails) {
    set<string> uniqueDomains;
    for (const string& email : emails) {
        // Find the index of the '@' symbol to extract the domain
        size_t atIndex = email.find('@');
        string domain = email.substr(atIndex + 1);
        uniqueDomains.insert(domain);
    }
    vector<string> result(uniqueDomains.begin(), uniqueDomains.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of email addresses and $M$ is the maximum length of an email address. This is because we're iterating over each email address and performing string operations.
> - **Space Complexity:** $O(N \cdot M)$, as we're storing the unique domains in a set. In the worst case, all email addresses could have unique domains.
> - **Why these complexities occur:** The time complexity is due to the iteration over each email address and the string operations to extract the domain. The space complexity is due to storing the unique domains in a set.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use the same approach as the brute force, but with minor optimizations.
- We can use the `std::unordered_set` instead of `std::set` for storing unique domains, as it provides faster lookup and insertion operations.
- We can also use `std::string::find` and `std::string::substr` to extract the domain from each email address.

```cpp
vector<string> uniqueEmailDomains(vector<string>& emails) {
    unordered_set<string> uniqueDomains;
    for (const string& email : emails) {
        // Find the index of the '@' symbol to extract the domain
        size_t atIndex = email.find('@');
        string domain = email.substr(atIndex + 1);
        uniqueDomains.insert(domain);
    }
    vector<string> result(uniqueDomains.begin(), uniqueDomains.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M)$, where $N$ is the number of email addresses and $M$ is the maximum length of an email address. This is because we're iterating over each email address and performing string operations.
> - **Space Complexity:** $O(N \cdot M)$, as we're storing the unique domains in a set. In the worst case, all email addresses could have unique domains.
> - **Optimality proof:** This is the optimal approach because we must iterate over each email address to extract the domain, and we must store the unique domains in a data structure. The use of `std::unordered_set` provides the fastest lookup and insertion operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string manipulation, set operations, and iteration over a list of strings.
- Problem-solving patterns identified: extracting relevant information from a list of strings and storing unique values in a set.
- Optimization techniques learned: using `std::unordered_set` for faster lookup and insertion operations.

**Mistakes to Avoid:**
- Common implementation errors: not checking for the presence of the '@' symbol in each email address, not handling edge cases with subdomains or special characters.
- Edge cases to watch for: email addresses with subdomains, local parts with special characters, and varying domain extensions.
- Performance pitfalls: using `std::set` instead of `std::unordered_set` for storing unique domains, which can lead to slower lookup and insertion operations.
- Testing considerations: testing the function with a variety of email addresses, including edge cases and different domain extensions.