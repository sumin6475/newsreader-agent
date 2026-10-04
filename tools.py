from crewai_tools import SerperDevTool
from playwright.sync_api import sync_playwright

search_tool = SerperDevTool()

def scrape_tool(url: str):
    """
    Use this when you need to read the content of a web page. 
    Return the content of the web page. In case the content is not available, it returns no content.
    Input should be a 'url' string. (for example: "https://crewai.com/blog/the-state-of-agentic-ai-in-2026")
    """

    print (f"Scrapping URL: {url}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)