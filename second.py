import requests
from bs4 import BeautifulSoup
source="""
<!--<!DOCTYPE html>-->
<html lang="en">
<head>

<!--<meta charset="utf-8" content="utf-8">-->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#2299c5">

<title>Synonyms - Verbal Ability Questions and Answers</title>
<meta name="keywords" content="synonyms, section, 1, verbal, ability, english, aptitude, grammar, questions, answers, explanation, solutions, examples, interview, entrance, exam, online, test, quiz, pdf, download, freshers, ebooks" />
<meta name="description" content="This is the verbal ability questions and answers section on &quot;Synonyms&quot; with explanation for various interview, competitive examination and entrance test. Solved examples with detailed answer description, explanation are given and it would be easy to understand." />
<link href="/_files/css/css-res-min-1-15.css" type="text/css" rel="stylesheet" media="screen" />
<script src="/_files/js/js-res-10.js" type="text/javascript"></script>
<link href="/favicon.ico" type="image/x-icon" rel="shortcut icon" />
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({
          google_ad_client: "ca-pub-0191447310372013",
          enable_page_level_ads: true
     });
</script>
</head>

<body>

<div class="whole-page">

     <!--[if IE]><div class="inner-page-ie"><![endif]-->
     <div class="inner-page">
        
        <div>
        
        <div class="logo"><a href="/"><img class="img-site-logo" src="/_files/images/website/logo.gif" title="IndiaBIX Home Page" alt="IndiaBIX.Com" /></a></div>
        <div class="search">
            <div class="search-holder">
                <form  method="get" name="searchform" action="https://www.google.co.in/search" target="_blank" class="mx-dummy"> 
                <input type="hidden" name="sitesearch" value="www.indiabix.com" />
                <div class="search-button" onclick="document.forms['searchform'].submit();" alt="Search">&nbsp;</div>
                <input name="as_q" id="skr" class="search-box" type="text" placeholder="Search..." />
                </form>
            </div>
        </div><input id="hdnTitleID" type="hidden" value="3" />
        <div class="menu">
            <a href="#" onclick="$('#divSubMenu').slideToggle()"><img src="/_files/images/website/menu.png" alt="Menu" title="View all menu items." /></a>
            <a class="hide-1" href="/">Home</a>
            <a href="/aptitude/questions-and-answers/">Aptitude</a>
            <a class="hide-1 hide-2" href="/logical-reasoning/questions-and-answers/" title="Logical Reasoning">Logical</a>
            <a class="hide-1 hide-2" href="/verbal-ability/questions-and-answers/" title="Verbal Ability">Verbal</a>
            <a class="show-1 show-2" href="/current-affairs/questions-and-answers/" title="Current Affairs Questions and Answers">CA</a>
            <a class="hide-1 hide-2" href="/current-affairs/questions-and-answers/">Current Affairs</a>
            <a href="/general-knowledge/questions-and-answers/" title="General Knowldege Questions and Answers">GK</a>
            <a class="hide-1 hide-2" href="/engineering/">Engineering</a>
            <a href="/interview/">Interview</a>
            <a href="/online-test/categories/" title="Online Tests"><span class="hide-1">Online </span>Tests</a>
            <a class="hide-1 hide-2" href="/puzzles/number-puzzles/">Puzzles</a>
            <!-- a class="hide-1 hide-2" href="http://www.meritanswers.com/questions/ask/" title="Ask a question at MeritAnswers.com!">Ask Now !</a --> 
        </div><div id="divSubMenu" class="div-sub-menu" style="display:none">
            
            <h3>Quantitative Aptitude</h3>
            <div>
                <a href="/aptitude/questions-and-answers/">Arithmetic Aptitude</a>
                <a href="/data-interpretation/questions-and-answers/">Data Interpretation</a>
            </div>
            
            <h3>Verbal and Reasoning</h3>
            <div>
                <a href="/verbal-ability/questions-and-answers/">Verbal Ability</a>
                <a href="/logical-reasoning/questions-and-answers/">Logical Reasoning</a>
                <a href="/verbal-reasoning/questions-and-answers/">Verbal Reasoning</a>
                <a href="/non-verbal-reasoning/questions-and-answers/">Nonverbal Reasoning</a>
            </div>
            
           <h3>Current Affairs &amp; GK</h3>
            <div>
                <a href="/current-affairs/questions-and-answers/">Current Affairs</a>
                <a href="/general-knowledge/questions-and-answers/" title="General Knowledge Questions and Answers">General Knowledge</a>
            </div>
            
            <h3>Interview</h3>
            <div>
                <a href="/hr-interview/questions-and-answers/">HR Interview</a>
                <a href="/group-discussion/topics-with-answers/">Group Discussion</a>
                <a href="/placement-papers/companies/">Placement Papers</a>
                <a href="/technical/interview-questions-and-answers/">Technical Interview</a>
            </div>
            
            <h3>Engineering</h3>
            <div>
                <a href="/mechanical-engineering/questions-and-answers/" title="Mechanical Engineering Questions and Answers">Mechanical Engineering</a>
                <a href="/civil-engineering/questions-and-answers/" title="Civil Engineering Questions and Answers">Civil Engineering</a>
                <a href="/electronics-and-communication-engineering/questions-and-answers/" title="Electronics and Communication Engineering Questions and Answers">ECE</a>
                <a href="/electrical-engineering/questions-and-answers/" title="Electrical Engineering Questions and Answers">EEE</a>
                <a href="/computer-science/questions-and-answers/" title="Computer Science Questions and Answers">CSE</a>
                <a href="/engineering/" title="Engineering Questions and Answers">Read more...</a>
            </div>
            
            <h3>Technical</h3>
            <div>
                <a href="/c-programming/questions-and-answers/" title="C Programming Questions and Answers">C Programming</a>
                <a href="/cpp-programming/questions-and-answers/" title="C++ Programming Questions and Answers">C++</a>
                <a href="/c-sharp-programming/questions-and-answers/" title="C# Programming Questions and Answers">C#</a>
                <a href="/java-programming/questions-and-answers/" title="Java Programming Questions and Answers">Java</a>
                <a href="/database/questions-and-answers/" title="Database Questions and Answers">Database</a>
                <a href="/networking/questions-and-answers/" title="Networking Questions and Answers">Networking</a>
            </div>
            
            <h3>Medical Science</h3>
            <div>
                <a href="/microbiology/questions-and-answers/">Microbiology</a>
                <a href="/biochemistry/questions-and-answers/">Biochemistry</a> 
                <a href="/biotechnology/questions-and-answers/">Biotechnology</a> 
                <a href="/biochemical-engineering/questions-and-answers/">Biochemical Engineering</a>
            </div>
            
            <h3>Others</h3>
            <div>
                <a href="/online-test/categories/" >Online Tests</a>
                <a href="/puzzles/number-puzzles/" title="Puzzles Quiz">Puzzles Quiz</a>
                <a href="/puzzles/sudoku/" >Sudoku</a>
                <!-- a href="http://www.meritanswers.com/questions/ask/" title="Ask a question at MeritAnswers.Com">Ask your question?</a -->
                <a href="#" onclick="$('#divSubMenu').slideToggle()" class="ib-red">Close Menu</a>
            </div>
            
        </div>
        </div>    
        
        <div class="pagehead"><h1>Verbal Ability - Synonyms</h1></div>
        <div id="divIntroduction" class="mx-none">
            <h2>Why Verbal Ability Synonyms?</h2>
            <p>In this section you can learn and practice Verbal Ability Questions based on "Synonyms" and improve your skills in order to face the interview, competitive examination and various entrance test (CAT, GATE, GRE, MAT, Bank Exam, Railway Exam etc.) with full confidence. </p>
            <h2>Where can I get Verbal Ability Synonyms questions and answers with explanation?</h2>
            <p>IndiaBIX provides you lots of fully solved Verbal Ability (Synonyms) questions and answers with Explanation. Solved examples with detailed answer description, explanation are given and it would be easy to understand. All students, freshers can download Verbal Ability Synonyms quiz questions with answers as PDF files and eBooks.</p>
            <h2>Where can I get Verbal Ability Synonyms Interview Questions and Answers (objective type, multiple choice)?</h2> 
            <p>Here you can find objective type Verbal Ability Synonyms questions and answers for interview and entrance examination. Multiple choice and true or false type questions are also provided.</p>
             <h2>How to solve Verbal Ability Synonyms problems?</h2>
            <p>You can easily solve all kind of Verbal Ability questions based on Synonyms by practicing the objective type exercises given below, also get shortcut methods to solve Verbal Ability Synonyms problems.</p>
            </div>
            <input type="hidden" value="2" id="idAgentType">
        
        <div class="breadcrumb">
             <a href="/">Home</a> &raquo; <a href="/verbal-ability/questions-and-answers/">Verbal Ability</a> &raquo; <a href="/verbal-ability/synonyms/">Synonyms</a> &raquo; Section 1
        </div>
        
        <div class="main-left">
            
<div class="div-ad-site-top"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Bixer Top -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0191447310372013"
     data-ad-slot="3107019861"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script>
</div><div class="div-top-left"><h3 class="overview"><span class="ib-gray">Exercise :: </span>Synonyms - Section 1</h3><ul class="ul-top-left"><li class="current">Synonyms - Section 1</li><li><a href="/verbal-ability/synonyms/004001">Synonyms - Section 2</a></li></ul></div> 

<div class="bix-div-direction" id="divDirection">
                        <div class="title-bar"><a id="lnkDirectionShowHide" href="javascript: void 0;" onclick="$('#divDirectionText').slideToggle('slow');"><span class="ib-green">Directions to Solve</span></a></div> 
                        <div class="div-spacer" id="divDirectionText">
                            <p>In the following the questions choose the word which best expresses the meaning of the given word.</p>
                        </div>
                    </div>


            <div class="bix-div-container">
            <table class="bix-tbl-container" cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="bix-td-qno"  rowspan="2" valign="top" align="left">1.&nbsp;</td>
                <td class="bix-td-qtxt" valign="top"><p>CORPULENT</p></td>
            </tr>
            <tr>
                <td class="bix-td-miscell" valign="top"><table class="bix-tbl-options" id="tblOption_584" border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_A_584"><a id="lnkOptionLink_A_584" href="javascript: void 0;">A.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_A_584">Lean</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_B_584"><a id="lnkOptionLink_B_584" href="javascript: void 0;">B.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_B_584">Gaunt</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_C_584"><a id="lnkOptionLink_C_584" href="javascript: void 0;">C.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_C_584">Emaciated</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_D_584"><a id="lnkOptionLink_D_584" href="javascript: void 0;">D.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_D_584">Obese</td></tr></table><input type="hidden" class="jq-hdnakq" id="hdnAnswer_584" value="D" />
                    <div class="bix-div-answer mx-none" id="divAnswer_584">
                        <p><span class="mx-green mx-bold">Answer:</span> Option <span class="jq-hdnakqb mx-bold">D</span></p> 
                        <p><span class="mx-green mx-bold">Explanation:</span></p> 
                        <div class="bix-ans-description"> No answer description available for this question. <a href="discussion-584">Let us discuss</a>. </div>
                    </div>
                    
                    <div class="bix-div-workspace mx-none" id="divWorkspace_584">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divWorkspace_584').slideToggle('slow');">Workspace</a></div>
                        <textarea rows="10" cols="65" class="mx-w-100p"></textarea>
                    </div>
                    
                    <div class="bix-div-report mx-none" id="divReport_584">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divReport_584').slideToggle('slow');">Report errors</a></div> 
                            <textarea class="mx-w-100p mx-pad-10 mx-marb-2" onchange="javascript:if(this.name == '')this.name='txtReport_584';" name="" id="txtReport_584" rows="8" cols="65">...




Name : 
Email: </textarea> 
                            <input id="btnReport_584" onclick="SendBixReport('1', '584')" type="button" value="Send Report" />
                        </div>
                    </div>
                    <div class="bix-div-toolbar" id="divToolBar_584">
    <a class="answer"      href="javascript: void 0;"  onclick="$('#divAnswer_584').slideToggle('slow')" >View Answer</a>
    <a class="discuss"     href="/verbal-ability/synonyms/discussion-584">Discuss<span class="hide-1" > in Forum</span></a>
    <a class="workspace"   href="javascript: void 0;"  onclick="$('#divWorkspace_584').slideToggle('slow')" ><span class="hide-1">Workspace</span></a>
    <a class="report"      href="javascript: void 0;"  onclick="$('#divReport_584').slideToggle('slow')" ><span class="hide-1">Report</span></a>
</div>
                    
                </td>
            </tr>
            </table>
            </div><hr />
            <div class="bix-div-container">
            <table class="bix-tbl-container" cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="bix-td-qno"  rowspan="2" valign="top" align="left">2.&nbsp;</td>
                <td class="bix-td-qtxt" valign="top"><p>BRIEF</p></td>
            </tr>
            <tr>
                <td class="bix-td-miscell" valign="top"><table class="bix-tbl-options" id="tblOption_549" border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_A_549"><a id="lnkOptionLink_A_549" href="javascript: void 0;">A.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_A_549">Limited</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_B_549"><a id="lnkOptionLink_B_549" href="javascript: void 0;">B.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_B_549">Small</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_C_549"><a id="lnkOptionLink_C_549" href="javascript: void 0;">C.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_C_549">Little</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_D_549"><a id="lnkOptionLink_D_549" href="javascript: void 0;">D.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_D_549">Short</td></tr></table><input type="hidden" class="jq-hdnakq" id="hdnAnswer_549" value="D" />
                    <div class="bix-div-answer mx-none" id="divAnswer_549">
                        <p><span class="mx-green mx-bold">Answer:</span> Option <span class="jq-hdnakqb mx-bold">D</span></p> 
                        <p><span class="mx-green mx-bold">Explanation:</span></p> 
                        <div class="bix-ans-description"> No answer description available for this question. <a href="discussion-549">Let us discuss</a>. </div>
                    </div>
                    
                    <div class="bix-div-workspace mx-none" id="divWorkspace_549">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divWorkspace_549').slideToggle('slow');">Workspace</a></div>
                        <textarea rows="10" cols="65" class="mx-w-100p"></textarea>
                    </div>
                    
                    <div class="bix-div-report mx-none" id="divReport_549">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divReport_549').slideToggle('slow');">Report errors</a></div> 
                            <textarea class="mx-w-100p mx-pad-10 mx-marb-2" onchange="javascript:if(this.name == '')this.name='txtReport_549';" name="" id="txtReport_549" rows="8" cols="65">...




Name : 
Email: </textarea> 
                            <input id="btnReport_549" onclick="SendBixReport('2', '549')" type="button" value="Send Report" />
                        </div>
                    </div>
                    <div class="bix-div-toolbar" id="divToolBar_549">
    <a class="answer"      href="javascript: void 0;"  onclick="$('#divAnswer_549').slideToggle('slow')" >View Answer</a>
    <a class="discuss"     href="/verbal-ability/synonyms/discussion-549">Discuss<span class="hide-1" > in Forum</span></a>
    <a class="workspace"   href="javascript: void 0;"  onclick="$('#divWorkspace_549').slideToggle('slow')" ><span class="hide-1">Workspace</span></a>
    <a class="report"      href="javascript: void 0;"  onclick="$('#divReport_549').slideToggle('slow')" ><span class="hide-1">Report</span></a>
</div>
                    
                </td>
            </tr>
            </table>
            </div><hr />
            <div class="bix-div-container">
            <table class="bix-tbl-container" cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="bix-td-qno"  rowspan="2" valign="top" align="left">3.&nbsp;</td>
                <td class="bix-td-qtxt" valign="top"><p>EMBEZZLE</p></td>
            </tr>
            <tr>
                <td class="bix-td-miscell" valign="top"><table class="bix-tbl-options" id="tblOption_583" border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_A_583"><a id="lnkOptionLink_A_583" href="javascript: void 0;">A.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_A_583">Misappropriate</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_B_583"><a id="lnkOptionLink_B_583" href="javascript: void 0;">B.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_B_583">Balance</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_C_583"><a id="lnkOptionLink_C_583" href="javascript: void 0;">C.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_C_583">Remunerate</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_D_583"><a id="lnkOptionLink_D_583" href="javascript: void 0;">D.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_D_583">Clear</td></tr></table><input type="hidden" class="jq-hdnakq" id="hdnAnswer_583" value="A" />
                    <div class="bix-div-answer mx-none" id="divAnswer_583">
                        <p><span class="mx-green mx-bold">Answer:</span> Option <span class="jq-hdnakqb mx-bold">A</span></p> 
                        <p><span class="mx-green mx-bold">Explanation:</span></p> 
                        <div class="bix-ans-description"> Main Entry: embezzle<br><br>

Part of Speech: verb<br><br>

Definition: steal money, often from employer<br><br>

Synonyms: abstract, defalcate, filch, forge, loot, misapply, <b class="ib-gray">misappropriate</b>, misuse, peculate, pilfer, purloin, put hand in cookie jar, put hand in till, skim, thieve<br><br>

Antonyms:	 compensate, give, pay, reimburse, return </div>
                    </div>
                    
                    <div class="bix-div-workspace mx-none" id="divWorkspace_583">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divWorkspace_583').slideToggle('slow');">Workspace</a></div>
                        <textarea rows="10" cols="65" class="mx-w-100p"></textarea>
                    </div>
                    
                    <div class="bix-div-report mx-none" id="divReport_583">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divReport_583').slideToggle('slow');">Report errors</a></div> 
                            <textarea class="mx-w-100p mx-pad-10 mx-marb-2" onchange="javascript:if(this.name == '')this.name='txtReport_583';" name="" id="txtReport_583" rows="8" cols="65">...




Name : 
Email: </textarea> 
                            <input id="btnReport_583" onclick="SendBixReport('3', '583')" type="button" value="Send Report" />
                        </div>
                    </div>
                    <div class="bix-div-toolbar" id="divToolBar_583">
    <a class="answer"      href="javascript: void 0;"  onclick="$('#divAnswer_583').slideToggle('slow')" >View Answer</a>
    <a class="discuss"     href="/verbal-ability/synonyms/discussion-583">Discuss<span class="hide-1" > in Forum</span></a>
    <a class="workspace"   href="javascript: void 0;"  onclick="$('#divWorkspace_583').slideToggle('slow')" ><span class="hide-1">Workspace</span></a>
    <a class="report"      href="javascript: void 0;"  onclick="$('#divReport_583').slideToggle('slow')" ><span class="hide-1">Report</span></a>
</div>
                    
                </td>
            </tr>
            </table>
            </div><hr />
            <div class="bix-div-container">
            <table class="bix-tbl-container" cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="bix-td-qno"  rowspan="2" valign="top" align="left">4.&nbsp;</td>
                <td class="bix-td-qtxt" valign="top"><p>VENT</p></td>
            </tr>
            <tr>
                <td class="bix-td-miscell" valign="top"><table class="bix-tbl-options" id="tblOption_601" border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_A_601"><a id="lnkOptionLink_A_601" href="javascript: void 0;">A.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_A_601">Opening</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_B_601"><a id="lnkOptionLink_B_601" href="javascript: void 0;">B.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_B_601">Stodge</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_C_601"><a id="lnkOptionLink_C_601" href="javascript: void 0;">C.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_C_601">End</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_D_601"><a id="lnkOptionLink_D_601" href="javascript: void 0;">D.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_D_601">Past tense of go</td></tr></table><input type="hidden" class="jq-hdnakq" id="hdnAnswer_601" value="A" />
                    <div class="bix-div-answer mx-none" id="divAnswer_601">
                        <p><span class="mx-green mx-bold">Answer:</span> Option <span class="jq-hdnakqb mx-bold">A</span></p> 
                        <p><span class="mx-green mx-bold">Explanation:</span></p> 
                        <div class="bix-ans-description"> No answer description available for this question. <a href="discussion-601">Let us discuss</a>. </div>
                    </div>
                    
                    <div class="bix-div-workspace mx-none" id="divWorkspace_601">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divWorkspace_601').slideToggle('slow');">Workspace</a></div>
                        <textarea rows="10" cols="65" class="mx-w-100p"></textarea>
                    </div>
                    
                    <div class="bix-div-report mx-none" id="divReport_601">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divReport_601').slideToggle('slow');">Report errors</a></div> 
                            <textarea class="mx-w-100p mx-pad-10 mx-marb-2" onchange="javascript:if(this.name == '')this.name='txtReport_601';" name="" id="txtReport_601" rows="8" cols="65">...




Name : 
Email: </textarea> 
                            <input id="btnReport_601" onclick="SendBixReport('4', '601')" type="button" value="Send Report" />
                        </div>
                    </div>
                    <div class="bix-div-toolbar" id="divToolBar_601">
    <a class="answer"      href="javascript: void 0;"  onclick="$('#divAnswer_601').slideToggle('slow')" >View Answer</a>
    <a class="discuss"     href="/verbal-ability/synonyms/discussion-601">Discuss<span class="hide-1" > in Forum</span></a>
    <a class="workspace"   href="javascript: void 0;"  onclick="$('#divWorkspace_601').slideToggle('slow')" ><span class="hide-1">Workspace</span></a>
    <a class="report"      href="javascript: void 0;"  onclick="$('#divReport_601').slideToggle('slow')" ><span class="hide-1">Report</span></a>
</div>
                    
                </td>
            </tr>
            </table>
            </div><hr />
            <div class="bix-div-container">
            <table class="bix-tbl-container" cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="bix-td-qno"  rowspan="2" valign="top" align="left">5.&nbsp;</td>
                <td class="bix-td-qtxt" valign="top"><p>AUGUST</p></td>
            </tr>
            <tr>
                <td class="bix-td-miscell" valign="top"><table class="bix-tbl-options" id="tblOption_585" border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_A_585"><a id="lnkOptionLink_A_585" href="javascript: void 0;">A.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_A_585">Common</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_B_585"><a id="lnkOptionLink_B_585" href="javascript: void 0;">B.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_B_585">Ridiculous</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_C_585"><a id="lnkOptionLink_C_585" href="javascript: void 0;">C.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_C_585">Dignified</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_D_585"><a id="lnkOptionLink_D_585" href="javascript: void 0;">D.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_D_585">Petty</td></tr></table><input type="hidden" class="jq-hdnakq" id="hdnAnswer_585" value="C" />
                    <div class="bix-div-answer mx-none" id="divAnswer_585">
                        <p><span class="mx-green mx-bold">Answer:</span> Option <span class="jq-hdnakqb mx-bold">C</span></p> 
                        <p><span class="mx-green mx-bold">Explanation:</span></p> 
                        <div class="bix-ans-description"> No answer description available for this question. <a href="discussion-585">Let us discuss</a>. </div>
                    </div>
                    
                    <div class="bix-div-workspace mx-none" id="divWorkspace_585">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divWorkspace_585').slideToggle('slow');">Workspace</a></div>
                        <textarea rows="10" cols="65" class="mx-w-100p"></textarea>
                    </div>
                    
                    <div class="bix-div-report mx-none" id="divReport_585">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divReport_585').slideToggle('slow');">Report errors</a></div> 
                            <textarea class="mx-w-100p mx-pad-10 mx-marb-2" onchange="javascript:if(this.name == '')this.name='txtReport_585';" name="" id="txtReport_585" rows="8" cols="65">...




Name : 
Email: </textarea> 
                            <input id="btnReport_585" onclick="SendBixReport('5', '585')" type="button" value="Send Report" />
                        </div>
                    </div>
                    <div class="bix-div-toolbar" id="divToolBar_585">
    <a class="answer"      href="javascript: void 0;"  onclick="$('#divAnswer_585').slideToggle('slow')" >View Answer</a>
    <a class="discuss"     href="/verbal-ability/synonyms/discussion-585">Discuss<span class="hide-1" > in Forum</span></a>
    <a class="workspace"   href="javascript: void 0;"  onclick="$('#divWorkspace_585').slideToggle('slow')" ><span class="hide-1">Workspace</span></a>
    <a class="report"      href="javascript: void 0;"  onclick="$('#divReport_585').slideToggle('slow')" ><span class="hide-1">Report</span></a>
</div>
                    
                </td>
            </tr>
            </table>
            </div><hr />
            <div class="bix-div-container">
            <table class="bix-tbl-container" cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="bix-td-qno"  rowspan="2" valign="top" align="left">6.&nbsp;</td>
                <td class="bix-td-qtxt" valign="top"><p>CANNY</p></td>
            </tr>
            <tr>
                <td class="bix-td-miscell" valign="top"><table class="bix-tbl-options" id="tblOption_538" border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_A_538"><a id="lnkOptionLink_A_538" href="javascript: void 0;">A.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_A_538">Obstinate</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_B_538"><a id="lnkOptionLink_B_538" href="javascript: void 0;">B.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_B_538">Handsome</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_C_538"><a id="lnkOptionLink_C_538" href="javascript: void 0;">C.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_C_538">Clever</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_D_538"><a id="lnkOptionLink_D_538" href="javascript: void 0;">D.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_D_538">Stout</td></tr></table><input type="hidden" class="jq-hdnakq" id="hdnAnswer_538" value="C" />
                    <div class="bix-div-answer mx-none" id="divAnswer_538">
                        <p><span class="mx-green mx-bold">Answer:</span> Option <span class="jq-hdnakqb mx-bold">C</span></p> 
                        <p><span class="mx-green mx-bold">Explanation:</span></p> 
                        <div class="bix-ans-description"> No answer description available for this question. <a href="discussion-538">Let us discuss</a>. </div>
                    </div>
                    
                    <div class="bix-div-workspace mx-none" id="divWorkspace_538">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divWorkspace_538').slideToggle('slow');">Workspace</a></div>
                        <textarea rows="10" cols="65" class="mx-w-100p"></textarea>
                    </div>
                    
                    <div class="bix-div-report mx-none" id="divReport_538">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divReport_538').slideToggle('slow');">Report errors</a></div> 
                            <textarea class="mx-w-100p mx-pad-10 mx-marb-2" onchange="javascript:if(this.name == '')this.name='txtReport_538';" name="" id="txtReport_538" rows="8" cols="65">...




Name : 
Email: </textarea> 
                            <input id="btnReport_538" onclick="SendBixReport('6', '538')" type="button" value="Send Report" />
                        </div>
                    </div>
                    <div class="bix-div-toolbar" id="divToolBar_538">
    <a class="answer"      href="javascript: void 0;"  onclick="$('#divAnswer_538').slideToggle('slow')" >View Answer</a>
    <a class="discuss"     href="/verbal-ability/synonyms/discussion-538">Discuss<span class="hide-1" > in Forum</span></a>
    <a class="workspace"   href="javascript: void 0;"  onclick="$('#divWorkspace_538').slideToggle('slow')" ><span class="hide-1">Workspace</span></a>
    <a class="report"      href="javascript: void 0;"  onclick="$('#divReport_538').slideToggle('slow')" ><span class="hide-1">Report</span></a>
</div>
                    
                </td>
            </tr>
            </table>
            </div><hr />
            <div class="bix-div-container">
            <table class="bix-tbl-container" cellspacing="0" cellpadding="0" border="0" width="100%">
            <tr>
                <td class="bix-td-qno"  rowspan="2" valign="top" align="left">7.&nbsp;</td>
                <td class="bix-td-qtxt" valign="top"><p>ALERT</p></td>
            </tr>
            <tr>
                <td class="bix-td-miscell" valign="top"><table class="bix-tbl-options" id="tblOption_591" border="0" cellpadding="0" cellspacing="0" width="100%"><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_A_591"><a id="lnkOptionLink_A_591" href="javascript: void 0;">A.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_A_591">Energetic</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_B_591"><a id="lnkOptionLink_B_591" href="javascript: void 0;">B.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_B_591">Observant</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_C_591"><a id="lnkOptionLink_C_591" href="javascript: void 0;">C.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_C_591">Intelligent</td></tr><tr><td class="bix-td-option" width="1%"  id="tdOptionNo_D_591"><a id="lnkOptionLink_D_591" href="javascript: void 0;">D.</a></td>
                 <td class="bix-td-option" width="99%" id="tdOptionDt_D_591">Watchful</td></tr></table><input type="hidden" class="jq-hdnakq" id="hdnAnswer_591" value="D" />
                    <div class="bix-div-answer mx-none" id="divAnswer_591">
                        <p><span class="mx-green mx-bold">Answer:</span> Option <span class="jq-hdnakqb mx-bold">D</span></p> 
                        <p><span class="mx-green mx-bold">Explanation:</span></p> 
                        <div class="bix-ans-description"> No answer description available for this question. <a href="discussion-591">Let us discuss</a>. </div>
                    </div>
                    
                    <div class="bix-div-workspace mx-none" id="divWorkspace_591">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divWorkspace_591').slideToggle('slow');">Workspace</a></div>
                        <textarea rows="10" cols="65" class="mx-w-100p"></textarea>
                    </div>
                    
                    <div class="bix-div-report mx-none" id="divReport_591">
                        <div class="title-bar"><a href="javascript: void 0;" onclick="$('#divReport_591').slideToggle('slow');">Report errors</a></div> 
                            <textarea class="mx-w-100p mx-pad-10 mx-marb-2" onchange="javascript:if(this.name == '')this.name='txtReport_591';" name="" id="txtReport_591" rows="8" cols="65">...




Name : 
Email: </textarea> 
                            <input id="btnReport_591" onclick="SendBixReport('7', '591')" type="button" value="Send Report" />
                        </div>
                    </div>
                    <div class="bix-div-toolbar" id="divToolBar_591">
    <a class="answer"      href="javascript: void 0;"  onclick="$('#divAnswer_591').slideToggle('slow')" >View Answer</a>
    <a class="discuss"     href="/verbal-ability/synonyms/discussion-591">Discuss<span class="hide-1" > in Forum</span></a>
    <a class="workspace"   href="javascript: void 0;"  onclick="$('#divWorkspace_591').slideToggle('slow')" ><span class="hide-1">Workspace</span></a>
    <a class="report"      href="javascript: void 0;"  onclick="$('#divReport_591').slideToggle('slow')" ><span class="hide-1">Report</span></a>
</div>
                    
                </td>
            </tr>
            </table>
            </div><hr /><div class="mx-pager-container"><p class="mx-pager mx-lpad-25"> <span class="mx-pager-current">1</span> <a href="/verbal-ability/synonyms/003002"><span class="mx-pager-no">2</span></a> <a href="/verbal-ability/synonyms/003003"><span class="mx-pager-no">3</span></a> <a href="/verbal-ability/synonyms/003004"><span class="mx-pager-no">4</span></a> <a href="/verbal-ability/synonyms/003005"><span class="mx-pager-no">5</span></a> <a href="/verbal-ability/synonyms/003006"><span class="mx-pager-no">6</span></a> <a href="/verbal-ability/synonyms/003007"><span class="mx-pager-no">7</span></a> <a href="/verbal-ability/synonyms/003008"><span class="mx-pager-no">8</span></a> <a href="/verbal-ability/synonyms/003009"><span class="mx-pager-no">9</span></a> <a href="/verbal-ability/synonyms/003010"><span class="mx-pager-no">10</span></a> <a href="/verbal-ability/synonyms/003011"><span class="mx-pager-no">11</span></a> <a href="/verbal-ability/synonyms/003012"><span class="mx-pager-no">12</span></a> <a href="/verbal-ability/synonyms/003013"><span class="mx-pager-no">13</span></a> <a href="/verbal-ability/synonyms/003014"><span class="mx-pager-no">14</span></a> <a href="/verbal-ability/synonyms/003015"><span class="mx-pager-no">15</span></a> <a href="/verbal-ability/synonyms/003002">Next&nbsp;&raquo;</a></p></div><hr /><div class="hide-1 div-ad-wrapper-bvf"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Bixer Bottom -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0191447310372013"
     data-ad-slot="6060486264"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div><div class="show-1 div-ad-wrapper-bvr"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Bixer Bottom -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0191447310372013"
     data-ad-slot="6060486264"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div><hr class="show-1" /><div class="div-ad-site-bottom"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<ins class="adsbygoogle"
     style="display:block"
     data-ad-format="autorelaxed"
     data-ad-client="ca-pub-0191447310372013"
     data-ad-slot="9227589860"></ins>
<script>
     (adsbygoogle = window.adsbygoogle || []).push({});
</script></div><hr /><div class="related-links"><h3 class="h3-read-more">Read more:</h3><ul><li><a href="/verbal-ability/synonyms/004001">Synonyms - Section 2</a></li></ul></div><input id="hdnAjaxImageCacheKey" type="hidden" value="abbcedabccbeeddcaadccaaddbaceabdcaedebcdba" />
 
 
        </div>
                    
        <div class="main-right" >
           <div class="div-right-inner"><div class="div-ad-site-blank">
            <h4><a href="/current-affairs/questions-and-answers/">Current Affairs 2019</a></h4>
            <a class="mx-bold" href="/interview/">Interview Questions and Answers</a>
            <!-- a class="mx-bold" href="https://play.google.com/store/apps/details?id=com.indiabix">Download: IndiaBIX Android App !</a//-->
            <!-- a class="mx-bold" target="_blank" href="http://www.meritanswers.com/questions/1-2">View Recent Questions</a //-->
        </div><div class="hide-1 hide-2 div-ad-site-right"><div class="div-ad-wrapper-rs"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Bixer Right -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0191447310372013"
     data-ad-slot="4583753066"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div><br /><div class="div-ad-wrapper-rs"><script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
<!-- Bixer Right -->
<ins class="adsbygoogle"
     style="display:block"
     data-ad-client="ca-pub-0191447310372013"
     data-ad-slot="4583753066"
     data-ad-format="auto"></ins>
<script>
(adsbygoogle = window.adsbygoogle || []).push({});
</script></div></div></div>
        </div>
        
        <div class="footer">
        <div class="inner-footer">
            <p class="mx-gray mx-fs-13 mx-lh-2">&copy; 2009 - 2019 by IndiaBIX&trade; Technologies. All Rights Reserved. | <a href="/about/copyright.php">Copyright</a> | <a href="/about/privacy-policy.php">Terms of Use &amp; Privacy Policy</a></p>
            <p class="mx-gray mx-fs-13 mx-lh-2">Contact us: <span class="mx-green mx-bold">info.india<span class="mx-none">- @ -</span>bix@gma<span class="mx-none">@</span>il.com</span></p>
            <!-- p class="mx-gray mx-fs-13 mx-lh-2"><script id="_waukkv">var _wau = _wau || []; _wau.push(["small", "4qnxqro1qj", "kkv"]);</script><script async src="//waust.at/s.js"></script></p //-->
         </div>
        </div>
        
    </div>
     <!--[if IE]></div><![endif]-->
     
</div>

<!-- Google Page Analysis Code -->
<script>
(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
ga('create', 'UA-11081049-2', 'auto');ga('send', 'pageview');
</script>
</body></html>"""


source = requests.get("")
soup = BeautifulSoup(source, 'html.parser')

print(soup.prettify())
soup.find_all('a')