/* * * * * * *
* Assign "active" class to navbar item based on current page.
*
* By Dave Rogers.
* https://gist.github.com/daverogers/5375778
* * * * * * */
$(document).ready(() => {
	// get current URL path and assign 'active' class
	var pathname = window.location.pathname;
	$('.nav > li > a[href="'+pathname+'"]').parent().addClass('active');
})