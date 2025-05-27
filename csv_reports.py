import urllib3
import csv
import os
import sys
from catalystwan.session import create_manager_session

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_vmanage_credentials():

    try:
        url = os.environ["VMANAGE_IP"]
        username = os.environ["VMANAGE_USER"]
        password = os.environ["VMANAGE_PASSWORD"]
        port = os.environ["VMANAGE_PORT"]
        return url, username, password, port

    except Exception as e:
        print("Error loading credentials: {}".format(e))
        sys.exit(1)


def parse_data_from_get_request(session, endpoint):

    print("Fetching data from {}".format(endpoint))

    response = session.get(endpoint)
    data = response.json()["data"]

    return data


def save_data_to_csv(destination_file, data):

    headers = data[0].keys()
    data_table = [list(item.values()) for item in data]

    with open(destination_file, "w") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(headers)
        csv_writer.writerows(data_table)

    print(f"{destination_file} saved!")


if __name__ == "__main__":

    url, username, password, port = get_vmanage_credentials()

    bfd_stats_endpoint = "/dataservice/statistics/approute/tunnels/health/latency?limit=100000"
    device_endpoint = "/dataservice/device"

    with create_manager_session(
        url=url,
        username=username,
        password=password,
        port=int(port),
    ) as session:

        if session:
            print("vManage Session created successfully!")

        device_list = parse_data_from_get_request(session, device_endpoint)
        print("Removing SDWAN Controllers from device list")
        edge_list = [
            device for device in device_list if device.get("device-type") == "vedge"
        ]
        print("Edges found: {}".format(len(edge_list)))
        save_data_to_csv("devices.csv", edge_list)

        tunnels_stats = parse_data_from_get_request(session, bfd_stats_endpoint)
        print("Tunnels found: {}".format(len(tunnels_stats)))
        save_data_to_csv("tunnels_stats.csv", tunnels_stats)

        print("Done!")

    print("vManage Session closed!")
