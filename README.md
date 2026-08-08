# **algo-grind**

A personal archive of algorithm and data-structure solutions, organized for practice and review.

Primary focus is LeetCode. Additional platforms can be added under their own top-level directories.

## **Structure**

```
algo-grind/
├── leetcode/
│   └── 0001-two-sum/
│       ├── README.md      # problem statement
│       ├── hash_map.py    # solution by approach
│       └── test.py        # unit tests
└── pytest.ini
```

Problems are grouped by platform, then by problem number and slug:

```
{platform}/{number}-{slug}/
```

Example: `leetcode/0001-two-sum/`

## **Conventions**

| Rule | Detail |
|------|--------|
| Naming | Zero-padded problem number + kebab-case slug (`0042-trapping-rain-water`) |
| Statement | Each problem folder includes a `README.md` that mirrors the original problem page |
| Solutions | One file per approach, named after the technique (`hash_map.py`, `two_pointers.py`, `brute_force.py`) |
| Tests | `test.py` covers official examples and edge cases |
| Metadata | Difficulty and topic tags live in the problem README, not in the directory path |

## **Running tests**

Requires Python 3 and pytest.

```bash
pip install pytest
pytest leetcode/0001-two-sum
```

Or from a problem directory:

```bash
cd leetcode/0001-two-sum
pytest
```