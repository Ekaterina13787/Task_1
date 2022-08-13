from pages.base_page import BasePage


class Dashboard(BasePage):
    main_page = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]/div[2]"
    players = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    langauges = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[1]/div[2]/span"
    sign_out = "//*[@id="__next"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    players_count = "//*[@id="__next"]/div[1]/main/div[2]/div[1]/div/div[1]"
    matches_count = "//*[@id="__next"]/div[1]/main/div[2]/div[2]/div/div[2]"
    reports_count = "//*[@id="__next"]/div[1]/main/div[2]/div[3]/div/div[2]"
    events_count = "//*[@id="__next"]/div[1]/main/div[2]/div[4]/div/div[1]"
    scouts_panel = "//*[@id="__next"]/div[1]/main/div[3]/div[1]/div/div[2]"
    add_player = "//*[@id="__next"]/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    test_name = "//*[@id="__next"]/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"