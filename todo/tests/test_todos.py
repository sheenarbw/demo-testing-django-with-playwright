from playwright.sync_api import Page, expect
import os
from django.urls import reverse
from todo.models import TodoItem

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = (
    "true"  # <<< need to run sync code from an async context
    #       #     models are sync
)


def reverse_url(
    live_server, viewname, urlconf=None, args=None, kwargs=None, current_app=None
):
    end = reverse(viewname, urlconf, args, kwargs, current_app)
    return f"{live_server.url}{end}"


def test_display_empty_list_on_first_load(live_server, page: Page):
    page.goto(reverse_url(live_server, "index"))
    page.wait_for_selector("text=Nothing to see")


def test_display_one_item_on_first_load(live_server, page: Page):
    TodoItem.objects.create(title="Test item")
    page.goto(reverse_url(live_server, "index"))
    page.wait_for_selector("text=Test item")
    assert page.get_by_test_id("todo_items_empty").is_hidden()


def test_add_new_item(live_server, page: Page):
    page.goto(reverse_url(live_server, "index"))
    page.fill("input[name=title]", "New item title")

    page.get_by_role("button", name="Add").click()
    page.wait_for_selector("text=New item title")

    assert TodoItem.objects.filter(title="New item title").exists()
    assert page.get_by_test_id("todo_items_empty").is_hidden()


# def test_form_clears_upon_submission(live_server, page: Page):
