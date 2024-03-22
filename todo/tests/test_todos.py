from frontend_test_mixin import FrontendTestMixin

class TestDisplayOnLoad(FrontendTestMixin):
    def test_display_empty_list(self):
        self.page.goto(self.reverse_url("index"))
        self.page.wait_for_selector("text=Nothing to see")
        self.page.screenshot(path="tests/screenshots/test_display_empty_list.png")
        

    