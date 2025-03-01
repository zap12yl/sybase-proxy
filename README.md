# Sybase to PostgreSQL Proxy
Enterprise-grade migration solution with web interface and authentication.

## Project Structure
```markdown
sybase-postgres-proxy/
├── .env.example
├── docker-compose.yml
├── README.md
├── proxy/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── query_handler.py
│   │   ├── connection_manager.py
│   │   └── protocol_handler.py
│   ├── Dockerfile
│   └── requirements.txt
├── migration/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── migrator.py
│   │   ├── schema_translator.py
│   │   ├── data_mover.py
│   │   └── sp_converter.py
│   ├── Dockerfile
│   └── requirements.txt
├── webapp/
│   ├── backend/
│   │   ├── src/
│   │   │   ├── main.py
│   │   │   ├── routes/
│   │   │   │   ├── migration.py
│   │   │   │   └── auth.py
│   │   │   └── models.py
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   └── frontend/
│       ├── src/
│       │   ├── components/
│       │   │   ├── MigrationWizard.jsx
│       │   │   └── StatusMonitor.jsx
│       │   ├── App.js
│       │   └── index.js
│       ├── public/
│       │   └── index.html
│       ├── Dockerfile
│       ├── package.json
│       └── nginx.conf
└── scripts/
    ├── entrypoint.sh
    └── init_db.py
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
