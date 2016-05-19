#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO

.. codeauthor:: Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de
"""


class EnglischDict:

	@staticmethod
	def set_up(_self):
		"""
		Sets up the englisch dictionary

		:param _self:
		:return: dictionary for the english language
		"""

		en_lang = dict()

		en_lang[_self.arguments] = 'arguments'
		en_lang[_self.error] = 'Error'
		en_lang[_self.iActuallyHave] = 'I actually have'
		en_lang[_self.insertOneArgument] = 'I have one argument:'
		en_lang[_self.insertDontCare] = 'I don’t care about this, leave me alone and take my statement as it is!'
		en_lang[_self.forgotInputRadio] = 'You forgot to choose the right interpretation'
		en_lang[_self.needHelpToUnderstandStatement] = 'We need your help to understand your statement!'
		en_lang[_self.setPremisegroupsIntro1] = 'You have used \'and\' in your statement: '
		en_lang[_self.setPremisegroupsIntro2] = '. There are two ways it could be interpreted. Please help us by selecting the right interpretation:'

		en_lang[_self.attack] = 'You disagreed with'
		en_lang[_self.support] = 'You agreed with'
		en_lang[_self.premise] = 'Premise'
		en_lang[_self.because] = 'because'
		en_lang[_self.moreAbout] = 'More about'
		en_lang[_self.undermine] = 'It is false that'
		en_lang[_self.support1] = ''
		en_lang[_self.undercut1] = 'It is false that'
		en_lang[_self.undercut2] = 'and this is no good counter-argument'
		en_lang[_self.overbid1] = 'It is false that'
		en_lang[_self.overbid2] = 'and this is a good counter-argument'
		en_lang[_self.rebut1] = 'It is right that'
		en_lang[_self.rebut2] = ', but I have a better statement'
		en_lang[_self.oldPwdEmpty] = 'Old password field is empty.'
		en_lang[_self.newPwdEmtpy] = 'New password field is empty.'
		en_lang[_self.confPwdEmpty] = 'Password confirmation field is empty.'
		en_lang[_self.newPwdNotEqual] = 'New passwords are not equal'
		en_lang[_self.pwdsSame] = 'New and old password are the same'
		en_lang[_self.oldPwdWrong] = 'Your old password is wrong.'
		en_lang[_self.pwdChanged] = 'Your password was changed'
		en_lang[_self.emptyName] = 'Your name is empty!'
		en_lang[_self.emptyEmail] = 'Your e-mail is empty!'
		en_lang[_self.emtpyContent] = 'Your content is empty!'
		en_lang[_self.maliciousAntiSpam] = 'Your anti-spam message is empty or wrong!'
		en_lang[_self.nonValidCSRF] = 'CSRF-Token is not valid'
		en_lang[_self.name] = 'Name'
		en_lang[_self.mail] = 'Mail'
		en_lang[_self.phone] = 'Phone'
		en_lang[_self.message] = 'Message'
		en_lang[_self.messageDeleted] = 'Message deleted'
		en_lang[_self.notification] = 'Notification'
		en_lang[_self.notificationDeleted] = 'Notification deleted'
		en_lang[_self.pwdNotEqual] = 'Passwords are not equal'
		en_lang[_self.nickIsTaken] = 'Nickname is taken'
		en_lang[_self.mailIsTaken] = 'E-Mail is taken'
		en_lang[_self.mailNotValid] = 'E-Mail is not valid'
		en_lang[_self.mailSettingsTitle] = 'Enables/Disables notifications in D-BAS.'
		en_lang[_self.notificationSettingsTitle] = 'Enables/Disables e-mails of D-BAS.'
		en_lang[_self.errorTryLateOrContant] = 'An error occured, please try again later or contact the author'
		en_lang[_self.accountWasAdded] = 'Your account was added and you are now able to log in.'
		en_lang[_self.accountRegistration] = 'D-BAS Account Registration'
		en_lang[_self.accountWasRegistered] = 'Your account was successfully registered for this e-mail.'
		en_lang[_self.accoutErrorTryLateOrContant] = 'Your account with the nick could not be added. Please try again or contact the author.'
		en_lang[_self.nicknameIs] = 'Your nickname is: '
		en_lang[_self.newPwdIs] = 'Your new password is: '
		en_lang[_self.dbasPwdRequest] = 'D-BAS Password Request'
		en_lang[_self.emailBodyText] = 'This is an automatically generated mail by the D-BAS System.\nFor contact please write an mail to krauthoff@cs.uni-duesseldorf.de\nThis system is part of a doctoral thesis and currently in an alpha-phase.'
		en_lang[_self.emailWasSent] = 'E-Mail was sent.'
		en_lang[_self.emailWasNotSent] = 'E-Mail was not sent.'
		en_lang[_self.antispamquestion] = 'What is'
		en_lang[_self.signs] = ['+', '*', '/', '-']
		en_lang['0'] = 'zero'
		en_lang['1'] = 'one'
		en_lang['2'] = 'two'
		en_lang['3'] = 'three'
		en_lang['4'] = 'four'
		en_lang['5'] = 'five'
		en_lang['6'] = 'six'
		en_lang['7'] = 'seven'
		en_lang['8'] = 'eight'
		en_lang['9'] = 'nine'
		en_lang['+'] = 'plus'
		en_lang['-'] = 'minus'
		en_lang['*'] = 'times'
		en_lang['/'] = 'divided by'
		en_lang[_self.defaultView] = 'Default View'
		en_lang[_self.wideView] = 'Seperate Nodes'
		en_lang[_self.tightView] = 'Stretch Nodes'
		en_lang[_self.showContent] = 'Show Content'
		en_lang[_self.hideContent] = 'Hide Content'

		en_lang[_self.addATopic] = 'Add a topic'
		en_lang[_self.pleaseEnterTopic] = 'Please enter your topic here:'
		en_lang[_self.pleaseEnterShorttextForTopic] = 'Please enter a shorttext for your topic here:'
		en_lang[_self.pleaseSelectLanguageForTopic] = 'Please select the language of the new discussion here:'
		en_lang[_self.editStatementViewChangelog] = 'Edit Statements / View Changelog'
		en_lang[_self.editStatementHere] = 'Please, edit the selected statement here:'
		en_lang[_self.save] = 'Save'
		en_lang[_self.cancel] = 'Cancel'
		en_lang[_self.submit] = 'Submit'
		en_lang[_self.close] = 'Close'
		en_lang[_self.urlSharing] = 'Share your URL'
		en_lang[_self.urlSharingDescription] = 'Please feel free to share this url:'
		en_lang[_self.warning] = 'Warning'
		en_lang[_self.islandViewFor] = 'Island View for'
		en_lang[_self.resumeHere] = 'Resume here'

		en_lang[_self.aand] = 'and'
		en_lang[_self.addedEverything] = 'Everything was added.'
		en_lang[_self.addStatementRow] = 'Add another row for adding a new statemtent.'
		en_lang[_self.addTopic] = 'Add a Topic'
		en_lang[_self.alreadyInserted] = 'This is a duplicate and already there.'
		en_lang[_self.addPremisesRadioButtonText] = 'Let me enter my reasons!'
		en_lang[_self.addArgumentsRadioButtonText] = 'Let me enter my own statements!'
		en_lang[_self.argumentContainerTextIfPremises] = 'You want to state your own reasons?'
		en_lang[_self.argumentContainerTextIfArguments] = 'You want to state your own arguments?'
		en_lang[_self.addPremiseRadioButtonText] = 'Let me enter my reason!'
		en_lang[_self.addArgumentRadioButtonText] = 'Let me enter my own statement!'
		en_lang[_self.argumentContainerTextIfPremise] = 'You want to state your own reason?'
		en_lang[_self.argumentContainerTextIfArgument] = 'You want to state your own argument?'
		en_lang[_self.argumentContainerTextIfConclusion] = 'What is your idea? What should we do?'
		en_lang[_self.argueAgainstPositionToggleButton] = 'Or do you want to argue against a position? Please toggle this button:'
		en_lang[_self.argueForPositionToggleButton] = 'Or do you want to argue for a position? Please toggle this button:'
		en_lang[_self.andIDoNotBelieveCounter] = 'and I do not believe that this is a good counter-argument for'
		en_lang[_self.andIDoNotBelieveArgument] = 'and I do not believe that this is a good argument for'
		en_lang[_self.andTheyDoNotBelieveCounter] = 'and they do not believe that this is a good counter-argument for'
		en_lang[_self.andTheyDoNotBelieveArgument] = 'and they do not believe that this is a good argument for'
		en_lang[_self.alternatively] = 'Alternatively'
		en_lang[_self.addArguments] = 'Add arguments'
		en_lang[_self.addStatements] = 'Add statements'
		en_lang[_self.addArgumentsTitle] = 'Adds new arguments'
		en_lang[_self.acceptItTitle] = 'Accept it...'
		en_lang[_self.acceptIt] = 'Accept it...'
		en_lang[_self.asReasonFor] = 'as reason for'
		en_lang[_self.argument] = 'Argument'
		en_lang[_self.attackPosition] = 'attack Position'
		en_lang[_self.at] = 'at'
		en_lang[_self.attackedBy] = 'You were attacked by'
		en_lang[_self.attackedWith] = 'You\'ve attacked with'
		en_lang[_self.agreeBecause] = 'I agree because '
		en_lang[_self.andIDoBelieveCounterFor] = 'and I do believe that this is a counter-argument for'
		en_lang[_self.andIDoBelieveArgument] = 'and I do believe that this is a argument for'
		en_lang[_self.attitudeFor] = 'Attitudes for'
		en_lang[_self.breadcrumbsStart] = 'Start'
		en_lang[_self.breadcrumbsChoose] = 'Multiple reasons for'
		en_lang[_self.breadcrumbsJustifyStatement] = 'Why do you think that'
		en_lang[_self.breadcrumbsGetPremisesForStatement] = 'Get premisses'
		en_lang[_self.breadcrumbsMoreAboutArgument] = 'More about'
		en_lang[_self.breadcrumbsReplyForPremisegroup] = 'Reply for group'
		en_lang[_self.breadcrumbsReplyForResponseOfConfrontation] = 'Justification of'  # 'Reply for confrontation'
		en_lang[_self.breadcrumbsReplyForArgument] = 'Reply for argument'
		en_lang[_self.butIDoNotBelieveCounterFor] = 'but I do not believe that this is a counter-argument for'
		en_lang[_self.butIDoNotBelieveReasonForReject] = 'but I do not believe that this is a reason for rejecting'
		en_lang[_self.butIDoNotBelieveArgumentFor] = 'but I do not believe that this is a argument for'
		en_lang[_self.butTheyDoNotBelieveCounter] = 'but they do not believe that this is a good counter-argument for'
		en_lang[_self.butTheyDoNotBelieveArgument] = 'but they do not believe that this is a good argument for'
		en_lang[_self.butOtherParticipantsDontHaveOpinionRegardingYourOpinion] = 'but other participants do not have any opinion regarding your selection'
		en_lang[_self.butOtherParticipantsDontHaveArgument] = 'but other participants do not have any argument for that.'
		en_lang[_self.butOtherParticipantsDontHaveCounterArgument] = 'but other participants do not have any counter argument for that.'
		en_lang[_self.because] = 'Because'
		en_lang[_self.butWhich] = 'but which one'
		en_lang[_self.butThenYouCounteredWith] = 'But then you did not agree with this because'
		en_lang[_self.butYouCounteredWith] = 'You did not agree with this because'
		en_lang[_self.butYouAgreedWith] = 'And you agreed with this because'
		en_lang[_self.canYouGiveAReason] = 'Can you give a reason?'
		en_lang[_self.canYouGiveAReasonFor] = 'Can you give a reason for'
		en_lang[_self.canYouGiveACounter] = 'Can you give a counter-argument?'
		en_lang[_self.canYouGiveACounterArgumentWhy1] = 'Can you give a counter-argument, why are you against'
		en_lang[_self.canYouGiveACounterArgumentWhy2] = '?'
		en_lang[_self.canYouGiveAReasonForThat] = 'Can you give a reason for that?'
		en_lang[_self.clickHereForRegistration] = 'Click <a href="" data-toggle="modal" data-target="#popup-login" title="Login">here</a> for log in or registration!'
		en_lang[_self.clickForMore] = 'Click for more!'
		en_lang[_self.countOfArguments] = 'Count of arguments'
		en_lang[_self.countOfPosts] = 'Count of posts'
		en_lang[_self.confirmation] = 'Confirmation'
		en_lang[_self.contact] = 'Contact'
		en_lang[_self.contactSubmit] = 'Submit your Notification'
		en_lang[_self.confirmTranslation] = 'If you change the language, your process on this page will be lost and you have to restart the discussion!'
		en_lang[_self.correctionsSet] = 'Your correction was set.'
		en_lang[_self.checkFirstname] = 'Better check your first name, because the input is empty!'
		en_lang[_self.checkLastname] = 'Better check your last name, because the input is empty!'
		en_lang[_self.checkNickname] = 'Better check your nickname, because the input is empty!'
		en_lang[_self.checkEmail] = 'Better check your email, because the input is empty!'
		en_lang[_self.checkPassword] = 'Better check your password, because the input is empty!'
		en_lang[_self.checkConfirmation] = 'Better check the confirmation of your password, because the input is empty!'
		en_lang[_self.completeView] = 'Complete View'
		en_lang[_self.completeViewTitle] = 'Shows the complete graph'
		en_lang[_self.checkPasswordConfirm] = 'Better check your passwords, because they are not equal!'
		en_lang[_self.clickToChoose] = 'Click to choose'
		en_lang[_self.clearStatistics] = 'Clear Statistics'
		en_lang[_self.currentDiscussion] = 'Current discussion is about'
		en_lang[_self.description_undermine] = 'This statement attacks the premise.'
		en_lang[_self.description_support] = 'This statement supports the premise.'
		en_lang[_self.description_undercut] = 'This statement attacks the justification (undercut). You do not believe that the premise justifies the conclusion.'
		en_lang[_self.description_overbid] = 'This statement supports the justification (overbid). You do believe that the premise justifies the conclusion.'
		en_lang[_self.description_rebut] = 'This statement is against the conclusion itstelf.'
		en_lang[_self.description_no_opinion] = 'You just have no opinion regarding the confrontation or you just want to skip this.'
		en_lang[_self.decisionIndex7] = 'Decision Index - Last 7 Days'
		en_lang[_self.decisionIndex30] = 'Decision Index - Last 30 Days'
		en_lang[_self.decisionIndex7Info] = 'Count of made decision (due to clicks in a discussion) in the last 7 days'
		en_lang[_self.decisionIndex30Info] = 'Count of made decision (due to clicks in a discussion) in the last 30 days'
		en_lang[_self.dateString] = 'Date'
		en_lang[_self.deleteTrack] = 'Delete track'
		en_lang[_self.deleteHistory] = 'Delete history'
		en_lang[_self.disagreeBecause] = 'I disagree because '
		en_lang[_self.dataRemoved] = 'Data was successfully removed.'
		en_lang[_self.didYouMean] = 'Top10 statements, which you probably could mean:'
		en_lang[_self.dialogView] = 'Dialog View'
		en_lang[_self.dialogViewTitle] = 'Show the dialog View'
		en_lang[_self.displayControlDialogGuidedTitle] = 'Dialog View'
		en_lang[_self.displayControlDialogGuidedBody] = 'You will never see something like an argumentation map, because the systems seems to be like a dynamic and generic.'
		en_lang[_self.displayControlDialogIslandTitle] = 'Island View'
		en_lang[_self.displayControlDialogIslandBody] = 'Okay, you want to see more as, but not everything. Therefore the island view will present you a list of every connected statement for an specific statement.'
		en_lang[_self.displayControlDialogExpertTitle] = 'Expert View'
		en_lang[_self.displayControlDialogExpertBody] = 'So, you think you are an expert? Okay, you can have a view of the complete argumentation map'
		en_lang[_self.discussionEnd] = 'The discussion ends here.'
		en_lang[_self.discussionEndLinkText] = 'You can click <a id="discussionEndStepBack" onclick="window.history.back();" style="cursor: pointer;">here</a> to go one step back or you can use the button above or <a id="discussionEndRestart" href="#">this link</a> to restart the discussion.'
		en_lang[_self.discussionInfoTooltip1] = 'The discussion was started'
		en_lang[_self.discussionInfoTooltip2] = 'and already has'
		en_lang[_self.discussionInfoTooltip3pl] = 'argument.'
		en_lang[_self.discussionInfoTooltip3sg] = 'arguments'
		en_lang[_self.duplicate] = 'Duplikat'
		en_lang[_self.duplicateDialog] = 'This textversion is deprecated, because it was already edited to this version.\nDo you want to set this version as the current one once again?'
		en_lang[_self.doesNotHold] = 'does not hold'
		en_lang[_self.doesNotHoldBecause] = 'does not hold, because'
		en_lang[_self.doNotHesitateToContact] = 'Do not hesitate to <span style="cursor: pointer;" id="contact-on-error"><strong>contact us (click here)</strong></span>'
		en_lang[_self.doesJustify] = 'does justify that'
		en_lang[_self.doesNotJustify] = 'does not justify that'
		en_lang[_self.doYouWantToEnterYourStatements] = 'Do you want to enter your statement(s)?'
		en_lang[_self.earlierYouArguedThat] = 'Earlier you argued that'
		en_lang[_self.editIndex] = 'Edit Index - Last 30 Tage'
		en_lang[_self.editIndexInfo] = 'Count of Edits'
		en_lang[_self.euCookiePopupTitle] = 'This website is using cookies and Piwik.'
		en_lang[_self.euCookiePopupText] = 'We use them to give you the best experience. If you continue using our website, we\'ll assume that you are happy to receive all cookies on this website and beeing tracked for academic purpose. All tracked data are saved anonymously with reduced masked IP-adresses.'
		en_lang[_self.euCookiePopoupButton1] = 'Continue'
		en_lang[_self.euCookiePopoupButton2] = 'Learn&nbsp;more'
		en_lang[_self.empty_news_input] = 'News title or text is empty or too short!'
		en_lang[_self.empty_notification_input] = 'Notification title or text is empty or too short!'
		en_lang[_self.email] = 'E-Mail'
		en_lang[_self.emailWasSent] = 'An E-Mail was sent to the given address.'
		en_lang[_self.emailWasNotSent] = 'Your message could not be send due to a system error!'
		en_lang[_self.emailUnknown] = 'The given e-mail address is unkown.'
		en_lang[_self.error_code] = 'Error code'
		en_lang[_self.edit] = 'Edit'
		en_lang[_self.editTitle] = 'Edit the statements.'
		en_lang[_self.feelFreeToLogin] = ' If you want to proceed, please feel free to <u><a href="" data-toggle="modal" data-target="#popup-login" title="Login">login</a></u> yourself :)'
		en_lang[_self.forText] = 'for'
		en_lang[_self.firstConclusionRadioButtonText] = 'Let me enter my idea!'
		en_lang[_self.firstArgumentRadioButtonText] = 'Let me enter my own statement(s)!'
		en_lang[_self.feelFreeToShareUrl] = 'Please feel free to share this url'
		en_lang[_self.fetchLongUrl] = 'Long URL'
		en_lang[_self.fetchShortUrl] = 'Short URL'
		en_lang[_self.forgotPassword] = 'Forgot Password'
		en_lang[_self.firstOneText] = 'You are the first one, who said: '
		en_lang[_self.firstOneInformationText] = 'You are the first one, who is interested in: '
		en_lang[_self.firstOneReason] = 'You are the first one with this argument, please give a reason.'
		en_lang[_self.firstPositionText] = 'You are the first one in this discussion!'
		en_lang[_self.firstPremiseText1] = 'You are the first one, who said that'
		en_lang[_self.firstPremiseText2] = 'Please enter your reason for your statement.'
		en_lang[_self.firstname] = 'Firstname'
		en_lang[_self.fillLine] = 'Please, fill this this line with your report'
		en_lang[_self.finishTitle] = 'Leave the discussion!'
		en_lang[_self.fromm] = 'from'
		en_lang[_self.gender] = 'Gender'
		en_lang[_self.goBack] = 'Go back'
		en_lang[_self.goHome] = 'Go home'
		en_lang[_self.goStepBack] = 'Go one step back'
		en_lang[_self.generateSecurePassword] = 'Generate secure password'
		en_lang[_self.goodPointTakeMeBackButtonText] = 'I agree, that is a good argument! Take me one step back.'
		en_lang[_self.group_uid] = 'Group'
		en_lang[_self.haveALookAt] = 'Hey, please have a look at '
		en_lang[_self.hidePasswordRequest] = 'Hide Password Request'
		en_lang[_self.hideGenerator] = 'Hide Generator'
		en_lang[_self.hold] = 'holds'
		en_lang[_self.howeverIHaveMuchStrongerArgumentRejecting] = 'However, I have a much stronger argument for rejecting that'
		en_lang[_self.howeverIHaveEvenStrongerArgumentRejecting] = 'However, I have an even stronger argument for rejecting that'
		en_lang[_self.howeverIHaveMuchStrongerArgumentAccepting] = 'However, I have a much stronger argument for accepting that'
		en_lang[_self.howeverIHaveEvenStrongerArgumentAccepting] = 'However, I have an even stronger argument for accepting that'
		en_lang[_self.iAgreeWithInColor] = 'I <span class=\'text-success\'>agree</span> with'
		en_lang[_self.iAgreeWith] = 'I agree with'
		en_lang[_self.iDisagreeWithInColor] = 'I <span class=\'text-danger\'>disagree</span> with'
		en_lang[_self.iDisagreeWith] = 'I disagree with'
		en_lang[_self.iDoNotKnow] = 'I do not know'
		en_lang[_self.iDoNotKnowInColor] = 'I <span class=\'text-info\'>do not know</span>'
		en_lang[_self.iHaveNoOpinionYet] = 'I have no opinion yet about'
		en_lang[_self.iHaveNoOpinion] = 'I have no opinion'
		en_lang[_self.iHaveNoOpinionYetInColor] = 'I have <span class=\'text-info\'>no opinion yet</span>, show me an argument for'
		en_lang[_self.informationForExperts] = 'Infos for experts'
		en_lang[_self.internalFailureWhileDeletingTrack] = 'Internal failure, please try again or did you have deleted your track recently?'
		en_lang[_self.internalFailureWhileDeletingHistory] = 'Internal failure, please try again or did you have deleted your history recently?'
		en_lang[_self.internalError] = '<strong>Internal Error:</strong> Maybe the server is offline.'
		en_lang[_self.issueList] = 'Topics'
		en_lang[_self.islandViewHeaderText] = 'These are all arguments for: '
		en_lang[_self.islandView] = 'Island View'
		en_lang[_self.islandViewTitle] = 'Shows the island View'
		en_lang[_self.irrelevant] = 'Irrelevant'
		en_lang[_self.itIsTrue] = 'it is true that'
		en_lang[_self.itIsFalse] = 'it is false that'
		en_lang[_self.itTrueIs] = 'it is true that'
		en_lang[_self.itFalseIs] = 'it is false that'
		en_lang[_self.isFalse] = 'is false'
		en_lang[_self.isNotAGoodIdea] = 'is not a good idea'
		en_lang[_self.isTrue] = 'is true'
		en_lang[_self.initialPosition] = 'Initial Position'
		en_lang[_self.initialPositionSupport] = 'What is your initial position you are supporting?'
		en_lang[_self.initialPositionAttack] = 'What is your initial position you want to attack?'
		en_lang[_self.initialPositionInterest] = 'What is the initial position you are interested in?'
		en_lang[_self.iAcceptCounter] = 'and I do accept that this is a counter-argument for'
		en_lang[_self.iAcceptArgument] = 'and I do accept that this is an argument for'
		en_lang[_self.iHaveMuchStrongerArgumentRejecting] = 'I have a much stronger argument for rejecting that'
		en_lang[_self.iHaveEvenStrongerArgumentRejecting] = 'I have an even stronger argument for rejecting that'
		en_lang[_self.iHaveMuchStrongerArgumentAccepting] = 'I have a much stronger argument for accepting that'
		en_lang[_self.iHaveEvenStrongerArgumentAccepting] = 'I have an even stronger argument for accepting that'
		en_lang[_self.iNoOpinion] = 'I have no opinion regarding'
		en_lang[_self.interestingOnDBAS] = 'Interesting discussion on DBAS'
		en_lang[_self.inputEmpty] = 'Input is empty!'
		en_lang[_self.informationForStatements] = 'Information for the statements'
		en_lang[_self.keyword] = 'Keyword'
		en_lang[_self.keywordStart] = 'Start'
		en_lang[_self.keywordChooseActionForStatement] = 'Choosing attitude'
		en_lang[_self.keywordGetPremisesForStatement] = 'Getting premises'
		en_lang[_self.keywordMoreAboutArgument] = 'More about'
		en_lang[_self.keywordReplyForPremisegroup] = 'Reply for argument'
		en_lang[_self.keywordReplyForResponseOfConfrontation] = 'Justification of'
		en_lang[_self.keywordReplyForArgument] = 'Confrontation'
		en_lang[_self.keepSetting] = 'Keep this'
		en_lang[_self.holds] = 'holds'
		en_lang[_self.hideAllUsers] = 'Hide all users'
		en_lang[_self.hideAllAttacks] = 'Hide all attacks'
		en_lang[_self.letMeExplain] = 'Let me explain it this way'
		en_lang[_self.levenshteinDistance] = 'Levenshtein-Distance'
		en_lang[_self.languageCouldNotBeSwitched] = 'Unfortunately, the language could not be switched'
		en_lang[_self.last_action] = 'Last Action'
		en_lang[_self.last_login] = 'Last Login'
		en_lang[_self.login] = 'Login'
		en_lang[_self.logfile] = 'Logfile for'
		en_lang[_self.letsGo] = 'Click here to start now!'
		en_lang[_self.letsGoBack] = 'Let\'s go back!'
		en_lang[_self.letsGoHome] = 'Let\'s go home!'
		en_lang[_self.more] = 'More'
		en_lang[_self.medium] = 'medium'
		en_lang[_self.next] = 'Next Entry'
		en_lang[_self.now] = 'Now'
		en_lang[_self.newPremiseRadioButtonText] = 'None of the above! Let me state my own reason!'
		en_lang[_self.newPremisesRadioButtonText] = 'None of the above! Let me state my own reason(s)!'
		en_lang[_self.newPremiseRadioButtonTextAsFirstOne] = 'Let me state my own reason!'
		en_lang[_self.newPremisesRadioButtonTextAsFirstOne] = 'Let me state my own reason(s)!'
		en_lang[_self.newStatementRadioButtonTextAsFirstOne] = 'Let me state my own statement!'
		en_lang[_self.newStatementsRadioButtonTextAsFirstOne] = 'Let me state my own statement(s)!'
		en_lang[_self.newConclusionRadioButtonText] = 'Neither of the above, I have a different idea!'
		en_lang[_self.newsAboutDbas] = 'News about D-BAS'
		en_lang[_self.nickname] = 'Nickname'
		en_lang[_self.noOtherAttack] = 'The system has no other counter-argument'
		en_lang[_self.noIslandView] = 'Could not fetch data for the island view. Sorry!'
		en_lang[_self.noCorrections] = 'No corrections for the given statement could be fetched.'
		en_lang[_self.noCorrectionsSet] = 'Correction could not be set, because your user was not fount in the database. Are you currently logged in?'
		en_lang[_self.noDecisionDone] = 'No decision was done.'
		en_lang[_self.notInsertedErrorBecauseEmpty] = 'Your idea was not inserted, because your text is too short or empty.'
		en_lang[_self.notInsertedErrorBecauseDuplicate] = 'Your idea was not inserted, because your idea is a duplicate.'
		en_lang[_self.notInsertedErrorBecauseUnknown] = 'Your idea was not inserted due to an unknown error.'
		en_lang[_self.notInsertedErrorBecauseInternal] = 'Your idea was not inserted due to an internal error.'
		en_lang[_self.noEntries] = 'No entries'
		en_lang[_self.noTrackedData] = 'No data was tracked.'
		en_lang[_self.number] = 'No'
		en_lang[_self.note] = 'Note'
		en_lang[_self.no_entry] = 'No entry'
		en_lang[_self.noRights] = 'You have no rights for this action!'
		en_lang[_self.notLoggedIn] = 'You are not logged in.'
		en_lang[_self.on] = 'On'
		en_lang[_self.off] = 'Off'
		en_lang[_self.onlyOneItem] = 'If you want to state a new reason, please click here to log in.'
		en_lang[_self.onlyOneItemWithLink] = 'If you want to state a new reason, please click <a href="" data-toggle="modal" data-target="#popup-login" title="Login">here</a> to log in.'
		en_lang[_self.unfortunatelyOnlyOneItem] = 'Unfortunately you only have one option to choose. If you want to state a new reason, please click <a href="" data-toggle="modal" data-target="#popup-login" title="Login">here</a> to log in.'
		en_lang[_self.otherParticipantsConvincedYouThat] = 'Other participants convinced you that'
		en_lang[_self.otherParticipantsThinkThat] = 'Other participants think that'
		en_lang[_self.otherParticipantsAgreeThat] = 'Other participants agree that'
		en_lang[_self.otherParticipantsDontHaveOpinion] = 'Other participants do not have any opinion regarding'
		en_lang[_self.otherParticipantsDontHaveOpinionRegaringYourSelection] = 'Other participants do not have any opinion regarding your selection'
		en_lang[_self.otherParticipantsDontHaveCounterForThat] = 'Other participants do not have any counter-argument for that'
		en_lang[_self.otherParticipantsDontHaveNewCounterForThat] = 'Other participants do not have any new counter-argument for that. You already have seen all other counter-arguments.'
		en_lang[_self.otherParticipantsDontHaveCounter] = 'Other participants do not have any counter-argument for '
		en_lang[_self.otherParticipantsDontHaveArgument] = 'Other participants do not have any argument for '
		en_lang[_self.otherParticipantsAcceptBut] = 'Other participants accept your argument, but'
		en_lang[_self.otherParticipantDisagreeThat] = 'Other participants disagree that '
		en_lang[_self.otherUsersClaimStrongerArgumentRejecting] = 'Other users claim to have a stronger statement for rejecting'
		en_lang[_self.otherUsersClaimStrongerArgumentAccepting] = 'Other users claim to have a stronger statement for accepting'
		en_lang[_self.otherUsersHaveCounterArgument] = 'Other users have the counter-argument that'
		en_lang[_self.otherUsersSaidThat] = 'Other users said that'
		en_lang[_self.opinionBarometer] = 'Opinion Barometer'
		en_lang[_self.pleaseAddYourSuggestion] = 'Please add your suggestion!'
		en_lang[_self.premiseGroup] = 'PremiseGroup'
		en_lang[_self.previous] = 'Previous Entry'
		en_lang[_self.publicNickTitle] = 'Enables/Disables the real nickname on your public page.'
		en_lang[_self.passwordSubmit] = 'Change Password'
		en_lang[_self.registered] = 'Registered'
		en_lang[_self.restartDiscussion] = 'Restart Discussion'
		en_lang[_self.restartDiscussionTitle] = 'Restart Discussion'
		en_lang[_self.restartOnError] = 'Please try to reload this page or restart the discussion, if reloading does not fix the problem.'
		en_lang[_self.recipientNotFound] = 'Recipient not found!'
		en_lang[_self.report] = 'Report'
		en_lang[_self.reportTitle] = 'Contact for reporting'
		en_lang[_self.right] = 'Right'
		en_lang[_self.requestTrack] = 'Request track'
		en_lang[_self.refreshTrack] = 'Refresh track'
		en_lang[_self.requestHistory] = 'Request history'
		en_lang[_self.refreshHistory] = 'Refresh history'
		en_lang[_self.requestFailed] = 'Request failed'
		en_lang[_self.remStatementRow] = 'Removes this row.'
		en_lang[_self.reactionFor] = 'Reactions for'
		en_lang[_self.questionTitle] = 'Get more information about the statement!'
		en_lang[_self.saveMyStatement] = 'Save my Statement!'
		en_lang[_self.selectStatement] = 'Please select a statement!'
		en_lang[_self.showAllUsers] = 'Show all users'
		en_lang[_self.showAllArguments] = 'Show all arguments'
		en_lang[_self.showAllArgumentsTitle] = 'Show all arguments, done by users'
		en_lang[_self.showAllUsersTitle] = 'Show all users, which are registered'
		en_lang[_self.supportPosition] = 'support position'
		en_lang[_self.strength] = 'Strength'
		en_lang[_self.strong] = 'strong'
		en_lang[_self.strongerStatementForAccepting] = 'but they claim to have a stronger statement for accepting'
		en_lang[_self.strongerStatementForRecjecting] = 'but they claim to have a stronger statement for rejecting'
		en_lang[_self.soYouEnteredMultipleReasons] = 'So you entered multiple reasons'
		en_lang[_self.soYourOpinionIsThat] = 'So your opinion is that'
		en_lang[_self.soYouWantToArgueAgainst] = 'So you want to counter-argue against'
		en_lang[_self.shortenedBy] = 'which was shortened with'
		en_lang[_self.shareUrl] = 'Share Link'
		en_lang[_self.showMeAnotherArgument] = 'Show me another argument'
		en_lang[_self.soThatOtherParticipantsDontHaveOpinionRegardingYourOpinion] = 'so that participants do not have any opinion regarding your selection'
		en_lang[_self.switchDiscussion] = 'Change the discussion\'s topic'
		en_lang[_self.switchDiscussionTitle] = 'Switch Discussion'
		en_lang[_self.switchDiscussionText1] = 'If you accept, you will change the topic of the discussion to'
		en_lang[_self.switchDiscussionText2] = 'and the discussion will be restarted.'
		en_lang[_self.switchLanguage] = 'Switch Language'
		en_lang[_self.statement] = 'Statement'
		en_lang[_self.statementIndex] = 'Statement Index - Last 30 Days'
		en_lang[_self.statementIndexInfo] = 'Count of added Statements'
		en_lang[_self.sureThat] = 'I\'m reasonably sure that '
		en_lang[_self.surname] = 'Surname'
		en_lang[_self.showMeAnArgumentFor] = 'Show me an argument for'
		en_lang[_self.textAreaReasonHintText] = 'Please use a new textarea for every reason, write short and clear!'
		en_lang[_self.theCounterArgument] = 'the counter-argument'
		en_lang[_self.therefore] = 'Therefore'
		en_lang[_self.thinkWeShould] = 'I think we should '
		en_lang[_self.track] = 'Track'
		en_lang[_self.textversionChangedTopic] = 'Statement was edited'
		en_lang[_self.textversionChangedContent] = 'Your original statement was edited by'
		en_lang[_self.to] = 'to'
		en_lang[_self.history] = 'History'
		en_lang[_self.topicString] = 'Topic'
		en_lang[_self.text] = 'Text'
		en_lang[_self.theySay] = 'They say'
		en_lang[_self.theyThink] = 'They think'
		en_lang[_self.thisIsACopyOfMail] = 'This is a copy of your mail'
		en_lang[_self.thisConfrontationIs] = 'This confrontation is a'
		en_lang[_self.veryweak] = 'very weak'
		en_lang[_self.wantToStateNewPosition] = 'If you want to state a new position, please click here to log in.'
		en_lang[_self.weak] = 'weak'
		en_lang[_self.wrong] = 'Wrong'
		en_lang[_self.wouldYourShareArgument] = 'Would you share your argument?'
		en_lang[_self.whatDoYouThinkAbout] = 'What do you think about'
		en_lang[_self.whatDoYouThinkAboutThat] = 'What do you think about that'
		en_lang[_self.whatIsYourIdea] = 'What is your idea / opinion? What should we do?'
		en_lang[_self.whatIsYourMostImportantReasonFor] = 'What is your most important reason for'
		en_lang[_self.whatIsYourMostImportantReasonWhy] = 'What is your most important reason why'
		en_lang[_self.whyDoYouThinkThat] = 'Why do you think that'
		en_lang[_self.wrongURL] = 'Your URL seems to be wrong.'
		en_lang[_self.whyAreYouDisagreeingWith] = 'Why are you disagreeing with'
		en_lang[_self.whyAreYouAgreeingWith] = 'Why are you agreeing with'
		en_lang[_self.whyAreYouDisagreeingWithInColor] = 'Why are you <span class=\'text-danger\'>disagreeing</span> with'
		en_lang[_self.whyAreYouAgreeingWithInColor] = 'Why are you <span class=\'text-success\'>agreeing</span> with'
		en_lang[_self.whyAreYouDisagreeingWithThat] = 'Why are you disagreeing with that?'
		en_lang[_self.youMadeA] = 'You made a'
		en_lang[_self.youMadeAn] = 'You made an'
		en_lang[_self.relation_undermine] = 'is a counter-argument for'
		en_lang[_self.relation_support] = 'is a reason for'
		en_lang[_self.relation_undercut] = 'is a counter-argument for'
		en_lang[_self.relation_overbid] = 'is a reason for'
		en_lang[_self.relation_rebut] = 'is a counter-argument for'
		en_lang[_self.uid] = 'ID'
		en_lang[_self.unfortunatelyNoMoreArgument] = 'Unfortunately there are no more arguments about'
		en_lang[_self.userPasswordNotMatch] = 'User / Password do not match'
		en_lang[_self.userOptions] = 'Users Options'
		en_lang[_self.voteCountTextFirst] = 'You are the first one with this opinion'
		en_lang[_self.voteCountTextMayBeFirst] = 'You would be the first one with this opinion'
		en_lang[_self.voteCountTextOneOther] = 'One other participant with this opinion'
		en_lang[_self.voteCountTextMore] = 'more participants with this opinion'
		en_lang[_self.welcome] = 'Welcome'
		en_lang[_self.welcomeMessage] = 'Welcome to the novel dialog-based argumentation system.<br>We hope you enjoy using this system and happy arguing!'
		en_lang[_self.youAreInterestedIn] = 'You are interested in'
		en_lang[_self.youAgreeWith] = 'You agree with'
		en_lang[_self.youDisagreeWith] = 'You disagree with'
		en_lang[_self.youSaidThat] = 'You said that'
		en_lang[_self.youUsedThisEarlier] = 'You used this earlier.'
		en_lang[_self.youRejectedThisEarlier] = 'You rejected this earlier.'
		en_lang[_self.youHaveMuchStrongerArgumentForAccepting] = 'You have a much stronger argument for accepting'
		en_lang[_self.youHaveMuchStrongerArgumentForRejecting] = 'You have a much stronger argument for rejecting'

		return en_lang
