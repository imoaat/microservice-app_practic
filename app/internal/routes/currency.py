from fastapi import APIRouter, HTTPException

from app.pkg.redis_tools.tools import RedisTools

router = APIRouter(
    prefix="api/v1/currency",
)

@router.get("/all_pairs")
async def get_all_pairs():
    pairs = RedisTools.ger_all_pairs()
    return {"pairs": pairs}

@router.get('/{pair}')
async def get_pair_currency(pair: str):
    if pair not in [s.decode('utf-8') for s in RedisTools.get_keys()]:
        return {'error': 'Pair does not exist'}
        # raise HTTPException(status_code=404, detail="Pair does not exist")

    return {
        'pair': pair,
        'price': RedisTools.get_pair(pair)
    }