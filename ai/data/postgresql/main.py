from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Team, PlayerPool, Player, Draft, DraftTeam, DraftHistory, SessionLocal
import json

session = SessionLocal()

def write_postgres_team(name, team_dict):
    json_data = json.dumps(team_dict)
    new_item = Team(name=name, data=json_data)
    session.add(new_item)
    session.commit()

def read_postgres_team(name):    # Retrieve data 
    retrieved_item = session.query(Team).filter_by(name=name).first()
    return json.loads(retrieved_item.data) if retrieved_item else None

def write_postgres_player_pool(id, player_pool_dict):
    
    if hasattr(player_pool_dict, 'model_dump'):
        player_pool_dict = player_pool_dict.model_dump(by_alias=True)
    json_data = json.dumps(player_pool_dict, default=str)
    new_item = PlayerPool(id=id, data=json_data)
    session.add(new_item)
    session.commit()

def read_postgres_player_pool(id):
    retrieved_item = session.query(PlayerPool).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


def write_postgres_player(id, player_dict):
    json_data = json.dumps(player_dict)
    new_item = Player(id=id, data=json_data)
    session.add(new_item)
    session.commit()

def read_postgres_player(id):
    retrieved_item = session.query(Player).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


def write_postgres_draft(id: str, data: dict) -> None:
    json_data = json.dumps(data)
    new_item = Draft(id=id, data=json_data)
    session.add(new_item)
    session.commit()

def read_postgres_draft(id: str) -> dict | None:
    retrieved_item = session.query(Draft).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


def read_postgres_drafts() -> list[dict | None]:
    rows = session.query(Draft).all()
    return [json.loads(row[0]) for row in rows if row[0]]
    
    
def write_postgres_draft_teams(id, draft_teams_dict):
    # If passed a list of Team objects, convert each to dict
    if isinstance(draft_teams_dict, list) and draft_teams_dict and hasattr(draft_teams_dict[0], 'model_dump'):
        draft_teams_dict = [team.model_dump(by_alias=True) for team in draft_teams_dict]
    elif hasattr(draft_teams_dict, 'model_dump'):
        draft_teams_dict = draft_teams_dict.model_dump(by_alias=True)
    json_data = json.dumps(draft_teams_dict, default=str)
    new_item = DraftTeam(id=id, data=json_data)
    session.add(new_item)
    session.commit()

def read_postgres_draft_teams(id):
    retrieved_item = session.query(DraftTeam).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None

def write_postgres_draft_history(id: str, data: dict) -> None:
    json_data = json.dumps(data)
    new_item = DraftHistory(id=id, data=json_data)
    session.add(new_item)
    session.commit()
    
def read_postgres_draft_history(id: str) -> dict | None:
    retrieved_item = session.query(DraftHistory).filter_by(id=id).first()
    return json.loads(retrieved_item.data) if retrieved_item else None


    
