# Jenkins Job Setup with Parameterized Test Selection

## Overview
This document provides step-by-step instructions to create a Jenkins job that connects to a GitHub repository and allows users to select which Python tests to run via a parameter.

## Prerequisites
- Jenkins installed on your Mac
- GitHub account and repository created
- Python 3 installed
- Git installed

## Step 1: Create the GitHub Repository

### 1.1 Initialize the Repository Locally
```bash
cd /Users/cristian/master-ism/repository/quality
git init
git config user.name "Cristian Ciobanu"
git config user.email "your.email@github.com"
```

### 1.2 Add Files to Git
```bash
git add test_login.py test_calculator.py requirements.txt Jenkinsfile README.md
git commit -m "Initial commit: Add test suites and Jenkinsfile"
```

### 1.3 Push to GitHub
1. Create a new repository on GitHub named: `SQMA_Ciobanu_Cristian`
2. Copy the repository URL from GitHub
3. Run:
```bash
git remote add origin https://github.com/YourUsername/SQMA_Ciobanu_Cristian.git
git branch -M main
git push -u origin main
```

## Step 2: Install Required Jenkins Plugins

1. Open Jenkins: `http://localhost:8080` (or your Jenkins URL)
2. Go to **Manage Jenkins** > **Manage Plugins**
3. Install these plugins:
   - **GitHub** (for GitHub integration)
   - **Pipeline** (for Jenkinsfile support)
   - **HTML Publisher** (for test reports)
4. Restart Jenkins

## Step 3: Create Jenkins Credentials for GitHub

1. Go to **Manage Jenkins** > **Manage Credentials**
2. Click **System** > **Global credentials**
3. Click **Add Credentials**
4. Select **Kind: Username with password**
   - Username: Your GitHub username
   - Password: Your GitHub Personal Access Token
   - ID: `github-credentials`
5. Click **Create**

## Step 4: Create a New Jenkins Pipeline Job

1. Click **New Item**
2. Enter job name: `SQMA_Ciobanu_Cristian`
3. Select **Pipeline** and click **OK**
4. Configure the pipeline:
   - **Definition**: Pipeline script from SCM
   - **SCM**: Git
   - **Repository URL**: `https://github.com/YourUsername/SQMA_YourLastName_Cristian.git`
   - **Credentials**: Select the GitHub credentials you created
   - **Branch**: */main
   - **Script Path**: Jenkinsfile
5. Click **Save**

## Step 5: Test the Jenkins Job

### 5.1 Run with Parameter Selection
1. Click **Build with Parameters**
2. Select a test suite:
   - **test_login**: Runs login-related tests (3 tests)
   - **test_calculator**: Runs calculator tests (5 tests)
3. Click **Build**

### 5.2 Monitor Execution
1. Click the build number to view **Console Output**
2. Check the stages:
   - **Checkout**: Clones repository
   - **Install Dependencies**: Installs pytest and other packages
   - **Run Selected Tests**: Executes selected test suite

## Test Suites Overview

### Test Login Suite (test_login.py)
- `test_valid_login()`: Validates correct login credentials
- `test_empty_username()`: Ensures empty username is rejected
- `test_password_length()`: Verifies password meets minimum length (8 chars)

### Test Calculator Suite (test_calculator.py)
- `test_addition()`: Tests 5 + 3 = 8
- `test_subtraction()`: Tests 10 - 4 = 6
- `test_multiplication()`: Tests 7 * 6 = 42
- `test_division()`: Tests 20 / 4 = 5
- `test_division_by_zero()`: Ensures division by zero raises error

## Running Tests Locally (Optional)

### Install dependencies:
```bash
cd /Users/cristian/master-ism/repository/quality
pip install -r requirements.txt
```

### Run all tests:
```bash
python3 -m pytest -v
```

### Run specific test file:
```bash
python3 -m pytest test_login.py -v
python3 -m pytest test_calculator.py -v
```

### Run specific test:
```bash
python3 -m pytest test_login.py::TestLogin::test_valid_login -v
```

## Expected Results

### Successful Test Execution
```
test_login.py::TestLogin::test_valid_login PASSED
test_login.py::TestLogin::test_empty_username PASSED
test_login.py::TestLogin::test_password_length FAILED  [Expected for demonstration]

=== 2 passed, 1 failed in 0.12s ===
```

### Jenkins Job Output
- **Build Status**: SUCCESS (if all selected tests pass)
- **Test Report**: Available via "Test Report" link in Jenkins UI
- **Console Log**: Shows detailed execution information

## Troubleshooting

### Jenkins cannot clone repository
- Verify GitHub credentials are correct
- Check repository URL format
- Ensure Jenkins has internet access

### Tests fail with "module not found"
- Run `pip install -r requirements.txt` in Jenkins
- Verify requirements.txt is in repository root

### Jenkinsfile not found
- Verify file is committed to repository
- Check that repository is on main branch

## Project Structure
```
SQMA_Ciobanu_Cristian/
├── test_login.py          # Login tests
├── test_calculator.py     # Calculator tests
├── requirements.txt       # Python dependencies
├── Jenkinsfile           # Jenkins pipeline configuration
└── README.md             # This documentation
```

## Next Steps
1. Customize tests based on your requirements
2. Add more test cases as needed
3. Implement additional test suites for different modules
4. Configure Jenkins webhooks for automatic builds on GitHub push
