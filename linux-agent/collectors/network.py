import psutil # pyright: ignore[reportMissingModuleSource]


def get_network_info():
    info = {}

    # Per-interface addresses (IPv4, IPv6, MAC)
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    interfaces = {}
    for iface_name, iface_addrs in addrs.items():
        iface_info = {
            "addresses": [],
            "is_up": stats[iface_name].isup if iface_name in stats else None,
            "speed_mbps": stats[iface_name].speed if iface_name in stats else None,
            "mtu": stats[iface_name].mtu if iface_name in stats else None,
        }
        for addr in iface_addrs:
            iface_info["addresses"].append({
                "family": str(addr.family),
                "address": addr.address,
                "netmask": addr.netmask,
                "broadcast": addr.broadcast,
            })
        interfaces[iface_name] = iface_info

    info["interfaces"] = interfaces

    # Overall I/O counters
    io = psutil.net_io_counters()
    info["io"] = {
        "bytes_sent": io.bytes_sent,
        "bytes_recv": io.bytes_recv,
        "packets_sent": io.packets_sent,
        "packets_recv": io.packets_recv,
        "errin": io.errin,
        "errout": io.errout,
        "dropin": io.dropin,
        "dropout": io.dropout,
    }

    return info


if __name__ == "__main__":
    print(get_network_info())