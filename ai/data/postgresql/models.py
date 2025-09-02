from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy.dialects.postgresql import JSONB
from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()

Base = declarative_base()
engine=None


if os.getenv("DEPLOYMENT_ENVIRONMENT") != 'DEV':
    db_url = os.getenv("DB_URL")
    print(db_url)
    engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Team(Base):
    __tablename__ = 'teams'
    name = Column(String, primary_key=True)
    data = Column(JSONB) 

class Draft(Base):
    __tablename__ = 'drafts'
    id = Column(String, primary_key=True, index=True)
    data = Column(JSONB) 

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSONB) 

class PlayerPool(Base):
    __tablename__ = 'player_pool'
    id = Column(String, primary_key=True, index=True)
    data = Column(JSONB) 

class DraftTeam(Base):
    __tablename__ = 'draft_teams'
    id = Column(String, primary_key=True, index=True)
    data = Column(JSONB) 

class DraftHistory(Base):
    __tablename__ = 'draft_history'
    id = Column(String, primary_key=True, index=True)
    data = Column(JSONB) 

if os.getenv("DEPLOYMENT_ENVIRONMENT") != 'DEV':
    Base.metadata.create_all(bind=engine)
