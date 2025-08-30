from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, inspect, insert
from .models import Team, PlayerPool, Player, Draft, DraftTeam, DraftHistory, SessionLocal
import json

session = SessionLocal()

def write_postgres_team(name, team_dict):
    insp = inspect(Team)
    pk_constraint_name = insp.get_pk_constraint(Team.__tablename__)["name"]
    json_data = json.dumps(team_dict)
    insert_stmt = insert(Team).values(name=name, data=json_data)
    do_update_stmt = insert_stmt.on_conflict_do_update(
        constraint=pk_constraint_name, set_=dict(data=json_data)
    )
    session.execute(do_update_stmt)
    session.commit()

def read_postgres_team(name):    # Retrieve data 
    retrieved_item = session.query(Team).filter_by(name=name).first()
    return json.loads(retrieved_item.data) if retrieved_item else None

def write_postgres_player_pool(id, player_pool_dict):
    insp = inspect(PlayerPool)
    if hasattr(player_pool_dict, 'model_dump'):
        player_pool_dict = player_pool_dict.model_dump(by_alias=True)
    pk_constraint_name = insp.get_pk_constraint(PlayerPool.__tablename__)["id"]
    json_data = json.dumps(player_pool_dict, default=str)
    insert_stmt = insert(PlayerPool).values(id=id, data=json_data)
    do_update_stmt = insert_stmt.on_conflict_do_update(
        constraint=pk_constraint_name, set_=dict(data=json_data)
    )
    session.execute(do_update_stmt)
    session.commit()


def read_postgres_player_pool(id):
    retrieved_item = session.query(PlayerPool).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


def write_postgres_player(id, player_dict):
    insp = inspect(Player)
    pk_constraint_name = insp.get_pk_constraint(Player.__tablename__)["id"]
    json_data = json.dumps(player_dict, default=str)
    insert_stmt = insert(Player).values(id=id, data=json_data)
    do_update_stmt = insert_stmt.on_conflict_do_update(
        constraint=pk_constraint_name, set_=dict(data=json_data)
    )
    session.execute(do_update_stmt)
    session.commit()

def read_postgres_player(id):
    retrieved_item = session.query(Player).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


def write_postgres_draft(id: str, data: dict) -> None:
    insp = inspect(Draft)
    pk_constraint_name = insp.get_pk_constraint(Draft.__tablename__)["id"]
    json_data = json.dumps(data)
    insert_stmt = insert(Draft).values(id=id, data=json_data)
    do_update_stmt = insert_stmt.on_conflict_do_update(
        constraint=pk_constraint_name, set_=dict(data=json_data)
    )
    session.execute(do_update_stmt)
    session.commit()

def read_postgres_draft(id: str) -> dict | None:
    retrieved_item = session.query(Draft).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


def read_postgres_drafts() -> list[dict | None]:
    rows = session.query(Draft).all()
    return [json.loads(row[0]) for row in rows if row[0]]
    
    
def write_postgres_draft_teams(id, draft_teams_dict):
    insp = inspect(DraftTeam)
    pk_constraint_name = insp.get_pk_constraint(Draft.__tablename__)["id"]
    # If passed a list of Team objects, convert each to dict
    if isinstance(draft_teams_dict, list) and draft_teams_dict and hasattr(draft_teams_dict[0], 'model_dump'):
        draft_teams_dict = [team.model_dump(by_alias=True) for team in draft_teams_dict]
    elif hasattr(draft_teams_dict, 'model_dump'):
        draft_teams_dict = draft_teams_dict.model_dump(by_alias=True)
    json_data = json.dumps(draft_teams_dict, default=str)
    insert_stmt = insert(Draft).values(id=id, data=json_data)
    do_update_stmt = insert_stmt.on_conflict_do_update(
        constraint=pk_constraint_name, set_=dict(data=json_data)
    )
    session.execute(do_update_stmt)
    session.commit()

    
   
    json_data = json.dumps(data)
    

def read_postgres_draft_teams(id):
    retrieved_item = session.query(DraftTeam).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None

def write_postgres_draft_history(id: str, data: dict) -> None:

    insp = inspect(DraftHistory)
    pk_constraint_name = insp.get_pk_constraint(DraftHistory.__tablename__)["id"]
    json_data = json.dumps(data)
    insert_stmt = insert(DraftHistory).values(id=id, data=json_data)
    do_update_stmt = insert_stmt.on_conflict_do_update(
        constraint=pk_constraint_name, set_=dict(data=json_data)
    )
    session.execute(do_update_stmt)
    session.commit()
    
def read_postgres_draft_history(id: str) -> dict | None:
    retrieved_item = session.query(DraftHistory).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


    
