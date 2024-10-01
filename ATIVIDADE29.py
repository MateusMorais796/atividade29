# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

alunos_presentes = []

while True:
    aluno = input('Digite o nome do aluno presente (digite "0" para parar: ) ')
    alunos_presentes.append(aluno)
    if aluno == '0':
        alunos_presentes.remove("0")
        break
   
alunospresentes = len(alunos_presentes)

if alunospresentes <5:
    print('Revise a lista')

print(f'Aluno presentes: {alunospresentes}')
print(f'Lista de alunos presentes: {alunos_presentes}')