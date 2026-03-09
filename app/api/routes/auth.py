from fastapi import APIRouter
router=APIRouter
@router.post("/register")
def register():
    email: str
    password: str
    
    