# 320-Movies

## Getting Started

To get started please follow these steps:

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/your-username/320-Movies.git
    ```
2. Before making any changes, run the following command to ignore changes to the config.py file:
    ```
    git update-index --skip-worktree config.py
    ```
This command will prevent any local changes to the config.py file from being tracked by Git.

## Change the Config File
1. Navigate to the config file and change the username/password to your ssh credentials. 

2. (Optional) To test if working please copy and paste the following code in main after cursor has been assigned and comment out anything after:
```
# Query Connection Test (should return 8 columns and datatypes for table users)
try:
	cursor.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'users';")
	columns_info = cursor.fetchall()
	
	print(f"Columns in Table 'users':")
	for column_info in columns_info:
		column_name, data_type = column_info
		print(f"{column_name}: {data_type}")
except psycopg2.Error as e:
	print("Error executing query:", e)
finally:
	cursor.close()
	connection.close()
```


