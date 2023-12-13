import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('estufa_inteligente.db')
cursor = conn.cursor()

# Criar tabela para sensores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Sensores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tipo TEXT,
        valor REAL,
        data_hora DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Criar tabela para informações das plantas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Plantas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        especie TEXT,
        data_plantio DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')

# Inserir dados de exemplo para sensores
sensores_data = [
    ('temperatura_ambiente', 25.5),
    ('umidade_ambiente', 60.2),
    ('iluminacao_ambiente', 800),
    ('temperatura_agua', 22.0),
    ('ph_agua', 6.5),
    ('tds_agua', 300),
    ('co2', 400),
]

for sensor in sensores_data:
    cursor.execute("INSERT INTO Sensores (tipo, valor) VALUES (?, ?)", sensor)

# Inserir dados de exemplo para plantas
cursor.execute("INSERT INTO Plantas (nome, especie) VALUES ('Tomate', 'Solanum lycopersicum')")
cursor.execute("INSERT INTO Plantas (nome, especie) VALUES ('Manjericão', 'Ocimum basilicum')")

# Commit para salvar as alterações
conn.commit()

# Fechar a conexão com o banco de dados
conn.close()
