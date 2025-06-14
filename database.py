import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    password="My@sql1",
    database="bank"
)

def db_query(query):
    cursor = mydb.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def db_execute(query, params=None):
    cursor = mydb.cursor()
    cursor.execute(query, params)
    mydb.commit()

def db_fetch(query, params=None):
    cursor = mydb.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

def create_customers_table():
    cursor = mydb.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            account_number INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(20) UNIQUE,
            password VARCHAR(255),
            name VARCHAR(50),
            age INT,
            city VARCHAR(50),
            balance INTEGER NOT NULL,
            status BOOLEAN
        )
    ''')
    mydb.commit()
    print("Customer table created or already exists.")

def create_transactions_table():
    query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50),
        type VARCHAR(20),
        amount DECIMAL(10, 2),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    db_execute(query)

if __name__ == "__main__":
    create_customers_table()
