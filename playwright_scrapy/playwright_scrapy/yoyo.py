

from playwright.sync_api import Playwright, sync_playwright, expect
def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://www.google.com/search?q=flipkart&oq=flipkart&aqs=chrome..69i57.2731j0j2&sourceid=chrome&ie=UTF-8
    page.goto("https://www.google.com/search?q=flipkart&oq=flipkart&aqs=chrome..69i57.2731j0j2&sourceid=chrome&ie=UTF-8")
    # Click text=Flipkart.com® Online Shop - Shop Online with Best Offers
    page.locator("text=Flipkart.com® Online Shop - Shop Online with Best Offers").click()
    # expect(page).to_have_url("https://www.flipkart.com/?s_kwcid=AL!739!3!582822043916!e!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_exe_buyers_goog&gclid=EAIaIQobChMIu_mNlqrO-AIV6Z1LBR2wmQgREAAYASAAEgLPoPD_BwE")
    # Click text=✕
    page.locator("text=✕").click()
    # Click text=Men's Jeans
    page.locator("text=Men's Jeans").click()
    # expect(page).to_have_url("https://www.flipkart.com/mens-jeans/pr?sid=clo,vua,k58,i51&fm=neo%2Fmerchandising&iid=M_fdac414d-5ead-40f5-822d-6eca08ff3002_2_372UD5BXDFYS_MC.AWKDIFDJVHWO&otracker=hp_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Fashion~Men%2527s%2BBottom%2BWear~Men%2527s%2BJeans_AWKDIFDJVHWO&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=AWKDIFDJVHWO")
    # Click ._2iDkf8.t0pPfW > ._24_Dny >> nth=0
    page.locator("._2iDkf8.t0pPfW > ._24_Dny").first.click()
    # expect(page).to_have_url("https://www.flipkart.com/mens-jeans/pr?sid=clo%2Cvua%2Ck58%2Ci51&fm=neo%2Fmerchandising&iid=M_fdac414d-5ead-40f5-822d-6eca08ff3002_2_372UD5BXDFYS_MC.AWKDIFDJVHWO&otracker=hp_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Fashion%7EMen%2527s%2BBottom%2BWear%7EMen%2527s%2BJeans_AWKDIFDJVHWO&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=AWKDIFDJVHWO&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove")
    # Click div:nth-child(3) > ._1Y4Vhm > ._2iDkf8 > ._24_Dny
    page.locator("div:nth-child(3) > ._1Y4Vhm > ._2iDkf8 > ._24_Dny").click()
    # expect(page).to_have_url("https://www.flipkart.com/mens-jeans/pr?sid=clo%2Cvua%2Ck58%2Ci51&fm=neo%2Fmerchandising&iid=M_fdac414d-5ead-40f5-822d-6eca08ff3002_2_372UD5BXDFYS_MC.AWKDIFDJVHWO&otracker=hp_rich_navigation_2_2.navigationCard.RICH_NAVIGATION_Fashion%7EMen%2527s%2BBottom%2BWear%7EMen%2527s%2BJeans_AWKDIFDJVHWO&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=AWKDIFDJVHWO&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.rating%255B%255D%3D3%25E2%2598%2585%2B%2526%2Babove")
    # ---------------------
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)
