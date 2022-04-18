from core import run_delete_campaign, start, run_create_campaign, run_create_line_item, run_retrieve_tracking_urls


def main():
    action = start()
    if action == "campaign":
        run_create_campaign()
    elif action == "dynamic":
        run_create_line_item()
    elif action == "streaming":
        run_create_line_item("streaming")
    elif action == "urls":
        run_retrieve_tracking_urls()
    elif action == "delete":
        run_delete_campaign()


if __name__ == "__main__":
    main()
