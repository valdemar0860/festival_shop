from sqlalchemy.orm import Session
from typing import List
from app.db.models import Tag
from app.schemas.tag import TagCreate


def create_tag(db: Session, tag: TagCreate) -> Tag:
    db_tag = Tag(name=tag.name)
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag


def get_tags(db: Session) -> List[Tag]:
    return db.query(Tag).all()
