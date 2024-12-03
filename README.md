# menu-dinamico-cli

comandos para levantar la base de datos

primero crea la red para conectarte desde python
```bash
docker network create menu-cli-network
```

despues crea la base de datos
```bash
docker run --detach --name menu-cli-db --network menu-cli-network -p 3306:3306 --env MARIADB_ROOT_PASSWORD=pato1324  mariadb:10.5
```

y con este comando puedes entrar a la base de datos y ejecutar los comandos del archivo `ddl.sql`
```bash
docker run -it --network menu-cli-network --rm mariadb mariadb:10.5 -hmenu-cli-db -uroot -p
```
