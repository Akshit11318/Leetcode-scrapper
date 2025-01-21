## Sort the Olympic Table
**Problem Link:** https://leetcode.com/problems/sort-the-olympic-table/description

**Problem Statement:**
- Input format: A 2D array `score` where `score[i][0]` is the country name and `score[i][1]`, `score[i][2]`, and `score[i][3]` are the gold, silver, and bronze medal counts, respectively.
- Expected output format: A sorted list of country names based on the number of gold medals in descending order, then the number of silver medals in descending order, and finally the number of bronze medals in descending order.
- Key requirements and edge cases to consider: Handling ties in medal counts, ensuring countries with no medals are placed at the end.
- Example test cases with explanations:
  - `score = [["USA",3,0,1],["Sweden",2,0,0]]`: The USA has more gold medals than Sweden, so the USA should be ranked first.
  - `score = [["USA",3,0,1],["Sweden",2,1,0]]`: The USA has more gold medals than Sweden, so the USA should be ranked first.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Sort the countries based on the number of gold medals, then the number of silver medals, and finally the number of bronze medals.
- Step-by-step breakdown of the solution:
  1. Create a custom comparator function that compares two countries based on the number of gold, silver, and bronze medals.
  2. Use a sorting algorithm (e.g., quicksort, mergesort) to sort the countries based on the custom comparator.
  3. Return the sorted list of country names.

```cpp
#include <vector>
#include <string>
#include <algorithm>

vector<string> sortOlympicTable(vector<vector<int>>& score) {
    vector<pair<string, vector<int>>> countryScores;
    for (auto& country : score) {
        string name = to_string(country[0]);
        vector<int> medals = {country[1], country[2], country[3]};
        countryScores.emplace_back(name, medals);
    }

    sort(countryScores.begin(), countryScores.end(), [](const auto& a, const auto& b) {
        if (a.second[0] != b.second[0]) return a.second[0] > b.second[0];
        if (a.second[1] != b.second[1]) return a.second[1] > b.second[1];
        return a.second[2] > b.second[2];
    });

    vector<string> result;
    for (auto& country : countryScores) {
        result.push_back(to_string(stoi(country.first)));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of countries.
> - **Space Complexity:** $O(n)$ for storing the country scores and the sorted result.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is due to the additional memory needed to store the country scores and the sorted result.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a lambda function as the custom comparator for the `sort` algorithm.
- Detailed breakdown of the approach:
  1. Create a lambda function that compares two countries based on the number of gold, silver, and bronze medals.
  2. Use the `sort` algorithm to sort the countries based on the lambda comparator.
  3. Return the sorted list of country names.
- Proof of optimality: This approach has the same time complexity as the brute force approach but with improved code readability and conciseness.

```cpp
#include <vector>
#include <string>
#include <algorithm>

vector<string> sortOlympicTable(vector<vector<int>>& score) {
    sort(score.begin(), score.end(), [](const auto& a, const auto& b) {
        if (a[1] != b[1]) return a[1] > b[1];
        if (a[2] != b[2]) return a[2] > b[2];
        return a[3] > b[3];
    });

    vector<string> result;
    for (auto& country : score) {
        result.push_back(to_string(country[0]));
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of countries.
> - **Space Complexity:** $O(n)$ for storing the sorted result.
> - **Optimality proof:** This approach has the same time complexity as the brute force approach but with improved code readability and conciseness.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Custom comparators, sorting algorithms.
- Problem-solving patterns identified: Using lambda functions to simplify code.
- Optimization techniques learned: Improving code readability and conciseness.
- Similar problems to practice: Sorting problems with custom comparators.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly implementing the custom comparator.
- Edge cases to watch for: Handling ties in medal counts.
- Performance pitfalls: Using inefficient sorting algorithms.
- Testing considerations: Verifying the correctness of the sorting result.