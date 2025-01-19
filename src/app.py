import argparse
from pathlib import Path
import sys
import logging
from leetcode_analyzer import LeetCodeAnalyzer
import time
from typing import Dict, List

import argparse
import textwrap

def show_welcome_message():
    # ASCII art and usage instructions
    ascii_logo = r"""
  _                  _      _____                                             
 | |                | |    / ____|                                            
 | |      ___   ___ | |_  | (___    ___  _ __  __ _  _ __   _ __    ___  _ __ 
 | |     / _ \ / _ \| __|  \___ \  / __|| '__|/ _` || '_ \ | '_ \  / _ \| '__|
 | |____|  __/|  __/| |_   ____) || (__ | |  | (_| || |_) || |_) ||  __/| |   
 |______|\___| \___| \__| |_____/  \___||_|   \__,_|| .__/ | .__/  \___||_|   
                                                   | |    | |                
                                                   |_|    |_| 
    """
    usage_instructions = textwrap.dedent("""
        Welcome to the LeetCode Scraper!

        Usage:
          app --range <RANGE> --api-key <API_KEY> [OPTIONS]

        Options:
          --range RANGE            Specify the range of problems (e.g., 1-100).
          --api-key API_KEY        Your API key for accessing the Groq API.
          --output-dir OUTPUT_DIR  Directory to save the output (default: ./notes).
          --model MODEL            Specify the model to use (default: llama-3.3-70b-versatile).
          --sleep SLEEP            Delay between requests in seconds (default: 30) | no sleep -1.

        Example:
          ./app --range 1-100 --api-key YOUR_API_KEY --output-dir ./results

        Created by: Akshit & Rohan
        """)

    print(ascii_logo)
    print(usage_instructions)




def setup_logging() -> logging.Logger:
    """Configure basic logging."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    return logging.getLogger(__name__)

def parse_range(range_str: str) -> List[int]:
    """Parse a range string (e.g., '1-34') into a list of problem IDs."""
    try:
        start, end = map(int, range_str.split('-'))
        if start > end:
            raise ValueError(f"Invalid range: start ({start}) is greater than end ({end})")
        return list(range(start, end + 1))
    except ValueError as e:
        raise ValueError(f"Invalid range format. Expected 'start-end', got '{range_str}'. Error: {str(e)}")

def process_problem(problem_id: int, api_key: str, output_dir: str, model_name: str, sleep_time: int) -> Dict:
    """Process a single LeetCode problem."""
    try:
        analyzer = LeetCodeAnalyzer(api_key)
        result = analyzer.analyze_problem(
            problem_id=problem_id,
            output_dir=output_dir,
            model_name=model_name
        )
        
        # Sleep after processing unless sleep_time is -1
        if sleep_time != -1:
            time.sleep(sleep_time)
            
        return result
    except Exception as e:
        return {
            "problem_id": problem_id,
            "status": "failed",
            "error": str(e)
        }


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='LeetCode Problem Analyzer CLI')
    parser.add_argument('--range', type=str,
                      help='Problem range (format: 1-34)')
    parser.add_argument('--api-key', type=str,
                      help='API key')
    parser.add_argument('--output-dir', type=str, default='./notes',
                      help='Output directory for generated notes')
    parser.add_argument('--model', type=str, 
                      default='llama-3.3-70b-versatile',
                      help='Model name to use')
    parser.add_argument('--sleep', type=int, default=30,
                      help='Sleep time between problems in seconds. Use -1 for no sleep')

    args = parser.parse_args()
    logger = setup_logging()

    if not args.range or not args.api_key:
        show_welcome_message()
        print("ERROR 401 : the following arguments are required: --range, --api-key")
        return

    try:
        show_welcome_message()
        # Create output directory
        output_dir = Path(args.output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Parse range into list of problem IDs
        problem_ids = parse_range(args.range)
        
        logger.info(f"Processing {len(problem_ids)} problems sequentially")
        if args.sleep != -1:
            logger.info(f"Sleeping {args.sleep} seconds between problems")

        # Process problems one by one
        for pid in problem_ids:
            try:
                result = process_problem(
                    pid, 
                    args.api_key, 
                    str(output_dir), 
                    args.model,
                    args.sleep
                )
                status = result.get('status', 'unknown')
                
                if status == 'success':
                    logger.info(f"Problem {pid}: Success")
                else:
                    error = result.get('error', 'Unknown error')
                    logger.error(f"Problem {pid}: Failed - {error}")
                    
            except Exception as e:
                logger.error(f"Problem {pid}: Error - {str(e)}")

        logger.info("Processing completed")

    except Exception as e:
        logger.error(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()