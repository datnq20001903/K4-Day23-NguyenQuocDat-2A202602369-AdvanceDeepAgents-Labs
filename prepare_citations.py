"""Run inside the sandbox: compile stable URL citations before finalization."""
import json
import re
import sys
from pathlib import Path

ROOT = Path('/tmp/work')
DRAFT = ROOT / 'report/draft.md'
REPORT = ROOT / 'report/report.md'
SOURCES = ROOT / 'research/sources.json'
CODE = re.compile(r'(```.*?```|`[^`\n]*`)', re.S)
MARKER = re.compile(r'\[@(https?://[^\]\s]+)\]')
NUMBER = re.compile(r'\[(\d+(?:\s*[,–-]\s*\d+)*)\](?!\()')

def body(text):
    return re.split(r'(?m)^##[ \t]+References[ \t]*$', text)[0].rstrip()

def registry(sources):
    if not isinstance(sources, list) or not sources:
        raise ValueError('sources must be a nonempty list')
    numbers, urls = set(), set()
    for source in sources:
        if not isinstance(source, dict):
            raise ValueError('source must be an object')
        n, url = source.get('n'), source.get('url')
        if type(n) is not int or n <= 0 or n in numbers:
            raise ValueError('source n must be a unique positive integer')
        if not isinstance(url, str) or not re.fullmatch(r'https?://[^\s\]]+', url) or url in urls:
            raise ValueError('source URL must be unique and valid')
        numbers.add(n)
        urls.add(url)
    return {s['url']: s['n'] for s in sources}

def render(text, sources):
    by_url = registry(sources)
    def replace(match):
        url = match.group(1)
        if url not in by_url:
            raise ValueError('citation URL missing from sources: ' + url)
        return f'[{by_url[url]}]'
    segments = CODE.split(body(text))
    for i in range(0, len(segments), 2):
        if NUMBER.search(segments[i]):
            raise ValueError('draft contains positional citations; use [@URL] for every source')
        segments[i] = MARKER.sub(replace, segments[i])
        if '[@' in segments[i]:
            raise ValueError('malformed stable citation marker')
    return ''.join(segments) + '\n'

def seed(text, sources):
    by_n = {n: url for url, n in registry(sources).items()}
    def replace(match):
        if not match.group(1).isdigit():
            raise ValueError('seed requires separate citation numbers')
        return '[@' + by_n[int(match.group(1))] + ']'
    return ''.join(segment if i % 2 else NUMBER.sub(replace, segment)
                   for i, segment in enumerate(CODE.split(body(text)))) + '\n'

def main():
    sources = json.loads(SOURCES.read_text(encoding='utf-8'))
    if '--seed' in sys.argv:
        DRAFT.write_text(seed(REPORT.read_text(encoding='utf-8'), sources), encoding='utf-8')
    else:
        REPORT.write_text(render(DRAFT.read_text(encoding='utf-8'), sources), encoding='utf-8')
    print('Stable citation draft ready' if '--seed' in sys.argv else 'URL citations compiled')

if __name__ == '__main__':
    main()
