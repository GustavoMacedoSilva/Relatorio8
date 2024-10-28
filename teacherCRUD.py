from database import Database

class TeacherCRUD:
    def __init__(self, database):
        self.db = database
        
    def create_teacher(self, name, ano_nasc, cpf):
        query = "CREATE (p:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf,}
        self.db.execute_query(query, parameters)
        
    def read_teacher(self, name):
        query = "MATCH (p:Teacher) WHERE p.name= $name RETURN p.ano_nasc AS ano_nasc, p.cpf AS cpf LIMIT 1"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(name, result["ano_nasc"], result["cpf"]) for result in results]
    
    def delete_teacher(self, name):
        query = "MATCH (p:Teacher) WHERE p.name= $name DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        
    def update_teacher(self, name, cpf):
        query = "MATCH (p:Teacher) WHERE p.name= $name SET p.cpf = $cpf"
        parameters = {"name": name, "cpf": cpf}
        self.db.execute_query(query, parameters)