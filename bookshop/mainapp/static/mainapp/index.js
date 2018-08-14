var bookList = ({ id, name, author, image, price}) => (
    `<div class="col-md-3">
        <div class="card mb-4 box-shadow text-center bordered">
            <img src="${ image }" alt="${ name }">
            <div class="card-body">
                <p class="book-name"><a href="${ id }/">${ name }</a></p>
                <p class="author-name"><a href="book/">${ author }</a></p>
                <div class="d-flex justify-content-between align-items-center">
                    <small class="price-catalog">${ price }</small>
                </div>
            </div>
        </div>
    </div>`
)

var renderData = res => {

    book_html = res.data.map(bookList).join('')

    bestsellers_container = document.getElementById('bestsellers')
    bestsellers_container.innerHTML = book_html

    newbooks_container = document.getElementById('new-books')
    newbooks_container.innerHTML = book_html
}