# Unbabel-Challenge (Unbabel CLI)

This command line application calculates the moving average of translation delivery time based on a stream of events provided in a JSON file.

## Objective

The objective of this application is to parse a stream of events and produce an aggregated output of the moving average translation delivery time for each minute.

## Installation

1. Clone this repository:
```
git clone https://github.com/Mohamed-Elareef/Unbabel-Challenge.git
```

2. Navigate to the project directory:
```
cd unbabel-cli
```

3. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
Run the application using the following command:

python Challenge.py --input_file events.json --window_size 10


- `--input_file`: Specifies the input file containing the stream of events.
- `--window_size`: Specifies the size of the window in minutes for calculating the moving average.

## Input Format

The input file should contain JSON-formatted events, each representing a translation delivery. Example:

```json
{"timestamp": "2018-12-26 18:11:08.509654", "translation_id": "5aa5b2f39f7254a75aa5", "source_language": "en", "target_language": "fr", "client_name": "airliberty", "event_name": "translation_delivered", "nr_words": 30, "duration": 20}
{"timestamp": "2018-12-26 18:15:19.903159", "translation_id": "5aa5b2f39f7254a75aa4", "source_language": "en", "target_language": "fr", "client_name": "airliberty", "event_name": "translation_delivered", "nr_words": 30, "duration": 31}
{"timestamp": "2018-12-26 18:23:19.903159", "translation_id": "5aa5b2f39f7254a75bb3", "source_language": "en", "target_language": "fr", "client_name": "taxi-eats", "event_name": "translation_delivered", "nr_words": 100, "duration": 54}
```


## Output Format

```json
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
```


## Testing

Automated tests have been provided to ensure the correctness of the application. To run the tests, execute the following command:
```
python AutoTest.py
```
 





