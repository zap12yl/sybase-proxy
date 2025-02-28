import asyncpg
from .type_mapper import TypeMapper

class SchemaMigrator:
    def __init__(self, source_conn, target_conn):
        self.source = source_conn
        self.target = target_conn
        self.type_mapper = TypeMapper()
    
    async def migrate_all(self):
        await self.migrate_tables()
        await self.migrate_indexes()
        await self.migrate_views()

    async def migrate_tables(self):
        tables = await self.source.fetch("""
            SELECT name, object_id 
            FROM sysobjects 
            WHERE type = 'U'
        """)
        for table in tables:
            await self.create_table(table['name'])
    
    async def create_table(self, table_name):
        columns = await self.get_columns(table_name)
        pg_ddl = f"CREATE TABLE {table_name} (\n"
        pg_ddl += ",\n".join(
            f"  {col['name']} {self.type_mapper.map(col['type'])}"
            for col in columns
        )
        pg_ddl += "\n);"
        await self.target.execute(pg_ddl)
