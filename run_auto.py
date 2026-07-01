# from playwright.sync_api import sync_playwright
# import time

# def main():
#     with sync_playwright() as p:
#         print("Launching headless browser...")
#         browser = p.chromium.launch(headless=True)
#         context = browser.new_context()
#         page = context.new_page()

#         spreadsheet_url = "https://docs.google.com/spreadsheets/d/1tdlBoFMRnPkawkPP3aBIh_36WWco4yywDFsvKq0L1h4/edit?gid=1796028663#gid=1796028663"
#         print("Navigating to spreadsheet...")
#         page.goto(spreadsheet_url)

#         print("Waiting 10 seconds for the sheet to load...")
#         page.wait_for_timeout(10000)

#         # ---- ADDED SCREENSHOT STEP ----
#         print("Taking a screenshot to check the page state...")
#         page.screenshot(path="debug_screenshot.png")
#         print("Screenshot saved as debug_screenshot.png")
#         # -------------------------------

#         try:
#             print("Locating cell input...")
#             cell_input = page.locator(".grid-io-focused-input")
            
#             cell_input.click()
#             page.keyboard.press("Control+A")
#             page.keyboard.press("Backspace")
#             cell_input.type("ngulati-wnsgur@ops.stripe.com")
#             page.keyboard.press("Enter")
#             print("Cell value updated successfully.")

#             page.wait_for_timeout(3000)

#             print("Searching for drawing buttons on sheet...")
#             drawing_buttons = page.locator("div.apps-embedded-object-container")
            
#             count = drawing_buttons.count()
#             if count > 0:
#                 print(f"Found {count} drawing(s) on this page tab.")
#                 target_button = drawing_buttons.nth(0)
#                 target_button.click()
#                 print("Drawing button clicked successfully!")
#             else:
#                 print("Could not find any drawing shapes.")

#         except Exception as e:
#             print(f"An automated step encountered an error: {e}")

#         page.wait_for_timeout(5000)
#         context.close()
#         browser.close()

# if __name__ == "__main__":
#     main()


import requests

WEB_APP_URL = "https://script.google.com/macros/s/AKfycbw9Ej-eKpgmcbWJDW0PLFdYb8ZxG8aDbTr2Zb3UaKKbRki7NjM6ESqjfUz8qSbvp-na/exec"
data=input("Type here: ")
payload = {
    "email": data
}

try:

    response = requests.post(
        WEB_APP_URL,
        json=payload
    )

    print("Status Code:", response.status_code)
    print("Response Text:")
    print(response.text)

except Exception as e:
    print("Error:", e)
