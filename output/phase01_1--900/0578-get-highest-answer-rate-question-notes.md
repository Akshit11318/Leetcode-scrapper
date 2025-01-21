## Get Highest Answer Rate Question

**Problem Link:** https://leetcode.com/problems/get-highest-answer-rate-question/description

**Problem Statement:**
- Input format and constraints: The problem provides a 2D array `questions` where each sub-array contains an integer `question_id` and a boolean `is_bookmarked`. It also provides an integer `category_id` and a boolean `difficulty`. The goal is to find the `question_id` with the highest answer rate for the given `category_id` and `difficulty`.
- Expected output format: The output should be a single integer representing the `question_id` with the highest answer rate.
- Key requirements and edge cases to consider: The problem requires handling cases where there are multiple `question_id`s with the same highest answer rate. In such cases, the output should be the smallest `question_id`.
- Example test cases with explanations:
  - Example 1: `questions = [[1, true], [2, false], [3, true], [4, true], [5, false]]`, `category_id = 1`, `difficulty = true`. The output should be `1` because it has the highest answer rate for the given `category_id` and `difficulty`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating over each question in the `questions` array and checking if it matches the given `category_id` and `difficulty`. For each matching question, we calculate the answer rate by checking the `is_bookmarked` status.
- Step-by-step breakdown of the solution:
  1. Initialize variables to store the maximum answer rate and the corresponding `question_id`.
  2. Iterate over each question in the `questions` array.
  3. For each question, check if it matches the given `category_id` and `difficulty`.
  4. If a match is found, calculate the answer rate by checking the `is_bookmarked` status.
  5. Update the maximum answer rate and the corresponding `question_id` if a higher answer rate is found.
- Why this approach comes to mind first: The brute force approach is straightforward and easy to implement. However, it may not be efficient for large inputs.

```cpp
int getHighestAnswerRateQuestion(vector<vector<int>>& questions, int category_id, bool difficulty) {
    int maxAnswerRate = 0;
    int maxAnswerRateQuestionId = -1;
    
    for (auto& question : questions) {
        int questionId = question[0];
        bool isBookmarked = question[1];
        
        // Calculate answer rate
        int answerRate = isBookmarked ? 1 : 0;
        
        // Update max answer rate and question id
        if (answerRate > maxAnswerRate) {
            maxAnswerRate = answerRate;
            maxAnswerRateQuestionId = questionId;
        } else if (answerRate == maxAnswerRate && questionId < maxAnswerRateQuestionId) {
            maxAnswerRateQuestionId = questionId;
        }
    }
    
    return maxAnswerRateQuestionId;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of questions. This is because we iterate over each question in the `questions` array once.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum answer rate and the corresponding `question_id`.
> - **Why these complexities occur:** The time complexity is linear because we perform a single pass over the input data. The space complexity is constant because we only use a fixed amount of space to store the maximum answer rate and the corresponding `question_id`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using a hash map to store the answer rates for each question. This allows us to efficiently look up and update the answer rates for each question.
- Detailed breakdown of the approach:
  1. Initialize a hash map to store the answer rates for each question.
  2. Iterate over each question in the `questions` array.
  3. For each question, check if it matches the given `category_id` and `difficulty`.
  4. If a match is found, update the answer rate for the question in the hash map.
  5. Find the question with the maximum answer rate in the hash map.
- Proof of optimality: The optimal solution has a time complexity of $O(n)$, which is the best possible time complexity for this problem. This is because we must iterate over each question in the `questions` array at least once to calculate the answer rates.

```cpp
int getHighestAnswerRateQuestion(vector<vector<int>>& questions, int category_id, bool difficulty) {
    unordered_map<int, int> answerRates;
    
    for (auto& question : questions) {
        int questionId = question[0];
        bool isBookmarked = question[1];
        
        // Update answer rate
        if (isBookmarked) {
            answerRates[questionId]++;
        }
    }
    
    int maxAnswerRate = 0;
    int maxAnswerRateQuestionId = -1;
    
    for (auto& pair : answerRates) {
        int questionId = pair.first;
        int answerRate = pair.second;
        
        // Update max answer rate and question id
        if (answerRate > maxAnswerRate) {
            maxAnswerRate = answerRate;
            maxAnswerRateQuestionId = questionId;
        } else if (answerRate == maxAnswerRate && questionId < maxAnswerRateQuestionId) {
            maxAnswerRateQuestionId = questionId;
        }
    }
    
    return maxAnswerRateQuestionId;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of questions. This is because we iterate over each question in the `questions` array once and then iterate over the hash map once.
> - **Space Complexity:** $O(n)$, as we use a hash map to store the answer rates for each question.
> - **Optimality proof:** The optimal solution has a time complexity of $O(n)$, which is the best possible time complexity for this problem. This is because we must iterate over each question in the `questions` array at least once to calculate the answer rates.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of hash maps to efficiently store and look up data.
- Problem-solving patterns identified: The problem requires iterating over each question in the `questions` array and updating the answer rates for each question.
- Optimization techniques learned: The optimal solution uses a hash map to store the answer rates for each question, which allows for efficient lookups and updates.
- Similar problems to practice: Similar problems include finding the maximum or minimum value in an array, or finding the most frequent element in an array.

**Mistakes to Avoid:**
- Common implementation errors: A common mistake is to forget to update the answer rate for each question in the hash map.
- Edge cases to watch for: An edge case is when there are multiple questions with the same maximum answer rate. In this case, the output should be the smallest question ID.
- Performance pitfalls: A performance pitfall is to use a nested loop to iterate over each question in the `questions` array, which would result in a time complexity of $O(n^2)$.