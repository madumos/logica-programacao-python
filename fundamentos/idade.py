idade = int(input('Qual a sua idade? '))

def aposentadoria(i):

    if i>=62:
        print('Você pode se aposentar.')
    else:
        print('Você é novo demais pra se aposentar.')

aposentadoria(idade)
  