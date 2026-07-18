from pathlib import Path


def create_module(name: str):
    module_dir = Path("src/cognit") / name
    module_dir.mkdir(parents=True, exist_ok=True)

    init_file = module_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text("# Cognit Module\n")

    print(f"✓ Module '{name}' created at {module_dir}")


def main():
    print("=== Cognit Builder v0.1 ===")

    while True:
        print("\n1. Create Module")
        print("2. Exit")

        choice = input("Select: ").strip()

        if choice == "1":
            name = input("Module name: ").strip().lower()
            create_module(name)

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()


