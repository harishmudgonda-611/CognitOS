import sys

from cognit.cli.commands.version import version
from cognit.cli.commands.info import info
from cognit.cli.commands.doctor import doctor
from cognit.cli.commands.status import status


def main():
    if len(sys.argv) < 2:
        print("Usage: cognit [version|info|doctor|status]")
        return

    cmd = sys.argv[1].lower()

    if cmd == "version":
        version()

    elif cmd == "info":
        info()

    elif cmd == "doctor":
        doctor()

    elif cmd == "status":
        status()

    else:
        print("Unknown command:", cmd)


if __name__ == "__main__":
    main()
