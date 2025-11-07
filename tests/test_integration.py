from playwright.sync_api import Page, expect

def test_homepage_title(running_server, page):
    base_url = running_server
    page.goto(base_url + "/") 
    expect(page).to_have_title("My website")

def test_homepage_content(running_server, page):
    base_url = running_server
    page.goto(base_url + "/") 
    heading = page.locator("h1")
    expect(heading).to_have_text("Home page!")

def test_pokemon_page(running_server, page):
    base_url = running_server
    page.goto(base_url + "/pokemon") 
    list_item = page.locator("li")
    expect(list_item).to_have_text([
        "Charizard",
        "Lucario",
        "Umbreon",
        "Pikachu"
    ])

def test_custom_page_not_found(running_server, page):
    base_url = running_server
    page.goto(base_url + "/non-existent-page")
    heading = page.locator("h1")
    sub_heading = page.locator("h2")
    expect(heading).to_have_text("404")
    expect(sub_heading).to_have_text("Page not found")

