import logging
from config.config import configuration
import requests
from bs4 import BeautifulSoup
from saveFiles.saveToJSON import save_player_details_to_json, save_batting_summary_to_json, save_bowling_summary_to_json, save_scorecards_urls_to_json, save_t20_data_to_json, save_player_details_with_imageurl_to_json
from saveFiles.saveToCSV import save_player_details_to_csv, save_batting_summary_to_csv, save_bowling_summary_to_csv, save_t20_data_to_csv, save_player_details_with_imageurl_to_csv
import pandas as pd

_scrape_logger = logging.getLogger("webscrapper")

base_url = configuration.get_property('base_url')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Fetch data from the ESPN Cricinfo page
def fetch_espn_data(url):
    try:
        _scrape_logger.info("Fetching T20 data from ESPN Cricinfo...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        _scrape_logger.info("T20 Data fetched successfully!")
        return response.text
    except requests.exceptions.RequestException as e:
        _scrape_logger.error(f"Error fetching data: {e}")
        return None

# Fetch data from the ESPN Cricinfo page
def fetch_match_data(url):
    try:
        _scrape_logger.info("Fetching Match data from ESPN Cricinfo...")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        _scrape_logger.info("Match Data fetched successfully!")
        return response.text
    except requests.exceptions.RequestException as e:
        _scrape_logger.error(f"Error fetching data: {e}")
        return None

# Extract player details from match scorecard
def get_player_details(player_url, name):
    response = requests.get(player_url)
    if response.status_code == 200 or response.status_code == 403:
        soup = BeautifulSoup(response.content, 'html.parser')

        player_info = {
            'name': name,
            'team': 'N/A',  # Default value if no team is found
            'born': 'N/A',
            'age': 'N/A',
            'nicknames': 'N/A',
            'battingStyle': 'N/A',
            'bowlingStyle': 'N/A',
            'fieldingPosition': 'N/A',
            'playingRole': 'N/A',
            'height': 'N/A'
        }

        # Extract player details from the profile page
        player_details_div = soup.find('div', class_='ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8')

        if player_details_div:
            for div in player_details_div.find_all('div'): # type: ignore
                label = div.find('p', class_='ds-text-tight-m ds-font-regular ds-uppercase ds-text-typo-mid3')
                value = div.find('span', class_='ds-text-title-s ds-font-bold ds-text-typo')
                print(value)

                if label and value:
                    label_text = label.get_text(strip=True)
                    value_text = value.get_text(strip=True)

                    # Update the player_info dictionary with the extracted values
                    if label_text == "Born":
                        player_info['born'] = value_text
                    elif label_text == "Age":
                        player_info['age'] = value_text
                    elif label_text == "Nicknames":
                        player_info['nicknames'] = value_text
                    elif label_text == "Batting Style":
                        player_info['battingStyle'] = value_text
                    elif label_text == "Bowling Style":
                        player_info['bowlingStyle'] = value_text
                    elif label_text == "Fielding Position":
                        player_info['fieldingPosition'] = value_text
                    elif label_text == "Playing Role":
                        player_info['playingRole'] = value_text
                    elif label_text == "Height":
                        player_info['height'] = value_text

        # Extract first team name from the TEAMS section
        teams_section = soup.find('div', class_='ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-y-4')
        if teams_section:
            first_team = teams_section.find('span', class_='ds-text-title-s ds-font-bold ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block') # type: ignore
            if first_team:
                player_info['team'] = first_team.get_text(strip=True)  # Store only the first team

        _scrape_logger.info(f"Player {player_info['name']} details fetched successfully!!")
        return player_info
    else:
        _scrape_logger.error(f"Failed to retrieve playr without image data for {name}")
        return None

# Extract player details with imageurl from match scorecard
def get_player_details_with_imageurl(player_url, name):
    response = requests.get(player_url)
    if response.status_code == 200 or response.status_code == 403:
        soup = BeautifulSoup(response.content, 'html.parser')

        player_info = {
            'name': name,
            'team': 'N/A',  # Store only the first team name
            'born': 'N/A',
            'age': 'N/A',
            'nicknames': 'N/A',
            'battingStyle': 'N/A',
            'bowlingStyle': 'N/A',
            'fieldingPosition': 'N/A',
            'playingRole': 'N/A',
            'height': 'N/A',
            'playerImageUrl': 'N/A'  # New field for player image URL
        }

        # Extract player details from the profile page
        player_details_div = soup.find('div', class_='ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-4 ds-mb-8')

        if player_details_div:
            for div in player_details_div.find_all('div'):
                label = div.find('p', class_='ds-text-tight-m ds-font-regular ds-uppercase ds-text-typo-mid3')
                value = div.find('span', class_='ds-text-title-s ds-font-bold ds-text-typo')

                if label and value:
                    label_text = label.get_text(strip=True)
                    value_text = value.get_text(strip=True)

                    # Update the player_info dictionary with the extracted values
                    if label_text == "Born":
                        player_info['born'] = value_text
                    elif label_text == "Age":
                        player_info['age'] = value_text
                    elif label_text == "Nicknames":
                        player_info['nicknames'] = value_text
                    elif label_text == "Batting Style":
                        player_info['battingStyle'] = value_text
                    elif label_text == "Bowling Style":
                        player_info['bowlingStyle'] = value_text
                    elif label_text == "Fielding Position":
                        player_info['fieldingPosition'] = value_text
                    elif label_text == "Playing Role":
                        player_info['playingRole'] = value_text
                    elif label_text == "Height":
                        player_info['height'] = value_text

        # Extract first team name from the TEAMS section
        teams_section = soup.find('div', class_='ds-grid lg:ds-grid-cols-3 ds-grid-cols-2 ds-gap-y-4')
        if teams_section:
            first_team = teams_section.find('span', class_='ds-text-title-s ds-font-bold ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block')
            if first_team:
                player_info['team'] = first_team.get_text(strip=True)  # Store only the first team

        # Extract player image URL
        image_div = soup.find('div', class_='ds-ml-auto ds-w-36 ds-h-36')
        if image_div:
            img_tag = image_div.find('img')
            if img_tag and 'src' in img_tag.attrs: # type: ignore
                player_info['playerImageUrl'] = img_tag['src'] # type: ignore

        _scrape_logger.info(f"Player {player_info['name']} details fetched successfully!!")
        return player_info
    else:
        _scrape_logger.error(f"Failed to retrieve playr with image data for {name}")
        return None

# Extract html data
def parse_html(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", class_="ds-table")
        if not table:
            _scrape_logger.error("Error: Table not found on the page.")
            return None, None, None, None

        # Extract table headers dynamically
        header_row = table.find("thead")
        headers = [th.find("span").text.strip() for th in header_row.find_all("td")] if header_row else []
        matches = []
        scorecard_urls = []
        batting_summary = []  # Will hold the final array
        bowling_summary = []  # Will hold the final array

        # Extract data rows from the table
        for row in table.find("tbody").find_all("tr"): # type: ignore
            cells = row.find_all("td")
            row_data = [cell.text.strip() for cell in cells]

            # Extract the scorecard link from the last column
            scorecard_tag = cells[-1].find("a") if cells else None
            scorecard_text = scorecard_tag.text.strip() if scorecard_tag else "N/A"
            scorecard_link = scorecard_tag["href"] if scorecard_tag else None

            full_scorecard_url = f"{base_url}{scorecard_link}" if scorecard_link else None

            # Ensure the row has the expected number of columns
            while len(row_data) < len(headers):
                row_data.append("N/A")

            row_data[-1] = scorecard_text  # Update the last column to the Scorecard text
            matches.append(row_data)
            if full_scorecard_url:
                scorecard_urls.append(full_scorecard_url)
            _scrape_logger.info(f"Saving T20 match Info for {scorecard_text}")
            save_t20_data_to_csv(headers, matches)
            save_t20_data_to_json(headers, matches)
            _scrape_logger.info(f"Saving Score Card Urls for {scorecard_text}")
            save_scorecards_urls_to_json(scorecard_urls)

            # Extracting Batting Summary (for ENG vs PAK, adjust the field names)
            if full_scorecard_url:
                match_details_html = fetch_match_data(full_scorecard_url)

                if match_details_html:
                    # Extracting batting data with batsmanName and batsmanNameUrl
                    batting_data = extract_batting_summary(match_details_html, row_data[1], row_data[0])  # Use team names

                    for batsman in batting_data:
                        batsman_name = batsman['batsmanName']
                        batsman_url = batsman['batsmanNameUrl']
                        player_details = get_player_details(batsman_url, batsman_name)
                        player_details_images = get_player_details_with_imageurl(batsman_url, batsman_name)
                        if player_details:
                            # batsman.update(player_details)  # Add player details (name, battingStyle, etc.)
                            # Save player details to a JSON file
                            save_player_details_to_json(player_details)
                            save_player_details_with_imageurl_to_json(player_details_images)
                            save_player_details_to_csv(player_details)
                            save_player_details_with_imageurl_to_csv(player_details_images)

                    batting_summary.append({"match": f"{row_data[1]} vs {row_data[0]}", "batting_summary": batting_data})
                    batting_df = pd.DataFrame(batting_summary)
                    match = batting_df['match'].iloc[0]
                    _scrape_logger.info(f"Saving Batting Summary for match {match}")
                    save_batting_summary_to_csv(batting_summary)
                    save_batting_summary_to_json(batting_summary)

                    # Extract Bowling Summary (for ENG vs PAK)
                    bowling_data = extract_bowling_summary(match_details_html, row_data[0], row_data[1])
                    for bowler in bowling_data:
                        bowler_name = bowler['bowlerName']
                        bowler_url = bowler['bowlerNameUrl']
                        player_details = get_player_details(bowler_url, bowler_name)
                        player_details_images = get_player_details_with_imageurl(bowler_url, bowler_name)
                        if player_details:
                            # bowler.update(player_details)  # Add player details (name, bowlingStyle, etc.)
                            # Save player details to a JSON file
                            save_player_details_to_json(player_details)
                            save_player_details_with_imageurl_to_json(player_details_images)
                            save_player_details_to_csv(player_details)
                            save_player_details_with_imageurl_to_csv(player_details_images)

                    bowling_summary.append({"match": f"{row_data[0]} vs {row_data[1]}", "bowling_summary": bowling_data})
                    bowling_df = pd.DataFrame(bowling_data)
                    match = bowling_df['match'].iloc[0]
                    _scrape_logger.info(f"Saving Bowling Summary for match {match}")
                    save_bowling_summary_to_json(bowling_summary)
                    save_bowling_summary_to_csv(bowling_summary)
        return headers, matches, scorecard_urls, batting_summary, bowling_summary
    except Exception as e:
        _scrape_logger.error(f"Error parsing HTML: {e}")
        return None, None, None, None, None

# Extract Batting Summary from the match scorecard
def extract_batting_summary(html, team1, team2):
    try:
        soup = BeautifulSoup(html, "html.parser")
        batting_tables = soup.find_all("table", class_="ci-scorecard-table")

        matches_summary = []

        # Function to extract batsman data
        def extract_inning_data(rows, team_name):
            batting_pos = 1  # Initialize batting position counter
            for row in rows:
                tds = row.find_all("td")

                # Only consider rows that have at least 8 columns and a batsman link
                if len(tds) >= 8 and tds[0].find("a"):
                    batsman_link = tds[0].find("a")
                    batsman_name = batsman_link.text.strip() if batsman_link else ""
                    batsman_url = (base_url + batsman_link["href"]) if batsman_link else ""

                    dismissal = tds[1].text.strip() if len(tds) > 1 else ""
                    matches_summary.append({
                        "match": f"{team1} Vs {team2}",
                        "battingTeam": team_name,
                        "battingPos": batting_pos,  # Assign correct batting position
                        "batsmanName": batsman_name,
                        "batsmanNameUrl": batsman_url,
                        "dismissal": dismissal,
                        "runs": tds[2].find("strong").text.strip(),
                        "balls": tds[3].text.strip(),
                        "4s": tds[5].text.strip(),
                        "6s": tds[6].text.strip(),
                        "SR": tds[7].text.strip()
                    })

                    batting_pos += 1  # Increment batting position for the next valid batsman

        # First Innings (for team1)
        extract_inning_data(batting_tables[0].find("tbody").find_all("tr"), team1)

        # Second Innings (for team2)
        extract_inning_data(batting_tables[1].find("tbody").find_all("tr"), team2)

        return matches_summary
    except Exception as e:
        _scrape_logger.error(f"Error extracting batting summary: {e}")
        return []

# Extract Bowling Summary from the match scorecard
def extract_bowling_summary(html, team1, team2):
    try:
        soup = BeautifulSoup(html, "html.parser")
        bowling_tables = soup.find_all("table", class_="ds-w-full ds-table ds-table-md ds-table-auto")

        matches_summary = []

        # Function to extract bowler data
        def extract_inning_data(rows, team_name):
            for index, row in enumerate(rows):
                tds = row.find_all("td")
                if len(tds) >= 11:
                    bowler_link = tds[0].find("a")
                    bowler_name = bowler_link.text.strip() if bowler_link else tds[0].text.strip()
                    bowler_url = (base_url + bowler_link["href"]) if bowler_link else ""

                    matches_summary.append({
                        "match": f"{team1} Vs {team2}",
                        "bowlingTeam": team_name,
                        "bowlerName": bowler_name,
                        "bowlerNameUrl": bowler_url,
                        "overs": tds[1].text.strip(),
                        "maidens": tds[2].text.strip(),
                        "runs": tds[3].text.strip(),
                        "wickets": tds[4].text.strip(),
                        "economy": tds[5].text.strip(),
                        "0s": tds[6].text.strip(),
                        "4s": tds[7].text.strip(),
                        "6s": tds[8].text.strip(),
                        "wd": tds[9].text.strip(),
                        "nb": tds[10].text.strip()
                    })

        # First Innings (for team1)
        if len(bowling_tables) > 0:
            extract_inning_data(bowling_tables[0].find("tbody").find_all("tr"), team1)

        # Second Innings (for team2)
        if len(bowling_tables) > 1:
            extract_inning_data(bowling_tables[1].find("tbody").find_all("tr"), team2)

        return matches_summary
    except Exception as e:
        _scrape_logger.error(f"Error extracting bowling summary: {e}")
        return []
