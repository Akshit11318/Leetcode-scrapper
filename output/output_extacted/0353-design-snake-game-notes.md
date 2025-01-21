## Design Snake Game
**Problem Link:** https://leetcode.com/problems/design-snake-game/description

**Problem Statement:**
- Input format and constraints: The game is played on a `width x height` grid, with the snake starting at position `(0, 0)`. The snake can move up, down, left, or right, and its length increases by one unit when it eats a food pellet. The game ends when the snake runs into the boundary of the grid or its own body.
- Expected output format: The `SnakeGame` class should have a constructor that takes in the width and height of the grid, as well as a list of food pellets. The `move` method should return the score of the game after moving the snake in the specified direction.
- Key requirements and edge cases to consider:
  - The snake's initial length is 1 unit.
  - The snake can only move in the four cardinal directions (up, down, left, right).
  - The snake cannot move into its own body or the boundary of the grid.
  - The game ends when the snake runs into the boundary of the grid or its own body.
- Example test cases with explanations:
  - Example 1: `width = 3`, `height = 3`, `food = [[1,2],[0,1]]`. The snake starts at position `(0, 0)` and moves in the order "DRU".
  - Example 2: `width = 3`, `height = 2`, `food = [[0,0],[0,1],[1,0],[1,2]]`. The snake starts at position `(0, 0)` and moves in the order "DLUR".

---

### Brute Force Approach
**Explanation:**
- Initial thought process: To solve this problem, we need to keep track of the snake's position, direction, and length. We also need to check if the snake has run into the boundary of the grid or its own body.
- Step-by-step breakdown of the solution:
  1. Initialize the snake's position and direction.
  2. Check if the snake has run into the boundary of the grid or its own body.
  3. Move the snake in the specified direction.
  4. Check if the snake has eaten a food pellet. If so, increase its length by one unit.
- Why this approach comes to mind first: This approach is straightforward and easy to implement, but it may not be efficient for large grids or long snakes.

```cpp
class SnakeGame {
public:
    int width, height;
    vector<vector<int>> food;
    int foodIndex;
    deque<pair<int, int>> snake;
    set<pair<int, int>> body;

    SnakeGame(int width, int height, vector<vector<int>>& food) {
        this->width = width;
        this->height = height;
        this->food = food;
        this->foodIndex = 0;
        this->snake.push_back({0, 0});
        this->body.insert({0, 0});
    }

    int move(string direction) {
        pair<int, int> head = snake.front();
        pair<int, int> newHead;

        if (direction == "U") newHead = {head.first - 1, head.second};
        else if (direction == "D") newHead = {head.first + 1, head.second};
        else if (direction == "L") newHead = {head.first, head.second - 1};
        else if (direction == "R") newHead = {head.first, head.second + 1};

        if (newHead.first < 0 || newHead.first >= height || newHead.second < 0 || newHead.second >= width || body.count(newHead)) return -1;

        snake.push_front(newHead);
        body.insert(newHead);

        if (foodIndex < food.size() && newHead.first == food[foodIndex][0] && newHead.second == food[foodIndex][1]) {
            foodIndex++;
        } else {
            pair<int, int> tail = snake.back();
            snake.pop_back();
            body.erase(tail);
        }

        return foodIndex;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of moves. Each move takes constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the snake. We need to store the snake's body in a set.
> - **Why these complexities occur:** The time complexity is linear because we perform a constant amount of work for each move. The space complexity is linear because we need to store the snake's body in a set.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a `deque` to store the snake's body and a `set` to store the snake's body for efficient lookup.
- Detailed breakdown of the approach:
  1. Initialize the snake's position and direction.
  2. Check if the snake has run into the boundary of the grid or its own body.
  3. Move the snake in the specified direction.
  4. Check if the snake has eaten a food pellet. If so, increase its length by one unit.
- Proof of optimality: This approach is optimal because we only perform a constant amount of work for each move, and we use a `deque` and a `set` to store the snake's body for efficient lookup.

```cpp
class SnakeGame {
public:
    int width, height;
    vector<vector<int>> food;
    int foodIndex;
    deque<pair<int, int>> snake;
    set<pair<int, int>> body;

    SnakeGame(int width, int height, vector<vector<int>>& food) {
        this->width = width;
        this->height = height;
        this->food = food;
        this->foodIndex = 0;
        this->snake.push_back({0, 0});
        this->body.insert({0, 0});
    }

    int move(string direction) {
        pair<int, int> head = snake.front();
        pair<int, int> newHead;

        if (direction == "U") newHead = {head.first - 1, head.second};
        else if (direction == "D") newHead = {head.first + 1, head.second};
        else if (direction == "L") newHead = {head.first, head.second - 1};
        else if (direction == "R") newHead = {head.first, head.second + 1};

        if (newHead.first < 0 || newHead.first >= height || newHead.second < 0 || newHead.second >= width || body.count(newHead)) return -1;

        snake.push_front(newHead);
        body.insert(newHead);

        if (foodIndex < food.size() && newHead.first == food[foodIndex][0] && newHead.second == food[foodIndex][1]) {
            foodIndex++;
        } else {
            pair<int, int> tail = snake.back();
            snake.pop_back();
            body.erase(tail);
        }

        return foodIndex;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of moves. Each move takes constant time.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the snake. We need to store the snake's body in a set.
> - **Optimality proof:** This approach is optimal because we only perform a constant amount of work for each move, and we use a `deque` and a `set` to store the snake's body for efficient lookup.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `deque` and a `set` to store the snake's body for efficient lookup.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and solving each one individually.
- Optimization techniques learned: Using a `deque` and a `set` to store the snake's body for efficient lookup.
- Similar problems to practice: Other problems that involve using a `deque` and a `set` to store data for efficient lookup.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the snake has run into the boundary of the grid or its own body.
- Edge cases to watch for: The snake's initial length is 1 unit, and the snake can only move in the four cardinal directions.
- Performance pitfalls: Not using a `deque` and a `set` to store the snake's body for efficient lookup.
- Testing considerations: Testing the game with different inputs and edge cases to ensure that it works correctly.