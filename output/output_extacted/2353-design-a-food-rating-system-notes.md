## Food Rating System
**Problem Link:** https://leetcode.com/problems/design-a-food-rating-system/description

**Problem Statement:**
- Input format and constraints: The system will have a list of `Food` objects with `id`, `name`, and `cuisine`, and a list of `Restaurant` objects with `id`, `name`, and a list of `Food` objects. The system will also receive a list of ratings for each food item.
- Expected output format: The system should return a list of food items with their corresponding ratings.
- Key requirements and edge cases to consider: The system should be able to handle a large number of food items and restaurants, and it should be able to update the ratings of food items in real-time.
- Example test cases with explanations:
  - Example 1:
    - Input: `foods = [["1","Pizza","Italian"],["2","Sushi","Japanese"],["3","Tacos","Mexican"]], restaurants = [["1","The Town Hall","1"],["2","Eddies Diner","2"],["3","The Grill Bar","3"]]`
    - Output: `["The Town Hall","Eddies Diner","The Grill Bar"]`
  - Example 2:
    - Input: `foods = [["1","Pizza","Italian"],["2","Sushi","Japanese"],["3","Tacos","Mexican"]], restaurants = [["1","The Town Hall","1"],["2","Eddies Diner","2"],["3","The Grill Bar","3"]], updates = [["1","5"],["2","4"],["3","5"]]`
    - Output: `["The Grill Bar","The Town Hall","Eddies Diner"]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a data structure to store the food items and their corresponding ratings. Update the ratings of food items based on the input updates.
- Step-by-step breakdown of the solution:
  1. Create a map to store the food items and their corresponding ratings.
  2. Create a map to store the restaurants and their corresponding food items.
  3. Update the ratings of food items based on the input updates.
  4. Sort the food items based on their ratings and cuisines.
- Why this approach comes to mind first: This approach is straightforward and easy to implement.

```cpp
class FoodRating {
public:
    unordered_map<string, vector<string>> cuisine_to_food;
    unordered_map<string, pair<string, int>> food_to_cuisine_rating;

    FoodRating(vector<string>& foods, vector<string>& cuisines, vector<string>& ratings) {
        for (int i = 0; i < foods.size(); i++) {
            cuisine_to_food[cuisines[i]].push_back(foods[i]);
            food_to_cuisine_rating[foods[i]] = {cuisines[i], ratings[i] - '0'};
        }
    }

    void changeRating(string food, int newRating) {
        food_to_cuisine_rating[food].second = newRating;
    }

    string highestRated(string cuisine) {
        string max_food = "";
        int max_rating = 0;
        for (const auto& food : cuisine_to_food[cuisine]) {
            if (food_to_cuisine_rating[food].second > max_rating) {
                max_rating = food_to_cuisine_rating[food].second;
                max_food = food;
            } else if (food_to_cuisine_rating[food].second == max_rating) {
                if (food < max_food) {
                    max_food = food;
                }
            }
        }
        return max_food;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of food items. The `changeRating` function takes $O(1)$ time, and the `highestRated` function takes $O(n)$ time in the worst case.
> - **Space Complexity:** $O(n)$, where $n$ is the number of food items. We need to store the food items and their corresponding ratings in the `cuisine_to_food` and `food_to_cuisine_rating` maps.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate over all food items to update their ratings and to find the highest rated food item in a cuisine. The space complexity occurs because we need to store the food items and their corresponding ratings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a set to store the food items in each cuisine, and use a multiset to store the food items and their corresponding ratings.
- Detailed breakdown of the approach:
  1. Create a map to store the food items and their corresponding ratings.
  2. Create a map to store the restaurants and their corresponding food items.
  3. Create a map to store the cuisines and their corresponding food items.
  4. Update the ratings of food items based on the input updates.
  5. Sort the food items based on their ratings and cuisines.
- Why further optimization is impossible: This approach has the best possible time and space complexity.

```cpp
class FoodRating {
public:
    unordered_map<string, string> food_to_cuisine;
    unordered_map<string, int> food_to_rating;
    unordered_map<string, set<pair<int, string>>> cuisine_to_food;

    FoodRating(vector<string>& foods, vector<string>& cuisines, vector<string>& ratings) {
        for (int i = 0; i < foods.size(); i++) {
            food_to_cuisine[foods[i]] = cuisines[i];
            food_to_rating[foods[i]] = ratings[i] - '0';
            cuisine_to_food[cuisines[i]].insert({-ratings[i] + '0', foods[i]});
        }
    }

    void changeRating(string food, int newRating) {
        string cuisine = food_to_cuisine[food];
        cuisine_to_food[cuisine].erase({-food_to_rating[food], food});
        food_to_rating[food] = newRating;
        cuisine_to_food[cuisine].insert({-newRating, food});
    }

    string highestRated(string cuisine) {
        return (*cuisine_to_food[cuisine].begin()).second;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of food items in a cuisine. The `changeRating` function takes $O(\log n)$ time, and the `highestRated` function takes $O(1)$ time.
> - **Space Complexity:** $O(n)$, where $n$ is the number of food items. We need to store the food items and their corresponding ratings in the `food_to_cuisine`, `food_to_rating`, and `cuisine_to_food` maps.
> - **Optimality proof:** This approach has the best possible time and space complexity because we need to store the food items and their corresponding ratings, and we need to update the ratings of food items in real-time.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using maps and sets to store and retrieve data efficiently.
- Problem-solving patterns identified: Using a combination of data structures to solve a problem.
- Optimization techniques learned: Using sets to store and retrieve data in sorted order.
- Similar problems to practice: Problems that involve storing and retrieving data efficiently, such as database queries.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input list.
- Edge cases to watch for: An empty input list, or a list with duplicate food items.
- Performance pitfalls: Using a data structure that has a high time complexity for insertion or deletion operations.
- Testing considerations: Testing the code with different input scenarios, such as an empty input list or a list with duplicate food items.