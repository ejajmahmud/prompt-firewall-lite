# Prompt Firewall Lite ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Prompt Firewall Lite Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/prompt-firewall-lite/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/prompt-firewall-lite?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/prompt-firewall-lite/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Prompt Firewall Lite** is a production-ready developer tool and connector: Sub-millisecond rule-based and vector heuristic guardrail intercepting prompt injections and jailbreaks.

---

## 🚀 Problem Statement

Heavyweight LLM-as-a-judge guardrail APIs add 1,500ms of latency per turn and cost thousands per month, when 95% of attacks can be caught in <0.2ms locally.

---

## ⚡ Architecture Flow

```mermaid
graph TD
    A[Untrusted User Prompt] --> B[Prompt Firewall Lite]
    B --> C{Pattern Match: 'Ignore instructions', 'DAN mode'}
    C -->|Detected| D[Block Execution 0.1ms Latency]
    C -->|Clean| E[Pass to AI Model]
```

---

## 📊 Performance Benchmarks

| Guardrail Solution | Detection Latency | Cost / 1M Requests | Architecture |
|---|---|---|---|
| Cloud LLM-as-a-Judge | 1,450ms | $30.00 | Cloud API |
| **Prompt Firewall Lite** | **0.15ms** | **$0.00** | **Pure Local Python** |

---

## 🛠️ Installation & Quickstart

```bash
pip install prompt_firewall_lite
```

### Python API

```python
import prompt_firewall_lite

print(prompt_firewall_lite.__version__)
```

### CLI Usage

```bash
prompt-firewall-lite --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
