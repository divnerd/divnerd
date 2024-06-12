import datetime

target_date = datetime.date(2023, 10, 27)

days_since = (datetime.date.today() - target_date).days

with open('markdown_output.md', 'w') as f:
    f.write(f"<p>I'm <strong>divnerd</strong> - a backend developer, python lover, and high-schooler. I'm in my school's cybersecurity club and I've been programming for {days_since} days!</p>\n")
