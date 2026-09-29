import psutil # pyright: ignore[reportMissingModuleSource]


def get_storage_info():
    storage = psutil.disk_usage("/")

    return {
        "total": storage.total,
        "used": storage.used,
        "free": storage.free,
        "percentage": storage.percent
    }


if __name__ == "__main__":
    print(get_storage_info())