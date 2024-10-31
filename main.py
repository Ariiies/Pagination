from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/index/<int:page>')
def index(page=1):
    # Reference is because pages typically need pagination as the content of the page 
    # extends due to some type of content; here, it's called reference as an example
    reference = 125 
    # Here, we get the total number of pages by dividing the reference by 10 
    # as an example of reference items to display
    pages = reference // 10 + (0 if reference % 10 < 0 else 1) 
    # Limit of pagination elements to display
    limit = 5
    # Calculate the range of pages to display
    start = max(1, page - limit // 2)
    end = min(pages, start + limit - 1)
    # Final adjustment to prevent the range from exceeding the total
    if end - start < limit:
        start = max(1, end - limit + 1)

    return render_template('index.html',
                           page=int(page),
                           pages=int(pages),
                           start=start,
                           end=end)


if __name__ == '__main__':
    app.run(debug=True)

