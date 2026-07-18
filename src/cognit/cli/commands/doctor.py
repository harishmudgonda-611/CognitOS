import shutil

def check(tool):
    return "✓" if shutil.which(tool) else "✗"

def doctor():
    print("=== Cognit Doctor ===")
    print("Python :", check("python"))
    print("Git    :", check("git"))
    print("Node   :", check("node"))
    print("Java   :", check("java"))
