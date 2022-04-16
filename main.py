import sys
import command_questions as cq


if __name__ == "__main__":

    if len(sys.argv) > 1:
        if sys.argv[1] == "-c":
            cq.run_create_campaigns()
        elif sys.argv[1] == "-t":
            cq.run_retrieve_tracking_urls()
        elif sys.argv[1] == "-d":
            dynamics = True
            cq.run_create_line_items(dynamics)
        elif sys.argv[1] == "-s":
            dynamics = False
            cq.run_create_line_items(dynamics)
    
    else:
        print("""
            Please include a command you would like to run:
            -c --> create a campaign
            -d --> create campaign dynamics
            -s --> create campaign streaming
            -t --> retrieve tracking urls
        """
        )
