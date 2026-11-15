IT10: Standard - README & Tidy
Execute these terminal commands to establish a clean, professional repository workshop structure, moving your files into the appropriate directories:

Bash
# Create standard directories
mkdir src data reports

# Move your core code
mv main.py src/
mv utils.py src/

# Commit exactly one sample input file for immediate usage
mv sample_dataset.csv data/

# Clean up the repository (delete dead files/experiments)
git rm obsolete_experiment.py
    README.md Template Structure:

Markdown
# [Project Name]

[One-sentence description of the problem solved]

## Setup and Execution
1. Ensure your input data is placed in the `data/` folder.
2. Run the main script from the root directory: `python src/main.py`
3. Outputs will be generated in the `reports/` folder
    
