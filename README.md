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

This uses:
- `├──` for branches with subsequent items
- `└──` for the last item in a level
- `│` characters for vertical connections
- 3-space indentation for each nesting level
- Comments added directly in-line with `#` notation
### Key Features Summary

#### Sybase-to-PostgreSQL Proxy
        TDS protocol implementation
        SQL translation with SQLGlot
        Optional SSL encryption
        Connection pooling
#### Web Application
        Migration configuration UI
        Real-time progress monitoring
        User authentication
        Audit logging
#### Migration Tools
        Schema conversion
        Data migration
        Stored procedure translation
        Type mapping
#### Authentication System
        SQLite user database
        JWT token management
        Role-based access
        Password hashing
#### Deployment
        Single Docker image
        Multi-port exposure (1433, 8000)
        Environment variable configuration
        Health checks
        
