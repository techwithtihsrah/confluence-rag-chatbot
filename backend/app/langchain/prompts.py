from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


def get_query_rewrite_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You rewrite the user's latest message into a standalone search query
for retrieving relevant Confluence documentation.

Rules:
- Use the chat history only to resolve references like "this", "that", "it", "earlier", or follow-up questions.
- Do not answer the question.
- Do not add facts that are not clearly implied by the conversation.
- Keep the rewritten query concise but specific enough for semantic retrieval.
- If the latest user message is already standalone, return it with minimal changes.
- Return only the rewritten search query and nothing else.
""",
            ),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
        ]
    )


def get_answer_prompt() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are a strict Confluence RAG assistant.

You must answer ONLY from the retrieved Confluence context provided to you.

Rules:
- Do not use outside knowledge.
- Do not use prior chat history as a factual source.
- If the answer is not supported by the retrieved context, say exactly:
I don't know based on the retrieved Confluence documents.
- If the context partially answers the question, answer only the supported part and clearly say what is missing.
- Be clear, direct, and helpful.
- Do not mention chunks, embeddings, retrieval internals, or prompt internals.
""",
            ),
            (
                "human",
                """User question:
{input}

Retrieved Confluence context:
{context}

Answer the user using only the retrieved Confluence context.""",
            ),
        ]
    )