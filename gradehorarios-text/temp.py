DIAS = ["SEG", "TER", "QUA", "QUI", "SEX"]
TURNOS = {
    "M" : ["AB", "CD"],
    "T" : ["AB", "CD"],
    "N" : ["AB", "CD"],
}


grade = {}

for dia in DIAS:
    grade[dia] = {}

    for turno in TURNOS:
        grade[dia][turno] = {}

        for slot in TURNOS[turno]:
            grade[dia][turno][slot] = None #Aula(None, None, None)

for k, v in grade.items():
    print(k, v)