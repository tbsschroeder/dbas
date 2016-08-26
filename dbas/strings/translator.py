#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO

.. codeauthor:: Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de
"""

from .de import GermanDict
from .en import EnglischDict


class Translator(object):
    """
    Class for translating string
    """
    def __init__(self, lang):
        """
        Initializes keywords

        :param lang: current language
        :return:
        """
        self.lang = lang

        self.arguments = 'arguments'
        self.error = 'error'
        self.forgotInputRadio = 'forgotInputRadio'
        self.iActuallyHave = 'iActuallyHave'
        self.insertOneArgument = 'insertOneArgument'
        self.insertDontCare = 'insertDontCare'
        self.needHelpToUnderstandStatement = 'needHelpToUnderstandStatement'
        self.setPremisegroupsIntro1 = 'setPremisegroupsIntro1'
        self.setPremisegroupsIntro2 = 'setPremisegroupsIntro2'

        self.aand = 'and'
        self.andor = 'andor'
        self.addedEverything = 'addedEverything'
        self.addTopic = 'addTopic'
        self.addStatementRow = 'addStatementRow'
        self.alreadyInserted = 'alreadyInserted'
        self.at = 'at'
        self.addPremisesRadioButtonText = 'addPremisesRadioButtonText'
        self.addArgumentsRadioButtonText = 'addArgumentsRadioButtonText'
        self.argumentContainerTextIfPremises = 'argumentContainerTextIfPremises'
        self.argumentContainerTextIfArguments = 'argumentContainerTextIfArguments'
        self.addPremiseRadioButtonText = 'addPremiseRadioButtonText'
        self.addArgumentRadioButtonText = 'addArgumentRadioButtonText'
        self.argumentContainerTextIfPremise = 'argumentContainerTextIfPremise'
        self.argumentContainerTextIfArgument = 'argumentContainerTextIfArgument'
        self.argumentContainerTextIfConclusion = 'argumentContainerTextIfConclusion'
        self.argueAgainstPositionToggleButton = 'argueAgainstPositionToggleButton'
        self.argueForPositionToggleButton = 'argueForPositionToggleButton'
        self.alternatively = 'alternatively'
        self.alreadyFlagged = 'alreadyFlagged'
        self.argument = 'argument'
        self.andIDoNotBelieveCounter = 'andIDoNotBelieveCounter'
        self.andIDoNotBelieveArgument = 'andIDoNotBelieveArgument'
        self.andTheyDoNotBelieveCounter = 'andTheyDoNotBelieveCounter'
        self.andTheyDoNotBelieveArgument = 'andTheyDoNotBelieveArgument'
        self.asReasonFor = 'asReasonFor'
        self.attackedBy = 'attackedBy'
        self.attackedWith = 'attackedWith'
        self.attackPosition = 'attackPosition'
        self.attitudeFor = 'attitudeFor'
        self.agreeBecause = 'agreeBecause'
        self.andIDoBelieveCounterFor = 'andIDoBelieveCounterFor'
        self.andIDoBelieveArgument = 'andIDoBelieveArgument'
        self.addArguments = 'addArguments'
        self.addStatements = 'addStatements'
        self.addArgumentsTitle = 'addArgumentsTitle'
        self.acceptItTitle = 'acceptItTitle'
        self.acceptIt = 'acceptIt'
        self.accepting = 'accepting'
        self.attack = 'attack'
        self.accountWasAdded = 'accountWasAdded'
        self.accountRegistration = 'accountRegistration'
        self.accountWasRegistered = 'accountWasRegistered'
        self.accoutErrorTryLateOrContant = 'accoutErrorTryLateOrContant'
        self.antispamquestion = 'antispamquestion'
        self.addATopic = 'addATopic'
        self.because = 'because'
        self.breadcrumbsStart = 'breadcrumbsStart'
        self.breadcrumbsChoose = 'breadcrumbsChoose'
        self.breadcrumbsJustifyStatement = 'breadcrumbsJustifyStatement'
        self.breadcrumbsGetPremisesForStatement = 'breadcrumbsGetPremisesForStatement'
        self.breadcrumbsMoreAboutArgument = 'breadcrumbsMoreAboutArgument'
        self.breadcrumbsReplyForPremisegroup = 'breadcrumbsReplyForPremisegroup'
        self.breadcrumbsReplyForResponseOfConfrontation = 'breadcrumbsReplyForResponseOfConfrontation'
        self.breadcrumbsReplyForArgument = 'breadcrumbsReplyForArgument'
        self.butOtherParticipantsDontHaveOpinionRegardingYourOpinion = 'butOtherParticipantsDontHaveOpinionRegardingYourOpinion'
        self.butOtherParticipantsDontHaveArgument = 'butOtherParticipantsDontHaveArgument'
        self.butOtherParticipantsDontHaveCounterArgument = 'butOtherParticipantsDontHaveCounterArgument'
        self.butIDoNotBelieveCounterFor = 'butIDoNotBelieveCounterFor'
        self.butIDoNotBelieveArgumentFor = 'butIDoNotBelieveArgumentFor'
        self.butIDoNotBelieveCounter = 'butIDoNotBelieveCounter'
        self.butIDoNotBelieveArgument = 'butIDoNotBelieveArgument'
        self.butIDoNotBelieveReasonForReject = 'butIDoNotBelieveReasonForReject'
        self.butTheyDoNotBelieveCounter = 'butTheyDoNotBelieveCounter'
        self.butTheyDoNotBelieveArgument = 'butTheyDoNotBelieveArgument'
        self.because = 'because'
        self.butWhich = 'butWhich'
        self.but = 'but'
        self.butThenYouCounteredWith = 'butThenYouCounteredWith'
        self.butYouCounteredWith = 'butYouCounteredWith'
        self.butYouAgreedWith = 'butYouAgreedWith'
        self.clickHereForRegistration = 'clickHereForRegistration'
        self.confirmation = 'confirmation'
        self.contact = 'contact'
        self.contactSubmit = 'contactSubmit'
        self.confirmTranslation = 'confirmTranslation'
        self.correctionsSet = 'correctionsSet'
        self.countOfArguments = 'countOfArguments'
        self.countOfPosts = 'countOfPosts'
        self.checkFirstname = 'checkFirstname'
        self.checkLastname = 'checkLastname'
        self.checkNickname = 'checkNickname'
        self.checkEmail = 'checkEmail'
        self.checkPassword = 'checkPassword'
        self.checkConfirmation = 'checkConfirmation'
        self.checkPasswordConfirm = 'checkPasswordConfirm'
        self.clickToChoose = 'clickToChoose'
        self.canYouGiveAReason = 'canYouGiveAReason'
        self.canYouGiveAReasonFor = 'canYouGiveAReasonFor'
        self.canYouGiveACounterArgumentWhy1 = 'canYouGiveACounterArgumentWhy1'
        self.canYouGiveACounterArgumentWhy2 = 'canYouGiveACounterArgumentWhy2'
        self.canYouGiveACounter = 'canYouGiveACounter'
        self.canYouGiveAReasonForThat = 'canYouGiveAReasonForThat'
        self.clearStatistics = 'clearStatistics'
        self.clickForMore = 'clickForMore'
        self.completeView = 'completeView'
        self.completeViewTitle = 'completeViewTitle'
        self.currentDiscussion = 'currentDiscussion'
        self.cancel = 'cancel'
        self.close = 'close'
        self.confPwdEmpty = 'confPwdEmpty'
        self.dialogView = 'dialogView'
        self.dialogViewTitle = 'dialogViewTitle'
        self.dateString = 'dateString'
        self.disagreeBecause = 'disagreeBecause'
        self.description_undermine = 'description_undermine'
        self.description_support = 'description_support'
        self.description_undercut = 'description_undercut'
        self.description_overbid = 'description_overbid'
        self.description_rebut = 'description_rebut'
        self.description_no_opinion = 'description_no_opinion'
        self.decisionIndex7 = 'decisionIndex7'
        self.decisionIndex30 = 'decisionIndex30'
        self.decisionIndex7Info = 'decisionIndex7Info'
        self.decisionIndex30Info = 'decisionIndex30Info'
        self.dataRemoved = 'dataRemoved'
        self.didYouMean = 'didYouMean'
        self.discussionEnd = 'discussionEnd'
        self.discussionEndLinkText = 'discussionEndLinkText'
        self.duplicate = 'duplicate'
        self.duplicateDialog = 'duplicateDialog'
        self.displayControlDialogGuidedTitle = 'displayControlDialogGuidedTitle'
        self.displayControlDialogGuidedBody = 'displayControlDialogGuidedBody'
        self.displayControlDialogIslandTitle = 'displayControlDialogIslandTitle'
        self.displayControlDialogIslandBody = 'displayControlDialogIslandBody'
        self.displayControlDialogExpertTitle = 'displayControlDialogExpertTitle'
        self.displayControlDialogExpertBody = 'displayControlDialogExpertBody'
        self.discussionInfoTooltip1 = 'discussionInfoTooltip1'
        self.discussionInfoTooltip2 = 'discussionInfoTooltip2'
        self.discussionInfoTooltip3sg = 'discussionInfoTooltip3sg'
        self.discussionInfoTooltip3pl = 'discussionInfoTooltip3pl'
        self.doesNotHold = 'doesNotHold'
        self.isNotRight = 'isNotRight'
        self.doesJustify = 'doesJustify'
        self.doesNotJustify = 'doesNotJustify'
        self.deleteTrack = 'deleteTrack'
        self.deleteHistory = 'deleteHistory'
        self.doYouWantToEnterYourStatements = 'doYouWantToEnterYourStatements'
        self.doNotHesitateToContact = 'doNotHesitateToContact'
        self.dbasPwdRequest = 'dbasPwdRequest'
        self.defaultView = 'defaultView'
        self.earlierYouArguedThat = 'earlierYouArguedThat'
        self.editIndex = 'editIndex'
        self.editIndexInfo = 'editIndexInfo'
        self.euCookiePopupTitle = 'euCookiePopupTitle'
        self.euCookiePopupText = 'euCookiePopupText'
        self.euCookiePopoupButton1 = 'euCookiePopoupButton1'
        self.euCookiePopoupButton2 = 'euCookiePopoupButton2'
        self.empty_news_input = 'empty_news_input'
        self.empty_notification_input = 'empty_notification_input'
        self.email = 'email'
        self.emailWasSent = 'emailWasSent'
        self.emailWasNotSent = 'emailWasNotSent'
        self.emailUnknown = 'emailUnknown'
        self.emailBodyText = 'emailBodyText'
        self.emailWasSent = 'emailWasSent'
        self.emailWasNotSent = 'emailWasNotSent'
        self.emailArgumentAddTitle = 'emailArgumentAddTitle'
        self.emailArgumentAddBody = 'emailArgumentAddBody'
        self.edit = 'edit'
        self.error_code = 'error_code'
        self.editTitle = 'editTitle'
        self.editIssueViewChangelog = 'editIssueViewChangelog'
        self.editInfoHere = 'editInfoHere'
        self.editTitleHere = 'editTitleHere'
        self.emptyName = 'emptyName'
        self.emptyEmail = 'emptyEmail'
        self.emtpyContent = 'emtpyContent'
        self.errorTryLateOrContant = 'errorTryLateOrContant'
        self.editStatementViewChangelog = 'editStatementViewChangelog'
        self.editStatementHere = 'editStatementHere'
        self.feelFreeToLogin = 'feelFreeToLogin'
        self.forText = 'forText'
        self.fillLine = 'fillLine'
        self.firstConclusionRadioButtonText = 'firstConclusionRadioButtonText'
        self.firstArgumentRadioButtonText = 'firstArgumentRadioButtonText'
        self.feelFreeToShareUrl = 'feelFreeToShareUrl'
        self.fetchLongUrl = 'fetchLongUrl'
        self.fetchShortUrl = 'fetchShortUrl'
        self.forgotPassword = 'forgotPassword'
        self.firstOneText = 'firstOneText'
        self.firstOneInformationText = 'firstOneInformationText'
        self.firstOneReason = 'firstOneReason'
        self.firstPositionText = 'firstPositionText'
        self.firstPremiseText1 = 'firstPremiseText1'
        self.firstPremiseText2 = 'firstPremiseText2'
        self.firstname = 'firstname'
        self.finishTitle = 'finishTitle'
        self.fromm = 'fromm'
        self.gender = 'gender'
        self.goBack = 'goBack'
        self.goHome = 'goHome'
        self.goStepBack = 'goStepBack'
        self.generateSecurePassword = 'generateSecurePassword'
        self.goodPointTakeMeBackButtonText = 'goodPointTakeMeBackButtonText'
        self.group_uid = 'group_uid'
        self.goBackToTheDiscussion = 'goBackToTheDiscussion'
        self.goBack = 'goBack'
        self.goForward = 'goForward'
        self.haveALookAt = 'haveALookAt'
        self.hidePasswordRequest = 'hidePasswordRequest'
        self.hideGenerator = 'hideGenerator'
        self.hold = 'hold'
        self.howeverIHaveMuchStrongerArgumentRejectingThat = 'howeverIHaveMuchStrongerArgumentRejectingThat'
        self.howeverIHaveMuchStrongerArgumentAcceptingThat = 'howeverIHaveMuchStrongerArgumentAcceptingThat'
        self.howeverIHaveMuchStrongerArgument = 'howeverIHaveMuchStrongerArgument'
        self.howeverIHaveEvenStrongerArgumentRejecting = 'howeverIHaveEvenStrongerArgumentRejecting'
        self.howeverIHaveEvenStrongerArgumentAccepting = 'howeverIHaveEvenStrongerArgumentAccepting'
        self.hideContent = 'hideContent'
        self.hidePositions = 'hidePositions'
        self.imprint = 'Imprint'
        self.islandViewFor = 'islandViewFor'
        self.internalFailureWhileDeletingTrack = 'internalFailureWhileDeletingTrack'
        self.internalFailureWhileDeletingHistory = 'internalFailureWhileDeletingHistory'
        self.internalError = 'internalError'
        self.internalKeyError = 'internalKeyError'
        self.inputEmpty = 'inputEmpty'
        self.informationForExperts = 'informationForExperts'
        self.issueList = 'issueList'
        self.islandViewHeaderText = 'islandViewHeaderText'
        self.irrelevant = 'irrelevant'
        self.itIsTrueThat = 'itIsTrueThat'
        self.itIsTrue1 = 'itIsTrue1'
        self.itIsTrue2 = 'itIsTrue2'
        self.itIsFalseThat = 'itIsFalseThat'
        self.itIsFalse1 = 'itIsFalse1'
        self.itIsFalse2 = 'itIsFalse2'
        self.itTrueIsThat = 'itTrueIsThat'
        self.itFalseIsThat = 'itFalseIsThat'
        self.islandView = 'islandView'
        self.isFalse = 'isFalse'
        self.isTrue = 'isTrue'
        self.areTrue = 'areTrue'
        self.initialPosition = 'initialPosition'
        self.initialPositionSupport = 'initialPositionSupport'
        self.initialPositionAttack = 'initialPositionAttack'
        self.initialPositionInterest = 'initialPositionInterest'
        self.islandViewTitle = 'islandViewTitle'
        self.iAcceptCounter = 'iAcceptCounter'
        self.iAcceptArgument = 'iAcceptArgument'
        self.iAcceptCounterThat = 'iAcceptCounterThat'
        self.iAcceptArgumentThat = 'iAcceptArgumentThat'
        self.iAgreeWithInColor = 'iAgreeWithInColor'
        self.iAgreeWith = 'iAgreeWith'
        self.iDisagreeWithInColor = 'iDisagreeWithInColor'
        self.iDoNotKnow = 'iDoNotKnow'
        self.iDoNotKnowInColor = 'iDoNotKnowInColor'
        self.iHaveNoOpinionYet = 'iHaveNoOpinionYet'
        self.iHaveNoOpinionYetInColor = 'iHaveNoOpinionYetInColor'
        self.iHaveNoOpinion = 'iHaveNoOpinion'
        self.iDisagreeWith = 'iDisagreeWith'
        self.iHaveMuchStrongerArgumentRejecting = 'iHaveMuchStrongerArgumentRejecting'
        self.iHaveEvenStrongerArgumentRejecting = 'iHaveEvenStrongerArgumentRejecting'
        self.iHaveMuchStrongerArgumentAccepting = 'iHaveMuchStrongerArgumentAccepting'
        self.iHaveEvenStrongerArgumentAccepting = 'iHaveEvenStrongerArgumentAccepting'
        self.iNoOpinion = 'iNoOpinion'
        self.isNotAGoodIdea = 'isNotAGoodIdea'
        self.isNotAGoodIdeaInColor = 'isNotAGoodIdeaInColor'
        self.interestingOnDBAS = 'interestingOnDBAS'
        self.informationForStatements = 'informationForStatements'
        self.invalidEmail = 'invalidEmail'
        self.jumpAnswer0 = 'jumpAnswer0'
        self.jumpAnswer1 = 'jumpAnswer1'
        self.jumpAnswer2 = 'jumpAnswer2'
        self.jumpAnswer3 = 'jumpAnswer3'
        self.jumpAnswer4 = 'jumpAnswer4'
        self.keyword = 'keyword'
        self.keywordStart = 'keywordStart'
        self.keywordChooseActionForStatement = 'keywordChooseActionForStatement'
        self.keywordGetPremisesForStatement = 'keywordGetPremisesForStatement'
        self.keywordMoreAboutArgument = 'keywordMoreAboutArgument'
        self.keywordReplyForPremisegroup = 'keywordReplyForPremisegroup'
        self.keywordReplyForResponseOfConfrontation = 'keywordReplyForResponseOfConfrontation'
        self.keywordReplyForArgument = 'keywordReplyForArgument'
        self.keepSetting = 'keepSetting'
        self.hideAllUsers = 'hideAllUsers'
        self.hideAllAttacks = 'hideAllAttacks'
        self.holds = 'holds'
        self.holdsInColor = 'holdsInColor'
        self.letMeExplain = 'letMeExplain'
        self.levenshteinDistance = 'levenshteinDistance'
        self.languageCouldNotBeSwitched = 'languageCouldNotBeSwitched'
        self.last_action = 'last_action'
        self.last_login = 'last_login'
        self.login = 'login'
        self.logfile = 'logfile'
        self.letsGo = 'letsGo'
        self.letsGoBack = 'letsGoBack'
        self.letsGoHome = 'letsGoHome'
        self.medium = 'medium'
        self.more = 'more'
        self.message = 'message'
        self.messageDeleted = 'messageDeleted'
        self.maliciousAntiSpam = 'maliciousAntiSpam'
        self.mail = 'mail'
        self.mailIsTaken = 'mailIsTaken'
        self.mailNotValid = 'mailNotValid'
        self.mailSettingsTitle = 'mailSettingsTitle'
        self.moreAbout = 'moreAbout'
        self.minLength = 'minLength'
        self.myArgument = 'myArgument'
        self.nickIsTaken = 'nickIsTaken'
        self.nicknameIs = 'nicknameIs'
        self.newPwdEmtpy = 'newPwdEmtpy'
        self.newPwdIs = 'newPwdIs'
        self.nonValidCSRF = 'nonValidCSRF'
        self.name = 'name'
        self.newPwdNotEqual = 'newPwdNotEqual'
        self.notificationSettingsTitle = 'notificationSettingsTitle'
        self.notification = 'notification'
        self.notificationDeleted = 'notificationDeleted'
        self.next = 'next'
        self.newNotification = 'newNotification'
        self.newMention = 'newMention'
        self.newPremisesRadioButtonText = 'newPremisesRadioButtonText'
        self.newPremisesRadioButtonTextAsFirstOne = 'newPremisesRadioButtonTextAsFirstOne'
        self.newStatementsRadioButtonTextAsFirstOne = 'newStatementsRadioButtonTextAsFirstOne'
        self.newPremiseRadioButtonText = 'newPremiseRadioButtonText'
        self.newPremiseRadioButtonTextAsFirstOne = 'newPremiseRadioButtonTextAsFirstOne'
        self.newStatementRadioButtonTextAsFirstOne = 'newStatementRadioButtonTextAsFirstOne'
        self.newConclusionRadioButtonText = 'newConclusionRadioButtonText'
        self.newsAboutDbas = 'newsAboutDbas'
        self.nickname = 'nickname'
        self.noOtherAttack = 'noOtherAttack'
        self.noIslandView = 'noIslandView'
        self.noCorrections = 'noCorrections'
        self.noDecisionDone = 'noDecisionDone'
        self.noCorrectionsSet = 'noCorrectionsSet'
        self.notInsertedErrorBecauseEmpty = 'notInsertedErrorBecauseEmpty'
        self.notInsertedErrorBecauseDuplicate = 'notInsertedErrorBecauseDuplicate'
        self.notInsertedErrorBecauseUnknown = 'notInsertedErrorBecauseUnknown'
        self.notInsertedErrorBecauseInternal = 'notInsertedErrorBecauseInternal'
        self.noEntries = 'noEntries'
        self.noTrackedData = 'noTrackedData'
        self.now = 'now'
        self.number = 'number'
        self.note = 'note'
        self.no_entry = 'no_entry'
        self.no_arguments = 'no_arguments'
        self.noRights = 'noRights'
        self.notLoggedIn = 'notLoggedIn'
        self.unfortunatelyOnlyOneItem = 'unfortunatelyOnlyOneItem'
        self.on = 'on'
        self.off = 'off'
        self.opinion = 'opinion'
        self.onlyOneItem = 'onlyOneItem'
        self.onlyOneItemWithLink = 'onlyOneItemWithLink'
        self.otherParticipantsConvincedYouThat = 'otherParticipantsConvincedYouThat'
        self.otherParticipantsThinkThat = 'otherParticipantsThinkThat'
        self.otherParticipantsAgreeThat = 'otherParticipantsAgreeThat'
        self.otherParticipantsDontHaveCounter = 'otherParticipantsDontHaveCounter'
        self.otherParticipantsDontHaveCounterForThat = 'otherParticipantsDontHaveCounterForThat'
        self.otherParticipantsDontHaveNewCounterForThat = 'otherParticipantsDontHaveNewCounterForThat'
        self.otherParticipantsDontHaveOpinion = 'otherParticipantsDontHaveOpinion'
        self.otherParticipantsDontHaveOpinionRegaringYourSelection = 'otherParticipantsDontHaveOpinionRegaringYourSelection'
        self.otherParticipantsDontHaveArgument = 'otherParticipantsDontHaveArgument'
        self.otherParticipantsAcceptBut = 'otherParticipantsAcceptBut'
        self.otherParticipantDisagreeThat = 'otherParticipantDisagreeThat'
        self.otherUsersClaimStrongerArgumentRejecting = 'otherUsersClaimStrongerArgumentRejecting'
        self.otherUsersClaimStrongerArgumentAccepting = 'otherUsersClaimStrongerArgumentAccepting'
        self.otherUsersHaveCounterArgument = 'otherUsersHaveCounterArgument'
        self.otherUsersSaidThat = 'otherUsersSaidThat'
        self.opinionBarometer = 'opinionBarometer'
        self.overbid1 = 'overbid1'
        self.overbid2 = 'overbid2'
        self.oldPwdEmpty = 'oldPwdEmpty'
        self.oldPwdWrong = 'oldPwdWrong'
        self.pleaseEnterTopic = 'pleaseEnterTopic'
        self.pleaseEnterShorttextForTopic = 'pleaseEnterShorttextForTopic'
        self.pleaseSelectLanguageForTopic = 'pleaseSelectLanguageForTopic'
        self.premise = 'premise'
        self.preferedLangTitle = 'preferedLangTitle'
        self.phone = 'phone'
        self.myPosition = 'myPosition'
        self.theirPosition = 'theirPosition'
        self.the_der = 'he_der'
        self.the_die = 'he_die'
        self.the_das = 'he_das'
        self.pwdNotEqual = 'pwdNotEqual'
        self.pwdsSame = 'pwdsSame'
        self.pwdChanged = 'pwdChanged'
        self.pleaseAddYourSuggestion = 'pleaseAddYourSuggestion'
        self.premiseGroup = 'premiseGroup'
        self.previous = 'previous'
        self.passwordSubmit = 'passwordSubmit'
        self.publicNickTitle = 'publicNickTitle'
        self.rebut1 = 'rebut1'
        self.rebut2 = 'rebut2'
        self.resumeHere = 'resumeHere'
        self.report = 'report'
        self.reportTitle = 'reportTitle'
        self.registered = 'registered'
        self.right = 'right'
        self.requestTrack = 'requestTrack'
        self.refreshTrack = 'refreshTrack'
        self.requestHistory = 'requestHistory'
        self.refreshHistory = 'refreshHistory'
        self.requestFailed = 'requestFailed'
        self.remStatementRow = 'remStatementRow'
        self.restartDiscussion = 'restartDiscussion'
        self.restartDiscussionTitle = 'restartDiscussionTitle'
        self.restartOnError = 'restartOnError'
        self.recipientNotFound = 'recipientNotFound'
        self.reactionFor = 'reactionFor'
        self.review = 'review'
        self.rejecting = 'rejecting'
        self.reason = 'reason'
        self.questionTitle = 'questionTitle'
        self.selectStatement = 'selectStatement'
        self.showAllUsers = 'showAllUsers'
        self.showAllArguments = 'showAllArguments'
        self.showAllArgumentsTitle = 'showAllArgumentsTitle'
        self.showAllUsersTitle = 'showAllUsersTitle'
        self.saveMyStatement = 'saveMyStatement'
        self.statementIsAbout = 'statementIsAbout'
        self.statementIndex = 'statementIndex'
        self.statementIndexInfo = 'statementIndexInfo'
        self.strength = 'strength'
        self.strong = 'strong'
        self.strongerStatementForAccepting1 = 'strongerStatementForAccepting1'
        self.strongerStatementForAccepting2 = 'strongerStatementForAccepting2'
        self.strongerStatementForAccepting3 = 'strongerStatementForAccepting3'
        self.strongerStatementForRecjecting1 = 'strongerStatementForRecjecting1'
        self.strongerStatementForRecjecting2 = 'strongerStatementForRecjecting2'
        self.strongerStatementForRecjecting3 = 'strongerStatementForRecjecting3'
        self.soYouEnteredMultipleReasons = 'soYouEnteredMultipleReasons'
        self.soYourOpinionIsThat = 'soYourOpinionIsThat'
        self.soYouWantToArgueAgainst = 'soYouWantToArgueAgainst'
        self.soThatOtherParticipantsDontHaveOpinionRegardingYourOpinion = 'soThatOtherParticipantsDontHaveOpinionRegardingYourOpinion'
        self.shortenedBy = 'shortenedBy'
        self.shareUrl = 'shareUrl'
        self.statement = 'statement'
        self.statementAdded = 'statementAdded'
        self.argumentAdded = 'argumentAdded'
        self.statementAddedMessageContent = 'statementAddedMessageContent'
        self.argumentAddedMessageContent = 'argumentAddedMessageContent'
        self.showMeAnotherArgument = 'showMeAnotherArgument'
        self.switchDiscussion = 'switchDiscussion'
        self.switchDiscussionTitle = 'switchDiscussionTitle'
        self.switchDiscussionText1 = 'switchDiscussionText1'
        self.switchDiscussionText2 = 'switchDiscussionText2'
        self.switchLanguage = 'switchLanguage'
        self.supportPosition = 'supportPosition'
        self.supportsNot = 'supportsNot'
        self.myStatement = 'myStatement'
        self.sureThat = 'sureThat'
        self.surname = 'surname'
        self.showMeAnArgumentFor = 'showMeAnArgumentFor'
        self.save = 'save'
        self.submit = 'submit'
        self.signs = 'signs'
        self.showContent = 'showContent'
        self.showPositions = 'showPositions'
        self.snapshotGraph = 'snapshotGraph'
        self.support = 'support'
        self.support1 = 'support1'
        self.isupport = 'isupport'
        self.assertion = 'assertion'
        self.tightView = 'tightView'
        self.textAreaReasonHintText = 'textAreaReasonHintText'
        self.theCounterArgument = 'theCounterArgument'
        self.therefore = 'therefore'
        self.thinkWeShould = 'thinkWeShould'
        self.thisConfrontationIs = 'thisConfrontationIs'
        self.thisIsACopyOfMail = 'thisIsACopyOfMail'
        self.theirArgument = 'theirArgument'
        self.thisArgument = 'thisArgument'
        self.textversionChangedTopic = 'textversionChangedTopic'
        self.textversionChangedContent = 'textversionChangedContent'
        self.thxForFlagText = 'thxForFlagText'
        self.to = 'to'
        self.this = 'this'
        self.textChange = 'textChange'
        self.track = 'track'
        self.history = 'history'
        self.topicString = 'topicString'
        self.text = 'text'
        self.theySay = 'theySay'
        self.theyThink = 'theyThink'
        self.veryweak = 'veryweak'
        self.wantToStateNewPosition = 'wantToStateNewPosition'
        self.weak = 'weak'
        self.wrong = 'wrong'
        self.wouldYourShareArgument = 'wouldYourShareArgument'
        self.wrongURL = 'wrongURL'
        self.whatDoYouThinkAbout = 'whatDoYouThinkAbout'
        self.whatDoYouThinkOf = 'whatDoYouThinkOf'
        self.whatDoYouThinkAboutThat = 'whatDoYouThinkAboutThat'
        self.whyDoYouThinkThat = 'whyDoYouThinkThat'
        self.whatIsYourIdea = 'whatIsYourIdea'
        self.whatIsYourMostImportantReasonFor = 'whatIsYourMostImportantReasonFor'
        self.whatIsYourMostImportantReasonWhyFor = 'whatIsYourMostImportantReasonWhyFor'
        self.whatIsYourMostImportantReasonWhyAgainst = 'whatIsYourMostImportantReasonWhyAgainst'
        self.whatIsYourMostImportantReasonWhyForInColor = 'whatIsYourMostImportantReasonWhyForInColor'
        self.whatIsYourMostImportantReasonWhyAgainstInColor = 'whatIsYourMostImportantReasonWhyAgainstInColor'
        self.whyAreYouDisagreeingWith = 'whyAreYouDisagreeingWith'
        self.whyAreYouAgreeingWith = 'whyAreYouAgreeingWith'
        self.whyAreYouDisagreeingWithInColor = 'whyAreYouDisagreeingWithInColor'
        self.whyAreYouAgreeingWithInColor = 'whyAreYouAgreeingWithInColor'
        self.whyAreYouDisagreeingWithThat = 'whyAreYouDisagreeingWithThat'
        self.youMadeA = 'youMadeA'
        self.youMadeAn = 'youMadeAn'
        self.relation_undermine = 'relation_undermine'
        self.relation_support = 'relation_support'
        self.relation_undercut = 'relation_undercut'
        self.relation_overbid = 'relation_overbid'
        self.relation_rebut = 'relation_rebut'
        self.uid = 'uid'
        self.unfortunatelyNoMoreArgument = 'unfortunatelyNoMoreArgument'
        self.userPasswordNotMatch = 'userPasswordNotMatch'
        self.userOptions = 'userOptions'
        self.undermine = 'undermine'
        self.undercut1 = 'undercut1'
        self.undercut2 = 'undercut2'
        self.urlSharing = 'urlSharing'
        self.urlSharingDescription = 'urlSharingDescription'
        self.userPasswordNotMatch = 'userPasswordNotMatch'
        self.voteCountTextFirst = 'voteCountTextFirst'
        self.voteCountTextMayBeFirst = 'voteCountTextMayBeFirst'
        self.voteCountTextOneOther = 'voteCountTextOneOther'
        self.voteCountTextMore = 'voteCountTextMore'
        self.warning = 'warning'
        self.where = 'where'
        self.wideView = 'wideView'
        self.welcome = 'welcome'
        self.welcomeMessage = 'welcomeMessage'
        self.youAreInterestedIn = 'youAreInterestedIn'
        self.youAgreeWith = 'youAgreeWith'
        self.youDisagreeWith = 'youDisagreeWith'
        self.youSaidThat = 'youSaidThat'
        self.youUsedThisEarlier = 'youUsedThisEarlier'
        self.youRejectedThisEarlier = 'youRejectedThisEarlier'
        self.youHaveMuchStrongerArgumentForAccepting = 'youHaveMuchStrongerArgumentForAccepting'
        self.youHaveMuchStrongerArgumentForRejecting = 'youHaveMuchStrongerArgumentForRejecting'

        self.sentencesOpenersArguingWithAgreeing = [self.agreeBecause, self.therefore]
        self.sentencesOpenersArguingWithDisagreeing = [self.disagreeBecause, self.alternatively]
        self.sentencesOpenersInforming = [self.thinkWeShould, self.letMeExplain, self.sureThat]

        self.en_dict = EnglischDict().set_up(self)
        self.de_dict = GermanDict().set_up(self)

    def get(self, sid):
        """
        Returns an localized string

        :param sid: string identifier
        :return: string
        """
        if self.lang == 'de' and sid in self.de_dict:
            return self.de_dict[sid]

        elif self.lang == 'en' and sid in self.en_dict:
            return self.en_dict[sid]

        elif self.lang == 'de' and sid not in self.de_dict:
            return 'unbekannter identifier im deutschen Wörterbuch'

        elif self.lang == 'en' and sid not in self.en_dict:
            return 'unknown identifier in the englisch dictionary'

        else:
            return 'unknown language: ' + str(self.lang)
