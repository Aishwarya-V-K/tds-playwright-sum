from playwright.sync_api import sync_playwright

seeds = list(range(44, 54))
total_sum = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)
        page.wait_for_load_state("networkidle")

        numbers = page.locator("table td").all_text_contents()

        for num in numbers:
            total_sum += int(num.strip())

    browser.close()

print("FINAL TOTAL:", total_sum)
