import sqlite3
from pathlib import Path
import sqlite3
from tools.tools import AgentTool


class ExecuteSQLTool(AgentTool):
    def get_name(self) -> str:
        return "execute_sql"

    def get_description(self) -> str:
        return """
Execute SQL statements against a database.

The tool:
- executes SELECT
- supports multi-statement scripts,

Returns structured results for agent recovery.
"""

    def get_parameters(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "SQL query execute.",
                },
            },
            "required": [
                "query",
            ],
        }

    def execute(self, parameters: dict) -> dict:
        query = parameters.get("query")

        if not query:
            return {
                "success": False,
                "error": "missing_required_field",
                "field": "query",
                "message": "query is required",
            }

        conn = None

        try:

            CURRENT_DIR = Path(__file__).resolve().parent.parent
            DB_PATH = CURRENT_DIR / "accidents_database.db"

            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            import streamlit as st
            st.write(DB_PATH)
            sql = query.strip()

            if sql.lower().startswith("select"):
                cursor.execute(sql)

                columns = [c[0] for c in cursor.description]
                rows = cursor.fetchall()

                results = [
                    dict(zip(columns, row))
                    for row in rows
                ]

                return {
                    "success": True,
                    "type": "select",
                    "row_count": len(results),
                    "columns": columns,
                    "rows": results,
                }

            else:
                return {
                    "success": False,
                    "error": "system_error",
                    "message": "You are allowed only to use SELECT command",
                }

        except sqlite3.Error as e:
            return {
                "success": False,
                "error": "sql_error",
                "message": str(e),
            }

        except Exception as e:
            return {
                "success": False,
                "error": "unexpected_error",
                "message": str(e),
            }

        finally:
            if conn:
                conn.close()
