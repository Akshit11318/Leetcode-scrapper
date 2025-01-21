## Subdomain Visit Count

**Problem Link:** https://leetcode.com/problems/subdomain-visit-count/description

**Problem Statement:**
- Input format: A list of strings `cpdomains` where each string represents a domain and its visit count.
- Constraints: The length of `cpdomains` will not exceed `100`.
- Expected output format: A list of strings where each string represents a subdomain and its visit count.
- Key requirements and edge cases to consider:
  - Subdomains are separated by dots (`.`).
  - The input list may contain duplicate subdomains with different visit counts.
- Example test cases with explanations:
  - Input: `["9001 discuss.leetcode.com"]`
    Output: `["9001 leetcode.com", "9001 discuss.leetcode.com"]`
  - Input: `["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]`
    Output: `["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each domain in `cpdomains`, split the domain into subdomains, and count the visits for each subdomain.
- Step-by-step breakdown of the solution:
  1. Split each domain into subdomains.
  2. Initialize a map to store the visit count for each subdomain.
  3. Iterate over each subdomain, increment its visit count in the map.
  4. Construct the output list from the map.
- Why this approach comes to mind first: It's straightforward to split the domains and count the visits.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <sstream>

vector<string> subdomainVisitCount(vector<string>& cpdomains) {
    map<string, int> subdomainCount;
    for (const auto& domain : cpdomains) {
        istringstream iss(domain);
        string countStr, domainStr;
        getline(iss, countStr, ' ');
        getline(iss, domainStr);
        int count = stoi(countStr);
        istringstream domainIss(domainStr);
        string subdomain;
        while (getline(domainIss, subdomain, '.')) {
            string fullSubdomain;
            if (!subdomain.empty()) {
                fullSubdomain = subdomain;
            }
            while (getline(domainIss, subdomain, '.')) {
                fullSubdomain = subdomain + "." + fullSubdomain;
                if (!subdomainCount.count(fullSubdomain)) {
                    subdomainCount[fullSubdomain] = 0;
                }
                subdomainCount[fullSubdomain] += count;
            }
            if (!subdomainCount.count(fullSubdomain)) {
                subdomainCount[fullSubdomain] = 0;
            }
            subdomainCount[fullSubdomain] += count;
        }
    }
    vector<string> result;
    for (const auto& pair : subdomainCount) {
        result.push_back(to_string(pair.second) + " " + pair.first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of domains and $m$ is the average number of subdomains per domain.
> - **Space Complexity:** $O(n \cdot m)$ for storing the subdomain visit counts.
> - **Why these complexities occur:** The nested loops over domains and subdomains cause the time complexity, and the map to store subdomain counts causes the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a more efficient data structure like `unordered_map` for storing subdomain counts, and iterate over the domains and subdomains more efficiently.
- Detailed breakdown of the approach:
  1. Split each domain into subdomains and iterate over them.
  2. Use an `unordered_map` to store the visit count for each subdomain.
  3. Construct the output list from the map.
- Proof of optimality: This approach has the same time complexity as the brute force approach but uses a more efficient data structure for storing subdomain counts.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <sstream>

vector<string> subdomainVisitCount(vector<string>& cpdomains) {
    unordered_map<string, int> subdomainCount;
    for (const auto& domain : cpdomains) {
        istringstream iss(domain);
        string countStr, domainStr;
        getline(iss, countStr, ' ');
        getline(iss, domainStr);
        int count = stoi(countStr);
        istringstream domainIss(domainStr);
        string subdomain;
        while (getline(domainIss, subdomain, '.')) {
            string fullSubdomain;
            if (!subdomain.empty()) {
                fullSubdomain = subdomain;
            }
            while (getline(domainIss, subdomain, '.')) {
                fullSubdomain = subdomain + "." + fullSubdomain;
                subdomainCount[fullSubdomain] += count;
            }
            subdomainCount[fullSubdomain] += count;
        }
    }
    vector<string> result;
    for (const auto& pair : subdomainCount) {
        result.push_back(to_string(pair.second) + " " + pair.first);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of domains and $m$ is the average number of subdomains per domain.
> - **Space Complexity:** $O(n \cdot m)$ for storing the subdomain visit counts.
> - **Optimality proof:** The use of an `unordered_map` reduces the constant factors in the time complexity, making this approach more efficient in practice.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration over domains and subdomains, use of maps to store visit counts.
- Problem-solving patterns identified: Splitting domains into subdomains, using efficient data structures for storing counts.
- Optimization techniques learned: Using `unordered_map` instead of `map` for storing subdomain counts.
- Similar problems to practice: Other problems involving domain and subdomain counting.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases like empty domains or subdomains.
- Edge cases to watch for: Duplicate subdomains with different visit counts.
- Performance pitfalls: Using inefficient data structures for storing subdomain counts.
- Testing considerations: Test with different input sizes and edge cases to ensure correctness and performance.