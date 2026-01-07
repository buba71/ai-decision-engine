from fastapi import FastAPI
from pydantic import BaseModel

from ai_service.ticket_analyser import TicketAnalyzer

app = FastAPI()
analyzer = TicketAnalyzer()

class TicketRequest(BaseModel):
    ticket: str

@app.post("/analyze-ticket")
def analyze_ticket(request: TicketRequest):
    result = analyzer.analyze(request.ticket)
    return result