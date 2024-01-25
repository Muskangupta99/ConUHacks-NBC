## Overview

This script is designed to read data from multiple JSON files, process and annotate the data, and then send it to a Power BI API endpoint for visualization and analysis. The script simulates sending real-time data to the Power BI endpoint.

![screen-capture-conuhack-NBC-ezgif com-video-to-gif-converter (1)](https://github.com/Muskangupta99/ConUHacks-NBC/assets/60093511/2e9ec4f8-2f43-4771-b21d-6fe9a0eaad7e)


## Usage

1. **Requirements:**
   - Ensure you have Python installed on your system.
   - Install the required Python packages using:
     ```bash
     pip install requests
     ```

2. **Configuration:**
   - Update the `endpoint` variable with your Power BI API endpoint.

3. **Data Files:**
   - Prepare JSON files ('Exchange_1.json', 'Exchange_2.json', 'Exchange_3.json') with the required data.

4. **Execution:**
   - Run the script using:
     ```bash
     python script_name.py
     ```

5. **Analysis:**
   - Analyze the data using the Power BI dashboard connected to the specified API endpoint.
   - The script sends data to the Power BI API endpoint in real-time, simulating a live data feed.

6. **Note:**
   - The script sends data to the Power BI API endpoint and prints the results.
   - A delay of 1 second is introduced between API requests.
