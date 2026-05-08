import os
os.environ["ANONYMIZED_TELEMETRY"] = "False"

from graph import build_graph

app = build_graph()

print("Customer Support Assistant (type 'exit' to quit)\n")

while True:
    query = input("User: ")

    if query.lower() == "exit":
        break

    result = app.invoke({"query": query})

    print("\nBot:", result["answer"])
