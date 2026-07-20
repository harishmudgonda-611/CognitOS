from pathlib import Path
import ast


def repair():
    print("=" * 40)
    print("        COGNIT REPAIR")
    print("=" * 40)

    root = Path("src/cognit")

    py_files = list(root.rglob("*.py"))
    repaired = 0

    print("Checking project...")

    for file in py_files:
        try:
            ast.parse(file.read_text())
        except Exception as e:
            print(f"✗ Syntax error: {file.name}")
            print(f"  {e}")

    if not (root / "mission").exists():
        (root / "mission").mkdir(parents=True)
        print("✓ Created mission directory")
        repaired += 1

    if not (root / "agents").exists():
        (root / "agents").mkdir(parents=True)
        print("✓ Created agents directory")
        repaired += 1

    if repaired == 0:
        print("✓ No repairs needed")
    else:
        print(f"✓ Repairs completed: {repaired}")

    print("=" * 40)
    print("Repair Finished")
    print("=" * 40)
    
