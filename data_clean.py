import duckdb

# Connect to the dev.duckdb file
conn = duckdb.connect(r'D:\Tasks\Duck Db\locally\duck_db_project\dev.duckdb')

# Run a query to retrieve data
result = conn.execute("SELECT * FROM main.sales").fetchall()

# Print the results
for row in result:
    print(row)
