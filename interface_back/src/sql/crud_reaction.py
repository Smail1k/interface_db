from src.sql.database import conn
from src.service.model.reaction.reaction import Reaction
from src.service.model.reaction.reaction_new import NewReaction


def insert_reaction(reaction: NewReaction):
    with conn.cursor() as curs:
        curs.execute('INSERT INTO t_reaction (reaction_url)'
                     'VALUES (?)', (reaction.url,))
        conn.commit()  # сохраняет изменения


def get_reaction(reaction_id: int) -> Reaction:
    with conn.cursor() as curs:
        curs.execute('SELECT * FROM t_reaction WHERE id= ?',
                     (reaction_id, ))
        result = curs.fetchone()
    return result


def delete_reaction(reaction_id: int):
    with conn.cursor() as curs:
        curs.execute('DELETE FROM t_reaction WHERE id = ?',
                     (reaction_id, ))
    curs.commit()
