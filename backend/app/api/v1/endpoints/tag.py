from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.tag import Tag, TagCreate
from app.services.tag_service import create_tag, get_tags
from app.db.session import get_db

router = APIRouter()

@router.post("/", response_model=Tag)
def create_new_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@router.get("/", response_model=List[Tag])
def read_tags(db: Session = Depends(get_db)):
    return get_tags(db)
