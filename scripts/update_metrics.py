import os
import sys
import urllib.request
import re

USERNAME = "jeevesh2515"

ENDPOINTS = {
    "assets/stats.svg": f"https://github-readme-stats-eight-theta.vercel.app/api?username={USERNAME}&show_icons=true&theme=tokyonight&hide_border=true",
    "assets/languages.svg": f"https://github-readme-stats-eight-theta.vercel.app/api/top-langs/?username={USERNAME}&layout=compact&theme=tokyonight&hide_border=true&card_width=369",
    "assets/activity-graph.svg": f"https://github-readme-activity-graph-eight.vercel.app/graph?username={USERNAME}&theme=tokyo-night&hide_border=true&area=true",
}

def is_valid_svg(content: str) -> bool:
    if not content or len(content) < 500:
        return False
    if "<svg" not in content:
        return False
    error_patterns = [
        r"something unexpected happened",
        r"deployment_paused",
        r"deployment_disabled",
        r"404 not found",
        r"402 payment required",
        r"rate limit exceeded"
    ]
    for pattern in error_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return False
    return True

def fetch_svg(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0 (GitHubActions-ProfileMetricsRefresher/1.0)"}
    )
    with urllib.request.urlopen(req, timeout=15) as response:
        return response.read().decode("utf-8")

def main():
    os.makedirs("assets", exist_ok=True)
    
    for filepath, url in ENDPOINTS.items():
        print(f"Fetching {filepath} from {url}...")
        try:
            content = fetch_svg(url)
            if is_valid_svg(content):
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(content)
                print(f"✅ Successfully updated {filepath} ({len(content)} bytes)")
            else:
                print(f"⚠️ Received invalid SVG or error for {filepath}. Keeping existing file.")
        except Exception as e:
            print(f"❌ Failed to fetch {filepath}: {e}. Keeping existing file.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
