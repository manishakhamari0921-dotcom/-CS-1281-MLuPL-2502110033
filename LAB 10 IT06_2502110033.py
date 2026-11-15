IT6: Precision - The Handover Pack
Add a hostile-input demonstration and a documented limitations section.

Hostile-Input Demo (src/run_tests.py):

Python
from main import process_data

def run_tests():
    print("--- Running Hostile Input Tests ---")

    print("\nTest 1: Missing File")
    process_data("data/does_not_exist.csv") # Should print your clean error message

    print("\nTest 2: Invalid Data Format")
    process_data("data/corrupted_sample.csv") # Should handle gracefully

if __name__ == "__main__":
    run_tests()
Sample Output: Generate a successful run and save the result as reports/example_report.txt, then commit it: git add reports/example_report.txt.

Limitations Section (Append to README.md):

Markdown
## Limitations
- **Scale:** Not optimized for datasets larger than 1GB; loads entire file into memory.
- **Format:** Currently only supports comma-separated `.csv` files (no JSON or Excel support).
- **Error Correction:** Does not automatically clean malformed rows; it
