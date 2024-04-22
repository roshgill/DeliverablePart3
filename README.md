# DeliverablePart3

## Introduction
This repository contains the SQL and Python code for managing a PostgreSQL database.

## Technologies
This project uses:
- **PostgreSQL**: A open source object-relational database system.
- **pgAdmin 4**: A web-based admin tool for PostgreSQL.
- **SQL**: Used for creating and managing the database structures (DDL/DML commands).
- **Python**: Utilized to create a user friendly CLI for database interaction.

----

## Getting Started

### Pre-Reqs
Before you can run the SQL scripts and Python code in this repository, you need to set up PostgreSQL with pgAdmin4. I recommend downloading the PostgreSQL package (which includes pgAdmin4) from a postgreSQL verified source provided by the EnterpriseDB (EDB) team.

### Installation Instructions

1. **Download PostgreSQL with pgAdmin4**:
   - Visit the official EnterpriseDB download page at [EDB Downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).
   - Select the version of PostgreSQL you wish to install. Make sure it matches your operating system's architecture.

2. **Set Up PostgreSQL**:
   - Once installed, launch pgAdmin4 and set up your connection to the local PostgreSQL server.

3. **Database Setup**:
   - In the Github repository, locate the 'createtables.sql' file containing the DDL (Data Definition Language) code. This file includes all necessary commands to create the tables required for this project.
   - Open pgAdmin4, connect to your database, and open the Query Tool.
   - Load the SQL file and execute the script to create your database schema.

### Uploading Data

Here's an added section to your README file that explains how to upload data from the CSV files of the Brazilian E-Commerce Public Dataset by Olist into each corresponding table in your PostgreSQL database. This section assumes that your tables have already been created using the provided SQL script.

## Data Import

### Source Dataset
The data for this project is from the [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=product_category_name_translation.csv) available on the Kaggle website. This dataset includes several CSV files, each containing data that correlates with a specific table in our PostgreSQL database.

### Pre-Reqs for Data Import
Before importing the data, ensure that:
- All required tables are created in your PostgreSQL database using the 'createtables.sql' file.
- You have downloaded the CSV files from the Kaggle link provided above.

### Steps to Import Data

1. **Download and Prepare the Data**:
   - Go to the [dataset page on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce?select=product_category_name_translation.csv) and download the zip file containing all the CSV files.

2. **Import CSV Files to PostgreSQL**:
   - Open pgAdmin4 and connect to your database.
   - For each CSV file, follow these steps to import the data into the corresponding table:
     - Right-click on the specific table in the pgAdmin dashboard and select the 'Import/Export' option.
     - Choose 'Import' in the dialog box, and browse to select the specific CSV file from your folder.
     - Map the CSV columns to the corresponding table columns in the database.
     - Click 'OK' to start importing the data.

----

## Executing the Python CLI

The Python script DatabaseCLI.py provides a command-line interface (CLI) for interacting with the PostgreSQL database.

### Prerequisites for Running the CLI

Before running the file, ensure that:
- Python 3 is installed on your system.
- `psycopg2` is installed. This can be done with pip:
  ```bash
  pip install psycopg2
  ```
- PostgreSQL is installed, running, and is available from your local machine at `localhost` on port `5432`.
- The database `postgres` exists with a user `postgres`.

### How to Execute

1. **Open your terminal.**

2. **Navigate to the directory containing `DatabaseCLI.py`:**

3. **Execute the script using Python 3:**
   ```bash
   python3 DatabaseCLI.py
   ```

### Using the Database CLI Interface

The CLI presents a menu of 11 options, each performing a unique SQL operation.:

- **1. Insert a New Customer From Sao Paulo**: Adds a new customer record into the Customer table.
- **2. Remove All Payments From the Payment Table made with vouchers**: Deletes records from the Payment table where the payment type is 'voucher'.
- **3. Update All Sellers Located in Campinas to Sao Paulo**: Updates records in the Seller table, changing the city from Campinas to Sao Paulo.
- **4. Search for All Customers Located in the City of Franca**: Retrieves and displays all customers located in Franca.
- **5. Calculate the Average Payment Value from All Recorded Payments**: Calculates and displays the average value of all payments.
- **6. Sort Payment Table Based off Recorded Payments in Descending Order**: Displays payments sorted by value in descending order.
- **7. Join the Customer and Order tables for Customers who have Placed Orders**: Displays customer IDs for those who have placed orders.
- **8. Show Product Weights and their Counts, Grouped by Weight**: Displays counts of products grouped by their weight.
- **9. Select Order IDs with 5 Star Reviews**: Retrieves order IDs that have received 5-star reviews.
- **10. Add a New Product Category 'Electrodomésticos' (Appliances) and List a New Item In The Product Table**: Inserts a new category and a new product associated with this category.
- **11. Exit**: Exits the CLI.

After making a selection, the results of the operation will be printed on the screen. The CLI loop allows for multiple operations during a single session.

### Note (Important)

Make sure to refactor password variable within 'connect_db' function to match the password you have created for the database.
