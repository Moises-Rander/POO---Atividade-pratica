from person import Person

people = []
while True:
    list_length = input('Quantas pessoas serão registradas? ')
    if list_length.isnumeric():
        list_length = int(list_length)
        break
    else:
        print('Por favor, digite um número.')

        
def cpfvalidation(cpf):
    if len(cpf) == 11:
        validador = True
        for i in range(len(cpf)):
            if cpf[i] not in '0123456789':
                validador = False
        return validador
    else:
        return False


def datainput():
    for i in range(list_lenght):
        while True:
            name_aux = input(f'\nInforme o nome da {i+1}ª pessoa: ').strip().title()
            if name_aux.replace(' ', '').isalpha():
                break
            else:
                print('Por favor, digite o seu nome utilizando apenas letras.\n')
        while True:
            age_aux = input(f'Informe a idade da {i + 1}ª pessoa: ').replace(' ', '')
            if age_aux.isnumeric():
                break
            else:
                print('Por favor, digite a sua idade utilizando apenas números.\n')
        while True:
            cpf_aux = input(f'Informe o CPF da {i+1}ª pessoa: ').replace('.', '').replace('-', '').replace(' ', '')
            if cpfvalidation(cpf_aux):
                break
            else:
                print('Por favor, digite o seu CPF utilizando apenas números.\n')
        people.append(Person(name_aux, age_aux, cpf_aux))


def dataprint():
    index = 1
    for obj in people:
        print(f'\nO nome da {index}ª pessoa: {obj.name}')
        print(f'A idade da {index}ª pessoa: {int(obj.age)}')
        print(f'O CPF da {index}ª pessoa: {obj.cpf[:3]}.{obj.cpf[3:6]}.{obj.cpf[6:9]}-{obj.cpf[9:]}\n')
        index += 1


datainput()
dataprint()
