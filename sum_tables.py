from playwright.sync_api import sync_playwright

urls = [
    "https://sanand0.github.io/tdsdata/js_table/?seed=66",
    "https://sanand0.github.io/tdsdata/js_table/?seed=67",
    "https://sanand0.github.io/tdsdata/js_table/?seed=68",
    "https://sanand0.github.io/tdsdata/js_table/?seed=69",
    "https://sanand0.github.io/tdsdata/js_table/?seed=70",
    "https://sanand0.github.io/tdsdata/js_table/?seed=71",
    "https://sanand0.github.io/tdsdata/js_table/?seed=72",
    "https://sanand0.github.io/tdsdata/js_table/?seed=73",
    "https://sanand0.github.io/tdsdata/js_table/?seed=74",
    "https://sanand0.github.io/tdsdata/js_table/?seed=75"
]

total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    for url in urls:
        page.goto(url)
        page.wait_for_selector("table")

        cells = page.locator("td").all_text_contents()

        for val in cells:
            try:
                total_sum += int(val)
            except:
                pass

    browser.close()

print("FINAL SUM:", total_sum)