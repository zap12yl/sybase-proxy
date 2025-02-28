class DataMigrator:
    def __init__(self, source_conn, target_conn, batch_size=1000):
        self.source = source_conn
        self.target = target_conn
        self.batch_size = batch_size
    
    async def migrate_table(self, table_name):
        count = await self.source.fetchval(f"""
            SELECT COUNT(*) FROM {table_name}
        """)
        
        for offset in range(0, count, self.batch_size):
            rows = await self.source.fetch(f"""
                SELECT * FROM {table_name}
                ORDER BY 1
                OFFSET {offset} ROWS
                FETCH NEXT {self.batch_size} ROWS ONLY
            """)
            
            await self.target.copy_records(table_name, rows)
