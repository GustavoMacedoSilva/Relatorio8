from database import Database
from query import Query
from teacherCRUD import TeacherCRUD
db = Database("bolt://3.236.184.254:7687", "neo4j", "wholesales-sled-stoves")
teacher_crud = TeacherCRUD(db)
#criei os nodes direto no neo4j sandbox usando o txt disponibilizado no exercicio como dito no video q era pra fazer

querry = Query(db)
#Questao 1
print(querry.get_professor("Renzo")) #a
print(querry.get_professor_starts_with("M")) #b
print(querry.get_city()) #c
print(querry.get_school_where_number_grater_and_lower()) #d

#Questao 2
print(querry.get_teacher_max_age_and_min_age()) #a
print(querry.media_population()) #b
print(querry.city_cep()) #c
print(querry.teacher_third_letter()) #d

#Questao 3
teacher_crud.create_teacher("Chris Lima", 1956, "189.052.396-66") #b
print(teacher_crud.read_teacher("Chris Lima")) #c
teacher_crud.update_teacher("Chris Lima", "162.052.777-77") #d
