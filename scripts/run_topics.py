"""Run preset topics sequentially; skip only locally verified result triplets."""
import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import research
from self_check import check_topic, load_topics, load_validator


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--indices", nargs="+", type=int, default=list(range(5)), choices=range(5))
    parser.add_argument("--force", action="store_true", help="Regenerate even valid existing reports")
    parser.add_argument("--resume-dir", type=Path, help="Machine-generated checkpoint for world-model topic only")
    parser.add_argument("--resume-root", type=Path, help="Directory containing machine checkpoints named by topic slug")
    parser.add_argument("--repair-file", type=Path, help="Reviewer instructions for an agent repair inside the sandbox")
    args = parser.parse_args()
    topics, validator = load_topics(), load_validator()
    failed = []
    for index in args.indices:
        topic = topics[index]
        if not args.force and not check_topic(topic, ROOT / "reports", validator):
            print(f"Already valid, skipped: {topic}", flush=True)
            continue
        seed_dir = args.resume_dir if index == 0 else None
        if seed_dir is None and args.resume_root is not None:
            candidate = args.resume_root / research.slugify(topic)
            if (candidate / "report.md").exists() and (candidate / "sources.json").exists() and len(list((candidate / "notes").glob("*.md"))) >= 3:
                try:
                    research.checkpoint_files(candidate)
                except (OSError, ValueError, RuntimeError) as exc:
                    print(f"Unusable checkpoint; starting fresh: {topic} ({type(exc).__name__})", flush=True)
                else:
                    seed_dir = candidate
        kwargs = {"seed_dir": seed_dir}
        if args.repair_file is not None:
            kwargs["repair_instruction"] = args.repair_file.read_text(encoding="utf-8")
        if research.main(topic, **kwargs):
            failed.append(topic)
    if failed:
        print("Failed topics:", *failed, sep="\n", flush=True)
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
