#!/bin/bash
# SQMA_Ciobanu_Cristian - GitHub Setup Script

echo "==================================="
echo "SQMA_Ciobanu_Cristian Setup Script"
echo "==================================="
echo ""

# Initialize Git
echo "Step 1: Initializing Git repository..."
git init
git config user.name "Cristian Ciobanu"
git config user.email "your.email@github.com"

# Add all files
echo "Step 2: Adding files to Git..."
git add test_login.py test_calculator.py requirements.txt Jenkinsfile README.md SETUP_DOCUMENTATION.md

# Initial commit
echo "Step 3: Creating initial commit..."
git commit -m "Initial commit: SQMA_Ciobanu_Cristian test suite and Jenkins configuration"

echo ""
echo "==================================="
echo "Setup Complete!"
echo "==================================="
echo ""
echo "NEXT STEPS:"
echo "1. Create a new repository on GitHub: https://github.com/new"
echo "   - Repository name: SQMA_Ciobanu_Cristian"
echo "   - Do NOT initialize with README, .gitignore, or license"
echo ""
echo "2. After creating the repository, copy the URL and run:"
echo "   git remote add origin https://github.com/YourUsername/SQMA_Ciobanu_Cristian.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Configure Jenkins (see SETUP_DOCUMENTATION.md for details)"
echo ""
