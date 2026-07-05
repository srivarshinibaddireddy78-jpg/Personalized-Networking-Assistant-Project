import json
import os

HISTORY_FILE = "data/history.json"


class HistoryLogger:

    def save_history(self, profile, conversation):
        os.makedirs("data", exist_ok=True)

        history = self.load_history()

        history.append({
            "profile": profile,
            "conversation": conversation
        })

        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)

    def load_history(self):
        if not os.path.exists(HISTORY_FILE):
            return []

        with open(HISTORY_FILE, "r") as file:
            return json.load(file)