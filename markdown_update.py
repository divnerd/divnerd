import datetime

target_date = datetime.date(2023, 10, 27)

days_since = (datetime.date.today() - target_date).days

with open('markdown_output.md', 'w') as f:
    f.write(f"<p>Days since {target_date.strftime('%Y-%m-%d')}: {days_since}</p>\n")
