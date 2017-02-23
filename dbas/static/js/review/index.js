/**
 * @author Tobias Krauthoff
 * @email krauthoff@cs.uni-duesseldorf.de
 */

$(document).ready(function () {
    'use strict';
    
	var tabs = $('#review-tabs');
	var id;
	
	// action for each tab
	$.each(tabs.find('a'), function(){
		$(this).click(function () {
			id = $(this).attr('href');
			hideAll();
			$(id).show();
		});
	});
	
	// show first
	hideAll();
	id = tabs.find('a:first').attr('href');
	$(id).show();
});

/**
 *
 */
function hideAll(){
    'use strict';
    
	var tabs = $('#review-tabs');
	var id;
	$.each(tabs.find('a'), function(){
		id = $(this).attr('href');
		$(id).hide();
	});
}