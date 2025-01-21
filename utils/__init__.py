import json


def elos(arquivo,target):

    possibilidades = ['Iron','Bronze','Silver','Gold','Platinum','Emerald','Diamond','Master',
                      'Unranked','Challenger','Grandmaster'] 
    
    contas = {'unknown':[]}

    for elo in possibilidades:
        contas[elo] = []
    
    with open(arquivo,'r',encoding="utf-8") as f:
        linhas = f.readlines()
        for linha in linhas:
            conta = {
                "user": linha.split(':')[0],
                "password": linha.split(':')[1].split(' -')[0],
                "informacoes": {
                "Nick": linha.split('Nick: ')[1].split(' -')[0] ,
                "Level": linha.split('Level: ')[1].split(' -')[0] ,
                "RP": linha.split('RP: ')[1].split(' -')[0] ,
                "BE": linha.split('- BE: ')[1].split(' -')[0] ,
                "Elo": linha.split('- Elo: ')[1].split(' - OldElo:')[0] ,
                "OldElo": linha.split('- OldElo: ')[1].split(' -')[0] ,
                "Flex": linha.split('- Flex: ')[1].split(' -')[0] ,
                "Champions": linha.split('- Champions: ')[1].split(' -')[0] ,
                "Skins": linha.split('- Skins: ')[1].split(' -')[0] ,
                "LastGame": linha.split('- LastGame: ')[1].split(' -')[0] ,
                "EmailStatus": linha.split('- EmailStatus: ')[1].split(' -')[0] ,
                "Region": linha.split('- Region: ')[1].split(' #')[0]
            }
            }

            if target == 'now':
                elo_target = conta["informacoes"]["Elo"].split(' ')[0]
                dir = 'game_accounts_sort/elos_atuais'
            elif target == 'before':
                elo_target = conta["informacoes"]["OldElo"].split(' ')[0]
                dir = 'game_accounts_sort/elos_antigos'
            
            if elo_target not in possibilidades:
                contas['unknown'].append(conta)
            else:
                contas[elo_target].append(conta)

    for elo in contas:
        if contas[elo]:
            with open(f"{dir}{elo}.json", 'a', encoding='utf-8') as f:
                json.dump(contas[elo], f, indent=4)

    print('Arquivos criados com sucesso!')

