# Bank Statement Parser Backend

A Django-based backend for parsing bank statements from various financial institutions.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Testing the API](#testing-the-api)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)
- [Sample Test Files](#sample-test-files)
- [Next Steps](#next-steps)

## Prerequisites
- Python 3.9+
- PostgreSQL
- [Poetry](https://python-poetry.org/docs/#installation)

## Setup Instructions

### Clone and Navigate
```bash
git clone your-repo-url
cd financial-insights/backend
```

### Install Dependencies
```bash
poetry install
```

### Activate Virtual Environment
```bash
poetry shell
```

### Configure PostgreSQL
1. Start PostgreSQL server
2. Create a database and user:
```sql
CREATE DATABASE bank_parser;
CREATE USER parser_user WITH PASSWORD 'dev_password';
ALTER ROLE parser_user SET client_encoding TO 'utf8';
ALTER ROLE parser_user SET default_transaction_isolation TO 'read committed';
GRANT ALL PRIVILEGES ON DATABASE bank_parser TO parser_user;
```
3. Run Migrations
```bash
python manage.py migrate
```
4. Start Development Server
```bash
python manage.py runserver
```

### Test API
Using curl
```bash
curl -X POST -F "file=@/path/to/chase_statement.pdf" http://localhost:8000/upload/
```

### Potential Issues
**PostgreSQL Connection Issues**
```bash
# Check PostgreSQL status
sudo service postgresql status

# Test connection
psql -h localhost -U parser_user -d bank_parser
```
**Dependency Issues**
```bash
# Re-sync dependencies
poetry install --sync
```

**File Upload Permissions**
```bash
mkdir -p media
chmod 755 media
```

## Next Steps
Implement JWT authentication
Add frontend integration
Support additional banks (Capital One, USBank)
Add data visualization endpoints
Containerize
