"""
Why pytest 
liveserver fixture
page fixture

pytest 
pytest --headed 
pytest --headed --slowmo=2000 
pytest --headed --slowmo=1000 --browser firefox
pytest --headed --slowmo=1000 --browser firefox --browser chromium

pytest --tracing=on --browser firefox --browser chromium
playwright show-trace test-results/todo-tests-test-todos-py-test-add-new-item-chromium/trace.zip

vscode debugging
breakpoint()

playwright codegen http://127.0.0.1:8181/
pytest  todo/tests/test_todos.py -k test_form_clears_upon_submission
hx-on::after-request="this.reset()" 

playwright --help 
"""

from playwright.sync_api import Page, expect
from django.urls import reverse
from todo.models import TodoItem


def test_display_empty_list_on_first_load(live_server, page: Page):
    url = reverse_url(live_server, "index")

    page.goto(url)  #                              # <<< visit pages
    page.wait_for_selector("text=Nothing to see")  # <<< wait for stuff
    #                                              #     (no need for explicit delay)


def test_display_one_item_on_first_load(live_server, page: Page):
    TodoItem.objects.create(title="Test item")
    page.goto(reverse_url(live_server, "index"))
    page.wait_for_selector("text=Test item")  # select dom elements
    assert page.get_by_test_id("todo_items_empty").is_hidden()


def test_add_new_item(live_server, page: Page):
    page.goto(reverse_url(live_server, "index"))
    page.fill("input[name=title]", "New item title")  # <<< fill form

    page.get_by_role("button", name="Add").click()  # <<< click
    page.wait_for_selector("text=New item title")

    assert TodoItem.objects.filter(title="New item title").exists()
    assert page.get_by_test_id("todo_items_empty").is_hidden()


def reverse_url(
    live_server, viewname, urlconf=None, args=None, kwargs=None, current_app=None
):
    end = reverse(viewname, urlconf, args, kwargs, current_app)
    return f"{live_server.url}{end}"


# def test_form_clears_upon_submission(live_server, page: Page):
