"""Exercise actual sandbox I/O and concurrent sessions without exposing secrets."""
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sandbox import open_sandbox, download, upload
from tools import redact


def main():
    start = time.monotonic()
    try:
        with open_sandbox() as backend:
            print("Sandbox created:", backend.id, flush=True)
            result = backend.execute("mkdir -p /tmp/work/preflight && python3 --version", timeout=60)
            print("Initial execute:", result.exit_code, result.output, flush=True)
            upload(backend, {"/tmp/work/preflight/input.txt": b"sandbox IO check\n"})
            print("Round-trip exact:", download(backend, ["/tmp/work/preflight/input.txt"])["/tmp/work/preflight/input.txt"] == b"sandbox IO check\n", flush=True)
            def execute(index):
                result = backend.execute(f"printf 'session-{index}\\n'", timeout=60)
                return result.exit_code, result.output
            with ThreadPoolExecutor(max_workers=4) as pool:
                for result in pool.map(execute, range(4)):
                    print("Concurrent execute:", result, flush=True)
        print("Elapsed:", round(time.monotonic() - start, 1), flush=True)
        return 0
    except Exception as exc:
        print("Sandbox preflight failed:", redact(f"{type(exc).__name__}: {exc}"), flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
