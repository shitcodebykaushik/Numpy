import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "http://localhost:8081/IQBAL"
total_requests = 1
concurrency = 100

def send_request():
    start_time = time.time()
    try:
        response = requests.get(url)
        status_code = response.status_code
    except Exception as e:
        status_code = f"Error: {e}"
    duration = time.time() - start_time
    return status_code, duration

def main():
    total_duration = 0.0
    results = []
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = [executor.submit(send_request) for _ in range(total_requests)]
        for i, future in enumerate(as_completed(futures), start=1):
            status_code, duration = future.result()
            total_duration += duration
            results.append(status_code)
            if i % 10000 == 0:
                print(f"{i} requests completed.")
    average_duration = total_duration / total_requests
    print("Completed all requests.")
    print(f"Average request time: {average_duration:.4f} seconds")
    
    # Optionally, print a summary of status codes
    status_summary = {}
    for status in results:
        status_summary[status] = status_summary.get(status, 0) + 1
    print("Status Code Summary:")
    for code, count in status_summary.items():
        print(f"{code}: {count}")

if __name__ == "__main__":
    main()
