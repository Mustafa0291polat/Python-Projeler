import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match the src attribute of an iframe element
    pattern = r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"'
    match = re.search(pattern, s)

    if match:
        # Extract the video ID
        video_id = match.group(1)
        # Return the shortened youtu.be URL
        return f"https://youtu.be/{video_id}"
    else:
        return None

if __name__ == "__main__":
    main()
