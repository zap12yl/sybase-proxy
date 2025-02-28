# Sybase proxy to Postgresql database backend

## Project Structure

```markdown
sybase-migration-proxy/
├── src/
│   ├── proxy/
│   │   ├── tds_handler.py        # TDS protocol handling
│   │   ├── query_translator.py   # SQL translation
│   │   └── auth_handler.py       # Authentication
│   ├── webapp/
│   │   ├── backend/              # FastAPI
│   │   │   ├── api/
│   │   │   ├── auth/
│   │   │   └── migrations/
│   │   └── frontend/             # React
│   ├── migrator/                 # Migration tools
│   └── database.py               # SQLite ORM
├── config/
│   ├── type_mappings.yaml
│   ├── ad_config.yaml
│   └── ssl/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```
### Key Features Summary
#### 1. Sybase-to-PostgreSQL Proxy
        TDS protocol implementation
        SQL translation with SQLGlot
        Optional SSL encryption
        Connection pooling
#### 2. Web Application
        Migration configuration UI
        Real-time progress monitoring
        User authentication
        Audit logging
#### 3. Migration Tools
        Schema conversion
        Data migration
        Stored procedure translation
        Type mapping
#### 4. Authentication System
        SQLite user database
        JWT token management
        Role-based access
        Password hashing
#### 5. Deployment
        Single Docker image
        Multi-port exposure (1433, 8000)
        Environment variable configuration
        Health checks
#### 6. Key Configuration Options
Environment Variable	Default	Description
PG_HOST	localhost	PostgreSQL server address
PG_PORT	5432	PostgreSQL port
SSL_ENABLED	false	Enable TLS encryption
AD_SERVER	-	Active Directory server (optional)
JWT_SECRET	random	JWT signing key
SQLITE_PATH	/app/data/db	User database path
