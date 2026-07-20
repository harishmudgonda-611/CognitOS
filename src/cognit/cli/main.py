import sys

from cognit.cli.commands.version import version
from cognit.cli.commands.info import info
from cognit.cli.commands.doctor import doctor
from cognit.cli.commands.verify import verify
from cognit.cli.commands.repair import repair
from cognit.cli.commands.status import status
from cognit.cli.commands.mission import mission
from cognit.cli.commands.ask import ask


def main():
    if len(sys.argv) < 2:
        print("Usage: cognit [version|info|doctor|verify|repair|status|mission|ask]")
        return

    cmd = sys.argv[1].lower()

    if cmd == "version":
        version()

    elif cmd == "info":
        info()

    elif cmd == "doctor":
        doctor()

    elif cmd == "verify":
        verify()

    elif cmd == "repair":
        repair()

    elif cmd == "status":
        status()

    elif cmd == "mission":
        mission()

    elif cmd == "ask":
        ask()

    else:
        print("Unknown command:", cmd)


if __name__ == "__main__":
    main()
    
