import sqlglot
from sqlglot import expressions as exp

class QueryTranslator:
    def __init__(self):
        self.type_mapping = self._load_type_mapping()
    
    def translate(self, query):
        try:
            return sqlglot.transpile(
                query,
                read="tsql",
                write="postgres",
                identify=True,
                mappings={
                    "@@ROWCOUNT": "ROW_COUNT",
                    "GETDATE()": "CURRENT_TIMESTAMP",
                    "TOP": "LIMIT"
                },
                transforms={
                    "dbo.": "public.",
                    "[": "\"",
                    "]": "\""
                }
            )[0]
        except sqlglot.errors.ParseError as e:
            raise TranslationError(f"Query translation failed: {str(e)}")

    def _load_type_mapping(self):
        return {
            'datetime': 'timestamp',
            'uniqueidentifier': 'uuid',
            'varbinary(max)': 'bytea',
            'money': 'numeric(19,4)'
        }
