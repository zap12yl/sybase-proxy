# Sybase proxy to Postgresql database backend

## Project Structure

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

### Key Features Summary

####Sybase-to-PostgreSQL Proxy
        TDS protocol implementation
        SQL translation with SQLGlot
        Optional SSL encryption
        Connection pooling
####Web Application
        Migration configuration UI
        Real-time progress monitoring
        User authentication
        Audit logging
####Migration Tools
        Schema conversion
        Data migration
        Stored procedure translation
        Type mapping
####Authentication System
        SQLite user database
        JWT token management
        Role-based access
        Password hashing
####Deployment
        Single Docker image
        Multi-port exposure (1433, 8000)
        Environment variable configuration
        Health checks
        
