import psutil # pyright: ignore[reportMissingModuleSource]


def get_battery_info():
    battery = psutil.sensors_battery()

    if battery is None:
        return {
            "available": False
        }

    return {
        "available": True,
        "percentage": battery.percent,
        "charging": battery.power_plugged
    }


if __name__ == "__main__":
    print(get_battery_info())