import os


def get_boot_mode():
    if os.path.exists("/sys/firmware/efi"):
        return "UEFI"

    return "Legacy BIOS"


if __name__ == "__main__":
    print("Boot Mode:", get_boot_mode())