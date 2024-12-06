
# Projeto EPBJC

Este projeto é uma aplicação para gestão de informações relacionada a alunos, professores e materiais, utilizando Python e SQLite.

## Estrutura do Projeto

- **epbjc/**
  - Diretório principal do projeto.

### Subdiretórios e Ficheiros

#### 1. **src/**
Contém o código fonte do projeto, dividido por funcionalidade:

- **app/**
  - `main.py`: Ponto de entrada principal da aplicação.

- **create/**
  - Scripts responsáveis por criar novos registos na base de dados.
    - `alunos_create.py`: Criação de dados relacionados a alunos.
    - `materiais_create.py`: Criação de dados relacionados a materiais.
    - `professores_create.py`: Criação de dados relacionados a professores.

- **read/**
  - Scripts responsáveis por ler dados da base de dados.
    - `alunos_read.py`: Leitura de dados de alunos.
    - `materiais_read.py`: Leitura de dados de materiais.
    - `professores_read.py`: Leitura de dados de professores.

- **update/**
  - Scripts responsáveis por atualizar registos existentes.
    - `alunos_update.py`: Atualização de dados de alunos.
    - `materiais_update.py`: Atualização de dados de materiais.
    - `professores_update.py`: Atualização de dados de professores.

- **delete/**
  - Scripts responsáveis por eliminar registos.
    - `alunos_delete.py`: Eliminação de dados de alunos.
    - `materiais_delete.py`: Eliminação de dados de materiais.
    - `professores_delete.py`: Eliminação de dados de professores.

#### 2. **sqlite-database/**
Contém a base de dados SQLite e backups:
- `epbjc.db`: Base de dados principal.
- `epbjc_backup_1.db`, `epbjc_backup_2.db`, `epbjc_backup_3.db`: Cópias de segurança da base de dados.

#### 3. **migracao/**
Atualmente vazio, possivelmente destinado a scripts ou ficheiros para migração de dados.

#### 4. **testes/**
Pasta preparada para ficheiros de teste. Atualmente está vazia.

#### 5. **README.md**
Este ficheiro descreve a estrutura do projeto e fornece informações gerais.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **SQLite**: Base de dados utilizada.
- **Estrutura Modular**: Código organizado por módulos e funcionalidades.

## Como Utilizar

1. Certifique-se de que possui o Python instalado na sua máquina.
2. Navegue até o diretório `src/app/` e execute o ficheiro `main.py`:
   ```bash
   python main.py
   ```
3. Para utilizar outras funcionalidades, explore os scripts nas subpastas `create/`, `read/`, `update/` e `delete/`.

## Notas Finais

Este projeto segue boas práticas de organização de código e está estruturado para facilitar a manutenção e expansão.
