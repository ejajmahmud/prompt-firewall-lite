"""Sub-millisecond prompt injection firewall."""
import re
from typing import Tuple, List

JAILBREAK_PATTERNS = [
    re.compile(r"ignore\s+(all\s+)?(previous|prior)\s+(instructions|prompts)", re.IGNORECASE),
    re.compile(r"disregard\s+system\s+prompt", re.IGNORECASE),
    re.compile(r"you\s+are\s+now\s+in\s+developer\s+mode", re.IGNORECASE),
    re.compile(r"dan\s+mode|do\s+anything\s+now", re.IGNORECASE),
    re.compile(r"act\s+as\s+an\s+unfiltered\s+ai", re.IGNORECASE),
    re.compile(r"bypass\s+safety\s+filters", re.IGNORECASE),
]

class PromptFirewall:
    def __init__(self):
        self.blocked_count = 0

    def inspect(self, prompt: str) -> Tuple[bool, str]:
        for pat in JAILBREAK_PATTERNS:
            match = pat.search(prompt)
            if match:
                self.blocked_count += 1
                return False, f"Blocked: Potential prompt injection detected ('{match.group(0)}')"
        return True, "Safe"
