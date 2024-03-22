function showIfEmpty({ itemClass, emptyListId }) {
  const count = Array.from(document.getElementsByClassName(itemClass)).length;

  if (count === 0) {
    document.getElementById(emptyListId).style.display = "block";
  } else {
    document.getElementById(emptyListId).style.display = "none";
  }
}

function todoListShowIfEmpty() {
  showIfEmpty({ itemClass: "todo_item", emptyListId: "todo_items_empty" });
}

window.onload = function () {
  const targetNode = document.getElementById("todo_items");

  const config = {
    attributes: true,
    childList: true,
    subtree: true,
  };

  const observer = new MutationObserver(todoListShowIfEmpty);

  observer.observe(targetNode, config);

  todoListShowIfEmpty();
};
