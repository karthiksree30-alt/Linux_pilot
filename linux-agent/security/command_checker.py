DANGEROUS_COMMANDS = [
    "mkfs",
    "fdisk",
    "parted",
    "dd",
    "rm -rf",
]


def check_command(command):

    command_lower = command.lower()

    for dangerous in DANGEROUS_COMMANDS:

        if dangerous in command_lower:

            return {
                "command": command,
                "risk": "DANGEROUS",
                "allowed": False,
                "reason": f"Command contains potentially destructive operation: {dangerous}"
            }

    return {
        "command": command,
        "risk": "LOW",
        "allowed": True,
        "reason": "No known high-risk pattern detected."
    }


if __name__ == "__main__":

    command = input("Enter command: ")

    result = check_command(command)

    print(result)