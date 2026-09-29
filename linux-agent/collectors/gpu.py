import subprocess


def get_gpu_info():
    result = subprocess.run(
        ["lspci"],
        capture_output=True,
        text=True
    )

    gpu_lines = []

    for line in result.stdout.splitlines():
        if any(keyword in line.lower() for keyword in ["vga", "3d", "display"]):
            gpu_lines.append(line)

    return gpu_lines


if __name__ == "__main__":
    print(get_gpu_info())