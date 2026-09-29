import platform


def get_system_info():
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor()
    }


if __name__ == "__main__":
    print(get_system_info())