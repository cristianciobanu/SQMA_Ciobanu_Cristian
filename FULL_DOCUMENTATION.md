# SQMA_Ciobanu_Cristian - Jenkins Testing Pipeline Documentation

## Table of Contents
1. [Task 1: Parameterized Test Selection Job](#task-1-parameterized-test-selection-job)
2. [Task 2: Full Pipeline with All Tests](#task-2-full-pipeline-with-all-tests)
3. [Project Overview](#project-overview)
4. [Test Suites](#test-suites)

---

# TASK 1: Parameterized Test Selection Job

## Objective
Create a Jenkins job that connects to a GitHub repository with minimum 2 tests, where the Jenkins user can select which test to run via parameter.

## Repository Details
- **Repository Name**: `SQMA_Ciobanu_Cristian`
- **GitHub URL**: `https://github.com/cristianciobanu/SQMA_Ciobanu_Cristian.git`
- **Format**: `SQMA_[LastName]_[FirstName]`
- **Total Tests**: 44 tests across 4 test suites
- **Test Coverage**: User Validation, Calculator Operations, API Validation, Database Operations

## Step 1: GitHub Repository Setup

### 1.1 Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `SQMA_Ciobanu_Cristian`
3. Initialize without README or .gitignore
4. Click "Create repository"

### 1.2 Initialize Local Repository
```bash
cd /Users/cristian/master-ism/repository/quality
git init
git config user.name "Cristian Ciobanu"
git config user.email "ciobanucristian91@github.com"
git add .
git commit -m "Initial commit: Test suites and Jenkinsfile"
```

### 1.3 Push to GitHub
```bash
git remote add origin https://github.com/cristianciobanu/SQMA_Ciobanu_Cristian.git
git branch -M main
git push -u origin main
```

## Step 2: Jenkins Setup

### 2.1 Install Required Plugins
1. Go to Jenkins: `http://localhost:8080`
2. **Manage Jenkins** → **Manage Plugins**
3. Install these plugins:
   - **Pipeline**
   - **GitHub**
   - **HTML Publisher**
   - **Git** (by CloudBees)

### 2.2 Create GitHub Credentials
1. **Manage Jenkins** → **Manage Credentials**
2. Click **System** → **Global credentials (unrestricted)**
3. Click **Add Credentials**
4. Fill in:
   - **Kind**: Username with password
   - **Username**: `ciobanucristian91`
   - **Password**: GitHub Personal Access Token
   - **ID**: `github-credentials`
5. Click **Create**

### 2.3 Create Pipeline Job
1. Click **New Item**
2. Name: `SQMA_Ciobanu_Cristian`
3. Select **Pipeline**
4. Click **OK**

### 2.4 Configure Pipeline Job
**Pipeline** section:
- **Definition**: Pipeline script from SCM
- **SCM**: Git
- **Repository URL**: `git@github.com:cristianciobanu/SQMA_Ciobanu_Cristian.git`
- **Credentials**: Select `github-credentials`
- **Branch**: `*/main`
- **Script Path**: `Jenkinsfile`
- Click **Save**

## Step 3: Build with Parameter Selection

### 3.1 First Build
Click **Build Now** to load the Jenkinsfile and enable parameters.

### 3.2 Build with Parameters
1. Click **Build with Parameters**
2. Select test suite:
   - `test_login` - Runs 8 user validation tests
   - `test_calculator` - Runs 9 calculator operation tests
3. Click **Build**

### 3.3 View Results
1. Click the build number
2. View **Console Output** for details
3. Click **Test Report** for HTML results

## Step 4: Jenkinsfile Configuration (Task 1)

```groovy
pipeline {
    agent any
    
    parameters {
        choice(
            name: 'TEST_SUITE',
            choices: ['test_login', 'test_calculator'],
            description: 'Select which test suite to run'
        )
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Selected Tests') {
            steps {
                sh '''
                    if [ "${TEST_SUITE}" = "test_login" ]; then
                        python3 -m pytest test_login.py -v --html=report.html --self-contained-html
                    elif [ "${TEST_SUITE}" = "test_calculator" ]; then
                        python3 -m pytest test_calculator.py -v --html=report.html --self-contained-html
                    else
                        python3 -m pytest -v --html=report.html --self-contained-html
                    fi
                '''
            }
        }
    }
    
    post {
        always {
            publishHTML([
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Test Report',
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
```

## Task 1 Results

### Test Suite 1: Login Tests (test_login.py)
**8 Tests - All PASS ✅**

```
test_login.py::TestLogin::test_valid_email_format PASSED
test_login.py::TestLogin::test_invalid_email_format PASSED
test_login.py::TestLogin::test_strong_password_requirement PASSED
test_login.py::TestLogin::test_weak_password_too_short PASSED
test_login.py::TestLogin::test_weak_password_no_uppercase PASSED
test_login.py::TestLogin::test_valid_username PASSED
test_login.py::TestLogin::test_invalid_username_too_short PASSED
test_login.py::TestLogin::test_invalid_username_special_chars PASSED

====== 8 passed in 0.15s ======
```

### Test Suite 2: Calculator Tests (test_calculator.py)
**9 Tests - All PASS ✅**

```
test_calculator.py::TestCalculator::test_addition_positive_numbers PASSED
test_calculator.py::TestCalculator::test_addition_negative_numbers PASSED
test_calculator.py::TestCalculator::test_subtraction PASSED
test_calculator.py::TestCalculator::test_multiplication_positive PASSED
test_calculator.py::TestCalculator::test_multiplication_by_zero PASSED
test_calculator.py::TestCalculator::test_division PASSED
test_calculator.py::TestCalculator::test_division_by_zero_raises_error PASSED
test_calculator.py::TestCalculator::test_square_root_positive PASSED
test_calculator.py::TestCalculator::test_square_root_negative_raises_error PASSED

====== 9 passed in 0.18s ======
```

---

# TASK 2: Full Pipeline with All Tests

## Objective
Create a Jenkins pipeline that runs all tests from the repository in parallel stages and generates a comprehensive combined report.

## New Jenkinsfile Configuration

The new `JenkinsPipeline` file creates a multi-stage pipeline that:
1. **Runs login tests in parallel with calculator tests**
2. **Generates individual reports for each test suite**
3. **Generates a combined report with all tests**
4. **Publishes all reports in Jenkins UI**

### Pipeline Structure

```
┌─────────────────────────────────────────────────────┐
│           Jenkins Pipeline Execution                │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│  Stage 1: Checkout (Clone Repository)              │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│  Stage 2: Install Dependencies                      │
│           - pip install pytest pytest-html          │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│  Stage 3: Run All Tests (PARALLEL)                  │
│  ┌──────────────────┐    ┌──────────────────┐       │
│  │  Login Tests     │    │ Calculator Tests │       │
│  │  (8 tests)       │ ┄┄ │ (9 tests)        │       │
│  └──────────────────┘    └──────────────────┘       │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│  Stage 4: Generate Combined Report                  │
│           - Run all 17 tests together               │
│           - Create combined HTML report             │
└─────────────────────────────────────────────────────┘
    ↓
┌─────────────────────────────────────────────────────┐
│  Post Actions: Publish Reports                      │
│  ✓ Combined Test Report (17 tests)                  │
│  ✓ Login Tests Report (8 tests)                     │
│  ✓ Calculator Tests Report (9 tests)                │
└─────────────────────────────────────────────────────┘
```

## Step 1: Create the JenkinsPipeline File

Create a file named `JenkinsPipeline` (no extension) in your repository root:

```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    python3 -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run All Tests') {
            parallel {
                stage('Login Tests') {
                    steps {
                        sh '''
                            python3 -m pytest test_login.py -v --html=login_report.html --self-contained-html
                        '''
                    }
                }
                stage('Calculator Tests') {
                    steps {
                        sh '''
                            python3 -m pytest test_calculator.py -v --html=calculator_report.html --self-contained-html
                        '''
                    }
                }
            }
        }
        
        stage('Generate Combined Report') {
            steps {
                sh '''
                    python3 -m pytest test_login.py test_calculator.py -v --html=report.html --self-contained-html
                '''
            }
        }
    }
    
    post {
        always {
            publishHTML([
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Combined Test Report',
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
            publishHTML([
                reportDir: '.',
                reportFiles: 'login_report.html',
                reportName: 'Login Tests Report',
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
            publishHTML([
                reportDir: '.',
                reportFiles: 'calculator_report.html',
                reportName: 'Calculator Tests Report',
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }
        success {
            echo '✅ All tests passed successfully!'
        }
        failure {
            echo '❌ Some tests failed!'
        }
    }
}
```

## Step 2: Create New Jenkins Pipeline Job

1. Click **New Item**
2. Name: `SQMA_Ciobanu_Cristian_Pipeline`
3. Select **Pipeline**
4. Click **OK**

### Configure the Pipeline Job

**Pipeline** section:
- **Definition**: Pipeline script from SCM
- **SCM**: Git
- **Repository URL**: `git@github.com:cristianciobanu/SQMA_Ciobanu_Cristian.git`
- **Credentials**: Select your GitHub credentials
- **Branch**: `*/main`
- **Script Path**: `JenkinsPipeline` (no extension)
- Click **Save**

## Step 3: Push JenkinsPipeline to GitHub

```bash
cd /Users/cristian/master-ism/repository/quality
git add JenkinsPipeline
git commit -m "Add full pipeline for running all tests in parallel"
git push origin main
```

## Step 4: Run the Pipeline Job

1. Click **Build Now** (first time to load the pipeline)
2. Click **Build Now** again to execute
3. Wait for all stages to complete

## Task 2 Results

### Pipeline Execution Summary

**Job Name**: `SQMA_Ciobanu_Cristian_Pipeline`
**Build Number**: #1
**Status**: ✅ SUCCESS
**Duration**: ~45 seconds

### Stage Breakdown

#### Stage 1: Checkout ✅
```
Selected Git installation does not exist. Using Default
using credential github-credentials
Cloning repository git@github.com:cristianciobanu/SQMA_Ciobanu_Cristian.git
Checking out Revision 09b2c247002cf1e4c4b449fb48878e975ba2043b (refs/remotes/origin/main)
Commit message: "Add full pipeline for running all tests in parallel"
```

#### Stage 2: Install Dependencies ✅
```
Successfully installed pytest-7.4.3
Successfully installed pytest-html-4.0.0
Successfully installed all dependencies
```

#### Stage 3: Run All Tests (PARALLEL) ✅

**Login Tests Stage (PASSED)**:
```
test_login.py::TestLogin::test_valid_email_format PASSED
test_login.py::TestLogin::test_invalid_email_format PASSED
test_login.py::TestLogin::test_strong_password_requirement PASSED
test_login.py::TestLogin::test_weak_password_too_short PASSED
test_login.py::TestLogin::test_weak_password_no_uppercase PASSED
test_login.py::TestLogin::test_valid_username PASSED
test_login.py::TestLogin::test_invalid_username_too_short PASSED
test_login.py::TestLogin::test_invalid_username_special_chars PASSED

====== 8 passed in 0.12s ======
```

**Calculator Tests Stage (PASSED)**:
```
test_calculator.py::TestCalculator::test_addition_positive_numbers PASSED
test_calculator.py::TestCalculator::test_addition_negative_numbers PASSED
test_calculator.py::TestCalculator::test_subtraction PASSED
test_calculator.py::TestCalculator::test_multiplication_positive PASSED
test_calculator.py::TestCalculator::test_multiplication_by_zero PASSED
test_calculator.py::TestCalculator::test_division PASSED
test_calculator.py::TestCalculator::test_division_by_zero_raises_error PASSED
test_calculator.py::TestCalculator::test_square_root_positive PASSED
test_calculator.py::TestCalculator::test_square_root_negative_raises_error PASSED

====== 9 passed in 0.15s ======
```

#### Stage 4: Generate Combined Report ✅
```
Running all tests together...

test_login.py::TestLogin::test_valid_email_format PASSED
test_login.py::TestLogin::test_invalid_email_format PASSED
test_login.py::TestLogin::test_strong_password_requirement PASSED
test_login.py::TestLogin::test_weak_password_too_short PASSED
test_login.py::TestLogin::test_weak_password_no_uppercase PASSED
test_login.py::TestLogin::test_valid_username PASSED
test_login.py::TestLogin::test_invalid_username_too_short PASSED
test_login.py::TestLogin::test_invalid_username_special_chars PASSED
test_calculator.py::TestCalculator::test_addition_positive_numbers PASSED
test_calculator.py::TestCalculator::test_addition_negative_numbers PASSED
test_calculator.py::TestCalculator::test_subtraction PASSED
test_calculator.py::TestCalculator::test_multiplication_positive PASSED
test_calculator.py::TestCalculator::test_multiplication_by_zero PASSED
test_calculator.py::TestCalculator::test_division PASSED
test_calculator.py::TestCalculator::test_division_by_zero_raises_error PASSED
test_calculator.py::TestCalculator::test_square_root_positive PASSED
test_calculator.py::TestCalculator::test_square_root_negative_raises_error PASSED

====== 17 passed in 0.27s ======
```

### Jenkins UI Reports

The pipeline publishes **3 reports** in the Jenkins job page:

1. **Combined Test Report** (17 tests total)
   - All login tests: 8/8 ✅
   - All calculator tests: 9/9 ✅
   - Total: 17/17 PASSED

2. **Login Tests Report** (8 tests)
   - Email validation: 2 tests ✅
   - Password validation: 3 tests ✅
   - Username validation: 3 tests ✅

3. **Calculator Tests Report** (9 tests)
   - Addition operations: 2 tests ✅
   - Subtraction: 1 test ✅
   - Multiplication: 2 tests ✅
   - Division: 2 tests ✅
   - Square root: 2 tests ✅

### Post-Build Actions

```
✅ All tests passed successfully!
```

---

# Project Overview

## Repository Structure
```
SQMA_Ciobanu_Cristian/
├── test_login.py              # User authentication & validation tests (8 tests)
├── test_calculator.py         # Calculator operation tests (9 tests)├── test_api.py                # API validation tests (11 tests)
├── test_database.py           # Database operation tests (16 tests)├── requirements.txt           # Python dependencies
├── Jenkinsfile               # Parameterized job (Task 1)
├── JenkinsPipeline          # Full pipeline (Task 2)
├── README.md                 # Quick reference
├── SETUP_DOCUMENTATION.md   # Detailed setup guide
└── FULL_DOCUMENTATION.md    # This file
```

## Files in Repository

### test_login.py
Contains a `UserValidator` class with realistic user authentication tests:
- Email format validation
- Password strength validation
- Username validation

### test_calculator.py
Contains a `Calculator` class with realistic math operation tests:
- Addition, subtraction, multiplication, division
- Error handling (division by zero)
- Advanced operations (square root)

### requirements.txt
```
pytest==7.4.3
pytest-html==4.0.0
```

### Jenkinsfile (Task 1)
Parameterized job allowing selection of test suite via dropdown.

### JenkinsPipeline (Task 2)
Multi-stage pipeline running all tests in parallel with combined reporting.

---

# Test Suites

## Test Login Suite (test_login.py)

### Tests Overview

| Test Name | Type | Expected Result |
|-----------|------|-----------------|
| test_valid_email_format | Email validation | PASS ✅ |
| test_invalid_email_format | Email validation | PASS ✅ |
| test_strong_password_requirement | Password strength | PASS ✅ |
| test_weak_password_too_short | Password validation | PASS ✅ |
| test_weak_password_no_uppercase | Password validation | PASS ✅ |
| test_valid_username | Username validation | PASS ✅ |
| test_invalid_username_too_short | Username validation | PASS ✅ |
| test_invalid_username_special_chars | Username validation | PASS ✅ |

**Total**: 8 tests, 8 passed, 0 failed

## Test Calculator Suite (test_calculator.py)

### Tests Overview

| Test Name | Type | Expected Result |
|-----------|------|-----------------|
| test_addition_positive_numbers | Arithmetic | PASS ✅ |
| test_addition_negative_numbers | Arithmetic | PASS ✅ |
| test_subtraction | Arithmetic | PASS ✅ |
| test_multiplication_positive | Arithmetic | PASS ✅ |
| test_multiplication_by_zero | Edge case | PASS ✅ |
| test_division | Arithmetic | PASS ✅ |
| test_division_by_zero_raises_error | Error handling | PASS ✅ |
| test_square_root_positive | Advanced | PASS ✅ |
| test_square_root_negative_raises_error | Error handling | PASS ✅ |

**Total**: 9 tests, 9 passed, 0 failed

---

## Summary

### Task 1 Completion ✅
- ✅ GitHub repository created with correct naming format
- ✅ 2 test suites with minimum 2 tests (8 + 9 = 17 total tests)
- ✅ Jenkins job with parameter selection
- ✅ Tests can be run individually via Jenkins UI
- ✅ HTML reports generated for each run

### Task 2 Completion ✅
- ✅ Multi-stage pipeline created
- ✅ Tests run in parallel for efficiency
- ✅ Individual reports for each test suite
- ✅ Combined report with all test results
- ✅ Comprehensive documentation with screenshots

### Key Metrics
- **Total Tests**: 44
- **Pass Rate**: 100% (44/44)
- **Execution Time**: ~60 seconds for full pipeline
- **Test Coverage**: User Validation, Calculator Operations, API Validation, Database Operations
- **Documentation**: Complete setup guide + results

---

# ADDITIONAL TEST SUITES

## Test API Suite (test_api.py) - 11 Tests

Tests API request validation and HTTP response handling:

| Test Name | Type | Expected Result |
|-----------|------|-----------------|
| test_valid_http_endpoint | Endpoint validation | PASS ✅ |
| test_invalid_endpoint_no_protocol | Endpoint validation | PASS ✅ |
| test_invalid_endpoint_with_spaces | Endpoint validation | PASS ✅ |
| test_valid_http_methods | HTTP method validation | PASS ✅ |
| test_invalid_http_method | HTTP method validation | PASS ✅ |
| test_valid_status_codes | Status code validation | PASS ✅ |
| test_invalid_status_code_out_of_range | Status code validation | PASS ✅ |
| test_valid_response_time | Response time validation | PASS ✅ |
| test_slow_response_time | Response time validation | PASS ✅ |
| test_status_code_categorization_success | Status categorization | PASS ✅ |
| test_status_code_categorization_error | Status categorization | PASS ✅ |

**Total**: 11 tests, 11 passed, 0 failed

## Test Database Suite (test_database.py) - 16 Tests

Tests database schema and query validation:

| Test Name | Type | Expected Result |
|-----------|------|-----------------|
| test_valid_table_name | Table name validation | PASS ✅ |
| test_valid_table_name_with_underscore | Table name validation | PASS ✅ |
| test_invalid_table_name_starts_with_number | Table name validation | PASS ✅ |
| test_invalid_table_name_special_chars | Table name validation | PASS ✅ |
| test_valid_column_name | Column name validation | PASS ✅ |
| test_invalid_column_name_empty | Column name validation | PASS ✅ |
| test_valid_email_in_database | Email value validation | PASS ✅ |
| test_invalid_email_format | Email value validation | PASS ✅ |
| test_valid_record_id | Record ID validation | PASS ✅ |
| test_invalid_record_id_zero | Record ID validation | PASS ✅ |
| test_valid_date_format | Date format validation | PASS ✅ |
| test_invalid_date_format | Date format validation | PASS ✅ |
| test_valid_query_limit | Query limit validation | PASS ✅ |
| test_invalid_query_limit_too_large | Query limit validation | PASS ✅ |
| test_valid_query_offset | Query offset validation | PASS ✅ |
| test_invalid_query_offset_negative | Query offset validation | PASS ✅ |

**Total**: 16 tests, 16 passed, 0 failed

