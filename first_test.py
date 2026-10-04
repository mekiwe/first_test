from playwright.sync_api import sync_playwright

def main():
    print("正在啟動 Playwright 自動化測試...")
    with sync_playwright() as p:
        # 開啟 Chromium 瀏覽器（headless=False 代表看得到瀏覽器跳出來操作）
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        
        # 1. 前往 Google
        page.goto("https://www.google.com")
        print("已成功進入 Google 首頁")
        
        # 2. 找到搜尋框並輸入關鍵字
        search_box = page.locator('textarea[name="q"]')
        search_box.fill("資工研究所")
        search_box.press("Enter")
        print("已完成搜尋關鍵字：資工研究所")
        
        # 等待 3 秒觀察結果
        page.wait_for_timeout(3000)
        browser.close()
        print("測試成功完成！")

if __name__ == "__main__":
    main() 