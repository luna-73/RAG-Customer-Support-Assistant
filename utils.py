from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import pipeline


def get_retriever():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="db",
        embedding_function=embeddings
    )

    return db.as_retriever(search_kwargs={"k": 2})


def get_llm():
    return pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_new_tokens=200
)



def generate_answer(query, docs, llm):
    # No documents retrieved
    if not docs or len(docs) == 0:
        return "This query is outside the support scope. Escalating to human support."

    # Remove duplicate chunks
    unique_texts = list(dict.fromkeys([d.page_content for d in docs]))

    #  Basic relevance check (very important)
    if len(" ".join(unique_texts).strip()) < 30:
        return "Not enough relevant information found. Escalating to human support."

    context = "\n".join(unique_texts)

    prompt = f"""
You are a professional customer support assistant.

Instructions:
- Answer ONLY from the context
- If the question is unrelated, say: "This is outside support scope"
- Keep answer short (max 2–3 points)
- Do NOT repeat sentences

Context:
{context}

Question:
{query}

Answer:
"""

    result = llm(prompt)
    answer = result[0]["generated_text"]

    # Clean output
    answer = answer.replace("\n", " ").strip()

    # Remove repeated sentences
    sentences = answer.split(". ")
    seen = set()
    cleaned = []

    for s in sentences:
        if s not in seen:
            cleaned.append(s)
            seen.add(s)

    answer = ". ".join(cleaned)

    # Final fallback if model still messes up
    if "do not repeat" in answer.lower() or len(answer) < 5:
        return "Unable to generate a reliable answer. Escalating to human support."

    return answer