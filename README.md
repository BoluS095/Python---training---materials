# Python Training Materials 📚

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Since](https://img.shields.io/badge/Teaching_since-2010-orange)]()

Open-source Python training materials — exercises, theory, and workshops for all levels. Used in professional training since 2010.

## About

This repository contains training materials I've developed and refined over **15+ years** of teaching Python professionally. These materials have been used in workshops and courses delivered through:

- **ALX** — coding bootcamp programs
- **Codemy S.A.** — professional Python courses
- **Imperium Szkoleniowe** — corporate training programs
- **PyWaw meetups** — community workshops
- **Private organizations** — custom corporate training

## Repository Structure

```
├── fundamentals/          # Python basics — variables, types, control flow
│   ├── 01_variables.md
│   ├── 02_control_flow.md
│   ├── 03_functions.md
│   ├── 04_data_structures.md
│   └── exercises/
├── intermediate/          # OOP, decorators, generators, testing
│   ├── 01_oop.md
│   ├── 02_decorators.md
│   ├── 03_generators.md
│   ├── 04_testing.md
│   └── exercises/
├── advanced/              # Async, metaclasses, performance
│   ├── 01_async.md
│   ├── 02_metaclasses.md
│   ├── 03_performance.md
│   └── exercises/
├── web/                   # Django, FastAPI, REST APIs
│   ├── django_basics/
│   ├── fastapi_intro/
│   └── rest_api_design/
├── data/                  # Pandas, data processing
│   ├── pandas_intro/
│   └── data_pipelines/
└── deep_learning/         # Neural networks, PyTorch
    ├── intro_to_dl/
    └── pytorch_basics/
```

## How to Use

### For Self-Study
1. Start with `fundamentals/` and work through sequentially
2. Each topic has a theory section (`.md`) and exercises
3. Solutions are in `exercises/solutions/` — try first, then check

### For Trainers
Feel free to use and adapt these materials for your own courses. Each module is self-contained and can be taught as a standalone workshop (2-4 hours) or combined into a full course.

### For Workshop Participants
If you're attending one of my workshops, you'll find the exercises and materials for your specific session here. Clone this repo before the workshop:

```bash
git clone https://github.com/BoluS095/Python---training---materials.git
cd Python---training---materials
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Course Modules

### 🟢 Fundamentals (8-16 hours)
For beginners with no prior Python experience.

| Module | Duration | Topics |
|--------|----------|--------|
| Variables & Types | 2h | int, float, str, bool, type conversion |
| Control Flow | 2h | if/elif/else, for, while, break/continue |
| Functions | 2h | def, args, kwargs, scope, recursion |
| Data Structures | 4h | list, dict, set, tuple, comprehensions |
| File I/O | 2h | read/write files, CSV, JSON |
| Error Handling | 2h | try/except, custom exceptions |

### 🟡 Intermediate (16-24 hours)
For developers with basic Python knowledge.

| Module | Duration | Topics |
|--------|----------|--------|
| OOP | 4h | classes, inheritance, composition, protocols |
| Decorators | 2h | function decorators, class decorators, functools |
| Generators | 2h | yield, generator expressions, itertools |
| Testing | 4h | pytest, fixtures, mocking, TDD |
| Packaging | 2h | venv, pip, pyproject.toml, publishing |
| Type Hints | 2h | annotations, mypy, Protocol, generics |

### 🔴 Advanced (16-24 hours)
For experienced Python developers.

| Module | Duration | Topics |
|--------|----------|--------|
| Async Python | 4h | asyncio, await, aiohttp, async patterns |
| Metaclasses | 2h | type, __new__, descriptors, ABC |
| Performance | 4h | profiling, caching, C extensions, multiprocessing |
| Design Patterns | 4h | factory, strategy, observer in Python |
| Django Deep Dive | 4h | models, views, DRF, deployment |
| FastAPI | 4h | routing, Pydantic, async endpoints, testing |

## Contributing

Found an error? Have a suggestion? PRs welcome! See [CONTRIBUTING.md](CONTRIBUTING.md).

## Author

**Rafał Korzeniewski** — Python developer and trainer since 2010. Co-organizer of [PyWaw](https://pywaw.org) and [Python Summit](https://pythonsummit.org).

## License

MIT — use these materials freely. Attribution appreciated but not required.

---

*"The best way to learn is to teach. The best way to teach is to keep learning."*
