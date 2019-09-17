Description:
    The tiny python application of movie database that perfectly lends itself to numerous tests of any platform.
    
1. Clone the repository:
    
    git clone https://github.com/Kartoshnikov/MovieDB.git
    
2. Enter into the directory:

    cd MovieDB

3. Build and start stack:

    docker-compose up -d

App is running on the port 8081.
Postgres is listening on port 5432 (user: django, passwd: 1111).

MovieDB/app/ is bound with python container's /app directory
postgres/data is bound with postgre container's /var/lib/postgresql/data
