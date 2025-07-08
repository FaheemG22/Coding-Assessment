from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    # URL of the public Google Doc
    url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

    # How much non essential data to trim manual
    skip = 5

    # Set up the WebDriver
    driver = webdriver.Chrome()

    # Calls Function to receive the data
    raw_data = selenium_get(driver, url, )

    #Calls function re-structures and cleans up the data
    x, y, unicode = data_cleanup(raw_data, skip)

    driver.quit()

    display(x, y, unicode)
    #Displays the data


# Finds elements by class and removes non-relevant data
def selenium_get(driver, url):
    driver.get(url)
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elements = driver.find_elements(By.CLASS_NAME, "c1")
    return elements

# Breaks up and sorts out all the data
def data_cleanup(elements, skip):
    # This removes the first few lines
    elements = elements[skip:]
    count = 0
    x = []
    y = []
    unicode = []

    # could be improved this is sloppy
    for element in elements:
        element = element.text.strip()
        if element == '':
            pass
        elif count == 0:
            x.append(element)
            count += 1
        elif count == 1:
            unicode.append(element)
            count += 1
        elif count == 2:
            y.append(element)

            count = 0
    """
    Debug
    print(x)
    print(y)
    """
    return x, y, unicode


def display(x, y, unicode):
    """
    Debug
    print(len(x), len(y), len(unicode))
    print(x[0], y[0], unicode[0])
    print(x[-1], y[-1], unicode[-1])
    """

    # Create a grid filled with spaces
    grid = [[' ' for _ in range(350)] for _ in range(350)]

    # Place the Unicode character at the specified positions
    for i in range(len(x)):
        xi = int(x[i])
        yi = int(y[i])
        if 0 <= xi < len(x) and 0 <= yi < len(y):
            grid[yi][xi] = unicode[i]
        else:
            print(f"Warning: Skipping out-of-bounds coordinate ({xi}, {yi})")

    # Print the grid
    for row in grid:
        print(''.join(row))


main()
