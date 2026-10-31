import os
import duckdb
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAYERS = ["ods", "dwd", "dws", "ads"]

def main():
    os.chdir(ROOT)  # 保证 SQL 里的相对路径都从项目根目录算
    con = duckdb.connect("warehouse.duckdb")
    for layer in LAYERS:
        con.execute(f"CREATE SCHEMA IF NOT EXISTS {layer}")
        for sql_file in sorted((ROOT / "sql" / layer).glob("*.sql")):
            print(f"running {layer}/{sql_file.name}")
            con.execute(sql_file.read_text(encoding="utf-8"))
    con.close()
    print("all done")

if __name__ == "__main__":
    main()
