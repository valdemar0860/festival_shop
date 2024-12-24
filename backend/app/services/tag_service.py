from sqlalchemy.orm import Session
from app.db.models.tag import Tag
from app.schemas.tag import TagCreate, TagOut
from app.crud.tag_crud import create_tag, get_tags


def create_tag(db: Session, tag_data: TagCreate) -> TagOut:
    """
    Створює новий тег.
    """
    existing_tag = db.query(Tag).filter(Tag.name == tag_data.name).first()
    if existing_tag:
        raise ValueError(f"Тег із назвою '{tag_data.name}' вже існує!")
    
    tag = create_tag(db, tag_data)
    return TagOut.from_orm(tag)


def get_tags(db: Session) -> list[TagOut]:
    """
    Отримує всі доступні теги.
    """
    tags = get_tags(db)
    return [TagOut.from_orm(tag) for tag in tags]
