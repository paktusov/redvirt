import json

import libvirt


def get_vms_statistic() -> list[str]:
    active_vms_ids = get_active_vms_ids()
    statistics = []
    for vm_id in active_vms_ids:
        current_vm_info = get_vm_info_by_id(vm_id)
        statistics.append(json.dumps(current_vm_info))
    return statistics


def get_active_vms_ids() -> list[int]:
    with libvirt.open("qemu:///system") as conn:
        domains = conn.listDomainsID()
        return domains


def get_vm_info_by_id(vm_id: int) -> dict[str, str]:
    with libvirt.open("qemu:///system") as conn:
        domain = conn.lookupByID(vm_id)
        state, maxmem, mem, cpus, cput = domain.info()
        ip_addresses = get_vm_ips(domain)
        return dict(name=domain.name(),  cpus_usege=cpus, mem_usage=mem, ip_addresses=ip_addresses)


def get_vm_ips(domain: libvirt.virDomain) -> list[str]:
    try:
        interfaces = domain.interfaceAddresses(libvirt.VIR_DOMAIN_INTERFACE_ADDRESSES_SRC_AGENT, 0)
    except libvirt.libvirtError:
        return []

    ip_addresses = []
    for interface_name, interface_data in interfaces.items():
        if interface_name == "lo":
            continue
        if interface_data['addrs']:
            for ipaddr in interface_data['addrs']:
                if ipaddr['type'] != libvirt.VIR_IP_ADDR_TYPE_IPV4:
                    continue
                ip_addresses.append(ipaddr['addr'])

    return ip_addresses


if __name__ == "__main__":
    current_statistics = get_vms_statistic()
