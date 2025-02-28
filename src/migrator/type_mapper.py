import yaml

class TypeMapper:
    def __init__(self, config_path="config/type_mappings.yaml"):
        with open(config_path) as f:
            self.mappings = yaml.safe_load(f)
    
    def map(self, sybase_type):
        return self.mappings['type_mappings'].get(
            sybase_type.lower(), 
            'varchar'
        )
