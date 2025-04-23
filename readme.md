# Assignment 10 – FastAPI QA Testing & Bug Fixes

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tushar140498/IS601_Assignment10.git
   cd IS601_Assignment10
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start services using Docker Compose**
   ```bash
   docker compose up --build
   ```

5. **Run tests with coverage**
   ```bash
   docker compose exec fastapi pytest --cov=app --cov-report=term-missing
   ```

## Closed Issues (Bug Fixes)

Here are the 6 issues I identified, fixed, tested, and merged:

1. **Bug #1:** [Swagger example mismatch](https://github.com/Tushar140498/IS601_Assignment10/issues/1)  
   *Fixed mismatches in login and registration example schemas.*

2. **Bug #2:** [Missing `nickname` field and weak password regex](https://github.com/Tushar140498/IS601_Assignment10/issues/2)  
   *Added `nickname` and improved password validation logic.*

3. **Bug #3:** [Missing test fixture for invalid email](https://github.com/Tushar140498/IS601_Assignment10/issues/3)  
   *Added `invalid_email_user_data` fixture for test coverage.*

4. **Bug #4:** [Duplicate `role` values in UserListResponse](https://github.com/Tushar140498/IS601_Assignment10/issues/4)  
   *Removed duplicates and corrected sample user role values.*

5. **Bug #5:** [Missing fields in test fixtures vs schema](https://github.com/Tushar140498/IS601_Assignment10/issues/5)  
   *Ensured test fixture data includes `nickname`, `first_name`, `last_name`, etc.*

6. **Bug #6:** [Email service tests and SMTP mocking](https://github.com/Tushar140498/IS601_Assignment10/issues/6)  
   *Wrote tests for `send_user_email`, mocked SMTP errors, validated HTML content, and handled template rendering errors.*

## Docker Image

You can find the deployed Docker image here:  
 **[DockerHub - tushar140498/assignment10](https://hub.docker.com/repository/docker/tushar140498/assignment10/general)**

To pull the image:
```bash
docker pull tushar140498/assignment10
```

## Test Coverage Report

To check test coverage, run:

```bash
docker compose exec fastapi pytest --cov=app --cov-report=term-missing
```
As of the final commit, test coverage is: 88%


## Reflection

Through this assignment, I deepened my understanding of schema validation, test-driven development, and real-world bug resolution using FastAPI and SQLAlchemy. Fixing issues like invalid regex patterns, missing test data, and misaligned examples taught me the importance of consistent schema and API documentation.

On the collaborative side, I practiced structured Git workflows: creating feature branches, linking issues to pull requests, and using proper commit hygiene. Writing meaningful test cases not only improved coverage (88%) but also made the app more robust. I also explored mocking email services and handling edge cases in Markdown templates, which was new and exciting.

This assignment highlighted how critical QA and testing are in the software lifecycle — not just to verify correctness, but to ensure the application behaves reliably in real scenarios. The debugging experience was hands-on, and I now feel more confident in contributing to production-level backend services.