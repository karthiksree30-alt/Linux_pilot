import subprocess


def run_command(command):
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return {
        "output": result.stdout,
        "error": result.stderr,
        "return_code": result.returncode
    }


def network_diagnostics():

    return {
        "interfaces": run_command(["ip", "link"]),
        "addresses": run_command(["ip", "addr"]),
        "network_manager": run_command(
            ["systemctl", "is-active", "NetworkManager"]
        )
    }


if __name__ == "__main__":
    results = network_diagnostics()

    for name, result in results.items():

        print("\n======", name, "======")

        print(result)