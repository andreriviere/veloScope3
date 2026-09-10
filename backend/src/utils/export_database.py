import os
from pathlib import Path

import dotenv

from dao.db_connection import DBConnection


class ExportDatabase:
    def __init__(self):
        self.base_path = Path(__file__).resolve().parent.parent.parent.parent
        self.output_path = self.base_path / "data" / "pop_db.sql"

    def run(self):
        dotenv.load_dotenv()

        schema = os.environ["POSTGRES_SCHEMA"]

        tables = [
            "player",
            "game",
        ]

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                with open(self.output_path, "w", encoding="utf-8") as file:
                    for table in tables:
                        cursor.execute(f"SELECT * FROM {schema}.{table}")

                        rows = cursor.fetchall()

                        if not rows:
                            continue

                        columns = list(rows[0].keys())

                        file.write(f"\n-- Data for {table}\n")

                        for row in rows:
                            values = []

                            for column in columns:
                                value = row[column]

                                if value is None:
                                    values.append("NULL")
                                elif isinstance(value, str):
                                    value = value.replace("'", "''")
                                    values.append(f"'{value}'")
                                else:
                                    values.append(str(value))

                            file.write(
                                f"INSERT INTO {table} "
                                f"({', '.join(columns)}) "
                                f"VALUES ({', '.join(values)});\n"
                            )

        print(f"Database exported to {self.output_path}")


if __name__ == "__main__":
    ExportDatabase().run()
