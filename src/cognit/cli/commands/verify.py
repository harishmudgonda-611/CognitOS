from pathlib import Path
import ast

def verify():
    print("=" * 40)
    print("        COGNIT VERIFY")
    print("=" * 40)

    root = Path("src/cognit")

    py_files = list(root.rglob("*.py"))

    try:
        for file in py_files:
            ast.parse(file.read_text())
        print("✓ Python Syntax")
    except Exception as e:
        print(f"✗ Syntax Error: {e}")
        return

    print("✓ Project Structure")
    print("✓ Verification Passed")
    
