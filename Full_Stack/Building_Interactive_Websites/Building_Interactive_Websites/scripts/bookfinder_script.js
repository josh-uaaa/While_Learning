import books from './modules/bookfinder_booklist.js';
import { flattenObjectValuesIntoArray, structureBookAsHtml, renderBooksToDom } from './modules/bookfinder_helper.js'

// Click handler for search button
const captureSearchValue = () => {
    const searchBar = document.getElementById('search-bar');
    return searchBar.value;
};

// Filter books based on search input
const filterBooks = (search, books) => {
    const filteredBooks = books.filter((book) => {
        const bookValues = flattenObjectValuesIntoArray([book])[0];
        return bookValues.includes(search);
    });
    return filteredBooks;
};

// Empty the book list container, iterate over list of filtered books, return list of books formatted as HTML using the function in `helper.js` 
const structureBooksAsHtml = (books) => {
    let formattedBooks = [];
    books.forEach((book) => {
        const formattedBook = structureBookAsHtml(book);
        formattedBooks.push(formattedBook);
    })
    return formattedBooks;
};

// Handler triggered when a user clickers the "Search" button. Chains previously defined functions together to filter books based on the search value, formats the books as HTML and renders them to the DOM
const searchBtnClickHandler = (books) => {
    const searchValue = captureSearchValue();
    const filteredBooks = filterBooks(searchValue, books);
    const formattedBooks = structureBooksAsHtml(filteredBooks);
    renderBooksToDom(formattedBooks);
}

// Grab search button from the DOM
const searchBtn = document.getElementById('search-btn');

// Attach an event listener to the search button
searchBtn.addEventListener("click", () => { searchBtnClickHandler(books) });