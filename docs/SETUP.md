# Setup Instructions
    Clone Repository
```
git clone https://github.com/fadjar340/sybase-postgres-proxy
cd sybase-postgres-proxy
```
# Initialize Environment

```
cp .env.example .env
mkdir -p config/ssl
```
# Generate SSL Certificates (Optional)

```
openssl req -x509 -newkey rsa:4096 -keyout config/ssl/proxy.key \
  -out config/ssl/proxy.crt -days 365 -nodes
```

# Create Htpasswd File

```
htpasswd -cB config/users.htpasswd admin
```

# Build & Start

```
docker-compose -f docker/docker-compose.yml up --build
```
