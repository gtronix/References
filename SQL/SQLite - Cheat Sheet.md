### SQLite Cheat Sheet

#### Basic Commands

- **Create a Database**
  ```sql
  sqlite3 database_name.db
  ```

- **Create a Table**
  ```sql
  CREATE TABLE table_name (
      column1 datatype PRIMARY KEY,
      column2 datatype,
      column3 datatype
  );
  ```

- **Insert Data**
  ```sql
  INSERT INTO table_name (column1, column2) VALUES (value1, value2);
  ```

- **Select Data**
  ```sql
  SELECT column1, column2 FROM table_name;
  ```

- **Update Data**
  ```sql
  UPDATE table_name SET column1 = value1 WHERE condition;
  ```

- **Delete Data**
  ```sql
  DELETE FROM table_name WHERE condition;
  ```

#### Data Types

- `INTEGER`: A signed integer.
- `REAL`: A floating point value.
- `TEXT`: A string.
- `BLOB`: A binary large object.

#### Query Clauses

- **WHERE Clause**
  ```sql
  SELECT * FROM table_name WHERE condition;
  ```

- **ORDER BY Clause**
  ```sql
  SELECT * FROM table_name ORDER BY column1 ASC|DESC;
  ```

- **LIMIT Clause**
  ```sql
  SELECT * FROM table_name LIMIT number;
  ```

- **GROUP BY Clause**
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1;
  ```

- **HAVING Clause**
  ```sql
  SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > value;
  ```

#### Joins

- **INNER JOIN**
  ```sql
  SELECT columns FROM table1 INNER JOIN table2 ON table1.column = table2.column;
  ```

- **LEFT JOIN**
  ```sql
  SELECT columns FROM table1 LEFT JOIN table2 ON table1.column = table2.column;
  ```

#### Indexes

- **Create an Index**
  ```sql
  CREATE INDEX index_name ON table_name (column1);
  ```

- **Drop an Index**
  ```sql
  DROP INDEX index_name;
  ```

#### Transactions

- **Begin a Transaction**
  ```sql
  BEGIN TRANSACTION;
  ```

- **Commit a Transaction**
  ```sql
  COMMIT;
  ```

- **Rollback a Transaction**
  ```sql
  ROLLBACK;
  ```

#### Miscellaneous

- **Show Tables**
  ```sql
  .tables
  ```

- **Show Schema of a Table**
  ```sql
  .schema table_name
  ```

- **Exit SQLite**
  ```sql
  .exit
  ```
