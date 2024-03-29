from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Cria um mecanismo de banco de dados SQLite e uma sessão de banco de dados
engine = create_engine('sqlite:///atividades.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

# Declarando uma classe Base para todas as classes de modelo
Base = declarative_base()
Base.query = db_session.query_property()

# Definição da classe Pessoas
class Pessoas(Base):
    __tablename__='pessoas'     # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True)  # Coluna de ID, chave primária
    nome = Column(String(40), index=True)   # Coluna de nome, com índice para busca eficaz
    idade = Column(Integer)                 # Coluna de idade

    def __repr__(self):
        return f'<Pessoa {self.nome}>'

    def save(self):   # Método para salvar uma instância no banco de dados
        db_session.add(self)
        db_session.commit()

    def delete(self):   # Método para excluir uma instância do banco de dados
        db_session.delete(self)
        db_session.commit()

# Definição da classe Atividades
class Atividades(Base):
    __tablename__='atividade'   # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True)  # Coluna de ID, chave primária
    nome = Column(String(80))               # Coluna de nome da atividade
    pessoa_id = Column(Integer, ForeignKey('pessoas.id')) # Chave estrangeira para pessoas
    pessoa = relationship("Pessoas")        # Relacionamento com a classe Pessoas

    def __repr__(self):
        return f'<Atividades {self.nome}>'

    def save(self):     # Método para salvar uma instância no banco de dados
        db_session.add(self)
        db_session.commit()

    def delete(self):   # Método para excluir uma instância no banco de dados
        db_session.delete(self)
        db_session.commit()

# Definição da classe Usuários
class Usuarios(Base):
    __tablename__='usuarios'    # Nome da tabela no banco de dados
    id = Column(Integer, primary_key=True)  # Coluna de ID, chave primária
    login = Column(String(20), unique=True)  # Coluna de nome de usuário, único
    senha = Column(String(20))               # Coluna de senha do usuário

    def __repr__(self):
        return f'<Usuario {self.login}>'

    def save(self):     # Método para salvar uma instância no banco de dados
        db_session.add(self)
        db_session.commit()

    def delete(self):   # Método para excluir uma instância no banco de dados
        db_session.delete(self)
        db_session.commit()

# Função para criar as tabelas no banco de dados
def init_db():
    Base.metadata.create_all(bind=engine)

# Verifica se este arquivo foi executado diretamente e, em caso afirmativo, inicializa o DB
if __name__ == '__main__':
    init_db()
