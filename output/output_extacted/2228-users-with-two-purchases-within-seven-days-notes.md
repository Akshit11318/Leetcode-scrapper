## Users With Two Purchases Within Seven Days

**Problem Link:** https://leetcode.com/problems/users-with-two-purchases-within-seven-days/description

**Problem Statement:**
- Input: A table `Purchases` with columns `id`, `user_id`, and `purchase_date`.
- Constraints: The table contains information about purchases made by users.
- Expected output: A list of `user_id`s who made two purchases within seven days.
- Key requirements and edge cases to consider:
  - Handling duplicate user IDs.
  - Ensuring the date range for the second purchase is within seven days of the first purchase.
- Example test cases with explanations:
  - A user with two purchases on consecutive days.
  - A user with multiple purchases, but none within seven days of each other.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over each user's purchases and check for any pair of purchases within seven days.
- Step-by-step breakdown of the solution:
  1. Group purchases by `user_id`.
  2. For each user, iterate over their purchases and compare each pair of purchases.
  3. Check if the difference between the two purchase dates is less than or equal to seven days.
- Why this approach comes to mind first: It directly addresses the problem statement by checking all possible pairs of purchases for each user.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <ctime>

struct Purchase {
    int id;
    int user_id;
    time_t purchase_date;
};

std::vector<int> usersWithTwoPurchasesWithinSevenDays(std::vector<Purchase>& purchases) {
    std::unordered_map<int, std::vector<time_t>> userPurchases;
    for (const auto& purchase : purchases) {
        userPurchases[purchase.user_id].push_back(purchase.purchase_date);
    }

    std::set<int> result;
    for (const auto& pair : userPurchases) {
        std::vector<time_t> dates = pair.second;
        for (size_t i = 0; i < dates.size(); ++i) {
            for (size_t j = i + 1; j < dates.size(); ++j) {
                double diff = difftime(dates[j], dates[i]);
                if (diff <= 604800) { // 604800 seconds in 7 days
                    result.insert(pair.first);
                    break;
                }
            }
            if (result.find(pair.first) != result.end()) break;
        }
    }

    std::vector<int> userIds(result.begin(), result.end());
    return userIds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$ where $n$ is the average number of purchases per user and $m$ is the number of users. This is because for each user, we potentially compare each purchase with every other purchase.
> - **Space Complexity:** $O(n \cdot m)$ for storing the purchases grouped by user.
> - **Why these complexities occur:** The nested loops over purchases for each user lead to the quadratic time complexity, and storing purchases for each user results in the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Instead of comparing all pairs of purchases for each user, we can sort the purchases by date and then check for any purchase that is within seven days of the previous one.
- Detailed breakdown of the approach:
  1. Group purchases by `user_id`.
  2. For each user, sort their purchases by `purchase_date`.
  3. Iterate over the sorted purchases and check if the current purchase is within seven days of the previous one.
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the comparison of all pairs of purchases, making it more efficient for large datasets.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
#include <ctime>
#include <algorithm>

struct Purchase {
    int id;
    int user_id;
    time_t purchase_date;
};

bool comparePurchases(const Purchase& a, const Purchase& b) {
    return a.purchase_date < b.purchase_date;
}

std::vector<int> usersWithTwoPurchasesWithinSevenDays(std::vector<Purchase>& purchases) {
    std::unordered_map<int, std::vector<Purchase>> userPurchases;
    for (const auto& purchase : purchases) {
        userPurchases[purchase.user_id].push_back(purchase);
    }

    std::set<int> result;
    for (auto& pair : userPurchases) {
        std::vector<Purchase>& purchases = pair.second;
        std::sort(purchases.begin(), purchases.end(), comparePurchases);
        for (size_t i = 0; i < purchases.size() - 1; ++i) {
            double diff = difftime(purchases[i + 1].purchase_date, purchases[i].purchase_date);
            if (diff <= 604800) { // 604800 seconds in 7 days
                result.insert(pair.first);
                break;
            }
        }
    }

    std::vector<int> userIds(result.begin(), result.end());
    return userIds;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot log(n))$ where $n$ is the average number of purchases per user and $m$ is the number of users. The sorting step dominates the complexity.
> - **Space Complexity:** $O(n \cdot m)$ for storing the purchases grouped by user.
> - **Optimality proof:** This approach is optimal because it minimizes the number of comparisons needed to find purchases within seven days of each other, by leveraging the efficiency of sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, grouping, and efficient comparison techniques.
- Problem-solving patterns identified: Reducing comparison complexity through sorting.
- Optimization techniques learned: Avoiding unnecessary comparisons by sorting data.
- Similar problems to practice: Other problems involving temporal relationships or efficient comparison techniques.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as duplicate user IDs or empty purchase lists.
- Edge cases to watch for: Users with no purchases, or purchases with identical dates.
- Performance pitfalls: Using inefficient algorithms for large datasets.
- Testing considerations: Thoroughly testing with various input scenarios, including edge cases.