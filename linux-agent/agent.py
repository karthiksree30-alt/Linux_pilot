from collectors.cpu import get_cpu_info
from collectors.memory import get_memory_info
from collectors.storage import get_storage_info
from collectors.gpu import get_gpu_info
from collectors.network import get_network_info
from collectors.battery import get_battery_info
from collectors.system import get_system_info
from diagnostics.boot import get_boot_mode


def collect_system_information():

    information = {
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "storage": get_storage_info(),
        "gpu": get_gpu_info(),
        "network": get_network_info(),
        "battery": get_battery_info(),
        "system": get_system_info(),
        "boot": get_boot_mode()
    }

    return information


if __name__ == "__main__":

    information = collect_system_information()

    for category, data in information.items():

        print("\n==============================")
        print(category.upper())
        print("==============================")

        print(data)