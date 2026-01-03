from playwright.sync_api import sync_playwright, expect

def verify_no_placeholders():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            page.goto("http://localhost:3000")
            page.wait_for_selector("text=Passport Pal", timeout=10000)

            # Verify no placeholders
            content = page.content()
            if "Lorem Ipsum" in content or "Insert Name" in content:
                print("Error: Placeholders found!")
            else:
                print("No placeholders found.")

            page.screenshot(path="verification/verification_final.png")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()

if __name__ == "__main__":
    verify_no_placeholders()
