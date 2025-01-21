## Find Cutoff Score for Each School

**Problem Link:** https://leetcode.com/problems/find-cutoff-score-for-each-school/description

**Problem Statement:**
- Input format: `scores` - a 2D vector of integers where `scores[i][0]` is the student ID and `scores[i][1]` is the student's score, and `k` - an integer representing the number of top students to select.
- Expected output format: a vector of integers representing the cutoff score for each school.
- Key requirements and edge cases to consider: 
  - Handling cases where there are multiple students with the same score.
  - Ensuring that the cutoff score is the minimum score that can be achieved by the top `k` students.
- Example test cases with explanations:
  - For example, if `scores = [[1,91],[1,92],[2,93],[2,99],[5,60],[5,70],[1,82],[2,81],[1,77]]` and `k = 3`, the output should be `[82,81,70]`.

### Brute Force Approach

**Explanation:**
- Initial thought process: First, we need to group the scores by school and then sort them in descending order. After that, we can find the cutoff score for each school by selecting the `k`th highest score.
- Step-by-step breakdown of the solution:
  1. Group the scores by school.
  2. Sort the scores for each school in descending order.
  3. Find the `k`th highest score for each school.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves grouping the scores, sorting them, and then selecting the `k`th highest score.

```cpp
vector<int> findCutoffScore(vector<vector<int>>& scores, int k) {
    unordered_map<int, vector<int>> schoolScores;
    for (auto& score : scores) {
        schoolScores[score[0]].push_back(score[1]);
    }
    
    vector<int> cutoffScores;
    for (auto& school : schoolScores) {
        sort(school.second.rbegin(), school.second.rend());
        cutoffScores.push_back(school.second[k - 1]);
    }
    
    return cutoffScores;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of students in a school, because we are sorting the scores for each school.
> - **Space Complexity:** $O(n)$ where $n$ is the total number of students, because we are storing the scores for each school in a separate vector.
> - **Why these complexities occur:** The time complexity occurs because we are sorting the scores for each school, and the space complexity occurs because we are storing the scores for each school in a separate vector.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a multiset to store the scores for each school and then use the `k`th element of the multiset as the cutoff score.
- Detailed breakdown of the approach:
  1. Group the scores by school using an unordered_map.
  2. For each school, use a multiset to store the scores.
  3. Use the `k`th element of the multiset as the cutoff score.
- Proof of optimality: This approach is optimal because it uses a multiset to store the scores, which allows us to find the `k`th highest score in $O(\log n)$ time.

```cpp
vector<int> findCutoffScore(vector<vector<int>>& scores, int k) {
    unordered_map<int, multiset<int>> schoolScores;
    for (auto& score : scores) {
        schoolScores[score[0]].insert(score[1]);
    }
    
    vector<int> cutoffScores;
    for (auto& school : schoolScores) {
        auto it = school.second.rbegin();
        for (int i = 0; i < k - 1; i++) {
            it++;
        }
        cutoffScores.push_back(*it);
    }
    
    return cutoffScores;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ where $n$ is the number of students in a school, because we are inserting scores into the multiset.
> - **Space Complexity:** $O(n)$ where $n$ is the total number of students, because we are storing the scores for each school in a separate multiset.
> - **Optimality proof:** This approach is optimal because it uses a multiset to store the scores, which allows us to find the `k`th highest score in $O(\log n)$ time.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a multiset to store scores and finding the `k`th highest score.
- Problem-solving patterns identified: Grouping scores by school and using a data structure to store scores.
- Optimization techniques learned: Using a multiset to reduce the time complexity of finding the `k`th highest score.
- Similar problems to practice: Finding the top `k` elements in an array, finding the median of an array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not using the correct data structure.
- Edge cases to watch for: Handling cases where there are multiple students with the same score.
- Performance pitfalls: Using a data structure that has a high time complexity for inserting or finding elements.
- Testing considerations: Testing the code with different inputs and edge cases.