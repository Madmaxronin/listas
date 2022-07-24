lista_cursos = ["Python", "Django", "Flask", "Ruby", "Java", "Rust"]
#                   0         1         2       3       4       5

lista_cursos_2 = ["C", "C++", "Docker"]

# [start:end]
# [start:] -> Obtenemos los ultimos elementos de la lista
# [:end]  -> Obtenemos los primeros elementos de la lista
# [start:end:skip] Obtenemos saltos
# [:] Obtenemos toda la lista

print(len(lista_cursos))

sub_lista = lista_cursos[1:]
print(sub_lista)

lista_cursos.append("MongoDB")
lista_cursos.append("C#")
lista_cursos.append("JavaScript")

lista_cursos.insert(1, "Rails")
lista_cursos.insert(0, "PyGame")

lista_cursos.extend(lista_cursos_2)

print(lista_cursos)

lista_cursos.remove("Flask")
del lista_cursos[0]

print(lista_cursos)

lista_cursos.clear()

print(len(lista_cursos))

