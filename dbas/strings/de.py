#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
TODO

.. codeauthor:: Tobias Krauthoff <krauthoff@cs.uni-duesseldorf.de
"""
from .keywords import Keywords as _

de_lang = {
    _.zero: 'null',
    _.one: 'eins',
    _.two: 'zwei',
    _.three: 'drei',
    _.four: 'vier',
    _.five: 'fünf',
    _.six: 'sechs',
    _.seven: 'sieben',
    _.eight: 'acht',
    _.nine: 'neun',
    _.plus: 'plus',
    _.minus: 'minus',
    _.times: 'mal',
    _.divided_by: 'durch',
    _.arguments: 'Argumente',
    _.error: 'Fehler',
    _.iActuallyHave: 'Ich habe',
    _.insertOneArgument: 'Ich habe eine Aussage:',
    _.insertDontCare: 'Es ist ein Argument und das System interpretiert es falsch!',
    _.forgotInputRadio: 'Sie haben eine Auswahl vergessen',
    _.needHelpToUnderstandStatement: 'Wir brauchen Hilfe zum Verständnis Ihrer Aussage!',
    _.setPremisegroupsIntro1: 'Sie haben \'und\' in Ihrer Aussage ',
    _.setPremisegroupsIntro2: ' benutzt. Daher existieren mehrere mögliche Auswertungen. Bitte helfen Sie uns, die richtig Eingabe zu wählen:',
    _.attack: 'Sie lehnen ab, dass',
    _.assertion: 'Behauptung',
    _.support: 'Sie akzeptieren',
    _.premise: 'Prämisse',
    _.because: 'Weil',
    _.moreAbout: 'Mehr über',
    _.undermine: 'Es ist falsch, dass',
    _.support1: 'Es ist richtig, dass',
    _.undercut1: 'Es ist falsch, dass',
    _.undercut2: 'und das ist ein schlechter Konter',
    _.overbid1: 'Es ist falsch, dass',
    _.overbid2: 'und das ist ein guter Konter',
    _.rebut1: 'Es ist richtig, dass',
    _.rebut2: ', aber ich habe etwas besseres',
    _.oldPwdEmpty: 'Altes Passwortfeld ist leer.',
    _.newPwdEmtpy: 'Neues Passwortfeld ist leer.',
    _.confPwdEmpty: 'Bestätigungs-Passwordfeld ist leer.',
    _.newPwdNotEqual: 'Passwort und Bestätigung stimmen nicht überein.',
    _.pwdsSame: 'Beide eingegeben Passwörter sind identisch.',
    _.oldPwdWrong: 'Ihr altes Passwort ist falsch.',
    _.pwdChanged: 'Ihr Passwort würde geändert.',
    _.emptyName: 'Ihr Name ist leer!',
    _.emptyEmail: 'Ihre E-Mail ist leer!',
    _.emtpyContent: 'Ihr Inhalt ist leer!',
    _.maliciousAntiSpam: 'Ihr Anti-Spam-Nachricht ist leer oder falsch!',
    _.nonValidCSRF: 'CSRF-Token ist nicht valide',
    _.name: 'Name',
    _.mail: 'Mail',
    _.phone: 'Telefon',
    _.message: 'Nachricht',
    _.messageDeleted: 'Nachricht gelöscht',
    _.notification: 'Benachrichtigung',
    _.notificationDeleted: 'Benachrichtigung gelöscht',
    _.pwdNotEqual: 'Passwörter sind nicht gleich.',
    _.nickIsTaken: 'Nickname ist schon vergeben.',
    _.mailIsTaken: 'E-Mail ist schon vergeben.',
    _.mailNotValid: 'E-Mail ist nicht gültig.',
    _.mailSettingsTitle: '(De-)Aktiviert E-Mail',
    _.notificationSettingsTitle: '(De-)Aktiviert Nachrichten',
    _.errorTryLateOrContant: 'Leider ist ein Fehler aufgetreten, bitte versuchen Sie später erneut oder kontaktieren Sie uns.',
    _.accountWasAdded: 'Ihr Account wurde angelegt. Sie können sich nun anmelden.',
    _.accountRegistration: 'D-BAS Benutzer Registrierung',
    _.accountWasRegistered: 'Ihr Account wurde erfolgreich für die genannte E-Mail registriert.',
    _.accoutErrorTryLateOrContant: 'Ihr Account konnte nicht angelegt werden, bitte versuchen Sie später erneut oder kontaktieren Sie uns.',
    _.nicknameIs: 'Ihr Nickname lautet: ',
    _.newPwdIs: 'Ihr Passwort lautet: ',
    _.dbasPwdRequest: 'D-BAS Passwort Nachfrage',
    _.antispamquestion: 'Was ist',
    _.defaultView: 'Standardansicht',
    _.positions: 'Positionen',
    _.labels: 'Beschriftungen',
    _.myStatements: 'Meine Aussagen',
    _.supportsOnMyStatements: 'Unterstützungen',
    _.attacksOnMyStatements: 'Angriffe',
    _.addATopic: 'Thema hinzufügen',
    _.pleaseEnterTopic: 'Bitte geben Sie Ihr Thema an:',
    _.pleaseEnterShorttextForTopic: 'Bitte geben Sie die Kurzform Ihres Themas an:',
    _.pleaseSelectLanguageForTopic: 'Bitte geben Sie die Sprache Ihres Themas an:',
    _.editIssueViewChangelog: 'Thema editieren / Änderungprotokoll einsehen',
    _.editTitleHere: 'Bitte bearbeiten Sie hier den Title:',
    _.editInfoHere: 'Bitte bearbeiten Sie hier die Info:',
    _.viewChangelog: 'Änderungprotokoll einsehen',
    _.editStatementHere: 'Bitte bearbeiten Sie hier die Aussage:', _.save: 'Sichern',
    _.cancel: 'Abbrechen', _.submit: 'Senden', _.close: 'Schließen',
    _.urlSharing: 'URL teilen', _.urlSharingDescription: 'Teilen Sie diese URL:',
    _.warning: 'Warnung', _.islandViewFor: 'Inselansicht für',
    _.resumeHere: 'Hier weitermachen', _.aand: 'und', _.andor: 'und/oder',
    _.addStatementRow: 'Weiteres Argument angegeben.',
    _.addedEverything: 'Alles wurde hinzugefügt.', _.addTopic: 'Thema hinzufügen',
    _.at: 'am', _.alreadyInserted: 'Dies ist ein Duplikat und schon vorhanden.',
    _.addPremisesRadioButtonText: 'Lass\' mich meine eigenen Gründe angeben!',
    _.addArgumentsRadioButtonText: 'Lass\' mich meine eigenen Aussagen angeben!',
    _.argumentContainerTextIfPremises: 'Sie möchten Ihre eigenen Gründe angeben?',
    _.argumentContainerTextIfArguments: 'Sie möchten Ihre eigenen Argumente angeben?',
    _.addPremiseRadioButtonText: 'Lass\' mich meinen eigenen Grund angeben!',
    _.addArgumentRadioButtonText: 'Lass\' mich meine eigene Aussage angeben!',
    _.argumentContainerTextIfPremise: 'Sie möchten Ihren eigenen Grund angeben?',
    _.argumentContainerTextIfArgument: 'Sie möchten Ihr eigenes Argument angeben?',
    _.argumentContainerTextIfConclusion: 'Was ist Ihre Idee? Was sollten wir unternehmen?',
    _.argueAgainstPositionToggleButton: 'Oder wenn Sie gegen eine Position argumentieren möchten, drücken Sie bitte diesen Schalter:',
    _.argueForPositionToggleButton: 'Oder wenn Sie für eine Position argumentieren möchten, drücken Sie bitte diesen Schalter:',
    _.argumentFlaggedBecauseOfftopic: 'Dieses Argument wurde von einer/m Benutzer/in gemeldet, da es möglicherweise <strong>nicht themenbezogen</strong> ist.',
    _.argumentFlaggedBecauseSpam: 'Dieses Argument wurde von einer/m Benutzer/in gemeldet, da es möglicherweise <strong>Spam</strong> ist.',
    _.argumentFlaggedBecauseHarmful: 'Dieses Argument wurde von einer/m Benutzer/in gemeldet, da es möglicherweise <strong>nicht angebracht, schädlich oder missbräuchlich</strong> ist.',
    _.argumentFlaggedBecauseOptimization: 'Dieses Argument wurde von einer/m Benutzer/in gemeldet, da es möglicherweise <strong>sprachlicher Korrektur</strong> bedarf.',
    _.argumentFlaggedBecauseEdit: 'Dieses Argument wurde von einer/m Benutzer/in sprachlich verbessert.',
    _.alternatively: 'Alternativ', _.argument: 'Argument', _.accepting: 'für',
    _.andIDoNotBelieveCounter: 'und ich glaube, dass ist kein gutes Gegenargument für',
    _.andIDoNotBelieveArgument: 'und ich glaube, dass ist kein gutes Argument für',
    _.andTheyDoNotBelieveCounter: 'und sie glauben, dass ist kein gutes Gegenargument für',
    _.andTheyDoNotBelieveArgument: 'und sie glauben, dass ist kein gutes Argument für',
    _.asReasonFor: 'als einen Grund für', _.attackedBy: 'Sie wurden attackiert mit',
    _.attackedWith: 'Sie haben attackiert mit', _.attackPosition: 'Position angreifen',
    _.agreeBecause: 'Ich stimme zu, weil ',
    _.andIDoBelieveCounterFor: 'und ich glaube, dass ist ein gutes Gegenargument für',
    _.andIDoBelieveArgument: 'und ich glaube, dass ist ein gutes Argument für',
    _.addArguments: 'Argumente hizufügen', _.addStatements: 'Aussagen hizufügen',
    _.addArgumentsTitle: 'Fügt neue Argumente hinzu', _.acceptItTitle: 'Einsenden...',
    _.acceptIt: 'Eintragen...', _.attitudeFor: 'Einstellungen zu',
    _.alreadyFlaggedByOthers: 'Diese Aussage wurde uns schon gemeldet!',
    _.alreadyFlaggedByYou: 'Diese Aussage haben Sie uns schon gemeldet!',
    _.breadcrumbsStart: 'Start', _.breadcrumbsChoose: 'Mehrere Gründe für',
    _.breadcrumbsJustifyStatement: 'Wieso denken Sie das',
    _.breadcrumbsGetPremisesForStatement: 'Prämissen',
    _.breadcrumbsMoreAboutArgument: 'Mehr Über',
    _.breadcrumbsReplyForPremisegroup: 'Antwort für Gruppe',
    _.breadcrumbsReplyForResponseOfConfrontation: 'Begründung von',
    _.breadcrumbsReplyForArgument: 'Antwort fürs Argument',
    _.butOtherParticipantsDontHaveOpinionRegardingYourOpinion: 'aber andere Teilnehmer haben keine Meinung bezüglich ihrer Eingabe',
    _.butOtherParticipantsDontHaveArgument: 'aber andere Teilnehmer haben keine Begründung für dafür',
    _.butOtherParticipantsDontHaveCounterArgument: 'aber andere Teilnehmer haben kein Gegenargument.',
    _.butIDoNotBelieveCounterFor: 'aber ich glaube nicht, dass es ein gutes Argument dagegen ist, dass',
    _.butIDoNotBelieveArgumentFor: 'aber ich glaube nicht, dass es ein gutes Argument dafür ist, dass',
    _.butIDoNotBelieveCounter: 'aber ich glaube nicht, dass es ein gutes Argument gegen',
    _.butIDoNotBelieveArgument: 'aber ich glaube nicht, dass es ein gutes Argument für',
    _.butIDoNotBelieveReasonForReject: 'aber ich glaube nicht, dass das zur Aussage führt',
    _.butTheyDoNotBelieveCounter: 'aber sie glauben, dass es kein gutes Argument dagegen ist, dass',
    _.butTheyDoNotBelieveArgument: 'aber sie glauben, dass es kein gutes Argument dafür ist, dass',
    _.butThenYouCounteredWith: 'Jedoch haben Sie dann das Gegenargument gebracht, dass',
    _.butYouCounteredWith: 'Jedoch haben Sie das Gegenargument gebracht, dass',
    _.butYouAgreedWith: 'Und Sie haben zugestimmt, weil', _.but: 'aber',
    _.butWhich: 'aber welches',
    _.clickHereForRegistration: 'Klick <a data-href="login" data-toggle="modal" data-target="#popup-login" title="Login">hier</a> für die Anmeldung oder eine Registrierung!',
    _.clickForMore: 'Klick hier!', _.confirmation: 'Bestätigung',
    _.contactSubmit: 'Nachricht senden', _.contact: 'Kontakt',
    _.confirmTranslation: 'Wenn Sie die Sprache ändern, geht Ihr aktueller Fortschritt verloren!',
    _.correctionsSet: 'Ihre Korrektur wurde gesetzt.',
    _.countOfArguments: 'Anzahl der Argumente', _.countOfPosts: 'Anzahl der Beiträge',
    _.checkFirstname: 'Bitte überprüfen Sie Ihren Vornamen, da die Eingabe leer ist!',
    _.checkLastname: 'Bitte überprüfen Sie Ihren Nachnamen, da die Eingabe leer ist!',
    _.checkNickname: 'Bitte überprüfen Sie Ihren Spitznamen, da die Eingabe leer ist!',
    _.checkEmail: 'Bitte überprüfen Sie Ihre E-Mail, da die Eingabe leer ist!',
    _.checkPassword: 'Bitte überprüfen Sie Ihre Passwort, da die Eingabe leer ist!',
    _.checkConfirmation: 'Bitte überprüfen Sie Ihre Passwort-Bestätigung, da die Eingabe leer ist!',
    _.checkPasswordConfirm: 'Bitte überprüfen Sie Ihre Passwörter, da die Passwärter nicht gleich sind!',
    _.clickToChoose: 'Klicken zum wählen', _.clearStatistics: 'Statistik löschen',
    _.canYouGiveAReason: 'Können Sie einen Grund angeben?',
    _.canYouGiveAReasonFor: 'Können Sie einen Grund für folgendes angeben:',
    _.canYouGiveACounterArgumentWhy1: 'Können Sie begründen, wieso sie gegen',
    _.canYouGiveACounterArgumentWhy2: 'sind?',
    _.canYouGiveACounter: 'Können Sie einen Grund dagegen angeben?',
    _.canYouGiveAReasonForThat: 'Können Sie dafür einen Grund angeben?',
    _.completeView: 'Komplette View', _.completeViewTitle: 'Kompletten Graphen anzeigen',
    _.currentDiscussion: 'Die aktuelle Diskussion hat folgendes Thema',
    _.dialogView: 'Dialog-Ansicht', _.dialogViewTitle: 'Dialog-Ansicht',
    _.dateString: 'Datum', _.disagreeBecause: 'Ich widerspreche, weil ',
    _.description_undermine: 'Diese Aussage ist gegen die Prämisse.',
    _.description_support: 'Diese Aussage ist für die Prämisse.',
    _.description_undercut: 'Diese Aussage ist gegen die Begründung (undercut). Sie glauben nicht, dass aus der Prämisse die Konklusion folgt.',
    _.description_overbid: 'Diese Aussage ist für die Begründung (overbid). Sie glauben nicht, dass aus der Prämisse die Konklusion folgt.',
    _.description_rebut: 'Diese Aussage ist gegen die Konklusion.',
    _.description_no_opinion: 'Sie haben keine Meinung odeWas ist Ihre Meinung?r möchten diesen Punkt nur überspringen.',
    _.decisionIndex7: 'Entscheidungs Index - Letzte 7 Tage',
    _.decisionIndex30: 'Entscheidungs Index - Letzte 30 Tage',
    _.decisionIndex7Info: 'Anzahl an getroffenen Entscheidungen (bedingt durch Klicks im System), in den letzten 7 Tage',
    _.decisionIndex30Info: 'Anzahl an getroffenen Entscheidungen (bedingt durch Klicks im System), in den letzten 30 Tage',
    _.dataRemoved: 'Daten wurden erfolgreich gelöscht.',
    _.didYouMean: 'Top 10 der Aussagen, die Sie eventuell meinten:',
    _.discussionEnd: 'Die Diskussion endet hier.',
    _.discussionEndLinkText: 'Sie können <a id="discussionEndStepBack" data-href="back" onclick="window.history.back();" style="cursor: pointer;">hier</a> klicken, um einen Schritt zurückzugehen oder den oberen Button bzw. <a id="discussionEndRestart" data-href="restart">diesen Link</a> nutzen, um die Diskussion neu zustarten.',
    _.duplicateDialog: 'Diese Textversion ist veraltet, weil Sie schon editiert wurde.\nMöchten Sie diese Version dennoch als die aktuellste markieren?',
    _.duplicate: 'Duplikat', _.displayControlDialogGuidedTitle: 'Dialog-Ansicht',
    _.displayControlDialogGuidedBody: 'Du wirst nie etwas wie eine Argumentationskarte sehen, da das System dich führt. Das System ist daher dynamisch und generisch für dich.',
    _.displayControlDialogIslandTitle: 'Insel-Ansicht',
    _.displayControlDialogIslandBody: 'Okay, Sie möchten mehr sehen, aber nicht alles? Genau dafür haben wie eine Insel-Ansicht als weitere Modus. Mit dieser Möglichkeit sehen Sie alle Aussagen, die mit Ihrem aktuellen Standpunkt verbunden sind.',
    _.displayControlDialogExpertTitle: 'Experten-Ansicht',
    _.displayControlDialogExpertBody: 'Du bist also ein Experte? Okay, dann darfst du wirklich alles auf einen Blick sehen.',
    _.displayControlDialogGraphTitle: 'Graph-Ansicht',
    _.displayControlDialogGraphBody: 'Darstellung der Diskussion als Graph.',
    _.discussionInfoTooltip1: 'Die Diskussion wurde',
    _.discussionInfoTooltip2: 'gestartet und hat schon',
    _.discussionInfoTooltip3pl: 'Argumente.', _.discussionInfoTooltip3sg: 'Argument.',
    _.doesNotHold: 'ist keine gute Idee', _.isNotRight: 'ist nicht richtig',
    _.doesJustify: 'gerechtfertigen, dass', _.doesNotJustify: 'nicht gerechtfertigen, dass',
    _.deleteTrack: 'Track löschen', _.deleteStatement: 'Aussage löschen',
    _.delete: 'Löschen', _.deleteHistory: 'History löschen',
    _.doYouWantToEnterYourStatements: 'Möchten Sie Ihre eigenen Gründe angeben?',
    _.doNotHesitateToContact: 'Zögern Sie nicht, uns zu <span style="cursor: pointer;" id="contact-on-error"><strong>kontaktieren (hier klicken)</strong></span>',
    _.dataAlreadyLockedByYou: 'Sie bearbeiten schon einen Datensatz. Schließen Sie diese Bearbeitung bitte zuerst ab!',
    _.dataAlreadyLockedByOthers: 'Dieser Datensatz wird gerade durch andere Teilnehmer bearbeitet.',
    _.earlierYouArguedThat: 'Zuerst haben Sie argumentiert, dass',
    _.editIndex: 'Änderungs Index - Letzte 30 Tage', _.editIndexInfo: 'Anzahl an Änderungen',
    _.euCookiePopupTitle: 'Diese Seite nutzt Cookies und Piwik.',
    _.euCookiePopupText: 'Wir benutzen Sie, um Ihnen die beste Erfahrung zu geben. Wenn Sie unsere Seite weiter nutzen, nehmen Sie alle Cookies unserer Seite an und sind glücklich damit. Zusätzlich tracken wir Ihre Aktionen und speichern diese anonym ab. Dabei wird Ihre IP-Adresse maskiert.',
    _.euCookiePopoupButton1: 'Weiter', _.euCookiePopoupButton2: 'Lerne&nbsp;mehr',
    _.empty_news_input: 'Nachrichten-Titel oder Text ist leer oder zu kurz!',
    _.empty_notification_input: 'Nachrichten-Titel oder Text ist leer oder zu kurz!',
    _.email: 'E-Mail', _.emailWasSent: 'E-Mail wurde gesendet.',
    _.emailWasNotSent: 'E-Mail wurde nicht gesendet.',
    _.emailUnknown: 'Die Adresse ist nicht gültig.',
    _.emailBodyText: 'Dies ist eine automatisch generierte E-Mail von D-BAS https://dbas.cs.uni-duesseldorf.de/.\nBei Rückfragen können Sie gerne eine E-Mail an krauthoff@cs.uni-duesseldorf.de verfassen.\nDieses System ist Teil einer Promotion und noch in der Testphase.',
    _.emailArgumentAddTitle: 'D-BAS Infos zum Argument',
    _.emailArgumentAddBody: 'Zu Ihrem Argument wurden weitere Informationen hinzugefügt. Schauen Sie doch mal rein:',
    _.edit: 'Bearbeiten', _.error_code: 'Fehler-Code', _.editTitle: 'Aussage bearbeiten',
    _.feelFreeToLogin: 'Wenn Sie weiter machen möchten, <u><a data-href="login" data-toggle="modal" data-target="#popup-login" title="Anmelden">melden</a></u> Sie sich bitte an :)',
    _.forText: 'für', _.forThat: 'dafür, dass',
    _.fillLine: 'Bitte, füllen Sie diese Zeilen mit Ihrer Meldung',
    _.firstConclusionRadioButtonText: 'Lass mich meine eigenen Ideen einfügen!',
    _.firstArgumentRadioButtonText: 'Lass mich meine eigenen Aussagen einfügen!',
    _.feelFreeToShareUrl: 'Bitte teilen Sie diese URL', _.fetchLongUrl: 'Normale URL',
    _.fetchShortUrl: 'Kurze URL', _.forgotPassword: 'Passwort vergessen',
    _.firstOneText: 'Sie sind der Erste, der sagt: ',
    _.firstOneInformationText: 'Sie sind der Erste, der Informationen haben möchte, über: ',
    _.firstOneReason: 'Sie sind der Erste mit diesem Argument. Bitte geben Sie Ihre Begründung an.',
    _.firstPositionText: 'Sie sind der Erste in dieser Diskussion!',
    _.firstPremiseText1: 'Sie sind der Erste, der sagt, dass ',
    _.firstPremiseText2: 'Bitte begründen Sie Ihre Aussage.', _.firstname: 'Vorname',
    _.fromm: 'von', _.finishTitle: 'Diskussion beenden', _.hold: 'stimmen',
    _.gender: 'Geschlecht', _.goBack: 'Klicken, um zurückzugehen', _.goHome: 'Startseite',
    _.goStepBack: 'Einen Schritt zurück', _.generateSecurePassword: 'Generate secure password',
    _.goodPointTakeMeBackButtonText: 'Ich stimme zu, dass ist ein gutes Argument. Geh einen Schritt zurück.',
    _.group_uid: 'Gruppe', _.goBackToTheDiscussion: 'Geh zur Diskussion',
    _.goForward: 'Klicken, um weiterzugehen', _.haveALookAt: 'Hey, schau dir mal das an: ',
    _.hidePasswordRequest: 'Verstecke die Passwort-Anfrage',
    _.hideGenerator: 'Verstecke Generator', _.history: 'Geschichte',
    _.howeverIHaveMuchStrongerArgumentRejectingThat: 'Jedoch habe ich ein viel stärkeres Argument dagegen, dass',
    _.howeverIHaveMuchStrongerArgumentAcceptingThat: 'Jedoch habe ich ein viel stärkeres Argument dafür, dass',
    _.howeverIHaveMuchStrongerArgument: 'Jedoch habe ich ein viel stärkeres Argument',
    _.howeverIHaveEvenStrongerArgumentRejecting: 'Jedoch habe ich ein stärkeres Argument gegen:',
    _.howeverIHaveEvenStrongerArgumentAccepting: 'Jedoch habe ich ein stärkeres Argument für:',
    _.imprint: 'Impressum',
    _.internalFailureWhileDeletingTrack: 'Interner Fehler, bitte versuchen Sie es später erneut.',
    _.internalFailureWhileDeletingHistory: 'Interner Fehler, bitte versuchen Sie es später erneut.',
    _.internalError: '<strong>Interner Fehler:</strong> Wahrscheinlich ist der Server nicht erreichbar. Bitte laden Sie die Seite erneut!.',
    _.internalKeyError: 'Interner Fehler beim verarbeiten von Daten.',
    _.inputEmpty: 'Ihre Eingabe ist leer!', _.informationForExperts: 'Infos für Experten',
    _.issueList: 'Themen', _.islandViewHeaderText: 'Dies sind alle Argumente für: ',
    _.irrelevant: 'Irrelevant', _.itIsTrueThat: 'ich akzeptiere, dass',
    _.itIsTrue1: 'ich akzeptiere', _.itIsTrue2: '', _.itIsFalseThat: 'ich lehne ab, dass',
    _.itIsFalse1: 'ich lehne', _.itIsFalse2: 'ab', _.itTrueIsThat: 'es richtig ist, dass',
    _.itFalseIsThat: 'es falsch ist, dass', _.islandView: 'Insel Ansicht',
    _.isFalse: 'ist falsch', _.isTrue: 'richtig ist', _.areTrue: 'sind richtig',
    _.isNotAGoodIdea: 'falsch ist',
    _.isNotAGoodIdeaInColor: '<span class=\'text-danger\'>falsch ist</span>',
    _.initialPosition: 'Anfangs-interesse',
    _.initialPositionSupport: 'Was ist Ihre Meinung, die Sie unterstützen?',
    _.initialPositionAttack: 'Was ist Ihre Meinung, die Sie angreifen möchten?',
    _.initialPositionInterest: 'Ich möchte über die Aussage reden, dass ...',
    _.invalidEmail: 'Ihre E-Mail ist ungültig!', _.islandViewTitle: 'Zeigt die Insel Ansicht',
    _.iAcceptCounter: 'und ich akzeptiere, dass es ein Argument gegen',
    _.iAcceptArgument: 'und ich akzeptiere, dass es ein Argument für',
    _.iAcceptCounterThat: 'und ich akzeptiere, dass es ein Argument dagegen ist, dass',
    _.iAcceptArgumentThat: 'und ich akzeptiere, dass es ein Argument dafür ist, dass',
    _.iAgreeWith: 'Ich akzeptiere es',
    _.iAgreeWithInColor: 'Ich <span class=\'text-success\'>akzeptiere es</span>',
    _.iDisagreeWith: 'Ich lehne es ab',
    _.iDisagreeWithInColor: 'Ich <span class=\'text-danger\'>lehne es ab</span>',
    _.iDoNotKnow: 'Ich weiß es nicht, dass',
    _.iDoNotKnowInColor: 'Ich <span class=\'text-info\'>weiß es nicht</span>',
    _.iHaveNoOpinionYet: 'Ich weiß es nicht, dass', _.iHaveNoOpinion: 'Ich weiß es nicht',
    _.iHaveNoOpinionYetInColor: 'Ich <span class=\'text-info\'>weiß es nicht</span>. Zeige mir eine Aussage für das Argument',
    _.iHaveMuchStrongerArgumentRejecting: 'Ich habe ein viel stärkeres Argument zum Ablehnen von',
    _.iHaveEvenStrongerArgumentRejecting: 'Ich habe ein stärkeres Argument zum Ablehnen von',
    _.iHaveMuchStrongerArgumentAccepting: 'Ich habe ein viel stärkeres Argument zum Akzeptieren von',
    _.iHaveEvenStrongerArgumentAccepting: 'Ich habe ein stärkeres Argument zum Akzeptieren von',
    _.iNoOpinion: 'Ich habe keine Meinung bezüglich',
    _.interestingOnDBAS: 'Interessante Diskussion in D-BAS',
    _.informationForStatements: 'Informationen zu den Aussagen',
    _.jumpAnswer0: 'Ja, ich halte die XXCONCLUSIONXX für richtig und finde die XXPREMISEXX gut.',
    _.jumpAnswer1: 'Ja, ich halte die XXCONCLUSIONXX für richtig, aber ich möchte meine eigene XXPREMISEXX angeben.',
    _.jumpAnswer2: 'Ja, ich halte die XXCONCLUSIONXX für richtig, aber sie wird nicht von der XXPREMISEXX unterstützt.',
    _.jumpAnswer3: 'Nein, ich halte die XXCONCLUSIONXX für falsch.',
    _.justLookDontTouch: 'Nur anschauen, nichts anfassen!', _.keyword: 'Schlüsselwort',
    _.keywordStart: 'Start', _.keywordChooseActionForStatement: 'Einstellung zu',
    _.keywordGetPremisesForStatement: 'Prämissen von', _.keywordMoreAboutArgument: 'Mehr über',
    _.keywordReplyForPremisegroup: 'Antwort auf das Argument',
    _.keywordReplyForResponseOfConfrontation: 'Begründung von',
    _.keywordReplyForArgument: 'Konfrontation', _.keepSetting: 'Entscheidung merken',
    _.holds: 'ist richtig', _.holdsInColor: 'ist <span class=\'text-success\'>richtig</span>',
    _.hideAllUsers: 'Verstecke alle Benutzer', _.hideAllAttacks: 'Verstecke alle Angriffe',
    _.letMeExplain: 'Lass\' es mich so erklären', _.levenshteinDistance: 'Levenshtein-Distanz',
    _.languageCouldNotBeSwitched: 'Leider konnte die Sprache nicht gewechselt werden',
    _.last_action: 'Letzte Aktion', _.last_login: 'Letzte Anmeldung', _.login: 'Login',
    _.logfile: 'Logdatei für', _.letsGo: 'Klicken Sie hier um direkt zu starten!',
    _.letsGoBack: 'Ab geht\'s zurück!', _.letsGoHome: 'Ab zur Startseite!',
    _.langNotFound: 'Sprache nicht gefunden', _.more: 'Mehr', _.medium: 'mittel',
    _.minLength: 'Mindestlänge', _.myArgument: 'mein Argument',
    _.newNotification: 'Sie haben eine neue Benachrichtigung.',
    _.newMention: 'Sie wurden in einem Beitrag erwähnt.',
    _.newPremisesRadioButtonText: 'Nichts von all dem. Ich habe neue Gründe!',
    _.newPremisesRadioButtonTextAsFirstOne: 'Ja, ich möchte neue Gründe angeben!',
    _.newStatementsRadioButtonTextAsFirstOne: 'Ja, ich möchte neue Aussagen angeben!',
    _.newPremiseRadioButtonText: 'Nichts von all dem. Ich möchte einen neuen Grund angeben!',
    _.newPremiseRadioButtonTextAsFirstOne: 'Ja, ich möchte einen neuen Grunde angeben!',
    _.newStatementRadioButtonTextAsFirstOne: 'Ja, ich möchte eine neue Aussage angeben!',
    _.newConclusionRadioButtonText: 'Nichts von all dem. Ich habe eine andere Idee!',
    _.newsAboutDbas: 'Nachrichten über D-BAS', _.next: 'Nächster Eintrag',
    _.nickname: 'Spitzname', _.noOtherAttack: 'Das System hat kein weiteres Gegenargument',
    _.noIslandView: 'Daten für die Island View konnten nicht geladen werden. Tschuldigung!',
    _.noCorrections: 'Keinte Korreturen für die aktuelle Aussage.',
    _.noDecisionDone: 'Es liegt keine Entscheidung vor.',
    _.noCorrectionsSet: 'Korrektur wurde nicht gespeichert, da der Benutzer unbekannt ist. Sind Sie angemeldet?',
    _.notInsertedErrorBecauseEmpty: 'Ihre Idee wurde nicht gespeichert, da das Feld leer oder der Inhalt zu kurz ist.',
    _.notInsertedErrorBecauseDuplicate: 'Ihre Idee wurde nicht gespeichert, da Ihre Idee ein Duplikat ist.',
    _.notInsertedErrorBecauseUnknown: 'Ihre Idee wurde aufgrund eines unbekannten Fehlers nicht gespeichert.',
    _.notInsertedErrorBecauseInternal: 'Ihre Idee wurde aufgrund eines internen Fehlers nicht gespeichert.',
    _.noEntries: 'Keine Einträge vorhanden', _.noTrackedData: 'Keine Daten wurden gespeichert.',
    _.number: 'Nr', _.note: 'Hinweis', _.now: 'Jetzt', _.no_entry: 'Kein Eintrag',
    _.no_arguments: 'Keine Argumente für diese Meinung',
    _.noRights: 'Sie haben nicht genügend Rechte!', _.notLoggedIn: 'Sie sind nicht angemeldet!',
    _.on: 'An', _.off: 'Aus', _.opinion: 'die Meinung',
    _.onlyOneItem: 'Sofern Sie eine neue Aussage hinzufügen möchten, klicken Sie bitte hier um sich anzumelden.',
    _.onlyOneItemWithLink: 'Sofern Sie eine neue Aussage hinzufügen möchten, klicken Sie bitte <a data-href="login" data-toggle="modal" data-target="#popup-login" title="Login">hier</a> um sich anzumelden.',
    _.unfortunatelyOnlyOneItem: 'Leider gibt es nur eine Auswahl. Sofern Sie eine neue Aussage hinzufügen möchten, klicken Sie bitte <a data-href="login" data-toggle="modal" data-target="#popup-login" title="Login">hier</a> m sich anzumelden.',
    _.otherParticipantsConvincedYouThat: 'Andere Teilnehmer haben Sie überzeuge, dass',
    _.otherParticipantsThinkThat: 'Andere Teilnehmer denken, dass',
    _.otherParticipantsAgreeThat: 'Andere Teilnehmer stimmen zu, dass',
    _.otherParticipantsDontHaveOpinion: 'Andere Teilnehmer haben keine Meinung, dazu dass',
    _.otherParticipantsDontHaveOpinionRegaringYourSelection: 'Andere Teilnehmer haben keine Meinung zu Ihrer Aussage',
    _.otherParticipantsDontHaveCounter: 'Andere Teilnehmer haben kein Gegenargument für ',
    _.otherParticipantsDontHaveCounterForThat: 'Andere Teilnehmer haben kein Gegenargument dafür',
    _.otherParticipantsDontHaveNewCounterForThat: 'Andere Teilnehmer haben kein neues Gegenargument dafür. Sie habe schon alle Gegenargumente gesehen.',
    _.otherParticipantsDontHaveArgument: 'Andere Teilnehmer haben kein Argument für ',
    _.otherParticipantsAcceptBut: 'Andere Teilnehmer akzeptieren Ihr Argument, aber',
    _.otherParticipantDisagreeThat: 'Andere Teilnehmer widersprechen, dass ',
    _.otherUsersClaimStrongerArgumentRejecting: 'Andere Teilnehmer haben eine stärkere Aussage zur Ablehnung davon, dass',
    _.otherUsersClaimStrongerArgumentAccepting: 'Andere Teilnehmer haben eine stärkere Aussage zur Annahme davon, dass',
    _.otherUsersHaveCounterArgument: 'Andere Teilnehmer haben das Gegenargument, dass',
    _.otherUsersSaidThat: 'Andere Teilnehmer haben gesagt, dass',
    _.opinionBarometer: 'Meinungsbarometer',
    _.pleaseAddYourSuggestion: 'Bitte geben Sie Ihren Vorschlag an!',
    _.previous: 'Vorheriger Eintrag', _.premiseGroup: 'Gruppe von Voraussetzung(en)',
    _.publicNickTitle: '(De-)Aktiviert Ihren richtigen Nickname auf Ihrer öffentlichen Seite',
    _.passwordSubmit: 'Passwort ändern',
    _.preferedLangTitle: 'Bevorzugte Sprache für alle Nachrichten/E-Mails',
    _.priv_access_opti_queue: 'Zugriff auf die Optimierungs-Queue',
    _.priv_access_del_queue: 'Zugriff auf die Löschantrags-Queue',
    _.priv_access_edit_queue: 'Zugriff auf die Editierungs-Queue',
    _.priv_history_queue: 'Zugriff auf alle Vergangenen Entscheidungen',
    _.publications: 'Veröffentlichungen', _.myPosition: 'meinen Standpunkt',
    _.theirPosition: 'deren Standpunkt', _.the_der: 'der', _.the_die: 'die',
    _.the_das: 'das', _.report: 'Melden', _.review: 'Prüfung',
    _.review_history: 'Vergangene Entscheidungen', _.review_ongoing: 'Aktuelle Entscheidungen',
    _.reason: 'Begründung', _.reportStatement: 'Aussage melden',
    _.reportArgument: 'Argument melden', _.remStatementRow: 'Entfernt diese Reihe.',
    _.registered: 'Registriert', _.right: 'Ja', _.rejecting: 'gegen',
    _.requestTrack: 'Track anfragen', _.refreshTrack: 'Track neuladen',
    _.requestHistory: 'History anfragen', _.refreshHistory: 'History neuladen',
    _.requestFailed: 'Anfrage fehlgeschlagen', _.restartDiscussion: 'Diskussion neustarten',
    _.restartDiscussionTitle: 'Diskussion neustarten',
    _.restartOnError: 'Bitte laden Sie die Seite erneut oder starten Sie die Diskussion neu, sofern der Fehler bleibt.',
    _.recipient: 'Empfänger', _.recipientNotFound: 'Empfänger konnte nicht gefunden werden.',
    _.reaction: 'Reaktionen', _.reactionFor: 'Reaktionen zu',
    _.rep_reason_first_argument_click: 'Sie haben ihr erstes Argument ausgewählt',
    _.rep_reason_first_confrontation: 'Sie haben ihre erste Konfrontation überlebt',
    _.rep_reason_first_position: 'Sie haben zum ersten mal eine Position eingeben',
    _.rep_reason_first_justification: 'Sie haben zum ersten mal eine Begründung eingeben',
    _.rep_reason_first_new_argument: 'Sie haben zum ersten mal ein Argument eingeben',
    _.rep_reason_new_statement: 'Für jedes weitere Argument, dass Sie eingeben haben',
    _.rep_reason_success_flag: 'Sie haben zum ersten Mal ein Argument markieren',
    _.rep_reason_success_edit: 'Sie haben zum ersten Mal eine Editierung vornehmen',
    _.rep_reason_bad_flag: 'Sie haben die Melde-Funktion missbrauchen',
    _.rep_reason_bad_edit: 'Sie haben einen schlechten Editierungsvorschlag gemacht',
    _.questionTitle: 'Erhalten Sie mehr Informationen über die Aussage!',
    _.saveMyStatement: 'Aussage speichern!', _.selectStatement: 'Bitte Wählen Sie eine Aussage!',
    _.showAllUsers: 'Zeig\' alle Benutzer', _.showAllArguments: 'Zeig\' alle Argumente',
    _.showAllArgumentsTitle: 'Zeigt alle Argumente', _.showAllUsersTitle: 'Zeige alle Nutzer',
    _.strength: 'Stärke', _.strong: 'stark',
    _.strongerStatementForAccepting1: 'aber Sie haben eine stärkere Aussage zur ',
    _.strongerStatementForAccepting2: 'Annahme', _.strongerStatementForAccepting3: 'davon, dass',
    _.strongerStatementForRecjecting1: 'aber Sie haben eine stärkere Aussage zur ',
    _.strongerStatementForRecjecting2: 'Ablehnung',
    _.strongerStatementForRecjecting3: 'davon, dass',
    _.soYouEnteredMultipleReasons: 'Sie haben mehrere Gründe eingegeben',
    _.soYourOpinionIsThat: 'Ihre Meinung ist, dass',
    _.soYouWantToArgueAgainst: 'Sie möchten ein Gegenargument bringen für',
    _.soThatOtherParticipantsDontHaveOpinionRegardingYourOpinion: 'sodass andere Teilnehmer haben keine Meinung bezüglich ihrer Eingabe',
    _.shortenedBy: 'welche gekürzt wurde mit', _.shareUrl: 'Link teilen',
    _.showMeAnotherArgument: 'Zeige mir ein weiteres Argument',
    _.switchDiscussion: 'Diskussionsthema ändern',
    _.switchDiscussionTitle: 'Diskussionsthema ändern',
    _.switchDiscussionText1: 'Wenn Sie akzeptieren, wird das Diskussionsthema gewechselt zu',
    _.switchDiscussionText2: 'und die Diskussion neugestartet.',
    _.switchLanguage: 'Sprache ändern', _.supportPosition: 'Position unterstützen',
    _.supportsNot: 'unterstützt nicht', _.isupport: 'ich halte', _.statement: 'Aussage',
    _.statementIsAbout: 'Die Aussage ist die, dass',
    _.statementAdded: 'Aussage wurde hinzugefügt', _.argumentAdded: 'Argument wurde hinzugefügt',
    _.statementAddedMessageContent: 'Hey, jemand hat seine Meinung zu Deiner Aussage hinzugefügt!',
    _.argumentAddedMessageContent: 'Hey, jemand hat sein Argument zu Deiner Aussage hinzugefügt!',
    _.statementIndex: 'Aussagen Index - Letzte 30 Tage',
    _.statementIndexInfo: 'Anzahl an hinzugefügten Aussagen',
    _.sureThat: 'Ich bin sehr sicher, dass ', _.surname: 'Nachname',
    _.myStatement: 'meine Aussage', _.showMeAnArgumentFor: 'Zeig\' mir ein Argument für',
    _.textAreaReasonHintText: 'Bitte nutzen Sie ein Feld für jeden Grund. Schreiben Sie kurz und prägnant!',
    _.theCounterArgument: 'dem Gegenargument', _.therefore: 'Daher',
    _.thinkWeShould: 'Ich denke, wir sollten ', _.thisConfrontationIs: 'Dieser Angriff ist ein',
    _.textChange: 'Eine Ihrer Aussagen wurde editiert.', _.track: 'Spur', _.this: 'Diese',
    _.textversionChangedTopic: 'Aussage wurde geändert',
    _.textversionChangedContent: 'Ihr Text wurde geändert von', _.to: 'zu',
    _.topicString: 'Thema', _.text: 'Text', _.theySay: 'Sie sagen, dass',
    _.theyThink: 'Sie denken, dass', _.thisIsACopyOfMail: 'Dies ist eine Kopie Ihrer Mail',
    _.theirArgument: 'deren Argument', _.thisArgument: 'das Argument',
    _.thxForFlagText: 'Danke für Ihre Meldung, wir kümmern uns drum!',
    _.veryweak: 'sehr schwach',
    _.wantToStateNewPosition: 'Um eine neue Aussage hinzuzufügen, klicken Sie bitte hier um sich anzumelden.',
    _.weak: 'schwach', _.where: 'Wo', _.wrong: 'Nein',
    _.wouldYourShareArgument: 'Können Sie einen Grund angeben?',
    _.wrongURL: 'Ihre URL scheint falsch zu sein.',
    _.whatDoYouThinkAbout: 'Was halten Sie davon, dass',
    _.whatDoYouThinkOf: 'Was halten Sie von',
    _.whatDoYouThinkAboutThat: 'Was denken Sie darüber',
    _.whatIsYourIdea: 'Ich denke / meine, dass ...',
    _.whatIsYourMostImportantReasonFor: 'Was ist Ihr wichtigster Grund für die Aussage',
    _.whatIsYourMostImportantReasonWhyFor: 'Was ist Ihr wichtigster Grund dafür, dass ',
    _.whatIsYourMostImportantReasonWhyAgainst: 'Was ist Ihr wichtigster Grund dagegen, dass ',
    _.whatIsYourMostImportantReasonWhyForInColor: 'Was ist Ihr wichtigster Grund <span class=\'text-success\'>dafür</span>, dass ',
    _.whatIsYourMostImportantReasonWhyAgainstInColor: 'Was ist Ihr wichtigster Grund <span class=\'text-danger\'>dagegen</span>, dass ',
    _.whyDoYouThinkThat: 'Wieso denken Sie, dass',
    _.whyAreYouDisagreeingWith: 'Warum sind sie dagegenen, dass',
    _.whyAreYouAgreeingWith: 'Warum sind sie dafür, dass',
    _.whyAreYouDisagreeingWithInColor: 'Warum sind sie <span class=\'text-danger\'>dagegenen</span>, dass',
    _.whyAreYouAgreeingWithInColor: 'Warum sind sie <span class=\'text-success\'>dafür</span>, dass',
    _.whyAreYouDisagreeingWithThat: 'Warum sind Sie anderer Meinung?',
    _.youMadeA: 'Sie machten ein/e', _.youMadeAn: 'Sie machten ein/e',
    _.relation_undermine: 'ist ein Gegenargument für',
    _.relation_support: 'ist ein Argument für',
    _.relation_undercut: 'ist ein Gegenargument für',
    _.relation_overbid: 'ist ein Argument für',
    _.relation_rebut: 'ist ein Gegenargument für',
    _.uid: 'ID',
    _.unfortunatelyNoMoreArgument: 'Leider gibt es keine weiteren Argumente für',
    _.userPasswordNotMatch: 'Benutzername und/oder Passwort stimmen nicht überein',
    _.userOptions: 'Benutzeroptionen',
    _.userNotFound: 'Benutzer konnte nicht gefunden werden',
    _.userIsNotAuthorOfStatement: 'Sie sind nicht Autor der Aussage',
    _.userIsNotAuthorOfArgument: 'Sie sind nicht Autor des Arguments',
    _.voteCountTextFirst: 'Sie sind der/die Erste mit dieser Meinung',
    _.voteCountTextMayBeFirst: 'Sie wären der/die Erste mit dieser Meinung',
    _.voteCountTextOneOther: 'Ein/e Andere/r mit dieser Meinung',
    _.voteCountTextMore: 'weitere Teilnehmer/innen mit dieser Meinung',
    _.visitDeleteQueue: 'Schauen Sie in die Queue für Löschanträge.',
    _.visitDeleteQueueLimitation: 'Sie brauchen mindestens XX Punkte, um sich die Löschanträge anzuschauen.',
    _.visitOptimizationQueue: 'Schauen Sie in die Queue für Optimierungen.',
    _.visitOptimizationQueueLimitation: 'Sie brauchen mindestens XX Punkte, um sich die Optimierungen anzuschauen.',
    _.visitEditQueue: 'Schauen Sie in die Queue für Änderungen.',
    _.visitEditQueueLimitation: 'Sie brauchen mindestens XX Punkte, um sich die Änderungen anzuschauen.',
    _.visitHistoryQueue: 'Schauen Sie sich alle vergangenen Entscheidungen an.',
    _.visitHistoryQueueLimitation: 'Sie brauchen mindestens XX Punkte, um in die Vergangenheit zu reisen.',
    _.visitOngoingQueue: 'Schauen Sie sich die aktuell laufenden Entscheidungen an.',
    _.welcome: 'Willkommen',
    _.welcomeMessage: 'Willkommen im neuen dialog-basierten Argumentations-System.<br>Wir wünschen viel Spaß beim Diskutieren!',
    _.youAreInterestedIn: 'Sie interessieren sich für',
    _.youAgreeWith: 'Ich bin der Meinung, dass',
    _.youDisagreeWith: 'Ich widerspreche, dass',
    _.youSaidThat: 'Sie haben gesagt, dass',
    _.youUsedThisEarlier: 'Sie haben diese Aussage schon benutzt.',
    _.youRejectedThisEarlier: 'Sie haben diese Aussage schon abgelehnt.',
    _.youHaveMuchStrongerArgumentForAccepting: 'Sie haben eine viel stärker Begründung für',
    _.youHaveMuchStrongerArgumentForRejecting: 'Sie haben eine viel stärker Ablehnung für',
    # _.insertDontCare': Es ist mir egal. Nimm\' meine Aussage wie sie ist!'
}
