"""check_citations.py - STUDENT IMPLEMENTS `check`.   Runs INSIDE the sandbox (standard library only).

research.py uploads this file to the sandbox and the lead agent runs it with the `execute` tool:
    python3 /tmp/work/research/check_citations.py [report.md] [sources.json]
It must exit 0 and print "OK: ..." when the report is consistent, else print each problem and exit 1.
"""
import json
import re
import sys
from collections import Counter

REPORT = "/tmp/work/report/report.md"
SOURCES = "/tmp/work/research/sources.json"


def check(report_text, sources):
    """Return a list of problem strings (empty list = OK).

    PSEUDO-CODE:
      problems = []
      if sources is empty: return ["no sources in sources.json"]
      for each source entry:
          n must be an int                       -> problem if not
          url must start with http:// or https://-> problem if not
          the same url must not appear twice     -> problem if duplicated
      split report_text at the heading "## References":
          body = text before it; if the heading is missing -> problem
      cited = set of numbers found as [n] in the BODY only (not in the reference list; use a regex)
      every number in `cited` must exist in sources -> problem "[n] cited but missing from sources.json"
      every source number must be in `cited`        -> problem "source [n] never cited"
      the lines of the References section that start with "[n]" (regex) are the reference lines:
          every source needs exactly ONE reference line (none missing, no number twice, no number that is not a source)
          each reference line holds exactly ONE http(s) URL and it must equal that source's url
          (a line bundling several sources under one number is a problem)
      return problems
    """
    problems = []
    if not isinstance(sources, list) or not sources:
        return ["no sources in sources.json (expected a nonempty array)"]
    if not isinstance(report_text, str):
        return ["report must be text"]
    by_number, urls = {}, set()
    for index, source in enumerate(sources):
        if not isinstance(source, dict):
            problems.append(f"source entry {index + 1} must be an object")
            continue
        n, url = source.get("n"), source.get("url")
        if type(n) is not int or n < 1:
            problems.append(f"source entry {index + 1}: n must be a positive integer")
        elif n in by_number:
            problems.append(f"duplicate source number [{n}]")
        else:
            by_number[n] = source
        if not isinstance(url, str) or not re.match(r"^https?://[^\s/]+(?:/|$)", url):
            problems.append(f"source entry {index + 1}: invalid http(s) url")
        elif url in urls:
            problems.append(f"duplicate source url: {url}")
        else:
            urls.add(url)
    headings = list(re.finditer(r"^## References\s*$", report_text, re.M))
    if not headings:
        problems.append("missing ## References heading")
        body, references = report_text, ""
    else:
        body, references = report_text[:headings[0].start()], report_text[headings[0].end():]
        if len(headings) != 1:
            problems.append("expected exactly one ## References heading")
        if re.search(r"^#{1,6}\s+", references, re.M):
            problems.append("References must be the last section")
    body = re.sub(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1[^\n]*$", "", body)
    body = re.sub(r"`+[^`\n]*`+", "", body)
    body = re.sub(r"!?\[[^\]\n]*\]\([^\n)]*\)", "", body)
    body = re.sub(r"^\s*\[[^\]\n]+\]:.*$", "", body, flags=re.M)
    cited = set()
    for match in re.finditer(r"\[(\d+(?:\s*[-–,]\s*\d+)*)\]", body):
        for group in match[1].split(","):
            bounds = re.split(r"[-–]", group)
            if len(bounds) == 1:
                cited.add(int(bounds[0]))
            elif len(bounds) == 2:
                start, stop = map(int, bounds)
                if stop < start or stop - start > 1000:
                    problems.append(f"invalid citation range [{group}]")
                else:
                    cited.update(range(start, stop + 1))
            else:
                problems.append(f"invalid citation range [{group}]")
    for n in sorted(cited - by_number.keys()):
        problems.append(f"[{n}] cited but missing from sources.json")
    for n in sorted(by_number.keys() - cited):
        problems.append(f"source [{n}] never cited")
    counts = Counter()
    for line in references.splitlines():
        match = re.match(r"^\[(\d+)\]\s*(.*)$", line)
        if not match:
            if re.match(r"^\[\d", line):
                problems.append("each reference line must start with a single [n]")
            continue
        n, text = int(match[1]), match[2]
        counts[n] += 1
        if n not in by_number:
            problems.append(f"reference [{n}] missing from sources.json")
        found_urls = re.findall(r"https?://[^\s<>]+", text)
        if len(found_urls) != 1:
            problems.append(f"reference [{n}] must contain exactly one URL")
        elif n in by_number and found_urls[0] != by_number[n].get("url"):
            problems.append(f"reference [{n}] URL differs from sources.json")
    for n in sorted(by_number):
        if counts[n] != 1:
            problems.append(f"source [{n}] needs exactly one reference line (found {counts[n]})")
    return problems


def main(argv):
    report_path = argv[1] if len(argv) > 1 else REPORT
    sources_path = argv[2] if len(argv) > 2 else SOURCES
    try:
        with open(report_path, encoding="utf-8") as f:
            report = f.read()
        with open(sources_path, encoding="utf-8") as f:
            sources = json.load(f)
    except (OSError, ValueError) as exc:
        print(f"cannot read inputs: {exc}")
        return 1
    problems = check(report, sources)
    if problems:
        print("\n".join(problems))
        return 1
    print(f"OK: {len(sources)} sources, all citations resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
