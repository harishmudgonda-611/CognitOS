from pathlib import Path
import ast


def doctor():
    print("=" * 40)
    print("        COGNIT DOCTOR")
    print("=" * 40)

    root = Path("src/cognit")

    py_files = list(root.rglob("*.py"))
    print(f"Python Files : {len(py_files)}")

    syntax_errors = []

    for file in py_files:
        try:
            ast.parse(file.read_text())
        except Exception as e:
            syntax_errors.append((file, str(e)))

    if syntax_errors:
        print("\nSyntax Errors:")
        for file, err in syntax_errors:
            print(f"✗ {file}")
            print(f"  {err}")
    else:
        print("✓ Syntax Check Passed")

    runner = root / "mission" / "runner.py"

    if runner.exists():
        text = runner.read_text()

        if "builder.react" in text:
            print("✓ builder.react registered")
        else:
            print("✗ builder.react NOT registered")
    else:
        print("✗ mission/runner.py not found")
    
