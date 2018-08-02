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

            console.log(item.dataset.price);

            // Change title.
            menu_modal.find('.modal-title').text(item.dataset.choice);

            // Change values of choice and item input fields.
            $( "#choice" ).val(item.dataset.choice);
            $( "#item" ).val(item.dataset.item);

            // HTML to add later.
            var radio_buttons = `<div id="size_radios">
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="size" id="size_small" value="S" checked>
                                                    <label class="form-check-label" for="exampleRadios1">
                                                    Small
                                                    </label>
                                                </div>
                                                <div class="form-check">
                                                    <input class="form-check-input" type="radio" name="size" id="size_large" value="L">
                                                    <label class="form-check-label" for="exampleRadios2">
                                                    Large
                                                    </label>
                                                </div>
                                            </div>`;
            var cheese_checkbox = `<div class="form-check" id="cheese_check">
                                        <input class="form-check-input" type="checkbox" value="cheese" name="extra_cheese" id="extra_cheese">
                                        <label class="form-check-label" for="extra_cheese">
                                        Extra cheese
                                        </label>
                                    </div>`;

            // If dinner platter, sub, or pizza was clicked.
            if (item.dataset.item == 'DIPL' || item.dataset.item == 'SUB' || item.dataset.item == 'REPI' || item.dataset.item == 'SIPI') {
                // Add radio buttons for size.
                $( "#form-inputs" ).append(radio_buttons);
            }

            // If sub was clicked.
            if (item.dataset.item == 'SUB') {
                // Add 'extra cheese' checkbox.
                $( "#form-inputs" ).append(cheese_checkbox);
            }
            // If pizza was clicked.
            else if (item.dataset.item == 'REPI' || item.dataset.item == 'SIPI') {
                // Change title.
                let title = item.dataset.item + ' with ' + item.dataset.num_toppings + ' toppings';
                menu_modal.find('.modal-title').text(title);

                // Make arrays for topping names and ids.
                topping_names = item.dataset.topping_names.split(",");
                topping_ids = item.dataset.topping_ids.split(",");

                // Put topping names and ids in HTML option tags.
                var options = [];
                topping_names.forEach((name, i) => {
                    options.push(`<option value="${topping_ids[i]}">${name}</option>`);
                });

                // Add select field for nummber of toppings that was clicked.
                for (i = 0; i < item.dataset.num_toppings; i++) {
                    let html = `<div class="form-group">
                                    <label for="topping_select_${i}">Choose topping ${i + 1}</label>
                                    <select class="form-control" id="topping_select_${i}" name="topping_select_${i}">
                                            ${options}
                                    </select>
                                </div>`;

                    $( "#form-inputs" ).append(html);
                }
            }

            // Change and show price.
            //$( "#outside_form" ).append(`<p>$ ${item.dataset.price}</p>`);
            $( "#price" ).val(item.dataset.price);

            // Add submit button.
            $( "#form-inputs" ).append('<button type="submit" class="btn btn-red">Add to order</button>');

            // Show modal.
            menu_modal.modal('show');
        });
    });

    // Erase modal contents when modal is closed.
    $('#menu_modal').on('hidden.bs.modal', function (e) {
        $( "#form-inputs" ).empty();
        $( "#outside_form" ).empty();
    });
});
