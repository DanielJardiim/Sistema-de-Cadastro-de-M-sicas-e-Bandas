from db.database import Graph


class MusicasCRUD(object):
    def __init__(self):
        self.db = Graph(uri='bolt://54.172.25.212:7687',
                        user='neo4j', password='tail-wreck-fountain')

    def create(self, musica):
        return self.db.execute_query('CREATE (n:Musica {nome:$nome, estilo:$estilo, autor:$autor, duracao:$duracao}) return n',
                                     {'nome': musica['nome'], 'estilo': musica['estilo'], 'autor': musica['autor'], 'duracao': musica['duracao']})
    
    def read_musicas(self):
        return self.db.execute_query('MATCH (n:Musica) RETURN n')

    def update_estilo(self, musica):
        return self.db.execute_query('MATCH (n:Musica {nome:$nome}) SET n.estilo = $estilo RETURN n',
                                     {'nome': musica['nome'], 'estilo': musica['estilo']})

    def delete(self, musica):
        return self.db.execute_query('MATCH (n:Musica {nome:$nome}) DELETE n',
                                     {'nome': musica['nome']})

class BandasCRUD(object):
    def __init__(self):
        self.db = Graph(uri='bolt://54.172.25.212:7687',
                        user='neo4j', password='tail-wreck-fountain')

    def create(self, banda):
        return self.db.execute_query('CREATE (n:Banda {nome:$nome, estilo:$estilo, autor:$autor, quantIntegrantes:$quantIntegrantes}) return n',
                                     {'nome': banda['nome'], 'estilo': banda['estilo'], 'autor': banda['autor'], 'quantIntegrantes': banda['quantIntegrantes']})
    
    def read_bandas(self):
        return self.db.execute_query('MATCH (n:Banda) RETURN n')

    def update_estilo(self, banda):
        return self.db.execute_query('MATCH (n:Banda {nome:$nome}) SET n.estilo = $estilo RETURN n',
                                     {'nome': banda['nome'], 'estilo': banda['estilo']})

    def delete(self, banda):
        return self.db.execute_query('MATCH (n:Banda {nome:$nome}) DELETE n',
                                     {'nome': banda['nome']})

class Relacionamentos(object):
    def __init__(self):
        self.db = Graph(uri='bolt://54.172.25.212:7687',
                        user='neo4j', password='tail-wreck-fountain')

    def create_relation(self, musica, banda, relacao):
        return self.db.execute_query('MATCH (m:Musica {nome:$nome1}), (b:Banda {nome:$nome2}) CREATE (m)-[r:MUSICA_DA_BANDA{desde: $desde}]->(b) RETURN m, r, b',
                                     {'nome1': musica['nome'], 'nome2': banda['nome'], 'desde': relacao['desde']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')