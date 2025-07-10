# csv_reports.py

This script connects to a Cisco vManage instance, retrieves device and tunnel statistics, and exports the data to CSV files.

## Prerequisites

- Python 3.9+
- `catalystwan` Python module installed
- Access to a Cisco vManage instance

## Setup

1. Install required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the script with the required CLI arguments:

```sh
python csv_reports.py --VMANAGE_IP <vmanage_ip> --VMANAGE_USER <username> --VMANAGE_PASSWORD <password> [--VMANAGE_PORT <port>]
```

Example:

```sh
python csv_reports.py --VMANAGE_IP 192.168.1.100 --VMANAGE_USER admin --VMANAGE_PASSWORD password123
```

Note: `--VMANAGE_PORT` is optional and defaults to 443.

This will:

- Connect to the vManage API
- Fetch device and tunnel statistics
- Save the results to `devices.csv` and `tunnels_stats.csv` in the current directory

## Output

- `devices.csv`: List of edge devices (vedge)
- `tunnels_stats.csv`: Tunnel health and latency statistics

## Notes

- The script filters out SDWAN controllers, saving only edge devices.
- Make sure your vManage credentials are correct and the API is reachable.
- All connection parameters are now provided via CLI arguments for better security and flexibility.

## Files

- [`csv_reports.py`](csv_reports.py): Main script

---
