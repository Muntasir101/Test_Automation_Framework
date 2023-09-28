import os


def capture_screenshot(driver, test_name):
    """
    Capture a screenshot and save it to the 'Screenshots' directory.

    Args:
        driver: The Selenium WebDriver instance.
        test_name (str): The name of the test to use as the screenshot filename.
    """
    screenshots_dir = os.path.join(os.getcwd(), "Screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    screenshot_filename = f"{test_name}.png"
    screenshot_path = os.path.join(screenshots_dir, screenshot_filename)

    try:
        driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved: {screenshot_path}")
    except Exception as e:
        logger.error(f"Failed to capture and save screenshot: {str(e)}")
