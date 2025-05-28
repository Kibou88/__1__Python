from ipaddress import IPv4Address
def ips_between(start, end):
    return int(IPv4Address(end)) - int(IPv4Address(start))

if __name__ == "__main__":
    start = "10.11.12.13"
    end = "10.11.13.0"

    # print(int(IPv4Address(start)))
    # print(int(IPv4Address(end)))
    # result = int(IPv4Address(end)) - int(IPv4Address(start))
    # print(result)
    print(ips_between(start, end))