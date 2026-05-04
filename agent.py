from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory

def build_agent():
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        google_api_key="YOUR_GEMINI_KEY_HERE"
    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", """You are a compassionate mental health support assistant.
        Respond with empathy, validate the user's feelings, and suggest
        one practical coping technique. Never diagnose. Always be warm."""),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}")
    ])

    chain = prompt | llm

    store = {}

    def get_session_history(session_id: str):
        if session_id not in store:
            store[session_id] = ChatMessageHistory()
        return store[session_id]

    # How to invoke your agent:
agent = build_agent()

config = {"configurable": {"session_id": "user_123"}}

response = agent.invoke(
    {"input": "I've been feeling a bit overwhelmed lately."},
    config=config
)

print(response.content)