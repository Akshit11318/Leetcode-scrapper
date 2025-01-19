import json
import time
from pathlib import Path
from typing import Optional, Dict, Any
from groq import Groq
from dataclasses import dataclass
import logging
import sys


@dataclass
class AnalysisStats:
    """Statistics for a single analysis run."""
    model: str
    input_tokens: int
    output_tokens: int
    total_tokens: int
    duration: float



class LeetCodeAnalyzer:
    # TODO check for the compile-time JSON binding

    def __init__(self, api_key: str, problems_json_path: str = "problems.json"):
        self.api_key = api_key
        self.problems_json_path = self._resolve_json_path(problems_json_path)
        self.client = Groq(api_key=api_key)
        self.logger = logging.getLogger(__name__)
        self.problems_data = None
        self._load_problems_data()

    def _resolve_json_path(self, problems_json_path: str) -> Path:
        """Resolve the path to the JSON file dynamically."""
        if getattr(sys, 'frozen', False):  # When running as an executable
            # sys._MEIPASS is the temporary directory created by PyInstaller
            base_path = Path(sys._MEIPASS)
        else:  # When running from source
            base_path = Path(__file__).parent

        return base_path / problems_json_path

    def _load_problems_data(self) -> None:
        """Load the problems data from the JSON file."""
        try:
            with open(self.problems_json_path, 'r', encoding='utf-8') as file:
                self.problems_data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Problems JSON file not found at {self.problems_json_path}"
            )
        except json.JSONDecodeError:
            raise ValueError(
                f"Invalid JSON format in {self.problems_json_path}"
            )


    def get_problem_link(self, problem_id: int) -> Optional[str]:
        """Get the LeetCode problem link for a given problem ID."""
        for question in self.problems_data.get("problemsetQuestionList", []):
            if str(question.get("questionFrontendId")) == str(problem_id):
                title_slug = question.get("titleSlug")
                if title_slug:
                    return f"https://leetcode.com/problems/{title_slug}/description"
        return None

    def get_file_name(self, problem_id: int) -> str:
        """Generate the output file name for a given problem ID."""
        for question in self.problems_data.get("problemsetQuestionList", []):
            if str(question.get("questionFrontendId")) == str(problem_id):
                title_slug = question.get("titleSlug")
                if title_slug:
                    return f"{problem_id:04d}-{title_slug}-notes.md"
        return f"{problem_id:04d}.md"

    def analyze_problem(
        self,
        problem_id: int,
        output_dir: str = "./",
        model_name: str = "llama-3.3-70b-versatile"
    ) -> Dict[str, Any]:
        """Analyze a LeetCode problem and generate detailed notes."""
        start_time = time.time()
        result = {
            "problem_id": problem_id,
            "status": "failed",
            "error": None,
            "output_file": None
        }
        
        try:
            output_dir = Path(output_dir)
            output_dir.mkdir(parents=True, exist_ok=True)
            
            link = self.get_problem_link(problem_id)
            if not link:
                raise ValueError(f"Problem ID {problem_id} not found")
            
            output_path = output_dir / self.get_file_name(problem_id)
            
            completion = self.client.chat.completions.create(
                model=model_name,
            messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert at solving programming problems mainly leetcode. For each problem, provide:\n"
                            "1. A brute force approach as the starting point\n"
                            "2. An optimal solution (required for all problems)\n"
                            "3. A better approach (only if it exists as an intermediate step between brute and optimal)\n"
                            "4. Alternative approaches (only if they offer unique insights)\n"
                            "5. Use bold and italics to highlight appealing words, incorporate KaTeX for complexity formulas, and enclose important terms in backticks for clarity."
                            "Ensure clear progression from simpler to more sophisticated solutions. use namespace std , no need for std:: in every line"
                        )
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Generate detailed solution notes for {link} "
                            "following this template. The optimal approach is mandatory. Include a better approach "
                            "only if there's an intermediate solution between brute force ause namespace std::nd optimal.\n\n"
                            
                            "## [Problem Name]\n\n"
                            f"**Problem Link:** [{link}]({link})\n\n"
                            
                            "**Problem Statement:**\n"
                            "- Input format and constraints\n"
                            "- Expected output format\n"
                            "- Key requirements and edge cases to consider\n"
                            "- Example test cases with explanations\n\n"
                            
                            "---\n\n"
                            "### Brute Force Approach\n\n"
                            "**Explanation:**\n"
                            "- Initial thought process\n"
                            "- Step-by-step breakdown of the solution\n"
                            "- Why this approach comes to mind first\n\n"
                            
                            "```cpp\n"
                            "// Well-commented code with:\n"
                            "// - Clear variable names\n"
                            "// - Input validation\n"
                            "// - Edge case handling\n"
                            "[Insert Code in Cpp]\n"
                            "```\n\n"
                            
                            "> Complexity Analysis:\n"
                            "> - **Time Complexity:** [Big O notation with detailed breakdown]\n"
                            "> - **Space Complexity:** [Memory usage analysis with explanation]\n"
                            "> - **Why these complexities occur:** [Explain which operations cause these complexities]\n\n"
                            
                            "---\n\n"
                            "[INCLUDE THIS SECTION ONLY IF THERE'S AN INTERMEDIATE SOLUTION BETWEEN BRUTE FORCE AND OPTIMAL:]\n\n"
                            "### Better Approach\n\n"
                            "**Explanation:**\n"
                            "- Key insight that leads to improvement\n"
                            "- How it improves upon the brute force\n"
                            "- Why this isn't yet the optimal solution\n"
                            "- Step-by-step breakdown\n\n"
                            
                            "```cpp\n"
                            "// Well-structured code with:\n"
                            "// - Error handling\n"
                            "// - Input validation\n"
                            "// - Clear optimizations\n"
                            "[Insert Code in cpp]\n"
                            "```\n\n"
                            
                            "> Complexity Analysis:\n"
                            "> - **Time Complexity:** [Detailed analysis with mathematical reasoning]\n"
                            "> - **Space Complexity:** [Memory usage patterns and trade-offs]\n"
                            "> - **Improvement over brute force:** [Quantify the improvement]\n\n"
                            
                            "---\n\n"
                            "### Optimal Approach (Required)\n\n"
                            "**Explanation:**\n"
                            "- Key insight that leads to optimal solution\n"
                            "- Detailed breakdown of the approach\n"
                            "- Proof of optimality\n"
                            "- Why further optimization is impossible\n\n"
                            
                            "```cpp\n"
                            "// Production-ready code with:\n"
                            "// - Complete error handling\n"
                            "// - Input validation\n"
                            "// - Optimal implementation\n"
                            "[Insert Code in cpp]\n"
                            "```\n\n"
                            
                            "> Complexity Analysis:\n"
                            "> - **Time Complexity:** [Prove this is optimal]\n"
                            "> - **Space Complexity:** [Memory usage analysis]\n"
                            "> - **Optimality proof:** [Explain why this is the best possible complexity]\n\n"
                            
                            "---\n\n"
                            "[INCLUDE THIS SECTION ONLY IF AN ALTERNATIVE APPROACH WITH DIFFERENT TRADE-OFFS EXISTS:]\n\n"
                            "### Alternative Approach\n\n"
                            "**Explanation:**\n"
                            "- Different perspective or technique\n"
                            "- Unique trade-offs\n"
                            "- Scenarios where this approach might be preferred\n"
                            "- Comparison with optimal approach\n\n"
                            
                            "```cpp\n"
                            "[Insert Code with detailed comments]\n"
                            "```\n\n"
                            
                            "> Complexity Analysis:\n"
                            "> - **Time Complexity:** [Analysis with practical implications]\n"
                            "> - **Space Complexity:** [Trade-offs in memory usage]\n"
                            "> - **Trade-off analysis:** [When to choose this over optimal approach]\n\n"
                            
                            "---\n\n"
                            "### Final Notes\n\n"
                            "**Learning Points:**\n"
                            "- Key algorithmic concepts demonstrated\n"
                            "- Problem-solving patterns identified\n"
                            "- Optimization techniques learned\n"
                            "- Similar problems to practice\n\n"
                            
                            "**Mistakes to Avoid:**\n"
                            "- Common implementation errors\n"
                            "- Edge cases to watch for\n"
                            "- Performance pitfalls\n"
                            "- Testing considerations\n\n"
                            "---"
                        )
                    }
                ],
                temperature=0.7,
                max_completion_tokens=3072,
                top_p=0.95,
                stream=True,
                stop=None,
            )

            
            content_buffer = []
            with open(output_path, "w", encoding='utf-8') as file:
                for chunk in completion:
                    if chunk.choices and chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        content_buffer.append(content)
                        
                        if len(content_buffer) >= 10:
                            file.write(''.join(content_buffer))
                            file.flush()
                            content_buffer = []
                
                if content_buffer:
                    file.write(''.join(content_buffer))
                    file.flush()
            
            if not output_path.exists() or output_path.stat().st_size == 0:
                raise ValueError(f"Failed to generate content for problem {problem_id}")
            
            result.update({
                "status": "success",
                "output_file": str(output_path)
            })
            
        except Exception as e:
            result["error"] = str(e)
            
        result["duration"] = time.time() - start_time
        return result