from core import start, run_create_campaign, run_create_line_item, run_retrieve_tracking_urls


def main():
    action = start()
    if action == "campaign":
        run_create_campaign()
    elif action == "dynamic":
        run_create_line_item()
    elif action == "urls":
        run_retrieve_tracking_urls()


if __name__ == "__main__":
    main()
