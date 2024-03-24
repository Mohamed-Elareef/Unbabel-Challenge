import json
from collections import deque
from datetime import datetime

def parse_event(event):
    return {
        'timestamp': datetime.strptime(event['timestamp'], '%Y-%m-%d %H:%M:%S.%f'),
        'duration': event['duration']
    }

def calculate_moving_average(events, window_size):
    moving_averages = []
    durations_window = deque(maxlen=window_size)
    total_duration = 0

    print("Calculating moving average...")
    for event in events:
        durations_window.append(event['duration'])
        total_duration += event['duration']
        
        if len(durations_window) == window_size:
            moving_averages.append(total_duration / window_size)
            total_duration -= durations_window.popleft()

            # Print moving average for debugging
            print("Moving average:", total_duration / window_size)

    return moving_averages

def generate_output(events, moving_averages):
    output = []
    print("Generating output...")
    for event, avg_duration in zip(events[len(events) - len(moving_averages):], moving_averages):
        output.append({
            'date': event['timestamp'].strftime('%Y-%m-%d %H:%M:00'),
            'average_delivery_time': avg_duration
        })

        # Print input and output data for debugging
        print("Input event:", event)
        print("Output event:", output[-1])

    return output

def main(input_file, window_size):
    print("Reading input file...")
    with open(input_file, 'r') as f:
        input_events = [json.loads(line) for line in f]

    events = [parse_event(event) for event in input_events]

    moving_averages = calculate_moving_average(events, window_size)
    output = generate_output(events, moving_averages)

    print("Writing output to file...")
    with open('output.json', 'w') as f:
        for entry in output:
            f.write(json.dumps(entry) + '\n')

    print("Process completed successfully!")

if __name__ == "__main__":
    input_file = "events.json"
    window_size = 2

    main(input_file, window_size)
