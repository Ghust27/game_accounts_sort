# Game Accounts Sorter

Este programa é utilizado para processar e organizar contas de jogo a partir de um arquivo de texto, categorizando-as por elo atual ou elo anterior. Ele também salva as informações das contas em arquivos JSON separados por categoria.

## Funcionalidades

- Lê um arquivo de texto contendo informações sobre contas de jogo.
- Extrai dados relevantes, como Nickname, Level, RP, BE, Elo atual, Elo anterior, entre outros.
- Organiza as contas por elo atual ou elo anterior.
- Salva as contas organizadas em arquivos JSON.

## Pré-requisitos

Certifique-se de que você tem o seguinte instalado:

- Python 3.x
- Biblioteca padrão `json`

## Como Usar

1. Insira as informações das contas no arquivo `game_accounts_sort/Contas.txt` no seguinte formato:
```
user:password - Nick: <Nick> - Level: <Level> - RP: <RP> - BE: <BE> - Elo: <Elo> - OldElo: <OldElo> - Flex: <Flex> - Champions: <Champions> - Skins: <Skins> - LastGame: <LastGame> - EmailStatus: <EmailStatus> - Region: <Region> #nigoschk
```

2. No arquivo `main.py`, configure o caminho do arquivo de entrada:
```python
arquivo = 'game_accounts_sort/Contas.txt'
```

3. Execute o programa:
```
python main.py
```

4. Os arquivos JSON organizados serão gerados nas pastas elos_atuais ou elos_antigos, dependendo do valor do parâmetro target.
```
target: Especifique se deseja organizar as contas pelo elo atual (now) ou elo anterior (before).
```

## Exemplo:

Se o arquivo de entrada Contas.txt contiver:
```
user1:pass1 - Nick: Player1 - Level: 50 - RP: 100 - BE: 200 - Elo: Gold - OldElo: Silver - Flex: Silver - Champions: 30 - Skins: 5 - LastGame: 2024-12-01 - EmailStatus: Verified - Region: NA #
user2:pass2 - Nick: Player2 - Level: 45 - RP: 200 - BE: 300 - Elo: Platinum - OldElo: Gold - Flex: Gold - Champions: 40 - Skins: 8 - LastGame: 2024-11-25 - EmailStatus: Verified - Region: EU #
```
O programa criará os seguintes arquivos JSON:
```
game_accounts_sort/elos_atuais/Gold.json
game_accounts_sort/elos_atuais/Platinum.json
```

