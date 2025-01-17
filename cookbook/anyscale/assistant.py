from phi.assistant import Assistant
from phi.llm.anyscale import Anyscale

assistant = Assistant(
    llm=Anyscale(),
    description="You help people with their health and fitness goals.",
)
assistant.print_response("Share a 2 sentence quick healthy breakfast recipe.", markdown=True)
