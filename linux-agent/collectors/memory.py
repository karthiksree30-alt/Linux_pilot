import psutil  # type: ignore[reportMissingModuleSource]


def get_memory_info():
    memory = psutil.virtual_memory()

    return {
        "total": memory.total,
        "available": memory.available,
        "used": memory.used,
        "percentage": memory.percent
    }


if __name__ == "__main__":
    print(get_memory_info())