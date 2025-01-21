## Queries Quality and Percentage
**Problem Link:** https://leetcode.com/problems/queries-quality-and-percentage/description

**Problem Statement:**
- Input format and constraints: Given a list of queries, each query contains three parameters: `query_name`, `preferred_languages`, and `score`. The goal is to calculate the quality and percentage of each query based on the given parameters.
- Expected output format: The output should be a list of queries with their calculated quality and percentage.
- Key requirements and edge cases to consider: The quality of a query is determined by its score and the number of preferred languages. The percentage is calculated based on the quality and the total number of queries.
- Example test cases with explanations: For example, if we have two queries with scores 10 and 20, and preferred languages 2 and 3 respectively, the quality of the first query will be 10 * 2 = 20 and the quality of the second query will be 20 * 3 = 60.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to calculate the quality and percentage of each query by iterating over the list of queries and applying the given formulas.
- Step-by-step breakdown of the solution: 
  1. Initialize an empty list to store the results.
  2. Iterate over the list of queries.
  3. For each query, calculate the quality by multiplying the score with the number of preferred languages.
  4. Calculate the total quality by summing up the qualities of all queries.
  5. Calculate the percentage of each query by dividing its quality by the total quality and multiplying by 100.
  6. Append the query with its calculated quality and percentage to the result list.
- Why this approach comes to mind first: This approach is straightforward and directly applies the given formulas to calculate the quality and percentage of each query.

```cpp
#include <iostream>
#include <vector>

struct Query {
    std::string query_name;
    int preferred_languages;
    int score;
    int quality;
    double percentage;
};

std::vector<Query> calculateQualityAndPercentage(std::vector<Query>& queries) {
    int totalQuality = 0;
    for (auto& query : queries) {
        query.quality = query.score * query.preferred_languages;
        totalQuality += query.quality;
    }

    for (auto& query : queries) {
        query.percentage = (query.quality / (double)totalQuality) * 100;
    }

    return queries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of queries. This is because we iterate over the list of queries twice: once to calculate the quality and once to calculate the percentage.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output. This is because we only use a constant amount of space to store the total quality.
> - **Why these complexities occur:** The time complexity occurs because we iterate over the list of queries twice. The space complexity occurs because we only use a constant amount of space to store the total quality.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can calculate the quality and percentage of each query in a single pass by maintaining a running total of the qualities.
- Detailed breakdown of the approach: 
  1. Initialize an empty list to store the results.
  2. Initialize a variable to store the total quality.
  3. Iterate over the list of queries.
  4. For each query, calculate the quality by multiplying the score with the number of preferred languages.
  5. Add the quality to the total quality.
  6. Calculate the percentage of the query by dividing its quality by the total quality and multiplying by 100.
  7. Append the query with its calculated quality and percentage to the result list.
- Proof of optimality: This approach is optimal because it only requires a single pass over the list of queries, resulting in a time complexity of $O(n)$.
- Why further optimization is impossible: Further optimization is impossible because we must at least read the input once, resulting in a time complexity of at least $O(n)$.

```cpp
#include <iostream>
#include <vector>

struct Query {
    std::string query_name;
    int preferred_languages;
    int score;
    int quality;
    double percentage;
};

std::vector<Query> calculateQualityAndPercentage(std::vector<Query>& queries) {
    int totalQuality = 0;
    for (auto& query : queries) {
        query.quality = query.score * query.preferred_languages;
        totalQuality += query.quality;
        query.percentage = (query.quality / (double)totalQuality) * 100;
    }

    return queries;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of queries. This is because we only iterate over the list of queries once.
> - **Space Complexity:** $O(1)$, excluding the space required for the input and output. This is because we only use a constant amount of space to store the total quality.
> - **Optimality proof:** This approach is optimal because it only requires a single pass over the list of queries, resulting in a time complexity of $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the concept of iterating over a list of queries and applying formulas to calculate the quality and percentage of each query.
- Problem-solving patterns identified: The problem identifies the pattern of calculating a running total and using it to calculate percentages.
- Optimization techniques learned: The problem teaches the optimization technique of reducing the number of passes over the input data.
- Similar problems to practice: Similar problems to practice include calculating statistics such as mean, median, and standard deviation.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to initialize the total quality variable.
- Edge cases to watch for: An edge case to watch for is when the list of queries is empty.
- Performance pitfalls: A performance pitfall is to use a nested loop to calculate the quality and percentage of each query, resulting in a time complexity of $O(n^2)$.
- Testing considerations: A testing consideration is to test the function with an empty list of queries and verify that it returns an empty list.