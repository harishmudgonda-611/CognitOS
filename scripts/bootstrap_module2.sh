#!/data/data/com.termux/files/usr/bin/bash

set -e

echo "== Cognit OS :: Module 2 Bootstrap =="

mkdir -p src/cognit/cli/commands

touch src/cognit/__init__.py
touch src/cognit/cli/__init__.py
touch src/cognit/cli/commands/__init__.py

cat > src/cognit/cli/commands/version.py << 'EOF'
def version():
    print("Cognit OS")
    print("Version : 0.1.0")
EOF

cat > src/cognit/cli/commands/info.py << 'EOF'
import platform

def info():
    print("===== Cognit OS =====")
    print("Version :", "0.1.0")
    print("Python  :", platform.python_version())
    print("Platform:", platform.system())
EOF

cat > src/cognit/cli/commands/doctor.py << 'EOF'
import shutil

def check(tool):
    return "✓" if shutil.which(tool) else "✗"

def doctor():
    print("=== Cognit Doctor ===")
    print("Python :", check("python"))
    print("Git    :", check("git"))
    print("Node   :", check("node"))
    print("Java   :", check("java"))
EOF

cat > src/cognit/cli/main.py << 'EOF'
import sys

from cognit.cli.commands.version import version
from cognit.cli.commands.info import info
from cognit.cli.commands.doctor import doctor

def main():
    if len(sys.argv) < 2:
        print("Usage: cognit [version|info|doctor]")
        return

    cmd = sys.argv[1].lower()

    if cmd == "version":
        version()
    elif cmd == "info":
        info()
    elif cmd == "doctor":
        doctor()
    else:
        print("Unknown command:", cmd)

if __name__ == "__main__":
    main()
EOF

echo
echo "Bootstrap Complete!"
echo
echo "Run:"
echo "PYTHONPATH=src python -m cognit.cli.main version"
