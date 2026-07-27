from playwright.sync_api import sync_playwright
from pathlib import Path
import img2pdf

def main():
    output_dir = Path("screenshots")
    output_dir.mkdir(exist_ok=True)
    link = input("SCRIB-DL\ninput scribd link: ")
    with sync_playwright() as p:
        browser = p.chromium.launch()

        page = browser.new_page(viewport={"width": 1600, "height": 3000})
        print("going to scribd file..")

        page.goto(link, wait_until="domcontentloaded")
        print("loaded DOM")

        uploader = page.get_by_label("Uploaded by").locator("..").locator("a").nth(0).inner_text()
        print(f"Uploaded by {uploader}")

        title = page.title()
        print(f"File: {title}")

        description = page.locator('[data-e2e="description"] > div').nth(0).inner_text()
        print(f"Description:\n{description}")

        #scroll to bypass scribd's lazy loading system that requires you to scroll the ENTIRE THING for all of the pages to load
        for i in range(30):
            page.mouse.wheel(0, 1000)
            page.wait_for_timeout(500)
        print("preloaded pages, downloading images of each page")
        pages = page.locator(".newpage")
        count = pages.count()
        print(f"found {count} pages")

        for i in range(count):
            div = pages.nth(i)

            div.scroll_into_view_if_needed()
            page.wait_for_timeout(500)

            div.screenshot(path=str(output_dir / f"page_{i + 1}.png"))
            print(f"Saved page_{i + 1}.png")
        screenshots = list(Path("screenshots").iterdir())
        with open(f"output.pdf", "wb") as f:
            f.write(
                img2pdf.convert(
                    screenshots,
                    author=uploader,
                    title=title,
                    subject=description,
                )
            )
        print("saved output.pdf")
        browser.close()

if __name__ == "__main__":
    main()