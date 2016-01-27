/**
 * @author Tobias Krauthoff
 * @email krauthoff@cs.uni-duesseldorf.de
 * @copyright Krauthoff 2015
 */

function get_hostname(url) {
	var m = url.match(/^http:\/\/[^/]+/);
	return m ? m[0] + '/' : null;
}
var mainpage = location.origin + '/'; //get_hostname(window.location.href);

/**
 * Returns a translated string
 * @param id of the string
 * @returns {string} which is translated or unknown value
 * @private
 */
_t = function(id){
	var this_id, value = 'unknown identifier';
	$('#' + languageDropdownId).children().each(function(){
		if ($(this).hasClass('active')){
			this_id = $(this).children().first().attr('id');

			if (this_id.indexOf('en') != -1 && dbas_en.hasOwnProperty(id)){				value= dbas_en[id];
			} else if (this_id.indexOf('de') != -1 && dbas_de.hasOwnProperty(id)){		value = dbas_de[id];
			} else {                                                    				value = 'unknown value';
			}
		}
	});
	return value;
};

/**
 * Returns the tag of current language. This is either {en,de} or 'unknown value' *
 * @returns {string} language tag
 */
getLanguage = function(){
	var this_id, value = 'unknown value';
	$('#' + languageDropdownId).children().each(function(){
		if ($(this).hasClass('active')){
			this_id = $(this).children().first().attr('id');
			if (this_id.indexOf('en') != -1){			value = 'en';
			} else if (this_id.indexOf('de') != -1){	value = 'de';
			} else {									value = 'unknown value';
			}
		}
	});
	return value;
};

/**
 * Messages & Errors
 * @type {string}
 */
var checkmark                                       = '&#x2713;'; // ✓
var ballot                                          = '&#x2717;'; // ✗

var addedEverything 								= 'addedEverything';
var alreadyInserted									= 'alreadyInserted';
var addPremisesRadioButtonText 						= 'addPremisesRadioButtonText';
var addArgumentsRadioButtonText 					= 'addArgumentsRadioButtonText';
var addPremiseRadioButtonText 						= 'addPremiseRadioButtonText';
var addArgumentRadioButtonText 						= 'addArgumentRadioButtonText';
var argumentContainerTextIfPremise 				    = 'argumentContainerTextIfPremise';
var argumentContainerTextIfArgument 				= 'argumentContainerTextIfArgument';
var argumentContainerTextIfConclusion 			    = 'argumentContainerTextIfConclusion';
var argueAgainstPositionToggleButton 				= 'argueAgainstPositionToggleButton';
var argueForPositionToggleButton 					= 'argueForPositionToggleButton';
var alternatively 									= 'alternatively';
var andIDoNotBelieveCounter							= 'andIDoNotBelieveCounter';
var andIDoNotBelieveArgument						= 'andIDoNotBelieveArgument';
var andTheyDoNotBelieveCounter						= 'andTheyDoNotBelieveCounter';
var andTheyDoNotBelieveArgument						= 'andTheyDoNotBelieveArgument';
var argument 										= 'argument';
var asReasonFor										= 'asReasonFor';
var attackedBy 										= 'attackedBy';
var attackedWith 									= 'attackedWith';
var attackPosition									= 'attackPosition';
var agreeBecause 									= 'agreeBecause';
var andIDoBelieve									= 'andIDoBelieve';
var addArguments 									= 'addArguments';
var addStatements 									= 'addStatements';
var acceptIt 										= 'acceptIt';
var addArgumentsTitle 								= 'addArgumentsTitle';
var acceptItTitle 									= 'acceptItTitle';
var because 										= 'because';
var butWhich 										= 'butWhich';
var contactSubmit									= 'contactSubmit';
var clickHereForRegistration 						= 'clickHereForRegistration';
var confirmation 									= 'confirmation';
var confirmTranslation 								= 'confirmTranslation';
var correctionsSet 									= 'correctionsSet';
var checkFirstname									= 'checkFirstname';
var checkLastname									= 'checkLastname';
var checkNickname									= 'checkNickname';
var checkEmail										= 'checkEmail';
var checkPassword									= 'checkPassword';
var checkConfirmation 								= 'checkConfirmation';
var checkPasswordConfirm							= 'checkPasswordConfirm';
var clickToChoose 									= 'clickToChoose';
var completeView 									= 'completeView';
var completeViewTitle								= 'completeViewTitle';
var countOfArguments                                = 'countOfArguments';
var dateString										= 'dateString';
var disagreeBecause 								= 'disagreeBecause';
var dialogView 										= 'dialogView';
var dialogViewTitle									= 'dialogViewTitle';
var dataRemoved 									= 'dataRemoved';
var description_undermine 							= 'description_undermine';
var description_support 							= 'description_support';
var description_undercut 							= 'description_undercut';
var description_overbid 							= 'description_overbid';
var description_rebut 								= 'description_rebut';
var description_no_opinion 							= 'description_no_opinion';
var didYouMean										= 'didYouMean';
var discussionEnd									= 'discussionEnd';
var discussionEndText								= 'discussionEndText';
var discussionEndFeelFreeToLogin					= 'discussionEndFeelFreeToLogin';
var duplicateDialog									= 'duplicateDialog';
var doesNotHold 									= 'doesNotHold';
var doesNotHoldBecause 								= 'doesNotHoldBecause';
var doesJustify 									= 'doesJustify';
var doesNotJustify 									= 'doesNotJustify';
var doNotHesitateToContact 							= 'doNotHesitateToContact';
var doYouWantToEnterYourStatements 					= 'doYouWantToEnterYourStatements';
var deleteTrack 									= 'deleteTrack';
var deleteHistory 									= 'deleteHistory';
var euCookiePopupTitle 								= 'euCookiePopupTitle';
var euCookiePopupText 								= 'euCookiePopupText';
var euCookiePopoupButton1 							= 'euCookiePopoupButton1';
var euCookiePopoupButton2 							= 'euCookiePopoupButton2';
var empty_news_input  								= 'empty_news_input';
var email 											= 'email';
var emailWasSent		 							= 'emailWasSent';
var emailWasNotSent		 							= 'emailWasNotSent';
var emailUnknown 	 								= 'emailUnknown';
var edit 											= 'edit';
var errorCode 										= 'error_code';
var editTitle										= 'editTitle';
var forText                                         = 'forText';
var fillLine 										= 'fillLine';
var firstConclusionRadioButtonText 					= 'firstConclusionRadioButtonText';
var firstArgumentRadioButtonText					= 'firstArgumentRadioButtonText';
var feelFreeToShareUrl 								= 'feelFreeToShareUrl';
var fetchLongUrl 									= 'fetchLongUrl';
var fetchShortUrl 									= 'fetchShortUrl';
var forgotPassword 									= 'forgotPassword';
var firstOneText 									= 'firstOneText';
var firstOneReason 									= 'firstOneReason';
var firstPositionText 								= 'firstPositionText';
var firstname 										= 'firstname';
var firstPremiseText1 								= 'firstPremiseText1';
var firstPremiseText2 								= 'firstPremiseText2';
var gender 											= 'gender';
var goStepBack 										= 'goStepBack';
var generateSecurePassword 							= 'generateSecurePassword';
var goodPointTakeMeBackButtonText 					= 'goodPointTakeMeBackButtonText';
var group_uid 										= 'group_uid';
var history 										= 'history';
var haveALookAt 									= 'haveALookAt';
var hidePasswordRequest 							= 'hidePasswordRequest';
var hideGenerator 									= 'hideGenerator';
var iAgreeWithInColor 								= 'iAgreeWithInColor';
var iAgreeWith 										= 'iAgreeWith';
var iDisagreeWithInColor 							= 'iDisagreeWithInColor';
var iDisagreeWith 									= 'iDisagreeWith';
var iDoNotKnow 										= 'iDoNotKnow ';
var iDoNotKnowInColor 								= 'iDoNotKnowInColor';
var internalFailureWhileDeletingTrack 				= 'internalFailureWhileDeletingTrack';
var internalFailureWhileDeletingHistory				= 'internalFailureWhileDeletingHistory';
var internalError 									= 'internalError';
var informationForExperts							= 'informationForExperts';
var issueList										= 'issueList';
var islandView 										= 'islandView';
var islandViewTitle									= 'islandViewTitle';
var islandViewHeaderText 							= 'islandViewHeaderText';
var irrelevant 										= 'irrelevant';
var itIsTrue 										= 'itIsTrue';
var itIsFalse 										= 'itIsFalse';
var iAcceptCounter									= 'iAcceptCounter';
var iAcceptArgument									= 'iAcceptArgument';
var iHaveMuchStrongerArgumentRejecting				= 'iHaveMuchStrongerArgumentRejecting';
var iHaveMuchEvenArgumentRejecting					= 'iHaveMuchEvenArgumentRejecting';
var iHaveMuchStrongerArgumentAccepting				= 'iHaveMuchStrongerArgumentAccepting';
var iHaveEvenStrongerArgumentAccepting				= 'iHaveEvenStrongerArgumentAccepting';
var iNoOpinion 										= 'iNoOpinion';
var interestingOnDBAS 								= 'interestingOnDBAS';
var initialPosition 								= 'initialPosition';
var initialPositionSupport 							= 'initialPositionSupport';
var initialPositionAttack 							= 'initialPositionAttack';
var initialPositionInterest 						= 'initialPositionInterest';
var inputEmpty										= 'inputEmpty';
var isFalse											= 'isFalse';
var isTrue											= 'isTrue';
var keepSetting										= 'keepSetting';
var keyword											= 'keyword';
var keywordStart 									= 'keywordStart';
var keywordChooseActionForStatement 				= 'keywordChooseActionForStatement';
var keywordGetPremisesForStatement 					= 'keywordGetPremisesForStatement';
var keywordMoreAboutArgument 						= 'keywordMoreAboutArgument';
var keywordReplyForPremisegroup 					= 'keywordReplyForPremisegroup';
var keywordReplyForResponseOfConfrontation 			= 'keywordReplyForResponseOfConfrontation';
var keywordReplyForArgument 						= 'keywordReplyForArgument';
var hideAllUsers 									= 'hideAllUsers';
var hideAllAttacks 									= 'hideAllAttacks';
var letMeExplain 									= 'letMeExplain';
var levenshteinDistance								= 'levenshteinDistance';
var languageCouldNotBeSwitched 						= 'languageCouldNotBeSwitched';
var last_action 									= 'last_action';
var last_login 										= 'last_login';
var logfile											= 'logfile';
var letsGo 											= 'letsGo';
var medium 											= 'medium';
var newPremisesRadioButtonText 						= 'newPremiseRadioButtonText';
var newPremisesRadioButtonTextAsFirstOne			= 'newPremiseRadioButtonTextAsFirstOne';
var newStatementsRadioButtonTextAsFirstOne 			= 'newStatementRadioButtonTextAsFirstOne';
var newPremiseRadioButtonText 						= 'newPremiseRadioButtonText';
var newPremiseRadioButtonTextAsFirstOne				= 'newPremiseRadioButtonTextAsFirstOne';
var newStatementRadioButtonTextAsFirstOne 			= 'newStatementRadioButtonTextAsFirstOne';
var newConclusionRadioButtonText 					= 'newConclusionRadioButtonText';
var nickname 										= 'nickname';
var noIslandView 									= 'noIslandView';
var noCorrections 									= 'noCorrections';
var noCorrectionsSet 								= 'noCorrectionsSet';
var noDecisionDone									= 'noDecisionDone';
var notInsertedErrorBecauseEmpty 					= 'notInsertedErrorBecauseEmpty';
var notInsertedErrorBecauseDuplicate 				= 'notInsertedErrorBecauseDuplicate';
var notInsertedErrorBecauseUnknown 					= 'notInsertedErrorBecauseUnknown';
var notInsertedErrorBecauseInternal					= 'notInsertedErrorBecauseInternal';
var notInsertedErrorBecauseTooShort					= 'notInsertedErrorBecauseTooShort';
var noTrackedData 									= 'noTrackedData';
var noEntries                                       = 'noEntries';
var note 											= 'note';
var number 											= 'number';
var otherParticipantsThinkThat 						= 'otherParticipantsThinkThat';
var otherParticipantsDontHaveCounter 				= 'otherParticipantsDontHaveCounter';
var otherParticipantsDontHaveArgument				= 'otherParticipantsDontHaveArgument';
var otherParticipantsAcceptBut 						= 'otherParticipantsAcceptBut';
var otherParticipantAgree 							= 'otherParticipantAgree';
var otherParticipantDisagree 						= 'otherParticipantDisagree';
var otherUsersClaimStrongerArgumentRejecting		= 'otherUsersClaimStrongerArgumentRejecting';
var otherUsersClaimStrongerArgumentAccepting		= 'otherUsersClaimStrongerArgumentAccepting';
var opinionBarometer                                = 'opinionBarometer';
var options                                         = 'options';
var report 											= 'report';
var reportTitle										= 'reportTitle';
var premiseGroup 									= 'premiseGroup';
var passwordSubmit 									= 'passwordSubmit';
var registered 										= 'registered';
var right 											= 'right';
var requestTrack 									= 'requestTrack';
var refreshTrack 									= 'refreshTrack';
var requestHistory 									= 'requestHistory';
var refreshHistory 									= 'refreshHistory';
var requestFailed 									= 'requestFailed';
var restartDiscussion 								= 'restartDiscussion';
var restartDiscussionTitle							= 'restartDiscussionTitle';
var restartOnError									= 'restartOnError';
var selectStatement 								= 'selectStatement';
var showAllUsers 									= 'showAllUsers';
var showAllAttacks 									= 'showAllAttacks';
var showMeAnArgumentFor 							= 'showMeAnArgumentFor';
var strength 										= 'strength';
var strong 											= 'strong';
var strongerStatementForRecjecting 					= 'strongerStatementForRecjecting';
var soYourOpinionIsThat 							= 'soYourOpinionIsThat';
var soYouWantToArgueAgainst							= 'soYouWantToArgueAgainst';
var shortenedBy 									= 'shortenedBy';
var switchDiscussion								= 'switchDiscussion';
var switchDiscussionText1 							= 'switchDiscussionText1';
var switchDiscussionText2 							= 'switchDiscussionText2';
var supportPosition 								= 'supportPosition';
var statement 										= 'statement';
var sureThat 										= 'sureThat';
var surname 										= 'surname';
var showAllAttacksTitle 							= 'showAllAttacksTitle';
var showAllUsersTitle 								= 'showAllUsersTitle';
var textAreaReasonHintText 							= 'textAreaReasonHintText';
var theCounterArgument 								= 'theCounterArgument';
var therefore 										= 'therefore';
var thinkWeShould 									= 'thinkWeShould';
var track 											= 'track';
var topicString										= 'topicString';
var text 											= 'text';
var thisConfrontationIs 							= 'thisConfrontationIs';
var theySay 										= 'theySay';
var veryweak 										= 'veryweak';
var weak 											= 'weak';
var wouldYourShareArgument							= 'wouldYourShareArgument';
var wrong 											= 'wrong';
var whatDoYouThinkAbout								= 'whatDoYouThinkAbout';
var whatDoYouThinkAboutThat							= 'whatDoYouThinkAboutThat';
var whyAreYouDisagreeing							= 'whyAreYouDisagreeing';
var whyDoYouThinkThat 								= 'whyDoYouThinkThat';
var wrongURL										= 'wrongURL';
var unfortunatelyNoMoreArgument 					= 'unfortunatelyNoMoreArgument';
var youMadeA 										= 'youMadeA';
var youMadeAn 										= 'youMadeAn';

var relation_undermine						= 'relation_undermine';		// used in 'relation_' + jsonData.relation
var relation_support						= 'relation_support';		// used in 'relation_' + jsonData.relation
var relation_undercut						= 'relation_undercut';		// used in 'relation_' + jsonData.relation
var relation_overbid						= 'relation_overbid';		// used in 'relation_' + jsonData.relation
var relation_rebut							= 'relation_rebut';			// used in 'relation_' + jsonData.relation

// cookies
var WARNING_CHANGE_DISCUSSION_POPUP = 'WARNING_CHANGE_DISCUSSION_POPUP';

/**
 * Text for the dialogue
 * @type {string[]}
 */
var sentencesOpenersForArguments = [
	soYourOpinionIsThat
	//'Okay, you have got the opinion: ',
	//'Interesting, your opinion is: ',
	//'You have said, that: ',
	];
var sentencesOpenersArguingWithAgreeing = [
	agreeBecause,
	therefore];
var sentencesOpenersArguingWithDisagreeing = [
	disagreeBecause,
	alternatively];
var sentencesOpenersInforming = [
	thinkWeShould,
	letMeExplain,
	sureThat];
var sentencesOpenersRequesting = [
	whyDoYouThinkThat
	//'Can you explain why '
	];

/**
 * URL's
 * @type {string}
 */
var attrStart 							= 'start';
var attrChooseActionForStatement 		= 'choose_action_for_statement';
var attrGetPremisesForStatement 		= 'get_premises_for_statement';
var attrMoreAboutArgument 				= 'more_about_argument';
var attrReplyForPremisegroup 			= 'reply_for_premisegroup';
var attrReplyForArgument 				= 'reply_for_argument';
var attrReplyForResponseOfConfrontation = 'reply_for_response_of_confrontation';
var attrGo 								= 'go';

var urlContact 							= 'contact';
var urlLogin 							= 'login';
var urlNews 							= 'news';
var urlContent 							= 'content';
var urlSettings 						= 'settings';
var urlImprint 							= 'imprint';
var urlLogout 							= 'logout';
