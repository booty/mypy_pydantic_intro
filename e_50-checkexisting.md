# Check Existing Code

Check existing folder and subfolders

```bash
mypy .
```

Check a specific file:

```bash
$ mypy e_40.py
```

## Pro Tip: ChatGPT / MonkeyType / PyAnnotate

Use ChatGPT to annotate your existing code! This works reasonably well.

```text
Please add mypy annotations to this code

(your code here)
```

Also check out `MonkeyType` or `PyAnnotate` (I have not used these)

## Add to Existing Project

```bash
pip install mypy
```

**Optionally:** Create `mypy.ini`:

```text
[mypy]
python_version = 3.8  # Replace with your project's Python version
ignore_missing_imports = True
disallow_untyped_calls = False
disallow_untyped_defs = False
warn_unused_ignores = True
strict_optional = True
check_untyped_defs = True

[some_critical_module]
disallow_untyped_calls = True
disallow_untyped_defs = True
```
