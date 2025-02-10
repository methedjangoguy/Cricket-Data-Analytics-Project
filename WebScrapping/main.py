import log.log as log
from config.config import configuration
from scrapper.webscrapper import fetch_espn_data, parse_html

_root_logger = log.setup_custom_logger("root")
t20_url = configuration.get_property('t20_url')

# Main execution logic
def main():
    _root_logger.info(f'WebScrapping "{t20_url}" Started')
    try:
        html = fetch_espn_data(t20_url)
        if html:
            parse_html(html)

    except KeyboardInterrupt:
        _root_logger.warning("\nProcess interrupted by user. Exiting gracefully...")
    except Exception as e:
        _root_logger.error(f"An unexpected error occurred: {e}")
    _root_logger.info('Full WebScrapping Execution Completed.')

if __name__ == "__main__":
    main()
