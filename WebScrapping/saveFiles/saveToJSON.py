import pandas as pd
from config.config import configuration
import logging
import os
import json
from pathlib import Path
import unicodedata

_json_logger = logging.getLogger("json")

espn_t20_wc_2022_results_json_filepath = configuration.get_property('espn_t20_wc_2022_results_json_filepath')
batting_summary_json_file_path = configuration.get_property('batting_summary_json_file_path')
bowling_summary_json_file_path = configuration.get_property('bowling_summary_json_file_path')
player_details_json_file_path = configuration.get_property('player_details_json_file_path')
player_details_with_imageurl_json_file_path = configuration.get_property('player_details_with_imageurl_json_file_path')
scorecard_urls_json_file_path = configuration.get_property('scorecard_urls_json_file_path')

def clean_text(text):
    if isinstance(text, str):
        return unicodedata.normalize("NFKC", text).strip()
    return text

# Save player info data to a json file
def save_player_details_to_json(player_details, file_path=player_details_json_file_path):
    try:
        # Check if file exists and read existing data
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []  # In case of invalid JSON
        else:
            data = []

        # Append new player details
        data.append(player_details)

        # Write back to the file
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        _json_logger.info(f"Player {player_details['name']} details successfully appended to {file_path}")
    except Exception as e:
        _json_logger.error(f"Error saving player details: {e}")

# Save bowling summary data to a json file
def save_bowling_summary_to_json(bowling_summary, filename=bowling_summary_json_file_path):
    try:
        formatted_summary = []

        for match_data in bowling_summary:
            cleaned_bowling_summary = []
            for bowler in match_data["bowling_summary"]:
                bowler["bowlerName"] = clean_text(bowler.get("bowlerName", ""))
                cleaned_bowling_summary.append(bowler)

            formatted_summary.append({"bowlingSummary": cleaned_bowling_summary})

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(formatted_summary, f, indent=4, ensure_ascii=False)

        _json_logger.info(f"Bowling summary saved successfully to {filename}")
    except Exception as e:
        _json_logger.error(f"Error saving bowling summary to JSON: {e}")

# Save batting summary data to a json file
def save_batting_summary_to_json(batting_summary, filename=batting_summary_json_file_path):
    try:
        df = pd.DataFrame(batting_summary)
        match = df['match'].iloc[0]
        formatted_summary = []

        for match_data in batting_summary:
            cleaned_batting_summary = []
            for player in match_data["batting_summary"]:
                player["batsmanName"] = clean_text(player.get("batsmanName", ""))
                cleaned_batting_summary.append(player)

            formatted_summary.append({"battingSummary": cleaned_batting_summary})

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(formatted_summary, f, indent=4, ensure_ascii=False)

        _json_logger.info(f"Batting summary for match {match} saved successfully to {filename}")
    except Exception as e:
        _json_logger.error(f"Error saving batting summary to JSON: {e}")

# Save parsed match data to a json file
def save_t20_data_to_json(headers, data, filename=espn_t20_wc_2022_results_json_filepath):
    try:
        # Convert data to list of dictionaries
        match_summary = [dict(zip(headers, [str(value).strip() for value in row])) for row in data]

        # Format as required JSON structure
        json_data = [{"matchSummary": match_summary}]

        # Save to JSON file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        _json_logger.info(f"T20 Match data saved successfully to {filename}")
    except Exception as e:
        _json_logger.error(f"Error saving data to JSON: {e}")

# Save parsed scorecard url data to a json file
def save_scorecards_urls_to_json(data, filename=scorecard_urls_json_file_path):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        _json_logger.info(f"Scorecard URLs saved successfully to {filename}")
    except Exception as e:
        _json_logger.error(f"Error saving data to JSON: {e}")

# Save player info with imageurl data to a json file
def save_player_details_with_imageurl_to_json(player_details, file_path=player_details_with_imageurl_json_file_path):
    try:
        # Check if file exists and read existing data
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []  # In case of invalid JSON
        else:
            data = []

        # Append new player details
        data.append(player_details)

        # Write back to the file
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        _json_logger.info(f"Player {player_details['name']} details with image URL successfully appended to {file_path}")
    except Exception as e:
        _json_logger.error(f"Error saving player details: {e}")
