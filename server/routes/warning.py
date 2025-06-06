from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import ContentWarning
from schemas.warnings import ContentWarningOut, ContentWarningWithPosts
from schemas.posts import PostOut
from crud.warning import get_warning, get_all_warnings, get_warning_with_posts, get_posts_of_warnings
from utils.user import get_current_user
from typing import List
from pydantic import BaseModel
from db import get_db

class MessageResponse(BaseModel):
    message: str

router = APIRouter(prefix = "/warning", tags = [ "Warning" ])

@router.get("/warnings", response_model=List[ContentWarningOut])
def get_warnings(count: int = 20, skip: int = 0, db: Session = Depends(get_db)) -> List[ContentWarningOut]:
    warnings = get_all_warnings(db, skip = skip, limit = count)
    return warnings

@router.get("/warnings/{id}")
def get(id: int, db: Session = Depends(get_db)) -> ContentWarningWithPosts:
    return get_warning_with_posts(db = db, warning_id = id)

@router.get("/warnings/{id}/posts")
def get_posts(id: int, count: int = 50, skip: int = 0, db: Session = Depends(get_db)) -> List[PostOut]:
    return get_posts_of_warning(db = db, warning_id = id, skip = skip, limit = count)
