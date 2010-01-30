function preloader() {
  var i = 0;
  imageObj = new Image();
  for(i=0; i<=4; i++) {
    imageObj.src=images[i];
  }
}

images = new Array(
//  "images/globalnav-bg-blue.png",
)

//preloader();


//check for ie5 mac
var bugRiddenCrashPronePieceOfJunk = (
    navigator.userAgent.indexOf('MSIE 5') != -1
    &&
    navigator.userAgent.indexOf('Mac') != -1
)

var W3CDOM = (!bugRiddenCrashPronePieceOfJunk &&
               typeof document.getElementsByTagName != 'undefined' &&
               typeof document.createElement != 'undefined' );


function initializeCollapsibles() {

    $('.collapsible_header').click(function() {   
        var header = $(this);
        var container = $(this).parents(".collapsible_container").get(0);
        if (!container)
            return true;
        var items = $('.collapsible_item', container);
        if (header.hasClass('collapsed')) {
    	items.show();
        } else {
    	items.hide();
        }
        $('.collapsible_header', container).toggleClass('collapsed').toggleClass('expanded');
    });

    $('.dropdown-actions-link').click(function() {   
	var c = $(this).parent().children('ul');
        if (c.hasClass('collapsed')) {
          c.show();
        } else {
    	  c.hide();
        }
        $(c).toggleClass('collapsed').toggleClass('expanded');
    });

}

function initializeSearchBox() {
	var searchbox = $("#z-portal-searchbox input[name='form.widgets.text']");
	searchbox.focus(function() {
		if (this.value == "Enter Search")
			this.value = "";
	});
	searchbox.blur(function() {
		if (this.value == "")
			this.value = "Enter Search";
	});
	$("#z-portal-searchbox form[name='searchForm']").submit(function() {
		var searchbox = $("#z-portal-searchbox input[name='form.widgets.text']");
		if (searchbox.attr("value") == "" || searchbox.attr("value")== "Enter Search")
			return false;
		return true;
	});
}

function before(element1, element2) {
	element2.before(element1);
}

function initializeListingExpandAll() {
    $(".listing-navigation a.expand-link").click(function(){
        $(".listing-item .collapsible_header").addClass("expanded").removeClass("collapsed");
        $(".listing-item .collapsible_item").show();
    });
    $(".listing-navigation a.collapse-link").click(function(){
        $(".listing-item .collapsible_header").addClass("collapsed").removeClass("expanded");
        $(".listing-item .collapsible_item").hide();
    });
} 

function goToWithCameFrom(url) {
	document.forms['came-from-form'].action = url;
	document.forms['came-from-form'].submit(); 
}

function showRateFormFromListing(anchor, itemURL) {
	$("#rate-form").remove();
	var container = $(anchor).parents(".listing-item").get(0);
	container = $(".rate-form-ct", container);
	container.load(itemURL+"/@@rateform",
		{"from_listing":"yes","came_from":document.forms['came-from-form']['came_from'].value}
	);
}

function rateItemFromListing(anchor, itemURL) {
	var url = itemURL + "/@@rateajax";
	var container = $(anchor).parents(".listing-item").get(0);
	container = $(".details-ct", container);
	var message = $("<div class=\"notification-message\"></div>");
	message.hide();
	container.append(message);
	var data = {'rate':document.forms['rate-form']['rate'].value};
	message.load(url, data, function(responseText, textStatus, request) {
		if (textStatus == "error") {
			$(this).html("Error occurred");
		}
		$(this).show();
		$(this).schedule("2s", function() {
			$(this).fadeOut("normal", function() {
				$(this).remove();
			});
		});
		$("#rate-form").remove();
		var container = $(this).parents(".listing-item").get(0);
		$(".rating-ct", container).load(itemURL+"/@@displayrating");
	});
}

function saveItemFromListing(anchor, itemURL) {
	var url = itemURL + "/@@saveajax";
	var container = $(anchor).parents(".listing-item").get(0);
	container = $(".details-ct", container);
	var message = $("<div class=\"notification-message\"></div>");
	container.append(message);
	message.load(url, function(responseText, textStatus, request) {
		if (textStatus == "error") {
			$(this).html("Error occurred");
		} else {
			var container = $(this).parents(".listing-item").get(0);
//			$(".save-link", container).hide();
//			$(".unsave-link", container).show();
		}
		$(this).schedule("2s", function() {
			$(this).fadeOut("normal", function() {
				$(this).remove();
			});
		});
	});
}


function hideAllMenus() {
    $('dl.actionMenu').removeClass('activated');
    $('dl.actionMenu').addClass('deactivated');
};

function toggleMenuHandler(event) {
    if (!event) var event = window.event; // IE compatibility

    // terminate if we hit a non-compliant DOM implementation
    // returning true, so the link is still followed
    if (!W3CDOM){return true;}

    var container = $(this).parents(".actionMenu").get(0);
    if (!container) {
        return true;
    }
    
    container = $(container);

    // check if the menu is visible
    if (container.hasClass('activated')) {
        // it's visible - hide it
	    container.removeClass('activated');
	    container.addClass('deactivated');
    } else {
        // it's invisible - make it visible
        container.removeClass('deactivated');
        container.addClass('activated');
    }
    return false;
};

function hideMenusHandler(event) {
    if (!event) var event = window.event; // IE compatibility
    hideAllMenus();
    // we want to follow this link
    return true;
};

function actionMenuDocumentMouseDown(event) {
    if (!event) var event = window.event; // IE compatibility

    if (event.target)
        targ = event.target;
    else if (event.srcElement)
        targ = event.srcElement;

    var container = $(targ).parents(".actionMenu").get(0);
    if (container) {
        // targ is part of the menu, so just return and do the default
        return true;
    }

    hideAllMenus();

    return true;
};

function actionMenuMouseOver(event) {
    
    if (!event) var event = window.event; // IE compatibility

    if (!this.tagName && (this.tagName == 'A' || this.tagName == 'a')) {
        return true;
    }

    var container = $(this).parents(".actionMenu").get(0);
    
    if (!container) {
        return true;
    }
    var menu_id = container.id;

    var switch_menu = false;
    // hide all menus
    var menus = $('dl.actionMenu').each(function(i) {
        // check if the menu is visible
        var menu = $(this);
        if (menu.hasClass('activated')) {
            switch_menu = true;
        }
        // turn off menu when it's not the current one
        if (menu.attr('id') != menu_id) {
            menu.removeClass('activated');
            menu.addClass('deactivated');
        }
    });

    if (switch_menu) {
        $('#'+menu_id).removeClass('deactivated');
        $('#'+menu_id).addClass('activated');
    }
    
    return true;
};

function initializeMenus() {
    // terminate if we hit a non-compliant DOM implementation
    if (!W3CDOM) {return false;}

    document.onmousedown = actionMenuDocumentMouseDown;

    hideAllMenus();

    // add toggle function to header links
    var menu_headers = $('dl.actionMenu > dt.actionMenuHeader > a').click(toggleMenuHandler);
    var menu_headers = $('dl.actionMenu > dt.actionMenuHeader > a').mouseover(actionMenuMouseOver);

    // add hide function to all links in the dropdown, so the dropdown closes
    // when any link is clicked
    var menu_contents = $('dl.actionMenu > dd.actionMenuContent').click(hideMenusHandler);

};

$(initializeMenus);
