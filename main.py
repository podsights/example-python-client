from questions import start, run_create_campaign, run_create_line_item


def main():
    action = start()
    if action == "campaign":
        run_create_campaign()
    elif action == "dynamic":
        run_create_line_item()
    elif action == "urls":
        pass


if __name__ == "__main__":
    main()
