### Pagination System in Flask

This pagination system in Flask displays a limited number of buttons to navigate through a large set of items.

#### Function `index` Overview

1. **Total Page Calculation**: Based on the total number of items (`reference = 125`) and items per page (10), it calculates the required number of pages.
2. **Defining the Page Range to Display**: Using `limit` (maximum 5 buttons), it defines a range around the current page (`page`). Adjusts `start` and `end` to ensure the range doesn't exceed the total number of pages.
3. **Rendering**: Returns the necessary variables to the template.

#### HTML for Pagination (with Jinja2)

html
<!-- "Prev" button if not on the first page -->
{% if page != 1 %}
    <button class="page-btn" onclick="window.location.href='{{ url_for('index', page=page-1) }}'">Prev</button>
{% endif %}

<!-- Numbered buttons with an active class for the current page -->
{% for pag in range(start, end + 1) %}
    <button class="page-btn{% if pag == page %} page_active{% endif %}"
            onclick="window.location.href='{{ url_for('index', page=pag) }}'">{{ pag }}</button>
{% endfor %}

<!-- "Next" button if not on the last page -->
{% if page != pages %}
    <button class="page-btn" onclick="window.location.href='{{ url_for('index', page=page+1) }}'">Next</button>
{% endif %} 

### Anotations.
1. "Prev" Button: Displays "Prev" only if not on the first page.
2. Numbered Buttons: Displays buttons within the [start, end] range and applies the page_active class to the button for the current page.
3. "Next" Button: Displays "Next" only if not on the last page.
