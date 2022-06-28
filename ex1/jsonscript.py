import re
import json

pagamentos = '''Fração,Jan,Fev,Mar,Abr,Mai,Jun,Jul,Ago,Set ,Out,Nov,Dez
1Dto,1,1,1,1,,,,,,,,
2Dto,,,,,,,,,,,,
3Dto,1,1,1,1,1,1,1,1,1,1,1,1
4Dto,1,1,1,1,1,1,1,1,1,1,1,1
5Dto,1,1,1,1,1,1,,,,,,
6Dto,1,1,1,1,1,1,1,1,,,,
7Dto,1,1,1,1,,,,,,,,
8Dto,,,,,,,,,,,,
1Esq,1,1,1,,,,,,,,,
3Esq,1,1,1,,,,,,,,,
5Esq,1,1,1,1,,,,,,,,
7Esq,1,1,1,1,,,,,,,,
Loja,,,,,,,,,,,,
'''

movimentos = '''Número,Tipo,Data,Valor,Entidade,Descrição
2020/001,Despesa,2020-01-04,7.28,CGD,Manutenção da conta
2020/002,Receita,2020-01-06,64.00,7Esq,Janeiro
2020/003,Receita,2020-01-06,406.62,2Dto,Abril a Dezembro de 2019
2020/004,Despesa,2020-01-08,222.65,EDP,Luz
2020/005,Receita,2020-01-16,45.18,7Dto,Janeiro
2020/006,Despesa,2020-02-01,7.28,CGD,Manutenção da conta
2020/007,Receita,2020-02-04,64.00,5Esq,Fevereiro
2020/008,Receita,2020-02-06,64.00,7Esq,Fevereiro
2020/009,Despesa,2020-01-20,439.77,Kone,Manutenção dos elevadores: 1º trimestre
2020/010,Receita,2020-02-12,384.00,1Esq e 3Esq,Janeiro Fevereiro e Março
2020/011,Receita,2020-02-20,45.18,7Dto,Fevereiro
2020/012,Despesa,2020-02-24,20.00,Serralheiro,Concerto do trinco da porta
2020/013,Despesa,2020-02-24,174.30,CMB,Inspeção dos elevadores
2020/014,Receita,2020-02-24,194.30,1Dto,Acertos: Janeiro Fevereiro Março Abril e 13.58 de Maio
2020/015,Receita,2020-03-11,271.08,5Dto,Janeiro a Junho
2020/016,Despesa,2020-03-11,1655.00,PluriRapel,Reparação das fachadas
2020/017,Receita,2020-02-26,64.00,5Esq,Março
2020/018,Receita,2020-02-29,542.16,3Dto,Janeiro a Dezembro
2020/019,Despesa,2020-03-04,236.59,EDP,Luz
2020/020,Receita,2020-03-06,64.00,7Esq,Março
2020/021,Despesa,2020-03-07,7.28,CGD,Manutenção da conta
2020/022,Receita,2020-03-15,45.18,7Dto,Março
2020/023,Receita,2020-03-30,64.00,5Esq,Abril 
2020/024,Despesa,2020-04-04,7.28,CGD,Manutenção da conta
2020/025,Receita,2020-04-06,64.00,7Esq,Abril
2020/026,Receita,2020-04-07,225.90,6Dto,Abril a Agosto
2020/027,Receita,2020-04-14,45.18,7Dto,Abril
2020/028,Despesa,2020-04-15,207.98,Vizinhos,Luz Comum
2020/029,Despesa,2020-04-15,1080.00,Limpeza,Limpeza 2020
2020/030,Receita,2020-04-15,542.16,4Dto,Janeiro a Dezembro
2020/031,Despesa,2020-04-01,439.77,Kone,Manutenção dos elevadores: 2º trimestre
'''

fracoes = '''Fração,Permilagem,Mensalidade
Loja,50,6.06
1Dto,24,36.45
1Esq,34,51.63
2Dto,24,36.45
3Dto,24,36.45
3Esq,34,51.63
4Dto,24,36.45
5Dto,24,36.45
5Esq,34,51.63
6Dto,24,36.45
7Dto,24,36.45
7Esq,34,51.63
8Dto,24,36.45
'''

mes = {1: 'jan', 2: 'fev', 3: 'mar', 4: 'abr', 5: 'mai', 6:'jun', 7:'jul', 8:'ago', 9:'set', 10:'out', 11:'nov', 12:'dez'}
pags = ''
for line in pagamentos.splitlines()[1:]:
    meses = ''
    for i,c in enumerate(line.split(',')):
        if (c == '1'):
            meses += '"' + mes[i] + '",'

    if (meses!=''):
        meses = '[' + meses[:-1] + ']'
    else:
        meses = '[]'

    pags += '{' + f'''"_id": "{line.split(',')[0]}",
    "meses_pagos": {meses}
    ''' + '},'

pagamentos_json = json.loads('[' + pags[:-1] + ']')

movs = ''
for line in movimentos.splitlines()[1:]:
    i = line.split(',')
    movs += '{' + f'''"_id": "{i[0]}",
    "tipo": "{i[1]}",
    "data": "{i[2]}",
    "valor": {i[3]},
    "entidade": "{i[4]}",
    "descricao": "{i[5]}"
    ''' + '},'
movimentos_json = json.loads('[' + movs[:-1] + ']')

fracs = ''
for line in fracoes.splitlines()[1:]:
    i = line.split(',')
    fracs += '{' + f'''"_id": "{i[0]}",
    "permilagem": {i[1]},
    "mensalidade": {i[2]}
    ''' + '},'
fracoes_json = json.loads('[' + fracs[:-1] + ']')


pagamentos_file = open('pagamentos.json','w')
movimentos_file = open('movimentos.json','w')
fracoes_file = open('fracoes.json','w')

json.dump(pagamentos_json, pagamentos_file, indent = 4, ensure_ascii=False)
json.dump(movimentos_json, movimentos_file, indent = 4, ensure_ascii=False)
json.dump(fracoes_json, fracoes_file, indent = 4, ensure_ascii=False)
