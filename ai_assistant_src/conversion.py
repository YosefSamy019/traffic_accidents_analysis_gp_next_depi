# import os
# import sqlite3
# import pandas as pd
#
#
# def csv_to_sqlite(
#     csv_path,
#     db_path="database.db",
#     table_name="data",
#     chunksize=100000,
# ):
#     """
#     Convert a CSV file into a SQLite database.
#
#     Parameters
#     ----------
#     csv_path : str
#         Path to CSV file.
#     db_path : str
#         Output SQLite database.
#     table_name : str
#         SQLite table name.
#     chunksize : int
#         Number of rows per chunk.
#     """
#
#     if not os.path.exists(csv_path):
#         raise FileNotFoundError(csv_path)
#
#     conn = sqlite3.connect(db_path)
#
#     try:
#         first_chunk = True
#
#         for chunk in pd.read_csv(csv_path, chunksize=chunksize):
#
#             chunk.to_sql(
#                 name=table_name,
#                 con=conn,
#                 if_exists="replace" if first_chunk else "append",
#                 index=False,
#             )
#
#             print(f"Imported {len(chunk):,} rows")
#
#             first_chunk = False
#
#         print("\nConversion completed successfully!")
#         print(f"Database : {db_path}")
#         print(f"Table    : {table_name}")
#
#     finally:
#         conn.close()
#
#
# if __name__ == "__main__":
#
#     csv_to_sqlite(
#         csv_path="temp/small_depi projectt.csv",
#         db_path="accidents_database.db",
#         table_name="accidents",
#     )
