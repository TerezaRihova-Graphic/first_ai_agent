from openai import OpenAI
from dotenv import load_dotenv
import os

# --- Načtení API klíče z .env ---
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("Agent: Ahoj! Jsem chytrá kalkulačka. Zadej svůj příklad, nebo napiš 'konec'.")

while True:
    # Uživatel zadá příklad
    priklad = input("Agent: Zadej příklad: ")

    if priklad.lower() == "konec":
        print("Agent: Ukončuji program.")
        break

    # Zavoláme LLM, které provede výpočet a vrátí výsledek
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Jsi kalkulačka. Spočítej zadaný příklad a vrať jen odpověď ve tvaru 'Výsledek je: ...'."},
            {"role": "user", "content": f"Spočítej: {priklad}"}
        ]
    )

    # Získáme odpověď LLM
    odpoved = response.choices[0].message.content.strip()

    # Vytiskneme odpověď LLM
    print(f"Odpověď: {odpoved}")