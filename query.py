from database import Database

class Query:
    def __init__(self, database):
        self.db = database
        

    def get_professor(self, name):
        query = "MATCH (p:Teacher) WHERE p.name= $name RETURN p.ano_nasc AS ano_nasc, p.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [(result["ano_nasc"], result["cpf"]) for result in results]
    
    def get_professor_starts_with(self, letra):
        query = "MATCH (p:Teacher) WHERE p.name STARTS WITH $letra RETURN p.name AS name , p.cpf AS cpf"
        parameters = {"letra": letra}
        results = self.db.execute_query(query, parameters)
        return [(result["name"], result["cpf"]) for result in results]
    

    def get_city(self):
        query = "MATCH (c:City) RETURN c.name AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def get_school_where_number_grater_and_lower(self):
        query = "MATCH (s:School) WHERE s.number >= 150 AND s.number <=550  RETURN s.name AS name, s.address AS address, s.number AS number"
        results = self.db.execute_query(query)
        return [(result["name"], result["address"], result["number"]) for result in results]
    
    def get_teacher_max_age_and_min_age(self):
        query1 = "MATCH (t:Teacher) RETURN MAX(t.ano_nasc) AS max_ano_nasc, t.name AS name ORDER BY max_ano_nasc DESC LIMIT 1"
        results1 = self.db.execute_query(query1)
        query2 = "MATCH (t:Teacher) RETURN MIN(t.ano_nasc) AS min_ano_nasc, t.name AS name ORDER BY min_ano_nasc ASC LIMIT 1"
        results2 = self.db.execute_query(query2)
        return [(result["name"], result["max_ano_nasc"]) for result in results1], [(result["name"], result["min_ano_nasc"]) for result in results2]
    
    
    def media_population(self):
        query = "MATCH (c:City) RETURN AVG(c.population) AS media"
        results = self.db.execute_query(query)
        return [result["media"] for result in results]
    
    def city_cep(self):
        query = "MATCH (c:City) WHERE c.cep='37540-000' RETURN REPLACE(c.name, 'a', 'A') AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]
    
    def teacher_third_letter(self):
        query = "MATCH (t:Teacher) RETURN RIGHT(LEFT(t.name, 3), 1) AS name"
        results = self.db.execute_query(query)
        return [result["name"] for result in results]