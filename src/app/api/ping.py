from fastapi import APIRouter

router = APIRouter()

@router.get('/ping')
async def pong():
    #some async code here :D
    return {'ping': 'pong!'}
