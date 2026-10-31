import sys
import duckdb

con = duckdb.connect("warehouse.duckdb", read_only=True)
print(con.sql(sys.argv[1]))
