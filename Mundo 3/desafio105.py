def notas(*n, sit=False):
    print('=='*30)
    dic = {}
    dic['Quantidade de notas'] = len(n)
    count = 0
    soma = 0
    for c in n:
        count+=1
        soma+=c
        if count == 1:
            dic['maior nota'] = c
            dic['menor nota'] = c
        elif c > dic['maior nota']:
            dic['maior nota'] = c
        elif c < dic['menor nota']:
            dic['menor nota'] = c
        dic['media da turma'] = soma / len(n)
    if sit == True:
        if dic['media da turma'] < 6:
            dic['situacao'] = 'RUIM'
        elif dic['media da turma'] > 6 and dic['media da turma'] < 7:
            dic['situacao'] = 'RAZOAVEL'
        else:
            dic['situacao'] = 'BOA'
    print(dic)
    print('=='*30)
notas(2,3,5,10,15, sit=True)
notas(6,7,2,4.16,15)