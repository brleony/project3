/* * * * * * *
* Name: Leony Brok
* Web Programming with Python and Javascript
*
*
* * * * * * */

// Wait until DOM has loaded.
document.addEventListener('DOMContentLoaded', () => {

    // Add on click event listener to every menu item.
    Array.from(document.getElementsByClassName('menu_item')).forEach( (item) => {
        item.addEventListener('click', () => {

            var menu_modal = $('#menu_modal');

            // Change title.
            menu_modal.find('.modal-title').text(item.dataset.choice);
            document.getElementById('choice').value = item.dataset.choice;

            // Change item.
            document.getElementById('item').value = item.dataset.item;

            // Change price.
            menu_modal.find('#shown_price').text('$' + item.dataset.price);
            document.getElementById('price').value = item.dataset.price;

            // If dinner platter was clicked.
            if (item.dataset.item == 'DIPL') {
                // Show size radio buttons.
                document.getElementById('size_radios').style = "visibility: visible;";
            }

            // If sub was clicked.
            if (item.dataset.item == 'SUB') {
                // Show size radio buttons.
                document.getElementById('size_radios').style = "visibility: visible;";

                // Show 'extra cheese' checkbox.
                document.getElementById('extra_cheese').style = "visibility: visible;";
            }

            // Show modal.
            menu_modal.modal('show');
        });
    });
});
