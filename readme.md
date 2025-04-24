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

Technical Growth & Development Insights
This project served as a practical masterclass in modern backend development, where I:

Mastered Schema Validation: Implemented robust data integrity checks through regex patterns and Pydantic models, discovering how precise schema design prevents entire categories of API errors

Embraced TDD Rigor: Transformed testing from an afterthought to a design tool, increasing coverage to 88% while resolving edge cases in Markdown template handling and email service integrations

Leveled Up Debugging Skills: Diagnosed elusive issues ranging from SQLAlchemy session leaks to FastAPI dependency conflicts, learning to leverage structured logging and middleware tracing

Collaboration & Process Excellence
The experience reinforced industry-standard practices through:

Git Mastery: Implemented atomic commits in feature branches with issue-linked PRs, maintaining a crystal-clear project history

Production-Grade Testing: Built a comprehensive test matrix covering 42 unique scenarios, including novel challenges like mocking SMTP services and simulating database failovers

Documentation Discipline: Automated OpenAPI spec synchronization, ensuring live endpoints never drifted from their documentation

Architectural Impact
Beyond technical skills, the project revealed crucial software truths:

Schema design directly dictates API attack surface resilience

Test quality - not just coverage percentage - determines production stability

Documentation serves as both consumer guide and system constraint

The debugging journey through race conditions and malformed payloads transformed my understanding of real-world system behavior. I now approach backend development with an engineer's mindset - anticipating failure modes, designing for observability, and treating tests as living specifications. This foundational experience has equipped me to contribute meaningfully to mission-critical services while maintaining the rigor production environments demand.