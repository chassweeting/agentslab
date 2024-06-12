from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .agent import run_agent
from .agent.schemas import ChatRequestSchema

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
async def chat(payload: ChatRequestSchema):
    resp = run_agent(user_request=payload.user_request, chat_history=payload.chat_history)
    return resp['output']
