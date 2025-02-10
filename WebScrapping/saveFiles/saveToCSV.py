import pandas as pd
from config.config import configuration
import logging
import os

_csv_logger = logging.getLogger("csv")

espn_t20_wc_2022_results_csv_file_path = configuration.get_property('espn_t20_wc_2022_results_csv_file_path')
batting_summary_csv_file_path = configuration.get_property('batting_summary_csv_file_path')
bowling_summary_csv_file_path = configuration.get_property('bowling_summary_csv_file_path')
player_details_csv_file_path = configuration.get_property('player_details_csv_file_path')
player_details_with_imageurl_csv_file_path = configuration.get_property('player_details_with_imageurl_csv_file_path')

# Save parsed match data to a CSV file
def save_t20_data_to_csv(headers, data, filename=espn_t20_wc_2022_results_csv_file_path):
    try:
        df = pd.DataFrame(data, columns=headers)
        df.to_csv(filename, index=False)
        _csv_logger.info(f"T20 Match data saved successfully to {filename}")
    except Exception as e:
        _csv_logger.error(f"Error saving data to CSV: {e}")

# Save batting summary data to a CSV file
def save_batting_summary_to_csv(batting_summary, filename=batting_summary_csv_file_path):
    try:
        all_batting_data = []
        for match_data in batting_summary:
            match = match_data["match"]
            for player in match_data["batting_summary"]:
                all_batting_data.append({
                    "match": match,
                    **player
                })
        df = pd.DataFrame(all_batting_data)
        match = df['match'].iloc[0]
        df.to_csv(filename, index=False)
        _csv_logger.info(f"Batting summary for match {match} saved successfully to {filename}")
    except Exception as e:
        _csv_logger.error(f"Error saving batting summary to CSV: {e}")

# Save bowling summary data to a CSV file
def save_bowling_summary_to_csv(bowling_summary, filename=bowling_summary_csv_file_path):
    try:
        all_batting_data = []
        for match_data in bowling_summary:
            match = match_data["match"]
            for player in match_data["bowling_summary"]:
                all_batting_data.append({
                    "match": match,
                    **player
                })
        df = pd.DataFrame(all_batting_data)
        match = df['match'].iloc[0]
        df.to_csv(filename, index=False)
        _csv_logger.info(f"Bowling summary for match {match} saved successfully to {filename}")
    except Exception as e:
        _csv_logger.error(f"Error saving Bowling summary to CSV: {e}")

# Save player info data to a CSV file
def save_player_details_to_csv(player_details, filename=player_details_csv_file_path):
    try:
        # Convert player details into a DataFrame
        df = pd.DataFrame([player_details])  # Convert single dictionary to a DataFrame
        player_name = df['name'].iloc[0]  # Using iloc
        # Check if the file exists to decide if headers are needed
        file_exists = os.path.isfile(filename)

        # Append data to the CSV file without overwriting
        df.to_csv(filename, mode='a', index=False, header=not file_exists, encoding='utf-8')

        _csv_logger.info(f"Player {player_name} Details saved successfully to {filename}")
    except Exception as e:
        _csv_logger.error(f"Error saving player details to CSV: {e}")

def save_player_details_with_imageurl_to_csv(player_details, filename=player_details_with_imageurl_csv_file_path):
    try:
        # Convert player details into a DataFrame
        df = pd.DataFrame([player_details])  # Convert single dictionary to a DataFrame
        player_name = df['name'].iloc[0]  # Using iloc
        # Check if the file exists to decide if headers are needed
        file_exists = os.path.isfile(filename)

        # Append data to the CSV file without overwriting
        df.to_csv(filename, mode='a', index=False, header=not file_exists, encoding='utf-8')

        _csv_logger.info(f"Player {player_name} Details with imageurl saved successfully to {filename}")
    except Exception as e:
        _csv_logger.error(f"Error saving player details to CSV: {e}")
