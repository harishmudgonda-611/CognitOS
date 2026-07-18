import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="cognit",
        description="Cognit OS Command Line Interface"
    )

    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status")
    sub.add_parser("doctor")
    sub.add_parser("verify")

    builder = sub.add_parser("builder")
    builder.add_argument("action")
    builder.add_argument("name")

    mission = sub.add_parser("mission")
    mission.add_argument("action")

    return parser
