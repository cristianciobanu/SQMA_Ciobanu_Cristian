# SQMA Project - Quick Setup Guide

## What's Included

### Test Files
- **test_login.py**: 3 test cases for user authentication
  - Valid login validation
  - Empty username handling
  - Password minimum length (8 characters)

- **test_calculator.py**: 5 test cases for basic math operations
  - Addition, Subtraction, Multiplication, Division
  - Division by zero error handling

### Configuration Files
- **Jenkinsfile**: Declarative pipeline with parameter selection
- **requirements.txt**: Python dependencies (pytest, pytest-html)
- **SETUP_DOCUMENTATION.md**: Complete step-by-step setup guide

## Quick Start

### 1. Initialize Git Repository
```bash
cd /Users/cristian/master-ism/repository/quality
git init
git config user.name "Cristian Ciobanu"
git config user.email "your.email@github.com"
git add .
git commit -m "Initial commit: SQMA_Ciobanu_Cristian project"
```

### 2. Create Repository on GitHub
1. Go to https://github.com/new
2. Repository name: `SQMA_Ciobanu_Cristian`
3. Click "Create repository"
4. Copy the repository URL

### 3. Push to GitHub
```bash
git remote add origin [YOUR_GITHUB_URL_HERE]
git branch -M main
git push -u origin main
```

## Parameter Options in Jenkins
- **test_login**: Runs login authentication tests
- **test_calculator**: Runs calculator operation tests

## Test Results
- HTML report generated after each build
- Test report available in Jenkins UI
- Pass/Fail status displayed in console output
