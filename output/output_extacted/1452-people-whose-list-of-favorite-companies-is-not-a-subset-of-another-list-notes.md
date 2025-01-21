## People Whose List of Favorite Companies Is Not a Subset of Another List

**Problem Link:** https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/description

**Problem Statement:**
- Input format and constraints: The input is a 2D list `list` where each inner list represents the list of favorite companies for a person. The task is to find the people whose list of favorite companies is not a subset of another person's list.
- Expected output format: The output should be a list of indices of people whose list of favorite companies is not a subset of another person's list.
- Key requirements and edge cases to consider: A subset is defined as a list where every element is also present in another list. The input list can contain duplicate inner lists, but the output should not contain duplicate indices.
- Example test cases with explanations:
  - Input: `list = [["leetcode"],["google"],["facebook"],["amazon"]]`
    Output: `[0, 1, 2, 3]`
  - Input: `list = [["leetcode"],["leetcode"]]`
    Output: `[1]`
  - Input: `list = [["Amazon", "Microsoft", "Google"]], ["Google", "Microsoft"]`
    Output: `[0]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to compare each person's list of favorite companies with every other person's list to check if it is a subset.
- Step-by-step breakdown of the solution:
  1. Iterate over each person's list of favorite companies.
  2. For each person, iterate over every other person's list.
  3. Check if the current person's list is a subset of the other person's list.
  4. If it is not a subset of any other list, add the person's index to the result list.
- Why this approach comes to mind first: It is a straightforward and intuitive solution that directly addresses the problem statement.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

vector<int> peopleIndexes(vector<vector<string>>& list) {
    vector<int> result;
    for (int i = 0; i < list.size(); i++) {
        bool isSubset = false;
        for (int j = 0; j < list.size(); j++) {
            if (i == j) continue;
            unordered_set<string> otherList(list[j].begin(), list[j].end());
            bool subset = true;
            for (const string& company : list[i]) {
                if (otherList.find(company) == otherList.end()) {
                    subset = false;
                    break;
                }
            }
            if (subset) {
                isSubset = true;
                break;
            }
        }
        if (!isSubset) result.push_back(i);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the number of people and $m$ is the maximum number of favorite companies a person can have. This is because for each person, we are potentially checking against every other person's list.
> - **Space Complexity:** $O(n \cdot m)$ for storing the result and the sets used for subset checks.
> - **Why these complexities occur:** The nested loops over the people and their favorite companies lead to the quadratic time complexity, while the space complexity comes from storing the result and the sets used for efficient lookups.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking for subsets by iterating over each list, we can use a more efficient data structure like `unordered_set` to store each person's favorite companies. This allows for constant time complexity when checking if a company is in another person's list.
- Detailed breakdown of the approach:
  1. Convert each list of favorite companies into an `unordered_set` for efficient lookups.
  2. Iterate over each person's set of favorite companies.
  3. For each person, iterate over every other person's set.
  4. Check if the current person's set is a subset of the other person's set by verifying that every company in the current person's set is also in the other person's set.
  5. If it is not a subset of any other set, add the person's index to the result list.
- Proof of optimality: This approach is optimal because it minimizes the number of operations required to check for subsets by utilizing the constant time complexity of `unordered_set` lookups.

```cpp
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

vector<int> peopleIndexes(vector<vector<string>>& list) {
    vector<int> result;
    vector<unordered_set<string>> sets;
    for (const auto& l : list) {
        sets.emplace_back(l.begin(), l.end());
    }
    for (int i = 0; i < sets.size(); i++) {
        bool isSubset = false;
        for (int j = 0; j < sets.size(); j++) {
            if (i == j) continue;
            if (includes(sets[j].begin(), sets[j].end(), sets[i].begin(), sets[i].end())) {
                isSubset = true;
                break;
            }
        }
        if (!isSubset) result.push_back(i);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the number of people and $m$ is the maximum number of favorite companies a person can have. Although the time complexity appears the same as the brute force approach, the use of `unordered_set` significantly improves the constant factors due to faster lookup times.
> - **Space Complexity:** $O(n \cdot m)$ for storing the sets and the result.
> - **Optimality proof:** This is the optimal approach because it leverages the most efficient data structure for subset checks, minimizing the time complexity of these operations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Efficient use of `unordered_set` for fast lookups and subset checks.
- Problem-solving patterns identified: Converting lists to sets for efficient operations, iterating over sets to check for subsets.
- Optimization techniques learned: Using data structures that minimize operation time complexities.
- Similar problems to practice: Other problems involving subset checks or efficient lookups.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as empty lists or duplicate inner lists.
- Edge cases to watch for: Lists with duplicate companies, lists with no companies.
- Performance pitfalls: Using inefficient data structures for subset checks.
- Testing considerations: Thoroughly testing with various input sizes and edge cases to ensure correctness and efficiency.