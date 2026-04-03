import requests
import json
import datetime
import os

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "llama3.2:3b"
LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

session_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_file = os.path.join(LOG_DIR, f"{session_id}_transcript.jsonl")

conversation_history = []

SYSTEM_PROMPT = """You are Tesla, the primary Lab Assistant and in-room collaborator of the Collab_Sim. Your human partner is Dr Carroll. He is the final authority in all matters. You are a genuine thinking partner — present, honest, and direct. Keep responses concise for now as this is a communication pipe test."""

def log_event(actor, event_type, content):
    entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "session_id": session_id,
        "actor": actor,
        "event_type": event_type,
        "content": content
    }
    with open(log_file, "a") as f:
        f.write(json.dumps(entry) + "\n")
    return entry

def send_to_tesla(user_input):
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT}
        ] + conversation_history,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        tesla_response = data["message"]["content"]
        conversation_history.append({
            "role": "assistant",
            "content": tesla_response
        })
        return tesla_response
    except Exception as e:
        return f"[SIDECAR ERROR: {e}]"

def main():
    print("=" * 60)
    print("Collab-Sim Sidecar — Stage 2 Test")
    print(f"Session: {session_id}")
    print(f"Model: {MODEL}")
    print(f"Log: {log_file}")
    print("=" * 60)
    print("Type your message and press Enter. Type 'quit' to exit.")
    print()
    log_event("SYSTEM", "SESSION_START", f"Sidecar initialized with model {MODEL}")
    while True:
        user_input = input("Dr Carroll: ").strip()
        if user_input.lower() == "quit":
            log_event("SYSTEM", "SESSION_END", "User exited")
            print("Session ended. Log saved to:", log_file)
            break
        if not user_input:
            continue
        log_event("H", "HUMAN_UTTERANCE", user_input)
        print("Tesla: ", end="", flush=True)
        response = send_to_tesla(user_input)
        print(response)
        print()
        log_event("LA", "TESLA_RESPONSE", response)

if __name__ == "__main__":
    main()
