"""Read-only API preflight; prints IDs and status, never credentials."""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from dotenv import load_dotenv
from tools import redact

load_dotenv()


def main():
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), timeout=30)
    configured = (os.getenv("LAB_MODEL") or "").removeprefix("openai:")
    try:
        ids = {model.id for model in client.models.list().data}
        print("Configured model:", configured)
        print("Exact ID accessible:", configured in ids)
        candidate = configured.strip("<>")
        print("Without placeholder brackets accessible:", candidate in ids)
        print("Matching accessible models:", sorted(m for m in ids if candidate in m)[:15])
        if len(sys.argv) > 1:
            model = sys.argv[1]
            result = client.chat.completions.create(model=model, messages=[{"role": "user", "content": "Reply with OK only."}], max_completion_tokens=30)
            print("Chat API:", model, result.choices[0].message.content)
        return 0
    except Exception as exc:
        print("Preflight failed:", redact(f"{type(exc).__name__}: {exc}"))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
