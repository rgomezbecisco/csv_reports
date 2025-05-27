# csv_reports.py

This script connects to a Cisco vManage instance, retrieves device and tunnel statistics, and exports the data to CSV files.

## Prerequisites

- Python 3.9+
- `catalystwan` Python module installed
- Access to a Cisco vManage instance
- Environment variables set for vManage credentials

## Setup

1. Install required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

2. Set the following environment variables (you can use the provided `samplecreds.sh`):
    - `VMANAGE_IP`
    - `VMANAGE_USER`
    - `VMANAGE_PASSWORD`
    - `VMANAGE_PORT`

    Example:

    ```sh
    source samplecreds.sh
    ```

## Usage

Run the script:

```sh
python csv_reports.py
```

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

## Files

- [`csv_reports.py`](csv_reports.py): Main script
- [`samplecreds.sh`](samplecreds.sh): Example credentials setup

---
