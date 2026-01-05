import json
from llm_client import LLMClient
from prompts import TICKET_ANALYSIS_PROMPT

class TicketAnalyzer:
    def __init__(self):
        self.llm = LLMClient()

    def analyze(self, ticket_text: str) -> dict:
        prompt = TICKET_ANALYSIS_PROMPT.format(ticket=ticket_text)

        messages = [
            {"role": "system", "content": "You are a precise and reliable AI assistant."},
            {"role": "user", "content": prompt}
        ]

        raw_response = self.llm.ask(messages)
        try:
            return json.loads(raw_response)

        except json.JSONDecodeError:

            return {
                "error": "Invalid response from LLM client - response was not valid JSON",
                "raw_response": raw_response[:500]  # Limit length for logging
            }
