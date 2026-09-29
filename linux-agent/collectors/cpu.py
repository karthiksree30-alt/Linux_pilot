import subprocess


def get_cpu_info():
    result = subprocess.run(
        ["lscpu"],
        capture_output=True,
        text=True
    )

    return result.stdout


if __name__ == "__main__":
    print(get_cpu_info())