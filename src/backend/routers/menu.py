from fastapi import APIRouter

from ..db.database import get_db
from ..db.models import MenuItem

router = APIRouter()

@router.get(
    "/cache",
    status_code=200,
    name="Agent cache",
    description="Returns full langchain agent cache.",
)
async def get_menu_items():
    # return "Oh whatever"
    # Telemetry
    # logger.info(f"Incoming chat message to generate code.  Payload: {payload}")
    # begin = time.time()
    # current_span = trace.get_current_span()
    # current_span.set_attribute("payload.question", payload.question)
    # current_span.set_attribute(
    #     "payload.history", [json.dumps(message.model_dump()) for message in payload.chat_history or []]
    # )
    # current_span.set_attribute("payload.code_block", payload.code_block or "")

    # Receive result
    db = get_db()
    result = db.query(MenuItem).all()
    # logger.info(f"Chat message processed in {time.time() - begin} seconds.")

    # _ = asyncio.ensure_future(
    #     evaluator_service.evaluate_inline(description=payload.question, generated_code=result.code_block)
    # )
    return result