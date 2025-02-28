# Sybase to PostgreSQL Proxy
Enterprise-grade migration solution with web interface and authentication.

## Project Structure
```markdown
sybase-postgres-proxy/
├── src/
│   ├── proxy/
│   │   ├── __init__.py
│   │   ├── server.py          # Main proxy server
│   │   ├── tds_handler.py     # TDS protocol handling
│   │   ├── query_translator.py# SQL translation
│   │   └── auth/
│   │       ├── htpasswd.py    # Htpasswd authentication
│   │       └── jwt_handler.py # JWT management
│   ├── webapp/
│   │   ├── backend/
│   │   │   ├── main.py        # FastAPI app
│   │   │   └── routes/
│   │   └── frontend/
│   │       ├── public/
│   │       └── src/
│   ├── migrator/              # Migration tools
│   └── cli.py                 # Command line interface
├── config/
│   ├── type_mappings.yaml     # Data type conversions
│   └── ssl/                   # SSL certificates
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   └── SETUP.md
├── migrations/
│   └── schemas/               # SQL migration scripts
├── .env.example               # Environment template
├── requirements.txt
├── .gitignore
└── README.md
```

### **Key Features**

1. **Authentication Methods**
   - `htpasswd` file-based authentication
   - Environment variable credentials
   - JWT token validation

2. **Migration Tools**
   - Schema conversion
   - Data type mapping
   - Stored procedure translation
   - Batch data migration

3. **Web Interface**
   - Real-time progress monitoring
   - Migration configuration
   - Connection statistics
   - Log viewer

4. **Security**
   - SSL/TLS encryption
   - Password hashing (bcrypt)
   - Role-based access control
   - Token revocation

This structure provides a production-ready solution that can be immediately deployed to GitHub. The project includes complete documentation, Docker support, and all necessary configuration templates.

## Installation

[See detailed setup instructions](docs/SETUP.md)

## Configuration

Environment variables:

| Variable         | Description                |
|------------------|----------------------------|
| PROXY_HOST       | Proxy binding address      |
| PROXY_PORT       | Proxy port (default 1433)  |
| PG_HOST          | PostgreSQL host            |
| HTPASSWD_FILE    | Path to htpasswd file      |

## Usage

```bash
# Connect via Sybase client
tsql -S localhost -U admin -P password -D database

# Access web interface
http://localhost:8000
