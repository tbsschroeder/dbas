/*global $, jQuery, alert, addActiveLinksInNavBar, removeActiveLinksInNavBar*/

/**
 * @author Tobias Krauthoff
 * @email krauthoff@cs.uni-duesseldorf.de
 */

/**
 *
 * @param linkname
 */
function setLinkActive(linkname) {
	'use strict';
	$('#navbar-right').find('>li').each(function(){
		$(this).removeClass('active')
	});
	$(linkname).addClass('active');
}

/**
 * Jumps to clicked chapter, which is defined in the header
 */
function jmpToChapter() {
	// jump to chapter-function
	$('a[href^="#"]').on('click', function (e) {
		try {
			var href = $(this).attr('href');
			$('html, body').animate({
				scrollTop: ($(href).offset().top - 100)
			}, 'slow');
			e.preventDefault();
		} catch (err) {
			// something like 'Cannot read property 'top' of undefined'
		}
	});
}

/**
 * Go back to top arrow
 */
function goBackToTop() {
	$(window).scroll(function () {
		if (jQuery(this).scrollTop() > 500) {
			$('.back-to-top').fadeIn('slow');
			setTimeout(function() { $('.back-to-top').fadeOut('slow'); }, 2500);
		} else {
			$('.back-to-top').fadeOut('slow');
		}
	});

	// going back to top
	$('.back-to-top').click(function (event) {
		event.preventDefault();
		$('html, body').animate({
			scrollTop: 0
		}, 500);
		return false;
	});
}

/**
 * Changes the navbar on background scrolling events
 */
function changeBackgroundOnScroll(){
	$(window).scroll(function () {
		if (jQuery(this).scrollTop() > 10) {
			$('#custom-bootstrap-menu').removeClass('navbar-transparent');
		} else {
			$('#custom-bootstrap-menu').addClass('navbar-transparent');
		}
	});
}

/**
 * Displays dialog
 * @param titleText
 * @param bodyText
 * @param functionForAccept
 */
function displayConfirmationDialog(titleText, bodyText, functionForAccept) {
	// display dialog
	$('#' + popupConfirmDialogId).modal('show');
	$('#' + popupConfirmDialogId + ' h4.modal-title').text(titleText);
	$('#' + popupConfirmDialogId + ' div.modal-body').html(bodyText);
	$('#' + popupConfirmDialogAcceptBtn).show().click( function () {
		$('#' + popupConfirmDialogId).modal('hide');
		functionForAccept();
	});
	$('#' + popupConfirmDialogRefuseBtn).show().click( function () {
		$('#' + popupConfirmDialogId).modal('hide');
	});
}

/**
 * Displays dialog
 * @param titleText
 * @param bodyText
 */
function displayConfirmationDialogWithoutCancelAndFunction(titleText, bodyText) {
	// display dialog
	$('#' + popupConfirmDialogId).modal('show');
	$('#' + popupConfirmDialogId + ' h4.modal-title').html(titleText);
	$('#' + popupConfirmDialogId + ' div.modal-body').html(bodyText);
	$('#' + popupConfirmDialogAcceptBtn).show().click( function () {
		$('#' + popupConfirmDialogId).modal('hide').find('.modal-dialog').removeClass('modal-sm');
	}).removeClass('btn-success');
	$('#' + popupConfirmDialogRefuseBtn).hide();
}

/**
 * Displays dialog with checkbox
 * @param titleText
 * @param bodyText
 * @param checkboxText
 * @param functionForAccept
 * @param isRestartingDiscussion
 */
function displayConfirmationDialogWithCheckbox(titleText, bodyText, checkboxText, functionForAccept, isRestartingDiscussion) {
	// display dialog only if the cookie was not set yet
	if (new Helper().isCookieSet(WARNING_CHANGE_DISCUSSION_POPUP)){
		window.location.href = functionForAccept;
	} else {
		$('#' + popupConfirmChecbkoxDialogId).modal('show');
		$('#' + popupConfirmChecbkoxDialogId + ' h4.modal-title').text(titleText);
		$('#' + popupConfirmChecbkoxDialogId + ' div.modal-body').html(bodyText);
		$('#' + popupConfirmChecbkoxDialogTextId).text(checkboxText);
		$('#' + popupConfirmChecbkoxDialogAcceptBtn).click( function () {
			$('#' + popupConfirmChecbkoxDialogId).modal('hide');
			// maybe set a cookie
			if ($('#' + popupConfirmChecbkoxId).prop('checked')) {
				new Helper().setCookieForDays(WARNING_CHANGE_DISCUSSION_POPUP, 7, true);
			}

			if (isRestartingDiscussion) {
				window.location.href = functionForAccept;
			} else {
				functionForAccept();
			}

		});
		$('#' + popupConfirmChecbkoxDialogRefuseBtn).click( function () {
			$('#' + popupConfirmChecbkoxDialogId).modal('hide');
		})
	}
}

/**
 *
 */
function displayBubbleInformationDialog(){
	if (!new Helper().isCookieSet(BUBBLE_INFOS)){
		var img = $('<img>').attr('src','../static/images/explanation_bubbles_' + ($(document).width() > 992?'long' : 'short') + '.png');
		$('#' + popupConfirmDialogId).modal('show');
		$('#' + popupConfirmDialogId + ' .modal-dialog').attr('style', 'width: ' + ($(document).width() > 992? '430' : '200') + 'px;');
		$('#' + popupConfirmDialogId + ' h4.modal-title').html('Introduction');
		$('#' + popupConfirmDialogId + ' div.modal-body').html(img);
		$('#' + popupConfirmDialogAcceptBtn).show().click( function () {
			$('#' + popupConfirmDialogId).modal('hide');
			new Helper().setCookieForDays(BUBBLE_INFOS, 30, true);
		}).removeClass('btn-success');
		$('#' + popupConfirmDialogRefuseBtn).hide();
	}
}

/**
 *
 * @param lang
 */
function setPiwikOptOutLink(lang){
	var src = mainpage + 'piwik/index.php?module=CoreAdminHome&action=optOut&idsite=1&language=';
	if (lang === 'de')	src += 'de';
	else 				src += 'en';
	$('#piwik-opt-out-iframe').attr('src',src);
}

/**
 *
 */
function setEasterEggs(){
	$('#roundhousekick').click(function(){ ajaxRoundhouseKick(); });
	//$('#yomamma').click(function(){ ajaxMama(); });

	if (window.location.href == mainpage) {
		/* christmas only
        var div = $('<div>'),
        christmas = $('<input>').attr('type','checkbox').attr('data-toggle','toggle').attr('data-onstyle','primary').bootstrapToggle('off'),
        silvester = $('<input>').attr('type','checkbox').attr('data-toggle','toggle').attr('data-onstyle','primary').bootstrapToggle('off'),
        spanChristmas = $('<span>').text('Christmas'),
        spanSilvester = $('<span>').text('Silvester');
        christmas.attr('style','margin-left: 5px;');
        silvester.attr('style','margin-left: 5px;');
        spanSilvester.attr('style','margin-left: 20px;');
        div.attr('style','padding-right: 50px; z-index: 200; text-align: right;')
		        .append(spanChristmas)
		        .append(christmas)
		        .append(spanSilvester)
		        .append(silvester);
		div.prependTo($('.first-container'));
		$('#cot_tl3_fixed').hide();
		$('#cot_tl4_fixed').hide();
		christmas.change(function() {
			if($(this).is(":checked")) {
				$('#cot_tl3_fixed').show();
				$('#cot_tl4_fixed').show();
			} else {
				$('#cot_tl3_fixed').hide();
				$('#cot_tl4_fixed').hide();
			}
		});
		silvester.change(function() {
			if($(this).is(":checked")) {
				document.body.appendChild(canvas);
				window.scrollTo(0,document.body.scrollHeight);
			} else {
				canvas.remove();
			}
		});
		*/
	}
}

/**
 *
 */
function hideExtraViewsOfLoginPopup(){
	$('#' + popupLoginWarningMessage).hide();
	$('#' + popupLoginFailed).hide();
	$('#' + popupLoginSuccess).hide();
	$('#' + popupLoginInfo).hide();
	$('#' + popupLoginRegistrationSuccess).hide();
	$('#' + popupLoginRegistrationFailed).hide();
	$('#' + popupLoginRegistrationInfo).hide();
	$('#' + popupLoginButtonRegister).hide();
	$('#' + popupLoginButtonLogin).hide();
	$('#' + popupLoginForgotPasswordBody).hide();
	$('#' + generatePasswordBodyId).hide();
}

/**
 * Prepares the login popup
 */
function prepareLoginRegistrationPopup(){
	var popupLoginGeneratePasswordBody = $('#' + popupLoginGeneratePasswordBodyId);
	// hide on startup
	hideExtraViewsOfLoginPopup();
	popupLoginGeneratePasswordBody.hide();

	// switching tabs
	$('.tab-login a').on('click', function (e) {
		e.preventDefault();
		$(this).parent().addClass('active');
		$(this).parent().siblings().removeClass('active');
		var target = $(this).attr('href');
		$('.tab-content > div').not(target).hide();
		$(target).fadeIn(600);

		if ($(this).attr('href').indexOf('signup') != -1){
			$('#' + popupLoginButtonLogin).hide();
			$('#' + popupLoginButtonRegister).show();
		} else {
			$('#' + popupLoginButtonLogin).show();
			$('#' + popupLoginButtonRegister).hide();
		}
	});

	$('#' + popupLoginButtonLogin).show().click(function() {
		ajaxLogin()
	}).keypress(function(e) { if (e.which == 13) { ajaxRegistration() } });

	$('#' + popupLoginForgotPasswordText).click(function(){
		if ($('#' + popupLoginForgotPasswordBody).is(':visible')){
			$('#' + popupLoginForgotPasswordBody).fadeOut();
			$('#' + popupLoginForgotPasswordText).text(_t(forgotPassword) + '?');
			$('#' + popupLoginFailed).fadeOut();
			$('#' + popupLoginSuccess).fadeOut();
			$('#' + popupLoginInfo).fadeOut();
		} else {
			$('#' + popupLoginForgotPasswordBody).fadeIn();
			$('#' + popupLoginForgotPasswordText).text(_t(hidePasswordRequest));
		}
	});

	$('#' + popupLoginGeneratePassword + ' > a').click(function(){
		if (popupLoginGeneratePasswordBody.is(':visible')){
			popupLoginGeneratePasswordBody.hide();
			$('#' + popupLoginGeneratePassword + ' > a').text(_t(generateSecurePassword));
		} else {
			popupLoginGeneratePasswordBody.show();
			$('#' + popupLoginGeneratePassword + ' > a').text(_t(hideGenerator));
			new PasswordHandler().generate_password($('#popup_password_example'));
		}
	});

	$('#' + popupLoginCloseButton).click(function(){
		hideExtraViewsOfLoginPopup();
		$('#' + popupLogin).modal('hide');
		$('#' + popupLoginButtonLogin).show();
	});

	$('#' + popupLoginPasswordInputId).keyup(function popupLoginPasswordInputKeyUp() {
		new PasswordHandler().check_strength($('#' + popupLoginPasswordInputId), $('#' + popupLoginPasswordMeterId),
				$('#' + popupLoginPasswordStrengthId), $('#' + popupLoginPasswordExtrasId));
	});

	$('#' + popupLoginButtonRegister).click(function(){
		var userfirstname   = $('#' + popupLoginUserfirstnameInputId).val(),
			userlastname    = $('#' + popupLoginUserlastnameInputId).val(),
			nick            = $('#' + popupLoginNickInputId).val(),
			email           = $('#' + popupLoginEmailInputId).val(),
			password        = $('#' + popupLoginPasswordInputId).val(),
			passwordconfirm = $('#' + popupLoginPasswordconfirmInputId).val(),
			text = '',
			i,
			fields = [userfirstname, userlastname, nick, email, password, passwordconfirm],
			tvalues = [_t(checkFirstname), _t(checkLastname), _t(checkNickname), _t(checkEmail),_t(checkPassword),
				_t(checkConfirmation), _t(checkPasswordConfirm)];

		// check all vields for obivously errors
		for (i=0; i<fields.length; i++){
			if (!fields[i] || /^\s*$/.test(fields[i]) || 0 === fields[i].length) {
				text = tvalues[i];
				break;
			}
		}

		if (text == '' ){
			$('#' + popupLoginWarningMessage).hide();
			ajaxRegistration();
		} else {
			$('#' + popupLoginWarningMessage).fadeIn("slow");
			$('#' + popupLoginWarningMessageText).text(text);
		}

	});

	// bind enter key
	$('#' + loginUserId).keypress(function(e) {							if (e.which == 13) {	ajaxLogin()			}	});
	$('#' + loginPwId).keypress(function(e) {							if (e.which == 13) {	ajaxLogin()			}	});
	$('#' + popupLoginUserfirstnameInputId).keypress(function(e) {		if (e.which == 13) {	ajaxRegistration()	}	});
	$('#' + popupLoginUserlastnameInputId).keypress(function(e) {		if (e.which == 13) {	ajaxRegistration()	}	});
	$('#' + popupLoginNickInputId).keypress(function(e) {				if (e.which == 13) {	ajaxRegistration()	}	});
	$('#' + popupLoginEmailInputId).keypress(function(e) {				if (e.which == 13) {	ajaxRegistration()	}	});
	$('#' + popupLoginPasswordconfirmInputId).keypress(function(e) {	if (e.which == 13) {	ajaxRegistration()	}	});

	$('#' + popupLoginButtonRequest).click(function() {
		ajaxPasswordRequest();
	});
}

// *********************
//	AJAX
// *********************

/**
 * Sends a request for language change
 * @param new_lang is the shortcut for the language
 */
function ajaxSwitchDisplayLanguage (new_lang){
	var csrfToken = $('#' + hiddenCSRFTokenId).val();
	$.ajax({
		url: 'ajax_switch_language',
		type: 'POST',
		data: { lang: new_lang},
		dataType: 'json',
		async: true,
		headers: {
			'X-CSRF-Token': csrfToken
		}
	}).done(function ajaxSwitchDisplayLanguageDone() {
		location.reload(true);
		setPiwikOptOutLink(new_lang);
	}).fail(function ajaxSwitchDisplayLanguageFail(xhr) {
		if (xhr.status == 400) {
			alert(_t(requestFailedBadToken));
		} else if (xhr.status == 500) {
			alert(_t(requestFailedInternalError));
		} else {
			alert(_t(languageCouldNotBeSwitched));
		}
	});
}

/**
 *
 */
function ajaxLogin (){
	var csrfToken = $('#' + hiddenCSRFTokenId).val();
	var user = $('#' + loginUserId).val(),
		password = $('#' + loginPwId).val(),
		url = window.location.href,
		keep_login = $('#keep-login-box').prop('checked') ? 'true' : 'false';

	$.ajax({
		url: 'ajax_user_login',
		type: 'POST',
		data: {
			user: user,
			password: password,
			url: url,
			keep_login: keep_login
		},
		dataType: 'html',
		async: true,
		headers: {
			'X-CSRF-Token': csrfToken
		}
	}).done(function ajaxLoginDone(data) {
		callbackIfDoneForLogin(data);
	}).fail(function ajaxLoginFail(xhr) {
		if (xhr.status == 200) {
			location.reload(true);
		} else if (xhr.status == 302) {
			location.href = xhr.getResponseHeader('Location');
		} else if (xhr.status == 400) {
			$('#' + popupLoginFailed).show();
			$('#' + popupLoginFailed + '-message').text(_t(requestFailedBadToken));
		} else if (xhr.status == 500) {
			$('#' + popupLoginFailed).show();
			$('#' + popupLoginFailed + '-message').text(_t(requestFailedInternalError));
		} else {
			$('#' + popupLoginFailed).show();
			$('#' + popupLoginFailed + '-message').text(_t(requestFailed));
		}
	}).always(function ajaxLoginAlways(){
		$('#' + loginPwId).val('');
	});
}

/**
 *
 */
function ajaxLogout (){
	var csrfToken = $('#' + hiddenCSRFTokenId).val();
	$.ajax({
		url: 'ajax_user_logout',
		type: 'POST',
		dataType: 'json',
		async: true,
		headers: {
			'X-CSRF-Token': csrfToken
		}
	}).done(function ajaxLogoutDone(data) {
		location.reload();
	}).fail(function ajaxLogoutFail(xhr) {
		if (xhr.status == 200) {
			if (window.location.href.indexOf('settings') != 0){
				window.location.href = mainpage;
			} else {
				location.reload(); // TODO page will not be reloaded properly
			}
		} else if (xhr.status == 403) {
			window.location.href = mainpage;
		} else {
			location.reload();
		}
	});
}

/**
 *
 */
function ajaxRegistration (){
	var csrfToken = $('#' + hiddenCSRFTokenId).val();
	var firstname = $('#userfirstname-input').val(),
		lastname = $('#userlastname-input').val(),
		nickname = $('#nick-input').val(),
		email = $('#email-input').val(),
		password = $('#' + popupLoginPasswordInputId).val(),
		passwordconfirm = $('#' + popupLoginPasswordconfirmInputId).val(),
		spamanswer = $('#popup-login-spamanswer-input').val(),
		gender = '';

	if ($('#' + popupLoginInlineRadioGenderN).is(':checked')) gender = 'n';
	if ($('#' + popupLoginInlineRadioGenderM).is(':checked')) gender = 'm';
	if ($('#' + popupLoginInlineRadioGenderF).is(':checked')) gender = 'f';

	$.ajax({
		url: 'ajax_user_registration',
		type: 'POST',
		data: { firstname: firstname,
				lastname: lastname,
				nickname: nickname,
				gender: gender,
				email: email,
				password: password,
				passwordconfirm: passwordconfirm,
				spamanswer: spamanswer,
				lang: getLanguage()},
		dataType: 'json',
		async: true,
		headers: {
			'X-CSRF-Token': csrfToken
		}
	}).done(function ajaxRegistrationDone(data) {
		callbackIfDoneForRegistration(data);
	}).fail(function ajaxRegistrationFail(xhr) {
		$('#' + popupLoginRegistrationFailed).show();
		if (xhr.status == 400) {		$('#' + popupLoginRegistrationFailed + '-message').text(_t(requestFailedBadToken));
		} else if (xhr.status == 500) {	$('#' + popupLoginRegistrationFailed + '-message').text(_t(requestFailedInternalError));
		} else {                		$('#' + popupLoginRegistrationFailed + '-message').text(_t(requestFailed));
		}
	}).always(function ajaxLoginAlways(){
		$('#' + popupLoginPasswordInputId).val('');
		$('#' + popupLoginPasswordconfirmInputId).val('');
	});
}

/**
 *
 */
function ajaxPasswordRequest (){
	var email = $('#password-request-email-input').val();
	var csrfToken = $('#' + hiddenCSRFTokenId).val();
	$.ajax({
		url: 'ajax_user_password_request',
		type: 'POST',
		data: { email: email, lang: getLanguage()},
		dataType: 'json',
		async: true,
		headers: {
			'X-CSRF-Token': csrfToken
		}
	}).done(function ajaxPasswordRequestDone(data) {
		callbackIfDoneForPasswordRequest(data);
	}).fail(function ajaxPasswordRequestFail(xhr) {
		$('#' + popupLoginRegistrationFailed).show();
		if (xhr.status == 400) {		$('#' + popupLoginRegistrationFailed + '-message').text(_t(requestFailedBadToken));
		} else if (xhr.status == 500) {	$('#' + popupLoginRegistrationFailed + '-message').text(_t(requestFailedInternalError));
		} else {            			$('#' + popupLoginRegistrationFailed + '-message').text(_t(requestFailed));
		}
	});
}

/**
 * Get-Request for an roundhouse kick
 */
function ajaxRoundhouseKick(){
	var csrfToken = $('#' + hiddenCSRFTokenId).val();
	$.ajax({
		url: 'additional_service',
		type: 'GET',
		data: {type:'chuck'},
		global: false,
		async: true,
		headers: {
			'X-CSRF-Token': csrfToken
		}
	}).done(function ajaxRoundhouseKickDone(data) {
		if (data.type == 'success'){
			displayConfirmationDialogWithoutCancelAndFunction('Chuck Norris Fact #' + data.value.id,
				'<h5>' + data.value.joke + '</h5>\n\n' +
				'<span style="float:right;">powered by <a href="http://www.icndb.com/" target="_blank">http://www.icndb.com/</a></span>');

		}
	});
}

/**
 * Get your mama
 */
function ajaxMama(){
	var csrfToken = $('#' + hiddenCSRFTokenId).val();
	$.ajax({
		url: 'additional_service',
		type: 'GET',
		data: {type:'mama'},
		global: false,
		async: true,
		headers: {
			'X-CSRF-Token': csrfToken
		}
	}).done(function ajaxMamaDone(data) {
		displayConfirmationDialogWithoutCancelAndFunction('Yo Mamma',  '<h4>' + data.joke + '</h4>\n\n<span' +
				' style="float:right;">powered by <a href="http://yomomma.info/">http://yomomma.info/</a></span>');
	});
}

// *********************
//	CALLBACKS
// *********************

/**
 *
 * @param data
 */
function callbackIfDoneForLogin(data){
	try {
		var jsonData = $.parseJSON(data);
		// It is JSON
		if (jsonData.error.length != 0) {
			$('#' + popupLoginFailed).show();
			$('#' + popupLoginFailed + '-message').text(jsonData.error);
		} else {
			$('#' + popupLogin).modal('hide');
			location.reload(true);
		}
	} catch(err){
		//var htmlData = $.parseHTML(data);
		var url = location.href;
		if (url.indexOf('?session_expired=true') != -1)
			url = url.substr(0, url.length - '?session_expired=true'.length);
		location.href = url;
	}

}

/**
 *
 * @param data
 */
function callbackIfDoneForRegistration(data){
	var parsedData = $.parseJSON(data);
	var success = $('#' + popupLoginSuccess); //popupLoginRegistrationSuccess);
	var failed = $('#' + popupLoginRegistrationFailed);
	var info = $('#' + popupLoginRegistrationInfo);
	success.hide();
	failed.hide();
	info.hide();

	if (parsedData.success.length > 0) {
		// trigger click
		$('a[href="#login"]').trigger('click');
		success.show();
		$('#' + popupLoginSuccess + '-message').text(parsedData.success);
	}
	if (parsedData.error.length > 0) {
		failed.show();
		$('#' + popupLoginRegistrationFailed + '-message').text(parsedData.error);
	}
	if (parsedData.info.length > 0) {
		info.show();
		$('#' + popupLoginRegistrationInfo + '-message').text(parsedData.info);
		$('#popup-login-spamanswer-input').attr('placeholder', parsedData.spamquestion).val('');
	}
}

/**
 *
 * @param data
 */
function callbackIfDoneForPasswordRequest(data){
	var parsedData = $.parseJSON(data);
	var success = $('#' + popupLoginSuccess);
	var failed = $('#' + popupLoginFailed);
	var info = $('#' + popupLoginInfo);
	success.hide();
	failed.hide();
	info.hide();
	if (parsedData.success.length > 0) {
		$('#' + popupLoginForgotPasswordBody).hide();
		$('#' + popupLoginForgotPasswordText).text(_t(forgotPassword) + '?');
		success.show();
		$('#' + popupLoginSuccess + '-message').text(parsedData.success);
	}
	if (parsedData.error.length > 0) {
		failed.show();
		$('#' + popupLoginFailed + '-message').text(parsedData.error);
	}
	if (parsedData.info.length > 0) {
		info.show();
		$('#' + popupLoginInfo + '-message').text(parsedData.info);
	}
}

// *********************
//	MAIN
// *********************

$(document).ready(function () {
	'use strict';
	var path = window.location.href, lang = $('#hidden_language').val();

	jmpToChapter();
	goBackToTop();
	setPiwikOptOutLink(lang);
	setEasterEggs();

	// set current file to active
		 if (path.indexOf(urlContact) != -1){ 	setLinkActive('#' + contactLink);	$('#' + navbarLeft).hide(); }
	else if (path.indexOf(urlLogin) != -1){		setLinkActive('#' + loginLinkId);	$('#' + navbarLeft).hide(); }
	else if (path.indexOf(urlNews) != -1){		setLinkActive('#' + newsLink);		$('#' + navbarLeft).hide(); }
	else if (path.indexOf(urlContent) != -1){ 	setLinkActive('#' + contentLink);	$('#' + navbarLeft).hide(); }
	else if (path.indexOf(urlSettings) != -1 ||
			 path.indexOf(urlImprint) != -1 ||
			 path.indexOf(urlLogout) != -1){										$('#' + navbarLeft).hide(); }
	else { 										setLinkActive(''); 					$('#' + navbarLeft).show(); }

	// language switch
	$('#' + translationLinkDe).click(function(){ ajaxSwitchDisplayLanguage('de') });
	$('#' + translationLinkEn).click(function(){ ajaxSwitchDisplayLanguage('en') });
	$('#' + translationLinkDe + ' img').click(function(){ ajaxSwitchDisplayLanguage('de') });
	$('#' + translationLinkEn + ' img').click(function(){ ajaxSwitchDisplayLanguage('en') });
	$('#' + logoutLinkId).click(function(e){
		e.preventDefault();
		ajaxLogout();
	});

	// gui preperation
	prepareLoginRegistrationPopup();

	// activate tooltips
	$(function () {
		$("body").tooltip({ selector: '[data-toggle=tooltip]' });
    });

	// ajax loading animation
	$(document).on({
		ajaxStart: function ajaxStartFct () { setTimeout("$('body').addClass('loading')", 0); },
		ajaxStop: function ajaxStopFct () { setTimeout("$('body').removeClass('loading')", 0); }
		// TODO: SEXY GLOBAL AJAX ERROR HANDLING
		//ajaxError: function myErrorHandler(event, xhr, ajaxOptions, thrownError) {
		//	$('#request_failed_container').fadeIn();
		//	new Helper().delay(function(){
		//		$('#request_failed_container').fadeOut();
		//	}, 3000);
		//}
	});
	//$(document).ajaxError(function myErrorHandler(event, xhr, ajaxOptions, thrownError) {
    //    alert("There was an ajax error!");
	//});

	if ($('#session_expired_container').length == 1)
		new Helper().delay(function(){
			$('#session_expired_container').fadeOut();
		}, 3000);

	// testring
	//var horde = gremlins.createHorde()
	//	.gremlin(gremlins.species.formFiller())
	//	.gremlin(gremlins.species.clicker().clickTypes(['click']))
	//	.gremlin(gremlins.species.typer())
	//	.gremlin(function() {
	//		window.$ = function() {};
	//	});
    //horde.unleash();
	// gremlins will act randomly, at 10 ms interval, 1000 times
});
