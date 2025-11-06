from playwright.sync_api import Page, expect

def test_homepage_title(running_server, page):
    base_url = running_server

    page.goto(base_url + "/") 
    
    expect(page).to_have_title("My website")