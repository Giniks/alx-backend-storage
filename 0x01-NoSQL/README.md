## Project Topic: NoSQL

## Project Overview:

This repository contains scripts for performing various tasks with MongoDB.

## Table of Contents

1. [List all databases](#list-all-databases)
2. [Create a database](#create-a-database)
3. [Insert document](#insert-document)
4. [All documents](#all-documents)
5. [All matches](#all-matches)
6. [Count](#count)
7. [Update](#update)
8. [Delete by match](#delete-by-match)
9. [List all documents in Python](#list-all-documents-in-python)
10. [Insert a document in Python](#insert-a-document-in-python)
11. [Change school topics](#change-school-topics)
12. [Schools by topic](#schools-by-topic)
13. [Log stats](#log-stats)

## 1. List all databases

### Description
This script lists all databases in MongoDB.

```bash
$ cat 0-list_databases | mongo
```

## 2. Create a database

### Description
This script creates or uses the database my_db.

```bash
$ cat 1-use_or_create_database | mongo
```

## 3. Insert document

### Description
This script inserts a document in the collection school.

```bash
$ cat 2-insert | mongo my_db
```

...

## Author
- Name: Ginika Elizabeth Nna
- Email: elizabethginika9@gmail.com

## Acknowledgments
Special thanks toAlx community for providing the project requirements.
