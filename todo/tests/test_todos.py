from frontend_test_mixin import FrontendTestMixin
from todo.models import TodoItem

class TestDisplayOnLoad(FrontendTestMixin):
    def test_display_empty_list(self):
        self.page.goto(self.reverse_url("index"))
        self.page.wait_for_selector("text=Nothing to see")
        # self.page.screenshot(path="tests/screenshots/test_display_empty_list.png")
        

    def test_display_one_item(self):
        TodoItem.objects.create(title="Test item")
        self.page.goto(self.reverse_url("index"))
        self.page.wait_for_selector("text=Test item")
        self.assertTrue(self.page.get_by_test_id("todo_items_empty").is_hidden())


class TestAddNewItem(FrontendTestMixin):
    def test_add_new_item(self):
        self.page.goto(self.reverse_url("index"))
        self.page.fill("input[name=title]", "New item title")
        
        self.page.get_by_role("button", name="Add").click()
        self.page.wait_for_selector("text=New item title")

        self.assertTrue(TodoItem.objects.filter(title="New item title").exists())
        self.assertTrue(self.page.get_by_test_id("todo_items_empty").is_hidden())

class TestDeleteItem(FrontendTestMixin):
    def test_delete_item(self):
        item = TodoItem.objects.create(title="Item to delete")
        self.page.goto(self.reverse_url("index"))
        self.page.wait_for_selector(f'text={item.title}')
        self.page.get_by_test_id(f"delete_item_{item.id}").click()
        self.page.wait_for_selector("text=Item deleted successfully")
        self.assertFalse(TodoItem.objects.filter(title="Item to delete").exists())
        self.assertTrue(self.page.get_by_test_id("todo_items_empty").is_visible())

        self.assertFalse(TodoItem.objects.filter(title="Item to delete").exists())


class TestToggleItem(FrontendTestMixin):
    def test_toggle_item(self):
        item = TodoItem.objects.create(title="Item to toggle")
        self.page.goto(self.reverse_url("index"))
        self.page.wait_for_selector(f'text={item.title}')
        self.page.get_by_test_id(f"toggle_item_{item.id}").click()
        self.page.wait_for_selector("text=Item completed")
        item.refresh_from_db()
        self.assertTrue(item.completed)

        self.page.get_by_test_id(f"toggle_item_{item.id}").click()
        self.page.wait_for_selector("text=Item marked as incomplete")
        item.refresh_from_db()
        self.assertFalse(item.completed)
