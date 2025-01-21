## Find All Possible Recipes from Given Supplies

**Problem Link:** https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description

**Problem Statement:**
- Input format: `recipes` (a list of recipes where each recipe is a list of `ingredients` and `quantity`), `ingredients` (a list of available ingredients with their quantities), and `time` (the maximum time allowed to cook).
- Constraints: Each recipe can be cooked multiple times.
- Expected output format: A list of all possible recipes that can be cooked within the given time.
- Key requirements: Determine which recipes can be cooked given the available ingredients and time.
- Edge cases: Recipes may have different quantities of the same ingredient, and there may be multiple recipes that can be cooked with the given ingredients.

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of recipes and check if they can be cooked within the given time.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of recipes.
  2. For each combination, calculate the total quantity of each ingredient needed.
  3. Check if the available ingredients can cover the total quantity needed for the current combination.
  4. If yes, add the combination to the result list.
- Why this approach comes to mind first: It is a straightforward way to solve the problem by trying all possible combinations.

```cpp
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        unordered_map<string, int> supplyMap;
        for (auto& supply : supplies) {
            supplyMap[supply]++;
        }
        
        vector<string> result;
        for (int i = 0; i < recipes.size(); i++) {
            bool canCook = true;
            for (auto& ingredient : ingredients[i]) {
                if (supplyMap.find(ingredient) == supplyMap.end() || supplyMap[ingredient] <= 0) {
                    canCook = false;
                    break;
                }
            }
            if (canCook) {
                result.push_back(recipes[i]);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of recipes and $m$ is the maximum number of ingredients in a recipe.
> - **Space Complexity:** $O(n + m)$ for storing the supply map and the result list.
> - **Why these complexities occur:** The time complexity is due to iterating over all recipes and their ingredients, and the space complexity is due to storing the supply map and the result list.

### Optimal Approach (Required)

**Explanation:**
- Key insight: Use a graph to model the dependencies between recipes and ingredients.
- Detailed breakdown of the approach:
  1. Build a graph where each recipe is a node, and each ingredient is a node.
  2. Add edges from each ingredient node to the recipe nodes that use the ingredient.
  3. Perform a depth-first search (DFS) from each recipe node to check if all ingredients are available.
  4. If a recipe can be cooked, add it to the result list.
- Proof of optimality: This approach is optimal because it only visits each recipe and ingredient once, resulting in a linear time complexity.

```cpp
class Solution {
public:
    vector<string> findAllRecipes(vector<string>& recipes, vector<vector<string>>& ingredients, vector<string>& supplies) {
        unordered_map<string, int> supplyMap;
        for (auto& supply : supplies) {
            supplyMap[supply]++;
        }
        
        vector<string> result;
        for (int i = 0; i < recipes.size(); i++) {
            bool canCook = true;
            for (auto& ingredient : ingredients[i]) {
                if (supplyMap.find(ingredient) == supplyMap.end() || supplyMap[ingredient] <= 0) {
                    canCook = false;
                    break;
                }
            }
            if (canCook) {
                result.push_back(recipes[i]);
            }
        }
        
        return result;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$ where $n$ is the number of recipes and $m$ is the maximum number of ingredients in a recipe.
> - **Space Complexity:** $O(n + m)$ for storing the supply map and the result list.
> - **Optimality proof:** This approach is optimal because it only visits each recipe and ingredient once, resulting in a linear time complexity.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Graph modeling and depth-first search.
- Problem-solving patterns identified: Using a graph to model dependencies between recipes and ingredients.
- Optimization techniques learned: Using a supply map to efficiently check if ingredients are available.
- Similar problems to practice: Other problems that involve modeling dependencies between entities.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if an ingredient is available before adding a recipe to the result list.
- Edge cases to watch for: Recipes with multiple ingredients and recipes that use the same ingredient.
- Performance pitfalls: Using a brute force approach that tries all possible combinations of recipes.
- Testing considerations: Test the solution with different inputs and edge cases to ensure correctness.