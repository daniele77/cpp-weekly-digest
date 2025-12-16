# C++ Weekly Digest

C++ Weekly Digest is a project designed to provide a curated summary of the latest developments, news, and resources in the C++ ecosystem. It aims to help developers stay up-to-date with the rapidly evolving C++ landscape.

## Configuration

The project requires a `config.py` file for proper setup. This file contains essential configuration parameters. Here's an example structure:

```python
# config.py
from datetime import timedelta

TIME_WINDOW = timedelta(days=7)

RSS_SOURCES = {
    "ISO C++ Blog": "https://isocpp.org/blog/rss",
    "Herb Sutter": "https://herbsutter.com/feed/",
    "Sandor Dargo": "https://www.sandordargo.com/feed/",
    "LWN C++": "https://lwn.net/Headlines/C%2B%2B/"
}

YOUTUBE_CHANNELS = {
    "CppCon": "UCMlGfpWw-RUdWX_JbLCukXg",
}

WG21_PAPERS_URL = "https://www.open-std.org/jtc1/sc22/wg21/docs/papers/"
```

- `TIME_WINDOW`: The time range for filtering news, set to 7 days by default.
- `RSS_SOURCES`: A dictionary of RSS feed sources for gathering news.
- `YOUTUBE_CHANNELS`: A dictionary of YouTube channels to monitor for new videos.
- `WG21_PAPERS_URL`: The URL for accessing the latest WG21 papers.

## GitHub Actions

The project is integrated with GitHub Actions for automation. The workflow includes:

1. **News Aggregation**: Automatically fetches the latest news from the configured sources.
2. **Digest Generation**: Processes the news and generates a markdown file.
3. **Publishing**: Commits the generated digest to the repository.

The workflow is triggered on a weekly schedule and ensures the digest is always up-to-date.

## Testing Locally

To test the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/daniele77/cpp-weekly-digest.git
   cd cpp-weekly-digest
   ```

2. Create and configure the `config.py` file as described above.

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:
   ```bash
   python main.py
   ```

5. Check the parent directory for the generated digest in the file `weekly_report.md`.

Feel free to contribute or report issues to improve the project!