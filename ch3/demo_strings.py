myCourse = "CS100 Scientific Computing"

#2.1 / What Python command will print the length of the variable myCourse?

print(len(myCourse)) # len() e.g. len(myCourse) == 26

#2.2 / What is the following command printing? print( myCourse[-9:-5])?

print(myCourse[-9:-5]) # Comp 

#2.3 / What is the following command printing? print( myCourse[17:21])?

print(myCourse[17:21]) # Comp 

#2.4 / What is the following command printing? print( myCourse[17] )?

print(myCourse[17]) # C 

#2.5 / What is the index of the first character 'S' in myCourse, and what command do you use to find it?

print(myCourse.index('S')) # 1, index() e.g. myCourse.index('S') will find the index of the first character 'S' in myCourse.

#2.6 / What is the result of typing print('100' in myCourse)?

print('100' in myCourse) # True 

#2.7 / What is the result of typing print('130' not in myCourse)?

print('130' not in myCourse) # True 

#2.8 / What is the result of typing print('wow'*5)?

print('wow'*5) # wowwowwowwowwow 

#2.9 / What is the result of typing print( ('.'*3 + 'y')*3 )?

print(('.'*3 + 'y')*3 ) # ...y...y...y

#3

print(myCourse+' Exam 1')

#4

print(myCourse.center(40))

#5

f = "fantastic"

#5.1
for i in range (len(f)):
    print(f[i])

#5.2    

print(f[-5:])

#5.3

print(f[-6:])
  
#6

s = input('Type something here: ') # <-- do not change this part
print(s) # Words or sentences that I wrote are printed.

#6.1

print(s[0:5])

#6.2

print(len(s))

#6.3
book = """
The Project Gutenberg eBook of The French Revolution 1789-1795
    
This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

Title: The French Revolution 1789-1795


Author: Bertha Meriton Cordery Gardiner

Release date: September 19, 2023 [eBook #71688]

Language: English

Original publication: London: Longmans, Green, and Co, 1921

Credits: The Online Distributed Proofreading Team at https://www.pgdp.net (This file was produced from images generously made available by The Internet Archive)


*** START OF THE PROJECT GUTENBERG EBOOK THE FRENCH REVOLUTION 1789-1795 ***





Transcriber’s Notes: Italic text is enclosed in _underscores_;
boldface text is enclosed in =equals signs=.

This ebook contains sidenotes. To distinguish them from regular text,
they are in diamond symbols: ♦sidenote text♦.

Other notes will be found near the end of this ebook.




                     HISTORICAL WORKS FOR SCHOOLS.


                       EPOCHS OF ANCIENT HISTORY.

                             EDITED BY THE
        Rev. Sir G. W. COX, Bart., M.A., and by C. SANKEY, M.A.


  =THE GRACCHI, MARIUS, AND SULLA.= By A. H. BEESLY, M.A. With 2 Maps.

  =THE EARLY ROMAN EMPIRE=, from the Assassination of Julius Cæsar to
    the Assassination of Domitian. By the Rev. W. WOLFE CAPES, M.A.
    With 2 Maps.

  =THE ROMAN EMPIRE OF THE SECOND CENTURY=, or the Age of the
    Antonines. By the Rev. W. WOLFE CAPES, M.A. With 2 Maps.

  =ROME TO ITS CAPTURE BY THE GAULS.= By WILHELM IHNE. With Map.

  =THE ROMAN TRIUMVIRATES.= By CHARLES MERIVALE, D.D., late Dean of
    Ely. With Map.

  =ROME AND CARTHAGE, the PUNIC WARS.= By R. BOSWORTH SMITH, M.A. With
    9 Maps and Plans.

  =THE GREEKS AND THE PERSIANS.= By the Rev. Sir G. W. COX, Bart., M.A.
    With 4 Maps.

  =THE ATHENIAN EMPIRE=, from the Flight of Xerxes to the Fall of
    Athens. By the Rev. Sir G. W. COX, Bart., M.A. With 5 Maps.

  =THE RISE OF THE MACEDONIAN EMPIRE.= By ARTHUR M. CURTEIS, M.A. With
    8 Maps.


                       EPOCHS OF ENGLISH HISTORY.

                Edited by MANDELL CREIGHTON, D.D., LL.D.
                         LATE BISHOP OF LONDON.

  =EARLY ENGLAND TO THE NORMAN CONQUEST.= By L. YORK POWELL, M.A.

  =ENGLAND A CONTINENTAL POWER=, 1066–1216. By Mrs. MANDELL CREIGHTON.

  =THE RISE OF THE PEOPLE AND THE GROWTH OF PARLIAMENT.= 1215–1485. By
    JAMES ROWLEY, M.A.

  =THE TUDORS AND THE REFORMATION.= 1485–1603. By MANDELL CREIGHTON,
    D.D., LL.D.

  =THE STRUGGLE AGAINST ABSOLUTE MONARCHY=, 1603–1688. By Mrs. S. R.
    GARDINER.

  =THE SETTLEMENT OF THE CONSTITUTION=, 1689–1784. By JAMES ROWLEY, M.A.

  =ENGLAND DURING THE AMERICAN AND EUROPEAN WARS.= 1765–1820. By the
    Rev. O. W. TANCOCK.

  =EPOCHS OF ENGLISH HISTORY.= Complete in One Volume, with 27 Tables
    and Pedigrees and 23 Maps. Fcp. 8vo.

  =THE SHILLING HISTORY OF ENGLAND=: being an Introductory Volume to
    the Series of _Epochs of English History_. By MANDELL CREIGHTON,
    D.D., LL.D. Fcp. 8vo.


               LONGMANS, GREEN & CO., 39 Paternoster Row,
            London, New York, Bombay, Calcutta, and Madras.




                       EPOCHS OF MODERN HISTORY.

              Edited by EDWARD E. MORRIS, M.A., J. SURTEES
                PHILLPOTTS, B.C.L., and C. COLBECK, M.A.
                               Fcp. 8vo.


  =The BEGINNING of the MIDDLE AGES.= By the Very Rev. RICHARD WILLIAM
    CHURCH, M.A. &c., late Dean of St. Paul’s. With 3 Maps.

  =The NORMANS in EUROPE.= By the Rev. A. H. JOHNSON, M.A. With 3 Maps.

  =The CRUSADES.= By the Rev. Sir G. W. COX, Bart., M.A. With a Map.

  =The EARLY PLANTAGENETS.= By W. STUBBS, D.D., late Bishop of Oxford.
    With 2 Maps.

  =EDWARD the THIRD.= By the Rev. W. WARBURTON, M.A. With 3 Maps and 3
    Genealogical Tables.

  =The ERA of the PROTESTANT REVOLUTION.= By F. SEEBOHM, LL.D. With 4
    Maps and 12 Diagrams.

  =The AGE of ELIZABETH.= By MANDELL CREIGHTON, D.D., LL.D., late
    Bishop of London. With 5 Maps and 4 Genealogical Tables.

  =The FIRST TWO STUARTS and the PURITAN REVOLUTION=, 1603–1660. By
    SAMUEL RAWSON GARDINER. With 4 Maps.

  =The THIRTY YEARS’ WAR=, 1618–1648. By SAMUEL RAWSON GARDINER. With a
    Map.

  =The ENGLISH RESTORATION and LOUIS XIV.= 1648–1678. By OSMUND AIRY,
    LL.D.

  =The FALL of the STUARTS; and WESTERN EUROPE= from 1678 to 1697. By
    the Rev. EDWARD HALE, M.A. With 11 Maps and Plans.

  =The AGE of ANNE.= By E. E. MORRIS, M.A. With 7 Maps and Plans.

  =FREDERICK the GREAT and the SEVEN YEARS’ WAR.= By F. W. LONGMAN.
    With 2 Maps.

  =The WAR of AMERICAN INDEPENDENCE=, 1775–1783. By J. M. LUDLOW. With
    4 Maps.

  =The FRENCH REVOLUTION.= 1789–1795. By Mrs. S. R. GARDINER. With 7
    Maps.

  =The EPOCH of REFORM=, 1830–1850. By JUSTIN MCCARTHY.


               LONGMANS, GREEN & CO., 39 Paternoster Row,
            London, New York, Bombay, Calcutta, and Madras.




                       _EPOCHS of MODERN HISTORY_

                               EDITED BY

               C. COLBECK, M.A.; EDWARD F. MORRIS, M.A.;
                AND J. SURTEES PHILLPOTTS, M.A., B.C.L.


                        _THE FRENCH REVOLUTION_

                             B. M. GARDINER

[Illustration: CENTRAL EUROPE 1789

_Longmans, Green & Co., London, New York, Bombay, Calcutta & Madras._]




                       _Epochs of Modern History_

                                  THE
                           FRENCH REVOLUTION
                               1789–1795

                                   BY
                        BERTHA MERITON GARDINER


                         _SIXTEENTH IMPRESSION_


                        LONGMANS, GREEN, AND CO.
                       39 PATERNOSTER ROW, LONDON
                 FOURTH AVENUE & 30TH STREET, NEW YORK
                      BOMBAY, CALCUTTA, AND MADRAS
                                  1921

                          All rights reserved




PREFACE.


In writing this handbook on the French Revolution, it has been my
endeavour to give a correct and impartial account of the most important
events of the revolutionary period, and of the motives by which the
leading characters were actuated. Much has necessarily been omitted
which finds a place in larger works. Those who wish to pursue the
subject further, and have time at their disposal, would do well to
study, besides general histories, some of the many books lately
published which deal with special branches of the subject, and often
enable the reader to form a more independent judgment both of men and
events than is possible from the perusal of works of the former class
alone. Amongst general histories those of Michelet and Louis Blanc
will probably be found most serviceable. No satisfactory account of
the relations of France with other countries is to be found in the
French tongue, partly because French historians still write with bias,
partly, also, because they hitherto either have been unacquainted
with, or have ignored the results of German research. Professor Von
Sybel’s well-known book, ‘Geschichte der Revolutionszeit,’ contains
the fullest and best account of the relations which existed between
the different States of Europe, but it is not an impartial one.
Hermann Hüffer’s books are valuable contributions to our knowledge of
diplomatic relations, and, being written from an opposite point of
view, should be studied by all readers of Von Sybel. The history of the
foreign policy of England during this period has still to be written.
M. Sorel has lately published in the pages of the ‘Révue Historique’ a
full account of the foreign policy pursued by the Committee of Public
Safety after Robespierre’s fall, and of the negotiations leading
to the treaties of peace signed in 1795 between France and Prussia
and France and Spain. Much fresh information regarding the internal
condition of France during the revolutionary period is to be found
scattered in local and special histories of various kinds. Amongst
such may be specially mentioned Mortimer Ternaux’s ‘Histoire de la
Terreur,’ and ‘La Justice Révolutionnaire,’ by Berriat St. Prix. M.
Taine in his great work has collected a large number of extracts from
documents lying in the archives of the departments, but entire absence
of classification, and the strong political bias of the writer, makes
this work of less value to the student than others of less pretensions.
Amongst the best of local histories are the works of M. Francisque
Mège, which reveal the course taken by the Revolution in the province
of Auvergne. Biographical works are numerous. Mirabeau’s character
will best be learnt from his correspondence with the Count de la
Marck. M. D’Héricault’s ‘Révolution de Thermidor’ contains a detailed
account of the policy pursued by Robespierre after the expulsion of
the Girondists. Danton’s life and character can best be studied in
the works of M. Robinet. Schmidt’s ‘Pariser Zustände während der
Revolutionszeit’ contains the best existing account of the economic
condition of Paris between 1789 and 1800. As it is improbable that
those for whom this book is in the first place intended will have
any idea of the amount represented by so many thousand or million
livres, I have invariably given the English equivalent of the French
money, following the table inserted by Arthur Young in his ‘Travels in
France.’ After the introduction of the revolutionary calendar, I have
in giving dates followed the table in ‘L’Art de vérifier les Dates.’ In
consequence of the different system of intercalation pursued in the two
calendars, the correspondence of dates varies from year to year, and
in consequence of leaving this fact unnoticed even French historians
sometimes give the date in the old style wrongly. I have only further
to add that the purple lines upon the map of France in provinces
represent the frontiers where customs duties were levied under the old
Monarchy. They are copied from a map published with Necker’s works. It
will be seen that Alsace and Lorraine, as well as Bayonne and Dunkirk,
were allowed to trade freely with the foreigner. Marseilles enjoyed the
same privilege.




CONTENTS.


  CHAPTER I.

  FEUDALISM AND THE MONARCHY.

                                                                    PAGE
  The Monarchy in France                                               1
  Social condition of France                                           3
  Feudal rights                                                        4
  Condition of the Church                                              6
  Government and administration                                        7
  The privileged classes                                               8
  Taxation                                                             9
  Condition of the People                                             11
  Interference with trade                                             13
  Public opinion in France                                            13
  Voltaire and his followers                                          13
  The Encyclopædists                                                  14
  The Church and Christian Theology attacked                          15
  The Economists                                                      16
  Rousseau                                                            16


  CHAPTER II.

  FRANCE UNDER LOUIS XVI., 1774–1789.

  The Ministry of Turgot                                              18
  Opposition raised to his reforms                                    19
  Character of Louis XVI.                                             19
  Character of Marie Antoinette                                       20
  1776. Dismissal of Turgot                                           21
  Movement of Reform extends over Europe                              21
  Condition of England                                                23
  Pitt in Office                                                      24
  Reaction after Turgot’s dismissal                                   25
  Ministry of Necker                                                  25
  Necker opposed by the Parliaments                                   25
  1781. He resigns office                                             26
  Desire for political liberty                                        26
  1776. American Declaration of Independence                          26
  1783. Ministry of Calonne                                           27
  1787. The Assembly of Notables                                      27
  Ministry of Brienne                                                 27
  General disaffection                                                28
  1788. Second Ministry of Necker, and calling of the States General  29
  Pamphlets and Cahiers                                               29
  Siéyès’ Pamphlet--What is the Third Estate?                         30
  Double Representation of the Third Estate                           31


  CHAPTER III.

  THE ASSEMBLY AT VERSAILLES, 1789.

  May 5, 1789. Meeting of the States General                          33
  Relation of the King to the Revolution                              33
  Question whether the States were to sit as one or as three
    chambers left undecided                                           33
  Evil consequences of the Royal policy                               34
  Character and policy of Mirabeau                                    35
  Title of National Assembly adopted by the Third Estate              37
  Excitement and disorder in Paris                                    38
  Louis takes part with the Upper Orders                              39
  June 20. Tennis Court Oath                                          40
  Royal Sitting of June 23                                            40
  The States constituted as one Chamber                               41
  July 14. The fall of the Bastille                                   43
  Establishment of a Municipality and of a National Guard in Paris    46
  Visit of Louis to the Capital                                       47
  Risings in the Provinces                                            48
  Decrees of August 4                                                 49
  Composition of the Assembly                                         51
  The Reactionary Right                                               51
  The Right Centre                                                    52
  The Centre and Left                                                 52
  The Extreme Left                                                    53
  Causes giving ascendency to the Left                                54
  Policy of Mirabeau                                                  56
  Declaration of the Rights of Man                                    58
  New Constitution; Legislature to be formed of one House;
    Veto given to the King                                            58
  Scarcity of Bread                                                   59
  Character of the National Guard of Paris                            60
  October 6. The King and Queen brought to Paris                      60


  CHAPTER IV.

  THE CONSTITUTION, 1789–1791.

  Results of the Movement of October 6                                63
  The Jacobins                                                        64
  The Constitution; Administrative Changes; Establishment
    of 44,000 Municipalities                                          65
  Judicial Reforms                                                    66
  Increase of the State debt                                          67
  Church Property appropriated by the State                           67
  Creation of Assignats                                               68
  Civil Constitution of the Clergy                                    69
  Feast of the Federation                                             69
  Emigration of the nobles                                            70
  Embitterment of the Relations between nobles and peasants           71
  Weakness of the Central Government                                  72
  Mutinies in the Army                                                73
  Imposition of an Oath on the Clergy; Schism in the Church           74
  The Constitution decried by the Ultra-Democrats                     76
  Brissot                                                             76
  Desmoulins                                                          77
  Marat                                                               78
  Sources of influence exercised by the Ultra-Democrats               79
  Influence exercised by Jacobin Clubs                                80
  September 1790. Resignation of Necker                               81
  The Commune of Paris; Composition of its Municipality               81
  Mirabeau’s policy; his Death, April 2, 1791                         84
  Position of the Constitutionalists                                  85


  CHAPTER V.

  THE FALL OF THE MONARCHY, 1791–1792.

  Unpopularity of Marie Antoinette                                    87
  June 20, 1791. Flight of the Royal Family                           88
  Ultra-Democrats seek the Establishment of a Republic                91
  July 17. Massacre of the Champ de Mars                              91
  Attempt to revise the Constitution                                  93
  The work of the National Assembly; legal and financial reforms      93
  Creation of Assignats of small value                                94
  Plans of the Queen                                                  94
  Policy of territorial aggrandisement pursued by the Great Powers    96
  Austria and Russia at war with Turkey                               97
  Death of Joseph II.                                                 97
  Treaty of Reichenbach                                               97
  Declaration of Pilnitz                                              98
  Designs of Catherine II. on Poland                                  98
  Leopold II. unwilling to engage in war with France                  98
  The new Legislative Assembly; its composition                       99
  Policy of the Girondists                                           100
  Ecclesiastical policy of the Legislature                           101
  Emigrants encouraged by Princes of the Empire                      101
  Growth of a warlike spirit in the Assembly                         102
  The French Revolution is more than a National movement             104
  Commencement of war with Austria and Prussia                       105
  The Jacobins embody a spirit of suspicion                          106
  Robespierre’s character                                            107
  Administrative anarchy                                             109
  Troubles at Avignon                                                110
  The Girondists hope for the best                                   111
  Lafayette denounces the Jacobins                                   112
  The mob invades the Tuileries on June 20                           113
  The Country declared in danger; Manifesto of the Duke of
    Brunswick                                                        114
  Preparations made for an insurrection                              115
  Insurrection of August 10; Suspension of the King                  117


  CHAPTER VI.

  THE FALL OF THE GIRONDISTS, 1792–1793.

  Formation of the new Commune of Paris                              119
  The September massacres                                            121
  The defence of the Argonnes                                        123
  The meeting of the Convention, and the abolition of Monarchy       124
  The Girondists and the Mountain                                    125
  Weakness of the Centre                                             128
  Re-election of the Commune                                         129
  Conquest of Savoy, Mainz, and Belgium                              130
  Question of the annexation of Belgium                              131
  The Opening of the Scheldt, and the order to the Generals
    to proclaim the Sovereignty of the People                        134
  Objects of the Allies                                              135
  Pitt’s ministry in England                                         136
  Views taken of the French Revolution in England                    137
  Trial and Execution of Louis XVI.                                  139
  War with England; the French expelled from Belgium                 141
  Establishment of the Revolutionary Court; Defeat of Neerwinden     143
  Party strife in the Convention                                     144
  Establishment of the Committee of Public Safety                    145
  Deputies in mission                                                146
  Laws against Emigrants and Nonjurors                               147
  Policy of the Mountain                                             148
  The economical situation                                           149
  Popular remedies opposed by the Girondists                         151
  The Commune leads a movement against the Girondists                153
  Expulsion of the leading Girondists                                155


  CHAPTER VII.

  THE COMMUNE AND THE TERROR, 1793.

  State of public feeling                                            156
  Girondist and Royalist movements; Resistance in Lyons and Toulon   157
  General submission to the Convention                               158
  War in La Vendée                                                   159
  Successes of the Vendeans                                          160
  Successes of the Allies                                            161
  Coolness between Austria and Prussia                               162
  Assassination of Marat                                             163
  Sanguinary tendencies of the Government                            165
  Growing strength of the Committee of Public Safety                 166
  Power of the Commune                                               167
  Views of Hébert and Chaumette                                      168
  Introduction of the conscription                                   170
  Maximum laws                                                       171
  Laws against speculation                                           172
  Depression of trade and agriculture                                173
  Law of ‘Suspected Persons’                                         175
  Increased activity of the Revolutionary Court                      176
  Execution of the Queen and the Girondists                          177
  Worship of Reason                                                  178
  Introduction of the Revolutionary calendar                         180
  Surrender of Lyons                                                 181
  Destruction of the Vendean army                                    182
  The Terror in the Departments                                      183
  The Terrorists a small minority                                    186


  CHAPTER VIII.

  THE FALL OF THE HÉBERTISTS AND DANTONISTS, 1793–1794.

  Condition of the Army                                              188
  Carnot’s military reforms                                          189
  Campaign in Belgium and the Rhine; Victories of Hondschoote and
    Wattignies                                                       191
  The Allies expelled from Alsace by Hoche and Pichegru              192
  Legislation of the Convention                                      193
  Cambon’s financial measures                                        195
  Growing feeling against the Commune                                196
  Robespierre attacks the Hébertists                                 197
  _The Old Cordelier_                                                199
  The Hébertists attack the Dantonists                               200
  Robespierre’s influence over the Jacobins                          201
  Robespierre abandons the Dantonists                                202
  Execution of the Hébertists and Dantonists                         204


  CHAPTER IX.

  THE FALL OF ROBESPIERRE, 1794.

  Despotism of the Committee of Public Safety                        204
  Aims of Robespierre                                                205
  Aims of St. Just                                                   206
  Financial object of the continuation of the Terror                 207
  The Terror systematised                                            208
  Renewal of the War in La Vendée                                    209
  Treaty of the Hague between England and Prussia                    209
  Insurrection in Poland                                             210
  Differences between England and Prussia                            211
  The Allied Forces driven from Belgium                              212
  Worship of the Supreme Being instituted by Robespierre             214
  Increased activity of the Revolutionary Court                      215
  Position of Robespierre                                            216
  Discords break out within the Committee of Public Safety           217
  Insurrection of Thermidor                                          219
  Execution of the Robespierrists                                    220


  CHAPTER X.

  FALL OF THE MONTAGNARDS, 1794–1795.

  Reactionary Movement in Paris and in the Departments               221
  Parties in the Convention                                          222
  Readmission of the expelled Girondist Deputies to the Convention   223
  Repeal of Maximum Laws, and suffering in Paris                     225
  Insurrection of Germinal 12                                        226
  Reaction in Paris, and in the Departments                          227
  The public exercise of all forms of worship permitted by the
    Convention                                                       228
  The White Terror                                                   229
  Insurrection of Prairial 1                                         230
  Proscription of Montagnards                                        231


  CHAPTER XI.

  THE TREATY OF BASEL AND THE CONSTITUTION OF 1795.

  Conquest of Holland by Pichegru                                    232

  Foreign policy of the Convention                                   233

  Foreign policy of Thugut                                           235

  Foreign policy of Catherine II.; Alliances between Russia and
    Austria                                                          236

  English foreign policy; Successes at Sea, and conquest of French
    Colonies                                                         237

  Prussian foreign policy; Peace made at Basel between Prussia and
    France                                                           238

  Position of Spanish Government; Treaty of Peace between France
    and Spain                                                        240

  War in the West; Hoche appointed Commander-in-Chief                242

  Expedition of Emigrants to Quiberon                                243

  Position of the Convention; its unpopularity                       245

  Death of the Dauphin                                               245

  The Convention sanctions the use of Churches for Catholic worship  246

  Position of the Clergy; Parties amongst them                       247

  The Convention frames the Constitution of 1795                     248

  Special Laws passed to maintain the Republican Party in Power      249

  Insurrection of Vendémiaire 13 suppressed by Napoleon Bonaparte    250

  Law of Brumaire 3, excluding relations of Emigrants from Office    250

  The Five Directors; Position of the New Government                 251

  INDEX                                                              255


MAPS.

  Europe in 1789                                    _To face title page_

  Map of France in Provinces                                           9

  Revolutionary Paris                                                 43

  Map of France in Departments                                        65

  Map of Belgium                                                     132

  Map of the Rhine                                                   190

  Map of Quiberon                                                    241


REVOLUTIONARY CALENDAR.

  Vendémiaire      Sept.   Oct.
  Brumaire         Oct.    Nov.
  Frimaire         Nov.    Dec.
  Nivose           Dec.    Jan.
  Pluviose         Jan.    Feb.
  Ventose          Feb.    March
  Germinal         Mar.    April
  Floréal          April   May
  Prairial         May     June
  Messidor         June    July
  Thermidor        July    Aug.
  Fructidor        Aug.    Sept.




LEADING DATES IN THE HISTORY OF THE FRENCH REVOLUTION.

  _Dates relating to military or foreign affairs are given in italics
    in order that the attention of the reader may be drawn to the
    relation between them and the domestic occurrences._


  1774

  Accession of Louis XVI.--Ministry of Turgot.


  1776

  Dismissal of Turgot--Ministry of Necker--_American Declaration
    of Independence_.


  1778

  _France allies itself with America._


  1781

  Resignation of Necker.


  1783

  Calonne’s Ministry.


  1787

  The Assembly of Notables--Brienne’s Ministry.


  1788

  Necker’s Second Ministry.


  1789

     May 5.  Meeting of the States General.

   June 17.  Adoption of the title of National Assembly.

   June 20.  The Tennis Court Oath.

   June 23.  The King comes to the Assembly to command the separation
               of the Orders.

   July 14.  Capture of the Bastille.

    Aug. 4.  Abolition of feudal rights.

    Oct. 6.  The King brought to Paris.


  1790

   July 14.  Feast of the Federation.

   Nov. 27.  Oath imposed on the Clergy.


  1791

   April 2.  Death of Mirabeau.

   June 20.  The Flight to Varennes.

   July 17.  The Massacre of the Champ de Mars

   Aug. 27.  _Declaration of Pilnitz._

  Sept. 30.  End of the Constituent Assembly.

    Oct. 1.  Meeting of the Legislative Assembly.


  1792

  April 20.  _Declaration of War against the King of Hungary and
               Bohemia, entailing also a War with Prussia._

   June 13.  Dismissal of the Girondist Ministers.

   June 20.  The King mobbed in the Tuileries.

   July 26.  _The Duke of Brunswick’s Manifesto._

   Aug. 10.  Overthrow of the Monarchy.

   Aug. 24.  _Surrender of Longwy._

 Sept. 2–7.  The September Massacres.

 Sept.  20.  _The Cannonade of Valmy._

 Sept.  21.  Meeting of the Convention.

 Sept.  22.  Proclamation of the Republic.

   Nov.  6.  _Victory of Jemmapes, followed by the occupation of
               Belgium, Savoy, Nice, and Mainz._

   Nov. 19.  The Convention offers assistance to all Peoples desirous
               of freedom.

   Dec.  2.  _The French driven out of Frankfort._

   Dec. 15.  The Convention orders its Generals to revolutionise
               the Foreign Countries in which they are.


  1793

   Jan. 21.  Execution of the King.

    Feb. 1.  _Declaration of War against England and Holland._

   Mar.  3.  _Miranda driven from Maestricht._

   Mar.  9.  Establishment of the Revolutionary Court.

   Mar. 18.  _Defeat of Neerwinden, followed by the loss of Belgium._

   April 6.  Constitution of the Committee of Public Safety.

    June 2.  Expulsion of the Girondists.

    July 3.  Assassination of Marat.

    July 8.  _Surrender of Mainz, Condé, and Valenciennes._

   Aug. 23.  The Levy of all men capable of bearing arms decreed.

  Sept.  8.  _Victory of Hondschoote._

  Sept. 17.  The great Maximum Law and the Law against Suspected Persons.

   Oct.  7.  _Capture of Lyons._

   Oct. 16.  Execution of the Queen.

   Oct. 16.  _Victory of Wattignies._

   Oct. 31.  Execution of the Girondists.

   Nov. 10.  Worship of Reason at Notre Dame.

   Dec. 10.  _Capture of Toulon._

   Dec. 12.  _Destruction of the Vendean Army at Le Mans._


  1794

   Mar. 24.  Execution of the Hébertists.

   April 5.  Execution of the Dantonists.

     April.  _Insurrection in Poland._

  April 18.  _Victory of Turcoing._

   June  1.  _Battle of June 1._

   June  8.  Feast in honour of the Supreme Being.

   June 26.  _Victory of Fleurus, followed by the evacuation of
               Belgium by the Allies._

   July 28.  Execution of the Robespierrists.

   Nov. 12.  Jacobin Club closed.

   Dec.  8.  Seventy-three Deputies of the Right readmitted into
               the Convention.

   Dec. 24.  Repeal of Maximum Laws.


  1795

       Jan.  _Invasion of Holland._

    Mar. 8.  Readmission to the Convention of survivors of Girondist
               Deputies proscribed on June 2, 1793.

   April 1.  (Germinal 12) Insurrection of Lower Classes against the
               Convention.

   Feb. 22.  Public exercise of all forms of worship permitted by the
               Convention.

    May 20.  (Prairial 1) Second insurrection by Lower Classes against
               the Convention.

   April 5.  _Treaty of Peace made at Basel between France and Prussia._

   June  8.  Death of the Dauphin.

   July 12.  _Treaty of Peace between France and Spain._

   July 21.  _Defeat of Emigrants at Quiberon._

  Sept. 23.  Proclamation of the Constitution of the Year III. (1795).

   Oct.  5.  (Vendémiaire 13) Insurrection of the Middle Classes
               against the Convention.

   Oct. 26.  (Brumaire 4) Meeting of the New Legislature.




THE FRENCH REVOLUTION.




CHAPTER I.

FEUDALISM AND THE MONARCHY.


♦The Monarchy in France.♦

Like the rest of Western Europe, France, in the Middle Ages, was ruled
by a feudal nobility, holding their lands of the king. Nowhere in
Western Europe in the tenth century was the power of the king less,
or the power of the nobles greater. The weight of their authority,
therefore, fell heavily upon the peasants on their estates, and upon
the inhabitants of the little towns scattered over the country. A
feudal noble, if he were a _seigneur_, answering to our lord of the
manor, ruled all dwellers on his estate. Their claims to property
were heard in his courts, and they were amenable to his jurisdiction
for crimes committed, or alleged to have been committed, by them. The
seigneur may not have been a worse tyrant than many kings and princes
of whom we read in history; but he was always close at hand, whilst
Nero or Ivan the Terrible was far off from the mass of his subjects.
He knew all his subjects by sight, had his own passions to gratify
amongst them, and his vengeance to wreak upon those whom he personally
disliked. To be free from this domination must have been the one
thought of thousands of miserable wretches.

To shake off the yoke by their own efforts was an impossibility. The
nearest ally on whom they could count was the king. He too was opposed
to the domination of the nobles, for as long as they could disregard
his orders with impunity, he was king in name alone. He was, in fact,
but one nobleman amongst many, with a higher title than the rest.

Dwellers in towns could more readily coalesce and resist the authority
of the seigneurs than dwellers in the country. By trade they acquired
wealth, and with wealth influence. In the twelfth century they
formed themselves into municipal communities, and, bidding defiance
to their seigneurs, called upon their king to aid them in achieving
independence. From that time to the end of the seventeenth century the
power of the Monarchy grew stronger with every succeeding generation.
The king was the dispenser of law and order, while the enemies of law
and order were the feudal nobles. When Louis XIV. took the government
into his own hands, in 1661, his will was law. Justice was administered
by parliaments or law courts acting in the name of the king. The
affairs of the provinces were administered by _intendants_, acting by
his commission. No nobleman, however wealthy or highly placed, dared
to resist his authority. With the frank gaiety of their nation the
nobles themselves accepted the position, and crowded to his court or
confronted death in his armies. He was able to say, without fear of
contradiction, ‘I am the State.’

Unhappily for his people, he could not say ‘I am the Nation.’ In him
the Monarchy had been victorious over its enemies, but it had not
accomplished its task. The nation wanted more work from its kings,
wanted simply that they should go on in the path which had been trodden
by their ancestors. The national wish was too feebly expressed to
reach the ears of Louis. He was thinking of military glory and courtly
display, not of the grievances of his people. He had overthrown the
power of the nobility so far as it threatened his own. He did not care
to inquire whether there was enough left to produce cruel wrong far
off from the splendid palace of Versailles. His great-grandson, the
vile, profligate Louis XV., had even less thought for the exercise of
the duties of a king, as father of his people. The Monarchy was in its
decline, not because it was intentionally tyrannical, but because it
had ceased to do its duty. The French people were not Republican. They
needed a government, and government in any true sense there was none.

♦Social condition of France.♦

In consequence of the king thus deserting the path trodden by his
ancestors, a state of things arose in France such as was found in no
other country. Nowhere did the nobility as a class do so little for
the service of their countrymen, yet nowhere were they in possession
of more social influence or greater privileges. Nowhere were the
mercantile and trading classes comparatively more wealthy and
intellectual, yet nowhere was the distinction between the noble and
the plebeian or bourgeois more rigorously maintained. Finally, in no
other country where, as was the case in France, the mass of peasants
were free men, did the owners of fiefs retain so many rights over the
dwellers on their estates, and yet live in such complete separation
from them.

After the nobles had lost political power they were cut off from
all healthy communication with their fellow subjects. In France all
sons and daughters of noblemen were noble, and their families did
not blend with those of other classes like the family of an English
peer. Nobles contemned the service of the administration as beneath
their birth; on the contrary, no one who was not of noble birth could
hold the rank of an officer in the army. The great lords flocked to
Paris and Versailles, where they wasted their substance in extravagant
living; the lesser nobles, men who in England would have occupied the
position of country gentlemen, were often through poverty compelled
to reside in their châteaux, where they lived in isolation, having no
common interests with their neighbours, while clinging tenaciously
to the possession of their rights as proprietors and feudal lords.
♦Feudal rights.♦ These feudal rights varied in every province, but were
of three general kinds. (1) Rights which had their origin when the
seigneur was also ruler--as, for instance, the right of administering
justice, though this he now almost invariably farmed to the highest
bidder; the right of levying tolls at fairs and bridges; and the
exclusive right of fishing and hunting. (2) Peasants in the position of
serfs were only to be found in Alsace and Lorraine; but rights still
existed all over the country which betrayed a servile origin. Thus, the
farmer might not grind his corn but at the seigneur’s mill, nor the
vine-grower press his grapes but at the seigneur’s press; and every man
living on the fief must labour for the seigneur without return so many
days in the year. (3) Finally, the courts ruled that wherever land was
held by a peasant from the owner of a fief, there was a presumption
that the owner retained a claim to enforce cultivation and the payment
of annual dues. Land so held was termed a _censive_--resembling an
English copyhold. The granting of land on these terms never stopped
from the close of the Middle Ages down to the Revolution. The dues
retained were often petty. One tenant might pay a small measure of
oats; another a couple of chickens. Yet the payments were often
sufficiently numerous to form the chief maintenance of many of the
nobles. The holders of these _censives_ possessed however, all the
rights of proprietors. They could not be dispossessed so long as they
paid the dues to which they were liable, and they could sell and devise
the land without the consent of the owners of the fief. Properties held
on these terms abounded in all parts of France, and though the extent
of each _censive_ was often no more than a couple of acres, it is
probable that before the Revolution at least a fifth of the soil had by
these means passed into the possession of the peasantry.

The existence of feudal rights produced three results exceedingly
detrimental to the national prosperity. It impeded a good cultivation
of the soil; it prevented the country from being inhabited by men
of the middle class, who preferred to reside in towns rather than
recognise the social superiority claimed by the seigneur; and,
finally, it was an incessant source of irritation to the whole rural
population. By the rights due to a seigneur as ruler, and by those
of servile origin, all dwellers upon the fief were affected, whether
occupiers of land or not. The cultivator suffered at every turn--in
the prohibition to plant what crops he pleased; in the prohibition
to destroy the seigneur’s deer and rabbits that roamed at will over
his fields and devoured his green corn; in the toll he paid for leave
to guard his crops while growing, and to sell them after they were
gathered in; and in many other ways. Such a system had become in the
course of centuries both excessively complicated and wholly unsuited to
existing social conditions. Sometimes half-a-dozen different persons
claimed dues from the same piece of land. The proprietorship of fiefs
and the ownership of feudal rights, or the greater part of them, were
constantly separated. Poverty induced the resident seigneur to sell his
rights, which, bought by a townsman, passed from hand to hand in the
market, like any other property, and were the more sought after because
their possession was held a sign of social superiority. Non-resident
owners farmed them, and middle-men were harsh and exacting in their
collection. The peasant, ignorant and poor, but thrifty and cunning,
and fondly attached to his plot of ground, disputed claims made upon
him to pay dues now to this man, now to that, in virtue of concessions
of which, in a vast number of cases, the origin was completely lost.
Innumerable lawsuits resulted, which left stored up in the peasant’s
mind bitter feelings of resentment against both judge and seigneur, one
of whom he accused of partiality, the other of rapacity and extortion.

♦The Church.♦

The maintenance of feudal relations between classes, when neither
government nor society rested on the same bases as in feudal times,
could only be productive of harm. In right of birth privileges and
advantages were claimed by nobles without regard to principles of
justice or of public utility. On every side, in the army, the navy,
the profession of the law, distinction between the nobleman and the
bourgeois still prevailed. But no institution suffered in consequence
of the privileges of the nobility so great moral detriment as the
Church. The Church was a rich, self-governed corporation, in possession
of an annual revenue of more than 8,750,000_l._, providing for about
130,000 persons, including monks and nuns. This great wealth was
unfairly distributed, and to a large extent misapplied. As a rule, all
higher posts were reserved for portionless daughters and younger sons
of noble families. Bishops and abbots, who revelled in wealth, were
nobles; parish priests, who had barely enough for subsistence, were
bourgeois and peasants. Thus the Church teemed with abuses, and exerted
little moral influence. Her wealth excited the jealousy of the middle
classes, whilst the luxurious and profligate lives led by many prelates
and holders of sinecures brought disgrace on the ecclesiastical
profession. Of reform there was no hope, since the lower clergy, who
had interest in effecting it, were excluded from all part in Church
government.

♦Government and administration.♦

Such abuses called aloud for the hand of a reformer. The material
result of social disorder was impoverishment and decay. ‘Whenever you
stumble on a grand seigneur,’ wrote an English traveller, ‘you are sure
to find his property a desert.... Go to his residence, wherever it may
be, and you will probably find it in the midst of a forest very well
peopled with deer, wild boars, and wolves. Oh! if I were the legislator
of France for a day, I would make such great lords skip.’ The king had
acquired power in right of the services he rendered the nation. When he
ceased to do good, as had been the case since Louis XIV. plunged the
nation into a series of wars of ambition, it was inevitable that he
should do harm. The welfare of the masses was dependent on the action
of the central government, and the central government sacrificed their
welfare for the sake of obtaining favour with the upper classes. Hence
administration was in a chaos, and the government, in appearance all
powerful, was in reality strong only when it had to deal with the
crushed and helpless peasant and artisan. The States-General, which
in some sort answered to our English Parliament, had last met in
1614. For the past two centuries the royal council had been engaged
in undermining local liberties, and establishing a centralised system
of administration. The work in all essentials was so thoroughly done,
that no parish business, down to the raising of a rate or the repairing
of a church-steeple, could be effected without authorisation from
Paris. Absolute and centralised, the government was also excessively
arbitrary. On plea of State necessity it repudiated debts, broke
contracts, over-ruled laws, and set aside proprietary rights without
scruple. The issue of warrants, called _lettres de cachet_ sealed
letters, ordering the imprisonment of the person designated in some
state fortress, was an ordinary mode of inflicting punishment.
Yet, however harsh and arbitrary in treatment of individuals, the
government sought to avoid collision with the upper classes as a body.
On all sides it left standing institutions of the Middle Ages, local
functionaries, and municipal assemblies, of which the existence in many
instances increased the weight of local charges and impeded attempts to
ameliorate the condition of the working classes. In the same way the
upper law courts, the Parliaments, were suffered as of old to meddle
in administrative matters. Privileges, so far from being assailed,
were respected. Whatever special rights provinces, towns, or classes
possessed were suffered to remain and were often extended.

♦Privileged classes.♦

The wars of Louis XIV. and the orgies of Louis XV. absorbed more and
more money. On the labouring classes, already overtaxed, an increased
weight of taxation was always being laid. Hence, of these classes the
king became the oppressor, and the oppression was the greater because
the upper classes, who were best able to pay taxes, contributed much
less than their fair share of the burden.

The nobles and clergy, styled the two upper orders, stood, in right
of their privileges, both pecuniary and honorary, apart from the
rest of the nation. Nobles did not pay any direct taxes in the same
proportion as their fellow subjects, and in the case of the _taille_,
a heavy property tax, their privilege approached very nearly to entire
exemption. The clergy, except in a few frontier provinces, paid
personally no direct taxes whatever. The bourgeoisie was regarded as
an inferior class. Those who were able acquired by purchase the rank
and privileges of nobles, and in this way had come into existence a
nobility of office and royal creation, which, although looked down
upon by the old nobility of the sword, enjoyed the same pecuniary
immunities. Those left on the other side of the line deeply resented
the social superiority claimed by the nobility in right of its
privileges. The upper section of the bourgeoisie was, however, itself
privileged to no inconsiderable extent. By living in towns, merchants,
shopkeepers, and professional men were able to avoid serving in the
militia and collecting the _taille_, from which in the country nobles
alone were exempt. They also purchased of the government petty offices,
created in order that they might be sold, to which no serious duties
were attached, but the possession of which conferred on the holders
partial exemption from payment of the _taille_ and of excise duties,
and other privileges of like character.

[Illustration: FRANCE IN PROVINCES 1769–1789.

_Longmans, Green & Co., London, New York, Bombay, Calcutta & Madras._]

♦Taxes.♦

Oppressive as taxation was, owing to its weight alone, and to its
unjust distribution between classes, it was rendered yet more so by
want of administrative unity, by the nature of some of the taxes and
the method of their assessment and collection. Internal custom-houses
and tolls impeded trade, gave rise to smuggling, and raised the price
of all articles of food and clothing. It took three and a half months
to carry goods from Provence to Normandy, which, but for delays
caused by the imposition of duties, might have travelled in three
weeks. Customs duties were levied with such strictness that artisans
who crossed the Rhône on their way to their work had to pay on the
victuals which they carried in their pockets. Excise duties were
laid on articles of commonest use and consumption, such as candles,
fuel, wine, and even on grain and flour. Some provinces and towns
were privileged in relation to certain taxes, and as a rule it was
the poorest provinces on which the heaviest burdens lay. One of the
most iniquitous of the taxes was the _gabelle_, or tax on salt. Of
this tax, which was farmed, two-thirds of the whole were levied on a
third of the kingdom. The price varied so much that the same measure
which cost a few shillings in one province cost two or three pounds
in another. The farmers of the tax had behind them a small army of
officials for the suppression of smuggling, as well as special courts
for the punishment of those who disobeyed fiscal regulations. These
regulations were minute and vexatious in the extreme. Throughout the
north and centre of France, the _gabelle_ was in reality a poll tax;
the sale of salt was a monopoly in the hands of the farmers; no one
might use other salt than that sold by them, and it was obligatory on
every person aged above seven years to purchase seven pounds yearly.
This salt, however, of which the purchase was obligatory, might only be
used for purely cooking purposes. If the farmer wished to salt his pig,
or the fisherman his fish, they must buy additional salt and obtain a
certificate that such purchase had been made. Thousands of persons,
either for inability to pay the tax, or for attempting to evade the
laws of the farm, were yearly fined, imprisoned, sent to the galleys,
or hanged. The chief of the property taxes, the _taille_, inflicted as
much suffering as the _gabelle_, and was also ruinous to agriculture.
Over two-thirds of France the _taille_ was a tax on land, houses, and
industry, reassessed every year not according to any fixed rate, but
according to the presumed capacity of the province, the parish, and
the individual taxpayers. The consequence was that, on the smallest
indication of prosperity, the amount of the tax was raised, and thus
parish after parish, and farmer after farmer, were reduced to the same
dead level of indigence.

♦Condition of the people.♦

Under the state of things here described, France had retrograded in
wealth and population. Intense misery prevailed amongst the working
classes. Artisans were unable to live on their wages; farmers and
small proprietors were constantly being reduced to beggary; ignorance
grew more dense. The government, by its own frequent setting aside of
laws, and by its intolerance and cruelty, helped to render the people
lawless, superstitious, and ferocious. Protestants were subjected to
persecuting laws. Thousands of them had been driven from the country,
or shot down by troops. The penal code was barbarous, and the brutal
breaking on the wheel was an ordinary mode of putting criminals
to death. It was only by very rough usage that fiscal regulations
were maintained, and the taxes gathered in. If the _taille_ and the
_gabelle_ were not paid, the defaulter’s goods were sold over his
head, and his house dismantled of roof and door. In all cases in
which the administration was concerned, whatever justice peasant and
artisan received was meted to them by administrative officials who
were themselves parties in the cause. Famine was like a disease which
counted its victims by hundreds. As a rule, the farmer was a poor and
ignorant peasant, living from hand to mouth, miserably housed, clothed,
and fed.

An Englishman, Arthur Young, travelling in France in the years
1788–1789, reports how he passed over miles and miles of country once
cultivated, but then covered with ling and broom; and how within a
short distance of large towns no signs of wealth or comfort were
visible. ‘There are no gentle transitions from ease to comfort,
from comfort to wealth; you pass at once from beggary to profusion.
The country deserted, or if a gentleman in it, you find him in some
wretched hole, to save that money which is lavished with profusion in
the luxuries of a capital.’ The same traveller tells us how, as he was
walking up a hill in Champagne, he was joined by a poor woman who
complained of the hardness of the times. ‘She said her husband had
but a morsel of land, one cow and a poor little horse, yet he had a
franchar (42 lbs.) of wheat and three chickens to pay as a quit rent to
one seigneur, and four franchars of oats, one chicken, and one shilling
to pay another, besides very heavy _tailles_ and other taxes. She had
seven children, and the cow’s milk helped to make the soup. It was
said, at present, that something was to be done by some great folks
for such poor ones, but she did not know who nor how, but God send us
better, “car les tailles et les droits nous écrasent.” This woman, at
no great distance, might have been taken for sixty or seventy, her
figure was so bent and her face so furrowed and hardened by labour, but
she said she was only twenty-eight.’

Since, owing to the weight of taxation, no profits were to be made by
farming, it was impossible that there should be a good cultivation of
the soil. The amount of capital employed on land in England was at
least double that employed in France. Hence, while in England famine
was unknown, in France production barely equalled consumption, and
scarcities were of incessant occurrence. A single bad season would
force the farmer to desert his land, and with his family beg or steal.
Whenever bread rose above three halfpence the pound men starved.
Bread riots constantly took place in one or another province, and
the country swarmed with beggars, brigands, poachers, and smugglers.
Thousands of these outcasts were imprisoned, sent to the galleys, or
hanged; but no severity could lessen their number, while the causes
producing them remained unremoved. Adequate means of providing for
the destitute there were none. A few hospitals and other charitable
institutions existed. Bishops, great seigneurs, and monasteries often
kept alive hundreds in seasons of scarcity. Hospitals, however, were
little better than plague houses, where the sick and infirm were taken
in to die, whilst private charity was partial and insufficient. There
was no general system of poor relief. With the object of keeping bread
at a price within the people’s reach, the corn trade was subject to a
variety of regulations and restrictions. Occasionally the government
made purchases of foreign corn, which was resold under price. Sometimes
the prices of corn and other articles of food were fixed. In towns
the price of bread was ordinarily regulated according to the price of
corn by police officers, a not unnecessary precaution when the baking
trade was in the hands of a close corporation. A more vicious mode of
relief could hardly have been devised, but to abandon it was no easy
matter. The arbitrary means taken to reduce the price of corn often had
the effect of raising it, and, when successful, only tended to lessen
production and lead to greater scarcities, since cutting down the
profit of the already overweighted corn grower was, in reality, casting
an additional tax upon him. On the other hand, it was no less true that
so long as the existing order continued, a slight rise in the price of
the pound of bread meant sheer starvation for the mass of artisans, and
for thousands of agricultural labourers and small proprietors who were
not corn growers. Accustomed to look to the government to provide them
with cheap bread, in every season of scarcity these clamoured for a
reduction in price, and unless authorities were complaisant, resorted
to riot and pillage.

♦Voltaire.♦

The misery of the working classes presented in itself reason enough for
revolution; but revolution only comes when there are men of ideas to
lead the unlettered masses. In France the educated classes entertained
revolutionary ideas, and the men of letters who promulgated those ideas
became the leaders of opinion, and exerted enormous influence over
their own and the following generations. First came the Voltairians,
led by Voltaire (1694–1778). During the century rapid advance was
being made in all branches of study--in history, jurisprudence,
mathematical and physical science. The idea of progress was definitely
conceived, and knowledge upheld as the chief factor in producing
virtue and happiness. For the increase and diffusion of knowledge the
recognition of two principles was indispensable--religious toleration
and the freedom of the press. Both these principles were, however,
in direct antagonism to the principles on which the authority of the
Roman Catholic Church was based--unity of faith and worship, the
subordination of philosophy and science to theology, the submission
of reason to the teaching of tradition. Protestant clergymen were put
to death as late as 1762; while in 1765 a lad convicted of sacrilege
was hanged, and his body afterwards burned. Such acts of intolerance
and cruelty were, however, condemned by public opinion, and, between
the Church and the exponents of the new ideas, violent collision
inevitably ensued. Voltaire made it the work of his life to destroy
belief in revealed religion. In verse and in prose, in historical
works, in letters and pamphlets by the dozen, with rude licence or sham
respect, he held up the Church to derision, indignation, and contempt,
as the great enemy of enlightenment and humanity. ‘The most absurd of
empires,’ he wrote, ‘the most humiliating for human nature, is that of
priests; and of all sacerdotal empires, the most criminal is that of
priests of the Christian religion.’

♦Encyclopædists.♦

Voltaire himself was a sceptic. Behind him followed men who denied
belief in a personal God and the immortality of the soul. Diderot
(1713–1784) and D’Alembert (1717–1783), with indefatigable energy
published the ‘Encyclopædia,’ or dictionary of universal knowledge,
inculcating, at least indirectly, atheistical opinions, and designed,
by the destruction of ignorance and superstition, to undermine the
whole fabric of Christian theology. Before the end of his long life,
in 1778, Voltaire was the most eminent man in France, and sceptical
and atheistical opinions were commonly held and openly professed by
men and women of the upper and middle classes. The triumph of the new
philosophy was not, indeed, due merely to the powers of irony or the
reasoning of its advocates. The scandalous abuses within the Church
had prepared the way for its reception. The attacked had no efficient
weapon with which to repel their assailants. The Church was without
reforming energy or proselytising zeal. On the arm of the State she
could not rely for support with the same confidence as in former times.
The government was incapable of stamping out the new movement, nor
was it prepared seriously to make the attempt. The official class,
which came out of the middle class, was, like all others, permeated
with the new ideas. The occasional arrest of authors and printers, and
seizure of types and presses, did but increase the virulence of the
attack, and made the forbidden books more eagerly sought after. The
clergy were the more open to attack because they were interested in
the maintenance of privileges and abuses which inflicted cruel wrongs
on the working classes, while the new philosophy aimed at destroying
whatever stood in the way of material progress and the happiness of
the masses. In opposition to the Church’s doctrine of the natural
depravity of human nature, its adherents taught that man is born
good, and that wrong-doing is the result of ignorance; inculcated
the importance of educating all classes, and refused to recognise
limits to the improvement of which both individuals and the race are
capable. Often accompanied by a sensual view of life, which accorded
with the profligacy common amongst the upper classes at the time,
this high opinion of human nature developed a respect for man as man,
regardless of social position, race, or creed, and a passionate hatred
of inequalities founded on such distinctions. ♦Economists.♦ A school of
political economists, starting from the theory that all men originally
had equal rights, and every man liberty to employ his time, his hands,
and his brains according to his own advantage, demonstrated the
principles of free trade, and declared entire liberty of agriculture,
entire liberty of commerce and industry, entire liberty of the press to
be the true foundations of national prosperity. Appealing to abstract
principles of justice, humanity and right, Voltairians and Economists
joined in opening a fire of scathing criticism on existing laws,
customs, and institutions. They exposed the abuses and sufferings
incident to the use of torture, serfdom, and the slave trade, to
excessive centralisation and interference with trade and agriculture,
to close guilds, feudal duties, internal custom-houses, to the _taille_
and the _gabelle_, and demanded the carrying out of reforms which
should set trade and industry free, destroy class and provincial
privileges, introduce unity in the administration, and equality of
rights between man and man.

♦Rousseau.♦

The Voltairians were specially characterised by their attack upon the
Church and Christianity; the Economists by the importance which they
attached to individual liberty. Neither regarded the ignorant and
oppressed masses as able to act for themselves, and both looked to the
royal power, enlightened by a free press, as the instrument through
which reform must be effected. Rousseau was a writer of a different
stamp. Instead of idolising knowledge he declared the untaught peasant
and artisan the superiors of the philosopher and man of culture. They
alone, he said, had retained that natural goodness of heart which
men had in times long since gone by, when social inequalities along
with idleness and luxury were unknown. Rousseau opposed also the
atheistic tendencies of the day, declaring belief in a personal God
and the immortality of the soul requisite to make life endurable to
the oppressed. His indifference to knowledge and culture caused him to
regard the masses themselves as alone able to regenerate France, if
indeed regeneration were still possible. Society, according to him,
was originally based on a contract by which every citizen in return
for protection of person and property placed himself under the general
will. Laws, therefore, were the expression of the general will; kings
were merely the servants of the people, and not they but the people
sovereign. Whatever was amiss in France, or in other countries, the
fault lay purely with society and government, and should ever idleness
and luxury disappear and the people recover their lost sovereignty,
then and then only, as in primitive times, would men be happy and
virtuous. ‘Man is born free,’ were the opening words of the ‘Social
Contract,’ the book in which these theories were maintained, ‘and
everywhere he is in chains.’




CHAPTER II.

FRANCE UNDER LOUIS XVI. (1774–1789).


When the necessity of reform had been demonstrated by a band of
powerful and brilliant writers, whose works were the popular reading of
the day, it was inevitable that desire for change should grow, as the
new ideas spread over wider circles, and sufferers from abuses became
more and more alive to their wrongs. Undermined by public opinion,
the existing order could not endure for long, and the vital question
before France was, by what means change should be accomplished. The
Voltairians called on the King to take the work in hand, and on the
death of Louis XV. in 1774, it appeared possible that the young Louis
XVI. would endeavour to regain the path that his predecessors had
abandoned, and, by relieving the people from their burdens, seek the
welfare of the entire nation. ♦Turgot’s Ministry.♦ Turgot, the new
Controller-General, who exercised the functions both of Minister of
Finance and Minister of the Interior, represented the party of reform,
and was in all his actions inspired by a strong love of knowledge and
by a passionate desire to benefit his fellow-men. He was not, like
the writers of his time, a mere theorist, but also a practised and
successful administrator, who for thirteen years had been Intendant of
the poor province of Limousin. Now that he was invested with higher
authority, it was Turgot’s aim to ameliorate the condition of the
people throughout France, by the introduction of reforms based on
those principles of equality and individual liberty which Voltairians
and Economists proclaimed. His chief reforms were the abolition of
restrictions on the internal trade in corn and wine; the abolition of
the _corvée_, or forced unpaid labour of the peasants for repair of
roads, for which he substituted a land-tax payable by all proprietors
whether privileged or not; and finally, the abolition of guilds, giving
liberty to every one, however poor, to exercise what trade he pleased
and to raise his condition according to his capacity. Besides these,
his most important measures, Turgot carried out many lesser reforms
tending to set labour and industry free, to cheapen food and clothing,
and to lessen the burdens of the poor by the equalisation of taxation,
and by the abolition of the fiscal abuses and sinecure offices which
enriched the monied aristocracy of Paris and the court nobility. The
reforms, however, which Turgot accomplished were but a small portion
of those which he had in contemplation. He aimed at the remodelling
of the whole system of taxation, the removal of all custom-houses to
the frontier, the abolition of the _gabelle_, and the substitution for
the _taille_ of a new tax to be imposed on the land of all proprietors
without exception, the gradual abolition of feudal dues, the grant
of civil rights to Protestants, and, finally, the decentralisation
of administration by the establishment of provincial assemblies, to
be elected by all landed proprietors without distinction of rank.
His work was no sooner begun than it was prematurely cut short. A
violent opposition party was at once formed, which comprised the court
nobility, the upper clergy, the nobility of office, farmers of the
_gabelle_ and other indirect taxes, judges in Parliament, masters of
guilds and state officials--in a word, all those who made profit out of
existing abuses, and whose special privileges were assailed. ‘Everybody
fears,’ a friend of Turgot wrote to him, ‘either for himself, or for
his brother, or for his friend.’

♦Louis XVI.♦

Whether Turgot was to stand or fall depended entirely on the resolution
of the King. Louis XVI. was well-intentioned, conscientious, and
sincerely desirous of ruling for the good of his subjects, but he
lacked the qualities which are requisite to a prince called on to
govern at a great national crisis. He was without self-confidence,
irresolute in action, and incapable of judging the real value of men,
or of grasping the real bearing of events and measures. He could not
even rule his own court. Simple in his tastes, and shy and reserved by
disposition, his happiest hours were spent in the hunting field, or
in the company of a blacksmith, mastering the art of making locks. It
was no wonder that such a King should be driven to and fro between
conflicting opinions, when those who surrounded his throne, and with
whom he came in daily contact, accused his Minister of violence and
injustice, and of entertaining projects destructive to monarchical
government. ‘The King,’ said Turgot, ‘is above all, for the good of
all.’ Louis could never rise to this conception of his position.
Turgot would have made him ruler of men equal before the law, and in
possession of equal rights as citizens. Desirous as Louis was to ease
the lower classes of their burdens, he was never able to conceive
of the noble as being on the same footing as the common man. ♦Marie
Antoinette.♦ The only person in whom he reposed confidence was his
wife, Marie Antoinette, a daughter of the Empress Maria Theresa, and
with fatal weakness he often yielded to her desires in opposition
to his own better judgment. She had been married to him while still
a child, and left to grow up uninstructed and without guides in the
corrupt atmosphere of the court of Versailles. At the age of nineteen,
when she became Queen, she was a bright and vivacious, but ignorant
and thoughtless woman, whose days were spent in a never ceasing round
of formalities and dissipation. She employed her influence over her
husband to obtain for her friends pensions and offices, without any
sense of what was due to her position as Queen in the midst of a
frivolous and intriguing court, or of what she owed to the starving
and suffering masses who were deprived of their hard-won earnings for
the enrichment of an idle and spendthrift nobility. When ministers
sought to put a check on her extravagance, or in any way thwarted her
inclinations, they provoked her resentment, dangerous in proportion to
the power that she was able to exercise over the King. Her aversion
to Turgot was the cause which finally produced his dismissal from
office. The Austrian ambassador, Mercy, informing Maria Theresa of the
event, used words of more pregnant meaning than he was himself aware.
‘The Controller-General,’ he said, ‘is of high repute for integrity,
and is loved by the people; and it is therefore a misfortune that his
dismissal should be in part the Queen’s work. Such use of her influence
may one day bring upon her the just reproaches both of her husband and
of the entire nation.’

Turgot was the greatest statesman that France had seen since Richelieu.
He had a clear comprehension of the economical and social evils under
which the country suffered, and of the remedies to be applied to them.
The best ideas of the age found room in his capacious mind, and all
that he attempted to do had ultimately to be accomplished, though by
other means than those which he contemplated. Louis had shown his
incapacity to see that it was his first duty to make himself the
repairer of wrong and injustice, and truly a representative king, who
could say, ‘I am the nation.’ After Turgot’s failure, revolution,
that is to say change accompanied by violence and convulsion, became
inevitable.

♦Reforming movement a European one.♦

The reforming movement, of which in France Turgot was the
representative, was not confined to that country, but was, in fact, an
European movement, of which the influence was felt, however faintly,
even in the most backward States. Kings and statesmen, under the
influence of Voltairian ideas, held sceptical opinions, and took
interest in the material condition of their subjects. It was perceived
that if monopolies enriched individuals they prevented the development
of commerce and industry; that if duties were levied between the
provinces of the same kingdom, exchange of commodities could only
with difficulty be effected; that if nobles did not pay their fair
share of taxation, the revenue of the State suffered, and the working
classes were overburdened. Jealous eyes were cast upon the territorial
wealth of the Catholic Church, and protests were raised against the
multiplication of monasteries, and the idle lives led by their inmates.
In many States efforts were made to increase the authority of the king
by the destruction of provincial and class privileges. The idea that
the sovereign reigned for the good of the nation was accepted, at
least in theory, by the most autocratic of European princes. In Russia
Catherine II., in Prussia Frederick II., invited to their courts and
patronised French philosophers. In Spain Aranda, in Tuscany Manfredini,
in Portugal Pombal endeavoured to lessen the privileges of nobles
and clergy, and to loosen the bonds in which industry and commerce
were held. In Savoy feudal charges were abolished, compensation being
given to the proprietors. In Parma, in Brunswick, and in other Italian
and German states, similar tendencies were manifested. But although
the reforming movement, on the lines laid down by Voltaire and the
Economists, was not confined to France, nowhere else was there to be
found amongst the people any strong desire for reform. In Germany,
in Spain, in Italy, the new views were confined to a few theorists
and statesmen, and did not penetrate beneath the surface of society.
The cause lay in the difference of social conditions. Outside France,
nobles, as a rule, lived at home on their estates, still administering
justice to peasants and serfs. The middle class took no interest in
matters of government, but devoted its energies to scientific and
literary pursuits. The lower classes, being still in dependence on the
upper, entertained no lively resentment of their privileges. Hence
reforming princes could never accomplish more than a few isolated
changes without danger of rousing rebellion. Nobles and clergy, the
moment their privileges were threatened, offered opposition; the
middle class did not care to render support; the lower classes were
more ready to follow the lead of nobles and clergy than the lead of
the government. Of all the princes of his time the Emperor Joseph II.
was the boldest innovator. In his hereditary dominions he offended the
nobles by the abolition of provincial states, the clergy by closing
monasteries and upholding principles of toleration, the people by
alterations in their religious services. An insurrection broke out
in Belgium under the leadership of nobles and clergy (1789). Both in
Galicia and Hungary the nobles threatened to take up arms, and for a
time it seemed as if the Austrian dominion would fall to pieces.

♦England.♦

In England the same ideas prevailed as on the Continent, but the social
and political condition of the country was such as to enable reforms
to be accomplished more gradually and with far less violent change
than was possible either in France or Austria. The English people had
for centuries formed an united nation. No sharp lines of division
divided one class from another. The laws were the same for all: younger
sons of noblemen ranked as commoners, and country gentlemen sat in
Parliament by the side of merchants and traders. A free press prepared
the way for change by allowing the discussion of questions of general
interest, and free institutions gave political experience, and taught
the governing classes the necessity of yielding in time to public
opinion. Parliament, which represented only the landed and commercial
interests, legislated selfishly, and was slow to admit or redress wrong
done to the unrepresented classes; but gross oppression of the lower
orders, such as existed in France, was unknown in England. Country
gentlemen looked after the affairs of parish and county. The body of
the rural population consisted of agricultural labourers maintained
by poor-rates when wages fell short. Charges on land due to the lord
of the manor, though far from being extinct, existed mainly in the
form of money payments, affecting only a comparatively small number of
persons. Although the same protective principles which prevailed on
the Continent prevailed also in England, whatever restraints were laid
either on persons in the selection of their calling, or on industry,
commerce and agriculture, there was to be found far more liberty than
elsewhere. The country was the most flourishing in Europe, and wealth
was being rapidly accumulated. Special advance was made in the system
of farming by the introduction of the rotation of crops and artificial
manures. Wages rose, and bread was cheap, and all classes for a time
shared in the general prosperity.

In England a large body of eminent men, philosophers, statesmen, and
philanthropists, entertained the new ideas and sought to bring them
into practice. In 1776, Adam Smith published the ‘Wealth of Nations,’
in which the principles of free trade were promulgated. The younger
Pitt, who took office in 1783, was his disciple. He proposed to abolish
restrictions on the trade of Ireland with England, and intended to
lessen the power of the aristocracy by a reform of the electoral
system. In 1787 a Treaty of Commerce was concluded between England and
France, designed to increase trade between the two countries. The most
important measures brought forward by Pitt were not, however, carried
through Parliament. This was in part owing to the factious opposition
of the Whigs, in part to the strong Conservative instincts of the
governing classes, but in part also because little discontent or desire
for change existed among the people at large.

♦Ministry of Necker.♦

If, however, England was slow to move, reforms once made rested on a
sure foundation. Such was not the case with those made in the name of
absolute princes on the Continent. After Turgot’s dismissal, fifty
out of seventy of the guilds which he had abolished were revived,
and the peasants were compelled by blows to resume their labours
on the roads. Necker, a Genevese banker, was Turgot’s successor
(October 1776). He was not a statesman, like Turgot, with definite
aims in view, but he was an able financier and a humane man, holding
the philanthropic sentiments of the day, and eager to relieve the
condition of the masses. A war with England increased the difficulties
of the government. In 1778 Louis, reluctantly following public
opinion, assisted the English colonies in America in their struggle
for independence. There were only three means of meeting the expenses
of the war: increased taxation, economy, and loans. The first was
impossible; the second only possible to a limited extent; and Necker,
therefore, was compelled to borrow. The loans that he opened were
quickly filled up, because men of the middle class, who were the chief
lenders, believed that their interests were safe while he directed the
finances. But the public debt was greatly increased, and the prospect
of the future, with reforms uneffected in the system of taxation,
rendered them more dark. Although Necker did not attempt to introduce
radical measures such as had excited opposition against Turgot, his
abolition of sinecures and other administrative changes gave offence
to the same classes. The Parliament of Paris, whose lead was followed
by the twelve provincial Parliaments, formed the chief organ of
resistance. These Parliaments or law-courts were, in fact, powerful
legal corporations to which many hundred persons were attached. The
judges belonged to the nobility of office, and were independent of the
government, since they held their offices in right of purchase, and
might not be dispossessed without proof of misconduct. They exercised,
besides judicial, a certain political function, since edicts of the
King’s council did not have the force of law until they had been
registered by the Parliaments. This right of registration in the
time of Louis XIV. had been a mere form. If the Parliament of Paris
hesitated to carry out his wishes, he held a so-called bed of justice
when he came to the court in person, and on his command registration
was compulsory. But now that the royal authority had fallen into
contempt, the Parliaments offered prolonged resistance, and before
the Government could obtain registration of its edicts, intimidation
and even the use of military force were resorted to. Necker, when he
sought to effect reform, necessarily became involved in quarrels with
the Parliaments, and, finding that the King gave but a half-hearted
support, he resigned office (1781).

♦Desire for political liberty.♦

Louis could relieve himself from momentary inconvenience by abandoning
a Minister of whom he was weary, but had no power to stay the course
of events. Those who had lent money to the government deeply resented
Necker’s fall, because they believed him able to secure regular payment
of the interest on the national debt. Desire for social change was
accompanied by desire for political change also. Rousseau had said
that the people was sovereign, and as the incompetency of the crown to
carry out the national will became with each successive ministry more
manifest, ideas long since vaguely floating in men’s minds gathered
strength and consistency. The cause of the American colonies was taken
up with immense enthusiasm. The Declaration of Independence (July
4, 1776), which, in accordance with the principles laid down in the
‘Social Contract,’ asserted that all men were created equal and endowed
with the natural right of overthrowing an unjust government, was hailed
as the enunciation of an universal truth, of which Frenchmen as well as
the colonists might reap the benefit. Meanwhile government in France
grew yearly more utterly weak and helpless. The war with England ended
in 1783, but financial embarrassments increased. ♦Calonne.♦ Calonne,
who became Controller-General the same year, pursued Necker’s system of
borrowing without his justification, and retained office by abstaining
from acts calculated to offend the privileged classes. The demands
of the Queen and the Court were complied with, and abuses destroyed
by Necker again called into existence. ‘If it is possible, madam,’
said the obsequious Minister, on an occasion when the Queen pressed
him for money, ‘it shall be done; if it is impossible, it shall be
done.’ But such squandering of the revenue could not last for ever.
Calonne’s credit broke down, and he was driven as a last resource to
propose the reform of the entire system of administration and taxation.
By publicity he hoped to overcome resistance. He called together an
extraordinary council or assembly of notables, nominated by the King
(February 1787), and laid his propositions before them, thinking that
in the existing state of opinion they would not venture to refuse
support. But this assembly, composed almost entirely of privileged
persons, proved recalcitrant. The majority were against the reforms
proposed, while the few who approved them were determined that they
should be made by an assembly representative of the nation.

♦Brienne.♦

Calonne gave place (1787) to Brienne, Archbishop of Toulouse, the
candidate of the Queen; but the new Minister had no choice except
to take up the plans of his predecessor, and the government became
involved in incessant strife with the Parliaments. The Parliaments
concealed their aversion to the principle of equality of taxation, by
denying the right of the King to impose new taxes without the consent
of the nation, and by demanding the meeting of the States-General.
The government, on its side, sought popularity by coupling edicts
for raising loans and taxes with reforming measures. But it could
obtain no support. The shifting policy which it had so long pursued,
the attempts at reform, made, abandoned, and then made again, had
destroyed confidence alike in its power and its good-will. Hence,
although the Parliaments defended the privileges of nobles and
clergy, their resistance was applauded, because it offered the surest
means of forcing the King’s hand, and leaving him no alternative
but to summon the nation to his aid. Along with equality, the word
‘liberty’ was on every man’s lips. The very nobles, who had so long
opposed administrative and economical change, had themselves become
vehement advocates of political change. More afraid of the crown than
of the classes beneath them, and blind to the complete isolation of
their own order, they looked forward to being at once leaders of a
political revolution and guardians of their own interests. In fact,
the privileged orders had no choice but either to submit at discretion
to the King, or to join in the popular cry for the meeting of the
States-General. Arbitrary attempts made by Brienne to free the crown
of dependence on the Parliaments failed, in the face of resistance
offered by all classes, and brought the country to the verge of actual
insurrection. Disaffection was rife in the army. Peasants and artisans,
excited by expectation of better days, were more ready than before to
rise in insurrection against local authorities, and were less easily
quelled. State bankruptcy impended. There was a deficit in the revenue
of more than 2,000,000_l._, and money was wanting with which to pay
the interest of the national debt. Under such circumstances Louis
reluctantly yielded to the demand made on every side. He declared his
intention of summoning the States-General and in order to regain
confidence restored to the head of the finances his former and still
popular minister, Necker (Aug. 1788).

♦Necker recalled to office.♦

Necker’s return to office was greeted with a burst of applause from
one end of France to the other. His financial ability was relied on to
stave off bankruptcy, and it was known that he had always opposed the
court, and that he now desired the meeting of the States-General. But
his popularity was due to those causes alone; not to any proof that he
had given or could give of his fitness to direct the royal policy. As
he failed to comprehend the real causes of the impending revolution, he
would be unable to moderate its violence.

♦Pamphlets and cahiers.♦

The hopes and desires of every class found expression first in
pamphlets, and subsequently in the _cahiers_ or petitions of grievances
drawn up by electoral assemblies to be laid before the States. The
importance and necessity of reform was generally admitted, except
where special interests or class prejudices made men averse to change.
Thus nobles combated the conservative tendencies of ecclesiastics,
ecclesiastics the conservative tendencies of nobles. Induced by
pressure of public opinion the nobles mostly declared their willingness
to admit the principle of equality of taxation. But agreement went no
further. Between the two privileged orders and the body of the nation
a gulf was fixed, of bridging which no hope existed. That which the
nobles had in view by the meeting of the States was the establishment
of constitutional monarchy, based on aristocratical institutions
and insuring political and social predominance to their own order.
The aim of the middle and working classes was absolutely to destroy
every distinction which gave to nobles and ecclesiastics a position
apart in the State. The members of the upper orders were not only to
bear their fair share of taxation, but to submit to the same law,
and to stand in all respects on exactly the same level as the mass
of their fellow-citizens. A pamphlet written by the Abbé Siéyès,
which gave clear articulation to the thought in men’s minds, acquired
for its author European celebrity. What, he asked, is the Third
Estate?--Everything. What hitherto has it been in the State?--Nothing.
He then proceeded to argue that the Third Estate, in other words the
people of France with the exception of the nobles, formed a complete
nation by themselves; that by them all useful work was done; and that
the nobility was merely an excrescence, preventing the growth and
development of national life. The Third Estate is, he said, a nation
fettered and oppressed. What would it be without the nobility?--A free
and flourishing nation.

Siéyès’ nation was a nation of twenty-five millions. The first two
orders numbered together about 1,500,000 persons. That they were
a minority was in itself no ground for crushing them. Reason and
justice might as well lie on the side of the minority as on that of
the majority. But Siéyès’ arguments were in existing circumstances
perfectly sound and unanswerable. The nobles represented no national
interests, and had long ceased to be the organs through which the
nation expressed its wants. To the exercise of political powers they
had no claim whatever. Their privileges and prejudices had for years
stood in the way of the common good. They were without experience
in political life, and as a rule without experience even in matters
of government and administration. Their position amongst their
fellow-citizens was that of an isolated caste; in short, all the bonds
of connection were wanting which cause men to place reliance in others,
and to accept them as leaders.

The privileges of the clergy and their claims to exercise power as
a special order met with as little favour as those of the nobles.
Clergy and laity were to stand on exactly the same footing with regard
to civil and political rights. The combined influence of sceptical
and liberal ideas made men desire to withdraw from the Church all
coercive means of maintaining authority. The press was to be free,
worship was also to be free, and nonconformists were to enjoy full
civil and political rights. Equality was to prevail within the Church
as well as within the State. The government of the Church was to be
reorganised on a democratic basis, and the Pope’s authority, as head
of the Church, to be confined to matters purely spiritual. Although
the provincial nobles were jealous of the great lords, and desired to
deprive them of whatever advantages they possessed above themselves,
yet the nobility as a body still formed a caste, of which all members,
except a small minority, were united in asserting rights and claiming
privileges in opposition to the rest of the nation. The clergy, on the
contrary, though held together by common interests as ecclesiastics,
were torn asunder by the same class divisions that prevailed amongst
laymen. The upper clergy, who were all of noble birth, proposed to
maintain authority in their own hands and to effect ecclesiastical
reform from inside; while the curés, who came from the ranks of the
people, demanded State interference, as the only means of securing for
themselves a full representation in Church councils, and a just share
in the distribution of Church property.

♦Double representation of the Third Estate.♦

The question round which for the time discussion centred was the form
to be taken by the States-General, as its solution would decide whether
political supremacy should rest with the first two orders or with the
Third Estate. Nobles and clergy demanded, in the first place, that they
should each be represented by as many deputies as the Third Estate; in
the second, that the deputies of each order should sit by themselves
in a separate chamber, and that each chamber should vote apart. The
bourgeoisie, backed by the people, on their side denied the right of
the two first orders to a separate representation, and demanded that
in any case the deputies of the Third Estate should equal in number
the deputies of nobles and clergy combined, and that the three orders
should sit together, forming a single chamber. The dispute engendered
strong displays of party feeling, leading to riot and bloodshed. The
Parliaments, formerly popular for contesting the royal authority, were
now hooted and mobbed for supporting the demands of nobles and clergy.
If at the present juncture Louis had taken clearly and unreservedly the
side of the nation, it might have been possible for the crown to gain
immense popularity and influence. The bourgeoisie, however democratic
its theories of government, was warmly attached to the monarchy, and
thoroughly loyal to the person of the King. But Louis, who had rejected
Turgot, was again incapable of making himself the leader of the nation.
In summoning the States he had acted, not through policy, but under
stress of circumstances which he was unable to control. He expected the
deputies of the Third Estate to aid him in subjecting the nobles to
taxation, and in carrying out administrative reforms; but he could not
understand that they expected him to join with them in destroying every
vestige of the old feudal system, and in establishing a completely
democratic rule. In relation to the point immediately at issue, the
King went so far as it seemed to suit his own purpose, and no further.
Accepting Necker’s advice, he consented that the deputies of the Third
Estate should equal in number the deputies of both clergy and nobles.
Whether after meeting the deputies were to sit as three chambers or as
one was left undecided.




CHAPTER III.

THE ASSEMBLY AT VERSAILLES.


♦The King and the Revolution.♦

The States-General were opened by the King at Versailles amid a vast
concourse on May 5, 1789. There were about 1,200 deputies, of whom
about 300 represented the clergy, 300 the nobility, and the other
600 the Third Estate. If the King wished to retain the direction of
affairs, it was imperative for him at once to declare for a single
chamber. The privileged orders could but involve the crown in their
own ruin, whilst behind the deputies of the Third Estate was the
nation. Louis, however, was not prepared to accept the change which
the formation of a single chamber implied--the abolition of all class
distinctions, and the swamping of the nobles in the Third Estate.
Necker, though more alive to the necessity of seeking popular support,
had as little comprehension of the real situation in which the
government stood. He wanted ultimately to establish a constitution
with two houses, and regarded as the most pressing work of the moment
the restoration of the finances. He did not perceive that civil and
political equality was what the deputies of the Third Estate had set
their heart upon effecting; and that until they were convinced that
the government would be on their side, they would pay no attention to
mere financial or administrative reforms. At the opening of the States,
after speaking at length on the subject of the finances, Necker advised
the deputies to appoint commissioners to settle what questions they
would discuss in common session, and what as three separate bodies.

The intention of the Minister probably was that the deputies of the
three orders should sit and vote together only when financial and
administrative questions were under discussion. All other subjects were
to be debated by the three estates sitting apart; and in cases in which
they failed to come to an agreement, the final decision was to be left
to the King.

Experience, indeed, has been in favour of the belief that, in ordinary
times, it is expedient that legislative assemblies should be divided
into two chambers. But in 1789 the work before the States-General was
not one of ordinary legislation. No good could be accomplished until
the abolition of the privileged existence of nobles and clergy had
been effected; and as an upper chamber could at that time only be
composed of nobles and clergy, such a chamber was certain to thwart
the Third Estate in doing that which the nation expected them to do.
It was, therefore, the vainest hope that Necker’s policy should give
satisfaction to the country and enable the King to retain authority.
He could only obtain the leadership of the Assembly by declaring
unreservedly for a single chamber. But to adopt this course Louis
must have been other than he was. Though he wanted to overcome the
opposition of the privileged orders to the crown, he regarded their
existence as inseparable from the monarchy. He was unable to conceive a
monarchy founded on democratic institutions, and strong in proportion
to the trust reposed in it. Education, surroundings, habits, his sense
of duty itself forbade him to break loose from his past and accept the
position of the People’s King. Yet all vestiges of the old feudal order
were doomed to perish, whatever attitude Louis assumed; and it would
have been well, both for him and France, could he at once have resigned
power or been deposed. For if he refused to lead the attack upon the
privileged orders, it would be made with all the greater violence,
and government, in the true sense of the word, there would be none.
Already disorder and riot were rife in many parts of the country.
Peasants refused to pay taxes and feudal dues. Educated men cast
suspicion on the intentions of the government. Officials were powerless
to act with rigour in opposition to the current of public opinion.
Intense excitement everywhere prevailed. In every town and hamlet men
waited with eagerness for the speedy accomplishment of the desires
which had found expression in the _cahiers_ drawn up to be laid before
the States.

♦Mirabeau.♦

If Louis was unable to forecast the future, so too was the great mass
of his subjects. Amongst the throng of deputies who met together
at Versailles, there was but one, the Marquis of Mirabeau, who
comprehended the real meaning of the revolution, and foresaw with
accuracy the course which events would take. This remarkable man was
endowed by nature with enormous energy, mental and physical. While
still a youth, he had left his mark for good or for ill wherever he
went. He had incurred debts, fought duels, kept order amongst hungry
peasants, eating, drinking, and working with them, obtained the
good-will of men prejudiced against him, and won the hearts of women.
His father, according to the fashion of the time, supported paternal
authority by obtaining _lettres de cachet_ from the government,
ordering the imprisonment of his son. Mirabeau was imprisoned, now in
one fortress, now in another, for months at a time. In early manhood,
at the age of twenty-eight, he entered the donjon of Vincennes, a state
fortress, where he inhabited a dark, barely-furnished room, and had
converse with none but his gaoler. His offences against social order
had not been light, for he had deserted his own wife for the wife of
another man. But in his vices Mirabeau was but a type of the generation
to which he belonged, and the real ground of his imprisonment lay
elsewhere. Books and paper were as a favour allowed him. ‘Without
books,’ he wrote, ‘I should be dead or mad.’ He read and wrote for
fifteen hours out of the twenty-four. After a confinement of more
than three years, the quarrel between him and his father was patched
up. In 1780 he was released, broken in health, harassed by debts, and
blackened in fame, but possessed of a large store of knowledge, a ready
pen, a fluent tongue, and a genius for statesmanship which no man in
France could rival. Genius was, however, no ground for advancement.
A man who had sufficiently powerful interest at court might rise to
the highest dignities in Church or State, whatever his incapacity,
or whatever the stains on his past life. Mirabeau had no interest at
court, while by Louis and his councillors talent was distrusted, and
the one statesman that France possessed occupied the position of an
unscrupulous adventurer, seeking by whatever means came first to hand
to force his way into the ministry. It was no matter of surprise that
so signal a victim of arbitrary government should prove an inveterate
enemy to the existing order. But Mirabeau did not, through resentment
for personal injuries, desire to weaken or degrade the royal authority.
He possessed too strong a capacity for the exercise of power. He saw,
moreover, too directly into the heart of the situation. He comprehended
what no man but himself comprehended at that time, that the real aim
of the French people was the sweeping away of all class distinctions,
and that the monarchy might be immensely strong if only the King could
be brought to adopt new principles of government, in accordance with
the democratic spirit of the age. Had he been at the head of affairs
he would at once have summoned the States-General and led the way
in opening the attack upon the privileged orders. Excluded from all
share in the government, he revenged himself by attacking it on every
side. The proposition was made to him that he should employ his pen
to destroy the popularity of the Parliaments. ‘I will never,’ was
his reply, ‘make war upon the Parliaments except in presence of the
nation.’ The hesitating and shuffling policy of the ministers; their
vain attempts to effect reform through the royal power alone; their
efforts to avoid or defer the meeting of the States; and, finally,
their refusal, after being driven to call the nation to their aid, to
declare for a single chamber, excited his scorn and indignation. He had
not only the clear perception that in order to maintain the monarchy
the first thing to be done was to crush the privileged orders; he had
also the clear perception that the second thing, if indeed it was not
of equal importance, was the organisation of government, and that this
was impracticable so long as distrust existed between the crown and
the nation. When the elections were held, rejected by his own order,
he took his seat as representative of the Third Estate of Aix. At
Versailles he was the mark of all observers. The wildness of his youth,
his long imprisonment, his quarrels with his father, his lawsuits with
his wife, his writings, and his eloquence, had given him notoriety
throughout France. With the meeting of the States Mirabeau knew that
the opportunity had come of making his power felt. ‘At last,’ he said,
‘we shall have men judged by the value of their brains.’

♦Title of National Assembly adopted by the Third Estate.♦

The inevitable consequence of the King’s refusal to declare himself
against the privileged orders at once ensued. Disputes arose between
the deputies as to the form that the legislature should take. There was
a small minority of nobles for union, and a large minority of clergy,
composed almost entirely of parish priests, who had to choose between
alliance with the Third Estate and dependence on their ecclesiastical
superiors. The questions at stake were too vital for compromise to be
possible, and thus, while the people impatiently awaited redress of
grievances, the Third Estate refused to proceed to business until they
were joined by the other two. Political excitement grew greater amongst
the middle classes, irritation and discontent amongst the lower. The
winter had been one of the coldest and longest on record. The price of
bread was rising, and misery, which sufferers expected to vanish on the
first meeting of the Estates, was on the increase. It had always been
a difficult matter to prevent rioting at Paris in times of political
excitement or of scarcity, and now both causes combined to create
disorder. In the Faubourg St. Antoine and other poor quarters of the
city existed a population including great numbers of ruffians, beggars,
and destitute workmen, of whom many were strangers from the country,
largely brought to Paris by hope of finding bread or labour, and whose
passions might readily be worked on with dangerous effect; while
pamphleteers and street orators, without sense of responsibility, and
full of passionate desire to assure the triumph of the Third Estate,
did not measure their words in seeking to rouse popular indignation
against the upper orders. Deputies distinguished as opponents of union
were mobbed and hustled at Versailles, and their names held up to
execration in Paris. The attitude of the capital gave strength to the
deputies of the Third Estate, who finally cut the knot by adopting the
title of National Assembly, inviting nobles and clergy to join them,
and declaring their purpose of proceeding to business without those who
refused to do so (June 17).

♦Royal sitting of June 23.♦

The assumption of this title was held an act of usurpation by the
opponents of union. Court nobles and ecclesiastics appealed to the
King to maintain the authority of his crown by interfering in support
of their rights. The deputies of the Third Estate had, it was said,
grasped at sovereign power to which they had no claim. As yet there
had been no direct collision between the Crown and the deputies of the
Third Estate. The long inefficiency of the King had, indeed, destroyed
belief in the royal power as an instrument of government. Men believed
in themselves, and they believed in the nation. They demanded liberty
for individuals, and they demanded that the nation should govern
itself. Yet, however democratic were the theories that prevailed, the
great body of the French people was deeply attached to monarchy as a
form of government, and thoroughly loyal to the person of the King. If
desire for the establishment of a democratic constitution was intensely
strong, there appeared no other means in the first place of destroying
the upper orders; in the second, of preventing their resurrection. Had
Louis taken the side of the nation, he might, as Mirabeau foresaw, have
exercised immense influence over the course of affairs. If he refused,
nominal sovereignty would be left to him, but men would be careful
that he should have no real power in his hands. Louis was honestly
prepared to cede constitutional rights to the country, which should set
limits to the royal authority, and secure the persons and properties
of his subjects against arbitrary usage. But he would not, so far as
he could prevent it, suffer the abolition of class distinctions, or
allow the real governing power to pass from himself and his council to
the representatives of the nation. Thus, although the deputies of the
Third Estate sought to conceal the fact from themselves, they had to
contend against the Crown as well as against the nobility. Louis, in
alarm for his authority, now thought to maintain it by openly taking
the part of nobles and clergy. Marie Antoinette, less patient than
her husband, witnessed with extreme resentment and indignation the
conduct of the Third Estate. To excited courtiers it seemed as easy a
matter for the King to impose his will on the representatives of the
nation as it had been for his predecessors in times past to impose
theirs on the Parliament of Paris. It was determined that the King
should hold a royal sitting or séance, and declare his intentions to
the assembled Estates. Meanwhile the deputies of the Third Estate were
excluded from their hall on pretext that preparations had to be made
for the reception of the King. Fully expecting a dissolution, they
repaired to a neighbouring tennis court, where with one voice and
hands raised to the sky they swore an oath never to separate before
they had established constitutional government. There was a dense
crowd outside. All approaches to the court were blocked, and the one
deputy who refused to take the oath was with difficulty saved from
outrage (June 20). The cause of the upper orders was now weakened by
desertions from their ranks. A large number of curés as well as a few
nobles joined the deputies of the Third Estate. This in itself, had
Louis been well advised, might have warned him against the course that
he proposed to take. On June 23 he came in state to the hall, where the
whole body of deputies was by his injunction assembled. There, by the
mouths of his ministers, he told them that they were to meet as three
separate orders. With his consent first obtained, they might form one
assembly for the discussion of matters of common interest; from which,
however, all the burning questions of the day, ecclesiastical, social,
and constitutional, were expressly excepted. Necker, who disapproved
the arbitrary form in which the royal will was signified, saved his
popularity by refusing to be present on the occasion. Before retiring,
Louis ordered all to disperse and assemble next day in their separate
chambers. In case of disobedience he would undertake by himself to
secure the happiness of his subjects. ‘Seul,’ he said, ‘je ferai le
bien de mes peuples.’ After he had gone, most of the nobility and the
upper clergy left the hall; but the deputies of the Third Estate as
well as many curés kept their seats. The Master of the Ceremonies, De
Brézé, asked Bailly, the President, whether he had heard the orders of
the King. ‘Yes, sir, we have heard the orders put in the King’s mouth,’
retorted Mirabeau, in words repeated and applauded throughout France,
‘and let me inform you that if your business is to turn us out, you had
better ask orders to employ force, for we shall only quit our seats
at the bayonet’s point.’ Before dispersing the recalcitrants declared
their persons inviolable for all that they said or did as deputies.

♦Union of the three orders.♦

After this defiance of the royal authority, the Queen and the court
would gladly have obtained the dissolution of the States. Difficulties,
however, stood in the way. The financial embarrassments of the
Government were still unrelieved. Further, it was clearly impossible
for the King to cause his commands to be obeyed, unless he was prepared
to appeal to military force, and the consequences of so doing were
exceedingly doubtful. Class distinctions prevailed in the army as in
other institutions of the old system. The officers, who were all noble,
lived in luxury, largely on perquisites made at the men’s expense.
The men, cheated of their pay, badly fed, and subjected to a harsh
discipline, bitterly resented their wrongs, and despised and hated
their officers. If an attempt were made to use intimidation there was
great probability that resistance would be offered, that Paris would
rise, and that the troops would refuse to fire on the insurgents.
Louis was never willing to take decided action, and, for the time, the
deputies of the Third Estate were left in enjoyment of victory. The
King himself requested the nobles and ecclesiastics, who still kept
aloof, to abandon further struggle, and thus after a delay of seven
weeks the three Estates were finally constituted as one assembly.

♦Excitement in Paris.♦

The evil consequences of that delay were already but too plainly
apparent. Since the meeting of the Estates agitation in Paris had
spread from day to day. The Government, unable to use arbitrary and
violent means of obtaining order, could no longer effectively perform
its duties, because no trust was reposed in it. Political liberty
threatened to degenerate rapidly into anarchy. No moral restraints
existed amongst a people for centuries unaccustomed to self-government.
There was no political organisation, and no standard of political
morality. There were no recognised leaders weighted with a sense of
responsibility, nor journals with a character to maintain. Appeals were
made to the lowest passions, rumours and libels circulated without
question of their truth or justice. The fiercer and more bitter his
language, the more sure was the orator or journalist to gain a hearing
and exert influence.

In the garden, surrounded by book and coffee shops, which was
attached to the Palais Royal, a palace belonging to the Duke of
Orleans--who, although distantly related to the King, had taken the
popular side--agitators, mounted on chairs and tables, discoursed to
excited throngs on the sovereignty of the people, and denounced the
opponents of a single chamber to popular wrath. Here neither police
officers nor supporters of the claims of nobles and clergy could
enter except at peril of violent and brutal usage. This licence was
the more dangerous because the hard times made the people more ready
for the commission of criminal actions. Nevertheless, the tradesmen,
merchants, and other persons in the middle class of life, who
under ordinary circumstances are the first to feel the effects of mob
violence, regarded the designs of the court as far more dangerous than
the oratory of the Palais Royal. For while the court demanded the
maintenance of class distinctions, the demagogues of the Palais Royal
demanded their abolition, guaranteed by the establishment of a free and
democratic constitution.

[Illustration: REVOLUTIONARY PARIS

_Longmans, Green & Co. London, New York, Bombay, Calcutta & Madras_.]

♦The fall of the Bastille, July 14.♦

The government, on the pretext of maintaining order, quartered round
and in Paris and Versailles regiments of Swiss and German troops
in the service of France. The Queen and the Court desired, if not
immediately to dissolve the Assembly, to compel its removal to some
provincial town, where the deputies might more readily be forced to
accept the terms offered by the King on June 23. Necker, supported by
a minority of his fellow-councillors, was opposed to any plans for the
intimidation of the Assembly; but he had no influence with the King,
and was detested by the Queen and the King’s brothers, the Counts
of Provence and Artois, of whose projects he was left in ignorance.
Louis relied on the troops to overawe the capital, but was averse to
resort to military force unless in self-defence. Meanwhile, their
neighbourhood increased excitement in Paris, and the middle classes
found themselves between two fires. On the one side they feared an
armed occupation of the town, and the proclamation of martial law; on
the other a rising of the populace, which might end in the dissolution
of all authority. The elections of deputies of the Third Estate had
been by two degrees. Paris had been divided into sixty districts,
returning 120 electors, who had elected twenty deputies to sit in
the States-General. These electors, wishing to induce the Government
to remove the troops, proposed the establishment of a civic guard
for the maintenance of order. It was not, however, an easy matter to
obtain the sanction of the Government to a measure that would put an
armed force at the disposition of the capital. The National Assembly,
agitated by fear lest violence should be exercised against itself,
repeatedly besought the King to order the withdrawal of the troops.
Louis refused, and at the same time dismissed Necker from office,
ordering him to leave the kingdom immediately (July 11). It was on
the presence of Necker in the council that the popular party relied
as security that force would not be employed against the Assembly or
the capital. Accordingly, the news of his dismissal, reported the
next morning, set Paris in motion. All believed that troops would
immediately advance, and the revolution be suppressed in blood. In
the Palais Royal a young man, Camille Desmoulins, leaping on a table,
exclaimed, ‘Citizens, they have driven Necker from office. They are
preparing a St. Bartholomew for patriots. To arms! To arms! For a
rallying sign take green cockades, the colour of hope.’ The leaves were
torn from the surrounding trees to serve as cockades. There was, in
fact, but one course which Louis could consistently pursue after he had
dismissed Necker from office. He must use force to suppress opposition,
taking whatever risk there was. But of decisive action there was no
chance. The King had dismissed Necker without making up his mind what
he would do afterwards. There was no plan formed, and no understanding
between different authorities. A regiment of German cavalry charged,
first, into a procession parading the streets with a bust of Necker,
and afterwards into the Tuileries gardens, dispersing the throngs which
excitement and curiosity had brought together. After blood had thus
been shed, and the alarm and rage of the populace had increased, no
further attempt was made to suppress the insurrection. Officers of the
army were afraid to act without authorisation, and could not trust
their men, many of whom deserted their regiments. The French guards,
3,600 strong, went over in a body to the people. Paving stones were
torn up to erect barricades. The cry was raised for arms; pikes were
fabricated by thousands; gunsmiths’ shops were ransacked, military
storehouses broken open, and muskets and powder carried off in triumph.

During the following night and day (July 13) the barriers where the
excise was levied were set on fire, the prisons opened, and bakers and
wine shops pillaged. There were none in authority, and none who obeyed.
The electors, sitting at the Hôtel de Ville, usurped what authority
they could, which they exercised surrounded by a raging mob at imminent
peril of their lives. At their appeal the bourgeoisie began promptly
to raise an organised militia force in each of the sixty districts.
Early next morning, July 14, the fury of the people was directed
against the Bastille, the great State fortress and prison in the
Faubourg St. Antoine, the ‘Tower’ of Paris, where for centuries past
prisoners, often without charge of crime, had wasted their lives away.
Its commander, the Marquis de Launay, had long since pulled up his
drawbridges and made ready for defence as he watched the insurrection
grow. His garrison was small, consisting only of thirty-two Swiss and
eighty-two old French soldiers or Invalides. But the massive walls of
the fortress and its double moat would effectually guard it against
the assault of an undisciplined multitude. Summoned to surrender by a
deputation from the Hôtel de Ville, De Launay replied that he would
rather set fire to the powder magazine and blow the place to the skies.
The population streamed by thousands to the spot, and the fortress
was soon surrounded by a surging mob. An old soldier succeeded in
cutting the chain which held up the drawbridge of the outer moat. A
shout of triumph was raised. The assailants rushed over the fallen
bridge, but only to be confronted by the second moat and unscaleable
walls of the fortress. The French guards, bringing with them cannon,
joined the besiegers, but all efforts to force the passage of the moat
were frustrated. For five hours an incessant fire of musketry had
been kept up. A hundred of the assailants lay dead, and but one of
the garrison, when the Bastille unexpectedly and suddenly succumbed.
The Invalides refused longer to resist, and compelled De Launay to
surrender. Hulin, an officer leading the French guards, accepted the
terms proposed--pardon and immunity for all. But he could not enforce
their observance. The mass of human beings behind knew nothing of what
those in front did. Enraged and uncontrollable, the mob broke into
the fortress, those behind pushing aside those who went before, and
striking blows at random. Six of the garrison were killed. De Launay
was sent with an escort of French guards to the Hôtel de Ville. On the
way the escort was hustled aside and the old man savagely murdered.
His head, fixed on a pike, was carried in triumph about the streets.
Late at night the news reached Versailles that the Bastille had fallen.
‘But,’ said Louis, ‘that is a revolt.’ ‘Sire,’ replied his informant,
the Duke of Liancourt, ‘it is not a revolt, it is a revolution.’

♦Establishment of a Municipality and of a National Guard in Paris.♦

A great revolution had indeed been accomplished. The fall of the
Bastille indicated the fall of the old monarchy, in which the King
alone represented the nation. Louis had said to the Assembly that,
unless he were obeyed, he would secure the happiness of his subjects
without its aid, and Paris had replied by rising in support of the
Assembly against himself. The falling away of the army had unmistakably
revealed his weakness and powerlessness to resist the national will.
His brother, the Count of Artois, and other unpopular courtiers, known
to be especially hostile to the people’s cause, fled the country
in disgust and alarm. Louis himself had no choice but to yield all
that was demanded of him. He ordered the withdrawal of the troops,
and recalled Necker to office. The Assembly sent eighty-eight of
its members to announce the good news to Paris. They were received
with enthusiasm, and escorted by thousands of national guards to
the Hôtel de Ville, where the electors exercised the functions of a
provisional municipality. Two deputies were singled out for special
honours. A young and popular nobleman, Lafayette, who had fought in
America against the English, and since the meeting of the Assembly had
supported the cause of the Third Estate, was by acclamation chosen
commander-in-chief of the new militia or national guard. Bailly, a
mathematician, who had been president of the Third Estate when the oath
was taken in the tennis court, was after the same fashion chosen mayor
of Paris. To the blue and red, the colours of Paris first worn by the
national guard, was subsequently, on Lafayette’s suggestion, added
white, the colour of France. This new flag would, he magniloquently
said, make the round of the world. Thus was instituted the famous
tricolour, the emblem to France of the revolution.

It only remained for Louis to recognise these new revolutionary
authorities, which made the capital of his kingdom independent of him
and of his government. Leaving the Queen weeping at Versailles in alarm
for his safety, he drove to Paris, attended merely by some members
of the Assembly and a few national guards. At the barrier of Passy,
the mayor, Bailly, presented him with the keys of the city, the same
which, on an occasion dissimilar to this had been presented to Henri
IV., when Paris had surrendered to him, ‘He,’ said Bailly to Louis,
‘had made conquest of his people. Now the people have made conquest of
their King.’ Arrived at the Hôtel de Ville, Louis fixed a tricolour
cockade on his hat and appeared on a balcony in front of the building.
The thousands assembled outside applauded him loudly, and shouts of
‘Vive le Roi’ mingled with shouts of ‘Vive la Nation.’ The enthusiasm
exhibited in his favour was not unreal. Amongst the multitude present,
no stronger desire existed than that of accomplishing the revolution in
accordance with the crown.

♦Risings in the provinces.♦

While political strife was raging at Paris, in the provinces the
people, impatient for relief, were taking upon themselves the work of
redressing their wrongs. Since the meeting of the States riots had
broken out by scores over the face of the country. Taxes were refused,
barriers for the collection of custom and excise duties burnt, the
collectors driven off, markets pillaged, municipal officers forced at
peril of their lives to fix a price for corn and bread. The news of the
great insurrection of July 14 gave courage to agitators, and added fuel
to the flame. In Paris, street mobs, goaded by hunger, were not easily
restrained from hanging objects of suspicion on the nearest lamp-post.
Foulon, an officer of the Government, accused truly or falsely of
having said that the people if hungry might eat grass, was savagely
murdered. His son-in-law, Berthier, suffered a like fate. Many other
persons escaped but narrowly with their lives. Nevertheless, owing to
the exertions of the new municipality and the national guard, life
and property were more secure in the capital than in many provinces.
Risings accompanied by pillage and murder took place in Strasbourg,
Rouen, Besançon, Lyons, and other provincial towns. In the east,
through Alsace, Franche-Comté, Lorraine, Burgundy and Dauphiny, the
rural population sought to settle the question of feudal services by
burning together the residences and the title-deeds of the seigneurs.
In the Maconnais and Beaujolais, bands of peasants sacked and burned
seventy-two country-houses in a fortnight. A panic spread through
the country on the report that brigands, instigated by the enemies
of the revolution, were on the march to destroy the crops. A general
cry was raised for arms; the example set by Paris was followed; the
middle classes combined to restore order; provisional municipalities
were established and national guards instituted. The order obtained,
however, was still most precarious. Municipal officers were in constant
danger of falling victims to mob violence, while in country districts
national guards often made common cause with the rioters.

Thus the result of the insurrection of July 14, and of the risings in
the provinces, was the utter disorganisation of all the old machinery
of government. Royal officers where they remained could not exercise
authority. The army was in mutiny; the people were armed. New popular
authorities had, as it were, of themselves sprung up over the face of
the country, and the National Assembly, in place of the royal council,
became the centre of government, so far as any government existed.

♦Decrees of August 4.♦

The Assembly was far more disquieted by the risings in the provinces
than by the insurrection of July 14. The fall of the Bastille assured
political power to the middle classes. This burning of country-houses
and the refusal to pay taxes and feudal dues struck at all alike,
and sapped the base on which the whole framework of society rested.
As yet, in the south-west and centre, where feudal dues were less
burdensome, riots were isolated and bloodshed rare, but there was
every probability that the movement, if unchecked, would spread over
the whole country. The injustice of the existing order, by which
provinces, towns, and individuals were privileged without regard to
public utility, the injury inflicted on agriculture by feudal dues,
and the oppressive nature of many rights exercised by seigneurs had
been demonstrated over and over again, and were admitted on all sides.
In an evening sitting on August 4, the Assembly laid the axe to the
root of the old order by adopting decrees based on the principles of
unity of State institutions, equality before the law, and individual
liberty. There was no province, town, class, or corporation whose
special interests these decrees did not touch. They were in part the
work of design, in part of the enthusiasm of the moment. No voices
were raised in opposition. Nobles, bishops, curés, representatives of
towns and provinces, vied with one another in proposing the abolition
of privileges and rights which stood in the way of the common good.
The decrees declared the feudal order destroyed, deprived seigneurs of
the exclusive right of hunting and of keeping rabbits and pigeons, and
abolished serfdom and servile dues off-hand; abolished also all special
privileges belonging to provinces, towns, and corporations, and laid
open to all citizens, without regard to birth, civil, military, and
ecclesiastical preferment; and, finally, abolished tithes paid to the
Church, and made promise of ecclesiastical reform in the future.

These decrees were not practical laws, but little more than an
enunciation of general principles in accordance with which reform was
afterwards to be effected. Thus the mass of feudal dues had still to
be rendered until compensation had been given to the proprietors; the
old taxes were to be paid until a new system of taxation based on
principles of equality had been introduced. This hasty legislation
could not, therefore, allay discontent, but excited a stronger
reluctance on the part of the people to endure burdens, the injustice
of which the National Assembly itself publicly proclaimed.

♦Composition of the Assembly.♦

The Assembly, on which rested the task of founding a new order amid
the ruins of the old, was without political experience or recognised
principles of action. It contained about 290 representatives of the
nobility, of whom 140 were provincial noblemen, 20 judges in the upper
courts, and 125 belonged to the court aristocracy. The clergy had
returned 200 curés and only 100 bishops, abbés, and other dignitaries.
A few more than 600 deputies represented the Third Estate, of whom
4 were ecclesiastics and 15 noblemen. The great majority were men
independent of the Government. The profession by far the most largely
represented was the law. There were 360 judges, barristers, and law
officers of various kinds. The chamber was fitted up like a theatre,
with a semi-circle of seats facing the president’s chair, beneath which
was a tribune whence all set speeches were made.

♦The Reactionary Right.♦

Four main lines of opinion divided the Assembly roughly into four
sections. The majority of nobles and the upper clergy sat together on
the president’s right hand, forming the right side of the Assembly.
Their standpoint was reactionary, in favour of the privileged orders.
The fusion of the three orders having been accomplished against
their will and in defiance of the royal authority, they regarded the
Assembly’s work as resting on no justifiable foundation, and looked
forward to reversing it on the first occasion. Here an officer,
Cazalès, eloquently and loyally defended monarchical principles of
government; the Abbé Maury, with vehemence and ability, the cause of
the upper clergy; and D’Espréménil, a judge in the Parliament of Paris,
the institutions of the old order.

♦The Right Centre.♦

The second section comprised deputies of all three orders. They were
defenders of individual liberty and parliamentary control, but were
bitterly opposed to the establishment of democratic institutions. They
did not believe in the endurance of monarchy without an aristocracy
and aristocratical institutions, and aimed at replacing the effete
nobility by an aristocracy of wealth. For the exercise of political
rights they would have required a high property qualification; and,
copying the constitution of the English parliament, would have
established a legislature composed of two houses, in both of which the
landed interest was to predominate. They detested insurrection as a
weapon, and were thoroughly alive to the danger in which since July 14
all authorities stood--of falling beneath the sway of mob violence.
The restoration of order was, from their point of view, the matter
of first moment, and they accordingly desired that the Assembly, in
place of discussing constitutional questions, should at once turn its
attention to the reform of the taxes and to other remedial laws, and
that at the same time ministers should be empowered to use coercive
measures for the punishment of rioters and the maintenance of the
public tranquillity. The upholders of these views, who sat next the
reactionary right, were but a small minority. Their most able speakers
were two deputies of the Third Estate--Mounier and Malouet, and two
nobles--Clermont-Tonnerre and Lally-Tollendal.

♦The Centre and Left.♦

The third and most numerous section, forming the centre and left of the
Assembly, consisted of curés and deputies of the Third Estate, with a
sprinkling of nobles and upper clergy. Though considerable differences
of opinion prevailed in this body of seven to eight hundred men, two
sentiments were common to all--passion for equality and desire for
self-government. Hence no schemes calculated to vest power in the
hands of large landed proprietors found favour with them. They were
not, however, pure democrats, nor by sentiment republicans. Their real
aim was government by the middle classes. To monarchy as a form of
government they were not only attached, but regarded its maintenance
as necessary to give stability to the constitution they were about
to establish. Amongst the most prominent men on this side of the
house were Thouret, Merlin of Douai, and other eminent lawyers, the
Marquis of Mirabeau, Lafayette, the Abbé Siéyès, two brothers, the
Lameths--both of them nobles and officers--and a young and eloquent
barrister, Barnave.

♦The Extreme Left.♦

The fourth section, sitting on the extreme left--which must be
distinguished from the left--was formed of a few deputies, some twenty
or thirty in all, who were pure democrats, and whose programme included
manhood suffrage, and the eligibility of all citizens to office
without property or other qualifications. A republic was their ideal
form of government, which they held alone compatible with free and
democratic institutions. At the same time they entertained no thought
of establishing such a government in France. The possibility of getting
rid of the throne had not yet suggested itself to their minds. In
the Assembly their opinions were regarded as exaggerated, and their
influence was small. Amongst them sat Pétion and Robespierre, whose
names afterwards rose into notoriety.

None of these four groups, except the last, properly speaking formed
a party of which the members ordinarily voted in a body. There was
no concerted action, no party discipline, no recognised leaders. The
galleries were often filled by an excited and noisy audience, which
interrupted debates and menaced unpopular speakers. Each deputy voted
independently, and was subject to be swayed by whatever influence at
the moment predominated--were it eloquence, enthusiasm, fear, or
prejudice. The provincial nobility followed but sullenly in the wake
of the court nobility, and on every opportunity made its hostility
manifest. Deputies belonging to the centre and left constantly voted
on opposite sides. According to the special point at issue, more or
less democratic opinions were entertained by the same person. Thus
Lafayette, although as a rule he was found in opposition to Malouet,
wished like him for the establishment of a legislature composed of
two houses, having become strongly convinced of the advantages of
that system through his affection to American institutions. The most
advanced group of the whole centre and left, headed by Barnave and the
Lameths, sat furthest left, next to Buzot and Robespierre, with whom
they not seldom voted.

♦Causes giving ascendancy to the Left.♦

In the chamber thus constituted, a variety of causes often gave
ascendancy to the group which followed Barnave and the Lameths. The
events of June 23 (p. 39) had destroyed confidence in the King, and
though not expressed in words fear always prevailed that Louis would
hereafter use whatever powers were given to him to effect a restoration
of the old order. The reactionary right also refused to work with
the advocates of the system of two chambers, such as Malouet and
Mounier, thus alienating the less democratic members of the centre
and propelling them towards the left. Nobles and ecclesiastics, who
had opposed the union of the three orders, in place of seeking to
establish a constitution based on monarchical principles, made it their
policy to vitiate the Assembly’s work and so increase the elements
of disorder as the surest and speediest means of producing reaction.
Sometimes they abstained from voting or attending debates; sometimes
they interrupted debates; at others they voted with the left against
the constitutional right. The ministry was too feeble and too divided
to exercise influence over the Assembly. It was without the first
requisite for acquiring confidence, a declared and open policy. Necker,
whose principles and aims coincided for the most part with those of
Malouet and Mounier, always received hearty support from them and
their friends. But, proud and irritable, accustomed to command and
not to lead, he did not take advantage of the opportunities which he
had for forming a ministerial party. While devising expedients for
avoiding bankruptcy, he failed even to lay before the Assembly any
complete account of the state of the finances. The reactionary right,
which never forgave him for recommending the double representation
of the Third Estate, and the extreme left, which distrusted him,
concurred in attacking him on every opportunity. His popularity rapidly
decreased, and his position in the ministry grew weak in proportion
as his relations to the Assembly became strained. Mirabeau, the most
powerful man in the house, was his enemy. The mass of deputies, without
trust in the Government and menaced by the right, looked to the people
for support, and through desire of maintaining popularity were the
more ready to adopt measures urged on them by the ultra democratic
press. Their minds were undisturbed, either by the violent language
of Parisian demagogues, or by the existence of riots and bloodshed in
many provinces. The one object that they kept steadily in view was
the establishment of constitutional government on foundations that
should make reaction hopelessly impossible; and compared with this the
restoration of order was to them a matter of secondary importance.
They had no fear of the people. Following the one-sided philosophy of
their day, and leaving out of account the dense ignorance of the lower
classes, the pride and prejudices of the upper, they believed that the
establishment of a free constitution, followed by remedial legislation,
would bring the revolution to an end within the course of a few months,
and render the country law-abiding, prosperous, and contented.

♦Policy of Mirabeau.♦

How vain was this dream, entertained by those with whom he sat
and voted, Mirabeau was well aware. He saw the people ignorant
and credulous, without confidence in the middle class, and ready
to follow the guidance of whoever promised them most; the middle
class unaccustomed to take part in government and divided into
factions, which were united merely by common hatred of aristocratic
institutions. Under such conditions Mirabeau gave small credit to
his countrymen for political capacity, and had no faith in the
endurance of any constitution which cast upon the nation the entire
work of administration and government. But, on the other hand, he did
not seek, like Malouet, to found a strong monarchy on aristocratic
institutions. No real aristocracy existed, and the passion for equality
was irresistible, for the very reason that it was justified by the
incapacity of those classes which had hitherto claimed to rise above
their fellow countrymen. The government which Mirabeau regarded as
alone suited to the requirements of the time was constitutional
monarchy, based on principles of equality and individual liberty,
upheld by the confidence of the middle class, and exercising influence
over the direction of public opinion. Local administration was to be
under the control of the central government; ministers were to have
seats in the legislative body; and the king, in case of difference
between himself and the legislature, was to have the right of refusing
his consent to bills and of appealing by a dissolution to the
constituencies. Mirabeau prophesied that unless the distrust which
the Assembly felt towards Louis were dissipated, the throne would be
overturned by the Parisian populace. His sense of danger quickened
his desire to obtain a place in the council. He had many qualities
fitting him to the task to which he aspired of at once domineering
over Louis, and obtaining a majority in the Assembly to follow his
guidance. He had insight into character, was master of his temper, and
able to inspire men with his own belief, and to fascinate those who
were prejudiced against him. As an orator he was unrivalled. The effect
that he produced on his hearers was so powerful that his very opponents
applauded him. But there were many drawbacks in his way. He came to the
Assembly with an ill reputation that told heavily against him. His life
even now was riotous and profligate, and he was known to be harassed
by debts and unscrupulous in action. His fellow deputies, afraid of
the crown acquiring influence over the Assembly by corruption, even
whilst they were under the spell of his genius, were mistrustful of
his political integrity. Lafayette refused to have dealings with a
man whom he contemned as a libertine. Barnave and the Lameths were
Mirabeau’s rivals for popularity, and jealous of the influence that
his superior eloquence at times allowed him to exercise. On the side
of the Government, which had no chance of surmounting the crisis under
any other guidance, he received no encouragement. Necker feared and
hated him as a dangerous and unprincipled demagogue, and repelled his
overtures; while the aversion of the Queen to all noblemen who took the
popular side was intense. ‘I trust,’ she one day said, ‘we shall never
be reduced to the painful extremity of seeking aid of Mirabeau.’

Thus circumstanced, Mirabeau did his best to weaken and degrade the
Government, expecting that in the course of a few months the King
would be compelled to recognise his claims to office. He never missed
an opportunity of undermining Necker’s popularity, and while defending
with vehemence what he held to be the essential prerogatives of
monarchy, maintained sway over the Assembly and the populace by fierce
attacks directed against the nobles, the clergy, and the court.

♦Declaration of the Rights of Man.♦

The first legislative work of the Assembly after the decrees of August
4 (p. 50), was a Declaration of the rights of man, which, in general
language, stated the aims which the greater part of the Assembly had in
view. This manifesto of the principles of the revolution declared that
men have natural and imprescriptible rights to liberty, property, and
security, and also the right of resisting tyranny; that men are born
equal in rights; that all citizens are equal in the eye of the law,
and are equally admissible to all offices without other distinctions
than those of virtue and talent; that the nation is sovereign, and
that laws are the expression of the general will. In accordance with
these principles, the Declaration announced the abolition of all orders
and corporations, and proclaimed liberty of the press and liberty of
worship.

♦Veto given to the King.♦

Debates on the form to be given to the new legislature followed the
adoption of the Declaration of the rights of man. The proposal that
there should be two houses was negatived by 499 against 89 votes. The
new legislature was to meet every two years. The question whether the
King was to have power to refuse his consent to decrees or exercise
a so-called veto upon them was the cause of great excitement both
at Versailles and Paris. Ultra-democratic agitators and journalists
declared that to allow the King a share in the legislative power was
to wrong the sovereignty of the nation. The relation existing between
Louis and the Assembly was thoroughly false. The deputies of the
centre and left were eager to avoid coming into collision with him,
but were aware that he was only following by compulsion in their wake.
On the ground that the nation was entitled to choose its own form of
government, they took for granted that Louis must sanction without
question or criticism all constitutional decrees. But they dared not
trust the King, whom they excluded from any share in the formation of
the new constitution, with authority which he might hereafter employ to
subvert it. On the question of the veto a compromise was adopted, and
the King empowered to refuse to pass the same decree during the sitting
of two consecutive legislatures (September 20).

♦Scarcity of bread.♦

While the Assembly was engaged in discussion on the rights of man,
all the causes which had been productive of crime and riot were still
at work. The price of bread remained high after the harvest. This was
due in part to deficiency in the crops, but much more generally to
interference with the corn trade. The Assembly, acting in accordance
with the free trade theories of the Economists, annulled all
regulations impeding the free circulation of corn and flour. But the
people, ignorant, distrustful and fierce, used the power that was in
their hands to carry out the old system more methodically, threatening
municipal officers with personal violence unless they took measures to
insure that markets were well supplied. Pillage of corn on transit and
purchases made by public bodies stopped ordinary trade, and produced an
appearance of scarcity even where corn was plentiful. In every large
town bread was sold under cost, the municipalities making good the
loss to the bakers. To provision Paris, convoys of flour were brought
into the town under military escort; large purchases of foreign corn
were made, the Government supplying funds; and by these means bread
was sold at about three halfpence the pound. But bread, if cheap, was
scarce. Purchasers stood for hours in long ranks or _queues_ at the
bakers’ doors, and those who came last often left empty-handed. On the
municipality and the national guard devolved the task of maintaining
order. The national guard formed an organised police force. Most
of those who served were volunteers, but 6,000, with whom had been
incorporated the French guards, were paid and lodged in barracks. The
officers were elected by the men. Lafayette, the commander-in-chief,
was a brave and chivalrous soldier, whose enthusiasm for liberty and
equality was unmixed with motives of personal aggrandisement. He was
very popular with his troops, but his influence over them was confined
within narrow limits. The guard, composed principally of the middle
and lower middle classes, retained its character of a citizen force,
possessing a strong political bias, and capable at any time of taking a
course of its own.

♦The 6th October.♦

During the month of September the idea of going to Versailles and
bringing the royal family to Paris fermented in the minds of the poorer
inhabitants of the city. There were rumours that the King intended
flight. The hungry people believed that their sufferings were solely
due to the intrigues of reactionary nobles and ecclesiastics, and that
bread would be abundant were the King once securely established in
their midst. Whatever was proposed at Paris was known at Versailles.
Since the revolution of July, plans of retreat to Metz and other
towns had been urged on Louis. It was impossible to adopt this course
without contemplating resource to arms. The Queen was willing, but
Louis preferred to let events drift on sooner than give occasion to
his subjects to throw on him the reproach cast on Charles I., of
having roused civil war and caused the shedding of blood. Meanwhile
the policy pursued was of a piece with that which preceded the fall
of the Bastille. Paris was defied by bringing an additional force of
a thousand foreign troops, the regiment of Flanders, from Arras to
Versailles, but no further measures were taken to repel aggression.
The officers of the royal body-guard held a banquet in honour of the
new comers in the palace theatre before a large audience. The occasion
was taken to make a strongly pronounced display of royalist sentiment.
Insulting words were spoken against the Assembly; national toasts
were left undrunk; the tricolor replaced by white cockades. The King
was induced to come to the theatre, and the Queen, with the Dauphin
in her arms, went the round of the table, making gracious speeches
(October 1). Exaggerated reports of what had taken place spread through
Paris. National guards were eager to avenge the insult offered to the
tricolour, which, it was said, had been trampled under foot. Early
on the morning of October 5 many thousands of hungry women began a
march from Paris to Versailles, stopping and forcing all of their own
sex whom they met on the way to accompany them. Bands of men soon
followed, and the national guards, in place of opposing the movement,
compelled Lafayette to march at their head after the mob. There was
heavy rain all day, and the women on their arrival at Versailles were
weary, fasting, and wet. They surrounded the palace, and broke into
the hall of the Assembly, shouting, in reply to the speeches of the
deputies, ‘Bread, bread, and not so many words!’ All through the day
new bands continued to arrive, composed of both men and women. The
royal body-guard, between whom and the mob shots were exchanged, were
withdrawn within the palace gates. A little before midnight Lafayette
at last arrived at the head of an orderly force of 20,000 men. He set
watches at the palace gates, and afterwards entered to take a short
rest. But at daybreak some of the mob broke into the palace courts,
killed two soldiers of the body guard who fired on them, wounded
others, and burst into the ante-room of the Queen’s bedchamber. Marie
Antoinette, roused by her women, fled for her life to the King’s
apartment. The alarm was given, and national guards arrived on the
spot in time to avert more bloodshed, and to drive back the intruders.
Louis, who had not been able to decide on flight while he still had
opportunity, yielded to the will of the populace. A dense crowd was
assembled in front of the palace, shouting, ‘The King to Paris!’ Louis
stepped out on a balcony, in sign of assent. The popular instinct
rightly fixed on the Queen as much more hostile to the revolution than
the King. As she stepped out after her husband, with her girl and boy
by her side, voices from below shouted, ‘No children.’ Pushing the
children back, she bravely advanced without hesitation alone, while
Lafayette, afraid for her safety, sought to make her peace with the
people by stooping and kissing her hand. All steps were now turned
towards Paris. First went a disorderly mob, rejoicing in their capture
of the royal family, and shouting that bread would be plentiful, for
they were bringing with them the baker, the baker’s wife, and the
baker’s boy. The heads of the slain body-guards, ghastly trophies of
their triumph, were carried on pikes. The royal carriages, surrounded
by national guards, followed in the wake of the mob. On their arrival
in Paris, the King and Queen were conducted to the Tuileries. The
Assembly, which after a few days followed the King, was established in
a riding-school in the neighbourhood of the palace.




CHAPTER IV.

THE CONSTITUTION.


♦Results of movement of October 6.♦

The movement of October 6 was not, like the rising of July 14,
unpremeditated. The scarcity of bread had been made use of by agitators
to suggest to the populace the idea of bringing the King to Paris.
Their object was to place both the King and the Assembly immediately
under the influence of the capital. To the Duke of Orleans at the
time was ascribed the intention of driving the royal family from
Versailles, and obtaining for himself, if not the throne, a regency.
The Duke, unprincipled and of mean capacity, was incompetent, if he
had the ambition, to play a prominent part in the revolution. The
possession of great wealth assured him hangers-on and partisans, but
he was generally despised, and no man of any standing ever openly
espoused his cause. Deputies of the centre and left, as well as the
municipality and Lafayette, regarded the residence of the court at
Paris as security against attempts to raise civil war by the removal
of the King and the division of the Assembly. From this time the royal
family was in fact in the keeping of Lafayette, whose troops composed
the palace guard. The court could see nothing in the event but one more
act of popular violence, which must before long cause reaction. After
the fall of the Bastille, the King’s brother, the Count of Artois, had
left France. Many court nobles, including deputies of the reactionary
right, now took the same course, with full expectation of shortly
returning and finding the old order of things restored. Two leaders
of the right centre, Mounier and Lally-Tollendal, quitted the capital
on the plea that their lives were in danger, and that the Assembly
was not free. It was true that those who took the lead in defending
unpopular opinions were subject to menace and insult, but it was not
true that deputies sitting on the right were precluded from taking part
in the debates or voting according to their pleasure. On the contrary,
if the galleries were often noisy and abusive, bishops and nobles found
opportunities not only of replying at length to their opponents, but
also of obstructing proceedings for hours by mere clamour. The ordinary
form of voting, which was simply by rising and sitting, prevented the
frequent publication of division lists. Much important work, in which
all could take part in safety, was done in private committees, and
drafts of laws prepared in them were often adopted by the Assembly with
little alteration. The withdrawal of deputies only helped to complete
the disorganisation of an already divided minority.

♦The Jacobins.♦

While the right side of the Assembly, in consequence of desertions,
disorganisation, and intimidation, became constantly less able to
exert influence over the centre, the left acquired new sources of
strength. With the object of concerting common action, a few deputies
used to meet in a building in the Rue St. Honoré, belonging to some
Dominican friars, who were commonly called Jacobins, because the church
of St. Jacques had been assigned to them when, in the thirteenth
century, they first arrived in Paris. In this building was organised
a debating club, entitled by its founders the Society of the Friends
of the Constitution, but which acquired celebrity under the name of
the Jacobins. All deputies of the left joined it, as well as many
persons who were not members of the Assembly, amongst whom were the
most radical politicians and journalists of Paris. Whatever questions
were debated in the Assembly were at the same time debated in the
club, where democratic opinion was more pronounced, and put forward
with less reserve. Barnave was in the club a more popular orator
than Mirabeau, and Robespierre, who could hardly obtain a hearing in
the Assembly, was listened to with attention and applause. Thus the
existence of the Jacobins gave organisation to the more democratic
party at a time when organisation was nowhere else to be found.

[Illustration: FRANCE IN DEPARTMENTS 1790

_Longmans, Green & Co., London, New York, Bombay, Calcutta & Madras_.]

♦The Constitution.♦

Under the influences above described, fear of reaction, belief
in theory, and desire for popularity, the Assembly completed the
constitution and carried reform into every department of the state.
Its work was based on principles of uniformity, decentralisation, and
the sovereignty of the people, and whatever institutions clashed with
these were swept away. The old division of the territory by provinces
was abandoned, and France was divided into eighty-three departments,
all as nearly as possible of the same extent, and named after
geographical features, such as rivers and mountains. The eighty-three
departments were subdivided into 374 districts. In every department
was an elected administrative body for the management of its affairs;
in every district an elected administrative body, subordinate to the
administration of the department, for the management of affairs special
to the district. These bodies were composed each of a general council
and a permanent executive, styled the directory. In every district
the former divisions, called communes, were left unaltered. Of these
communes there were no less than 44,000 in France, some being large
towns, whilst others were mere villages. The local affairs of these
communes were placed under the direction of municipalities. The members
of these municipalities were elected by all men inhabiting the commune
twenty-five years old, and paying yearly in direct taxes, according to
a reformed system of taxation, a sum varying from eighteen pence to two
shillings, the value of three days’ labour. Manhood suffrage would
have given 6,000,000 voters, while this qualification limited their
number to about 4,300,000 only. Persons qualified to vote were required
to serve in the national guard, and were called active citizens, whilst
those disqualified were known as passive citizens. For the election
of the administrative bodies of the district and the department, as
well as of deputies to the legislature, the system adopted was by two
degrees. There were many primary assemblies, consisting of all active
citizens in each department, each of which chose a certain number
of electors, who in turn elected the administrative bodies of the
districts and of the department, as well as the deputies who were to
represent the department in the legislature. The qualification for
being a member of a municipality, or of any administrative body, was
the payment yearly in direct taxes of a sum varying from six to eight
shillings. A special and higher qualification was required for sitting
in the legislature--the payment in direct taxes of a marc, in value
nearly fifty shillings.

♦Judicial reform.♦

The new administrative divisions served as judicial divisions also.
The old courts, including the parliaments, were one after another
abolished. Each district was divided into cantons, and the primary
assemblies in each canton elected judges, called justices of the peace
(_juges de paix_), for the trial of petty causes. Every district
had a civil, every department a criminal court, of which the judges
were respectively elected by the electors of the district and the
department. Persons belonging to any branch of the legal profession
were eligible as judges, who were elected for six years only. Much
directly remedial legislation accompanied this new framework. Procedure
was rendered more favourable to the accused. Trial by jury on the
English system was adopted in criminal cases, every department having
its grand jury. Securities were taken against arbitrary arrest
and imprisonment, and the law was made the same for all, without
distinction of persons. A new penal code was drawn up which contrasted
most favourably with the criminal law in force in other countries.
Heresy and magic were no longer recognised as crimes. Torture was
abolished, and the punishment of death confined to four or five
offences.

♦Church property appropriated by the State.♦

Economical and financial reforms were also effected. Internal custom
houses were removed, monopolies and trade restrictions abolished.
The Assembly, however, trod here with more cautious steps than when
effecting constitutional and administrative reforms. The tariff of
export and import duties was modified, but fear of injuring French
industries prevented the adoption of free trade principles in
regulating the commercial relations between France and other countries.
The restoration of the finances in the midst of revolution was not a
work to be easily accomplished. The Assembly delayed to abolish the
old taxes until a new system of taxation was organised, but meanwhile
thousands refused to pay them, and the revenue proportionately
decreased. To meet the expenses of government Necker was compelled
to borrow, and in the autumn of 1789 the State debt reached about
43,750,000_l._ To prevent its increase and to meet the claims of
creditors, the Assembly had resource to Church property. By the
abolition of tithes on August 4, a revenue of 5,818,750_l._ passed
into the hands of landed proprietors and agriculturists. The Church,
however, remained possessed of property valued at a capital of more
than 100,000,000_l._, bringing in a revenue of about 3,500,000_l._ All
this property was declared to be at the service of the State, which
undertook henceforth to provide for the clergy. Crown lands and Church
lands to the value of 17,500,000_l._ were offered for sale, and state
paper money to the same amount issued in the form of notes of the value
of 44_l._, bearing a forced currency and called assignats, which were
to be used in payment of state creditors, and were to be received back
by the state from purchasers of the land so offered for sale, and thus
to be gradually withdrawn from circulation and destroyed.

The upper clergy, supported by the nobles, vehemently opposed these
measures, which entirely altered the status of the clergy. The clergy
regarded themselves as administrators of property for Church purposes,
and as independent of state influence; whereas they would henceforth be
brought into close dependence on the state and lose the social position
which wealth and independence gave them. The Abbé Maury accused the
Assembly of interfering with the rights of property, and of being
guilty of an act of spoliation. But the supporters of the new laws
formed an overwhelming majority. Sceptics and theists, Jansenists who
sought to reform the Church in accordance with the primitive usages of
Christianity, lawyers who were merely following the legal traditions
of the old monarchy in arguing that the state interest was paramount,
informed the bishops that the clergy were not proprietors, but merely
administrators of national property, who were justly deprived of a
trust which they had executed ill. By the sale of Church lands the
Assembly designed not merely to restore the finances, but by motives
of self-interest to bind thousands to the work of revolution by
indissoluble ties, since every purchaser of Church lands, every holder
of assignats, every state creditor, would have a direct interest in the
maintenance of the new order.

♦Civil constitution of the clergy.♦

The laws for the appropriation and sale of Church property were
followed by laws for the reform of the Church. Monasteries and
nunneries were suppressed, the existing inmates being pensioned and
left at liberty to return to the world or live in such houses as were
assigned to them. A special code, entitled the ‘Civil Constitution of
the Clergy,’ undertook to carry out in the Church what had been already
done for the state. The old diocesan and parochial divisions were
abandoned. Every department was made a bishopric, and the boundaries of
the parishes were changed according to convenience. Bishops were to be
elected by all the electors of the department, curés by the electors of
each district. Bishops were to signify their election to the Pope, but
not to seek confirmation of their appointments at his hands. Chapters
and ecclesiastical courts were abolished, and in exercising his
functions each bishop was to be assisted by an ecclesiastical council,
composed of chaplains selected amongst the curés of the diocese. The
incomes of bishops were lowered, and those of curés raised. The whole
expense of the establishment was estimated at nearly 3,000,000_l._

♦Federation, July 14, 1790.♦

It was only by degrees that these changes were carried out. The
municipalities and other administrative bodies were elected during
the spring of 1790, the new judges not till the autumn, while the
Civil Constitution of the Clergy came into force in the summer of
the same year. An enormous strain was laid upon the patriotism and
intelligence of the country. Active citizens were incessantly called
upon to give time and thought to public affairs, by taking part in
elections and serving in the national guard; while there were more
than a million of unpaid administrative and municipal officers charged
with important duties and great responsibility. All the local business
of the departments devolved on them, the maintenance of roads and
bridges, the police regulations, the care of hospitals, the imposition
and collection of taxes, the sale of national property, and generally
the carrying out of the decrees of the Assembly. Nevertheless, the
country responded with admirable energy. Men believed that a new era
of freedom and prosperity was about to open, and numbers came forward
who unsparingly devoted time and money in discharge of civic duties,
arduous and often dangerous. During the spring all over France the
inhabitants of different villages, towns, and provinces met together
to hold federations, or feasts of union, in honour of the new
constitution. On July 14, the anniversary of the fall of the Bastille,
a federation for the whole of France, at which the King presided, was
held at Paris. Every department sent its deputation of national guards,
who came to the number of 15,000 men. An altar was raised in the middle
of the Champ de Mars, where Talleyrand, Bishop of Autun, said mass, and
blessed the banners of the departments. The thousands assembled swore
with one voice to be faithful to the nation, the law, and the King.
Louis, from his throne, took an oath to maintain the constitution,
and the air resounded with shouts of ‘Long live the King.’ The
Parisians entertained the visitors, and the day closed amid general
lightheartedness and rejoicing. The Bastille was already razed to the
ground, and crowds came to dance on the place where it had stood.

♦The nobles and the revolution.♦

The joy and enthusiasm exhibited at the festival of the federation was
a genuine expression of desire for union entertained by the main and
best part of the population, but this desire rested on no substantial
basis. As the Assembly continued its work divisions multiplied, party
spirit increased in violence, and the country, in place of enjoying
order and settled government, drifted further in the direction of
anarchy. The upper nobility did not conceal its detestation of the
work of the revolution, or its expectation that the whole would
be reversed. Most great nobles left the country, and establishing
themselves at Coblentz or Turin proscribed all who took part in the
revolution, threatened invasion, and called on foreign powers to
restore the King to his rights by force. Those who remained in France
assumed an attitude of scornful defiance, and by protests and intrigues
sought to stir up hatred against the Assembly, and to bring it into
contempt with the country. The lower nobles, if in some way losers,
would have greatly gained by the revolution if it had proceeded no
further; but various causes induced them to declare against it. The
Assembly made no efforts to conciliate them, and a decree abolishing
titles and armorial bearings had deeply hurt the pride of the whole
order (June 9). By many it was held a point of honour to remain true to
their caste; and, in fact, those who gave support to the revolutionary
laws were placed under a social ban. Many nobles quitted the country
with their families, owing to the insecurity of their lives. Those
who were arming on the frontiers brought on all who belonged to their
order the suspicion of being their accomplices. The peasantry needed
no incentive to turn upon the seigneurs. Although the Assembly had
abolished the feudal rights of a servile origin, and those which
represented sovereignty, it maintained, until compensation was made to
the owners, all dues presumed to have had their origin in agreement,
and to represent the price paid for the possession of land. The
arrangement was just, and, if it had been feasible, would have been
of advantage to almost everyone interested. But to effect it a strong
government was required, and France was in the midst of revolution.
The peasants, in whose minds all feudal rights were inextricably bound
up together, refused to recognise legal distinctions between them.
The machinery, moreover, provided by the Assembly for effecting
enfranchisement, in place of being speedy and simple, was complicated
and in many cases practically inoperative. Hence the relations between
peasants and seigneurs, as the revolution advanced, grew more and
more embittered. While the owners of the dues threatened suits, their
debtors resorted to violence. Scenes similar to those witnessed in the
east in 1789 now occurred over a large portion of the country. Again
and again, in 1790 and 1791, in the centre, in La Marche and Limousin,
further south in Perigord and Rouergue, in the west in Bretagne, as
well as in the east in Lyonnais, Alsace, Franche-Comté, and Champagne,
peasants and vagabonds went about the country in bands, burning
country-houses and title-deeds, and murdering those who attempted
resistance.

♦Weakness of the Central Government.♦

The central government, whose duty it was to protect life and property,
was impotent even to attempt the restoration of order. The Assembly,
through fear that the King would use authority for the undoing of its
work, had left him without means of enforcing obedience to the laws.
His only agents were the administrative bodies, and he had no means
of compelling them to perform their duties. The highest authority in
reality rested with the administrative bodies which were lowest in the
hierarchical scale--namely, with the municipalities. Of these there
were no less than 44,000, each acting independently of the other,
and though, according to the constitution, bound to carry out the
instructions of the directories of districts and departments, able to
disregard them with impunity. For the maintenance of order a Riot Act
had been passed, but that the King might not take advantage of it for
the suppression of constitutional rights, the municipalities alone had
been empowered to put it in force. Sometimes municipal officers were
unable, sometimes unwilling, to call out the national guard for the
forcible dispersion of rioters. In towns the bourgeoisie served on the
national guard, and there was no want of educated men to hold office.
But in rural districts there were no inhabitants except a few nobles
and curés and an unlettered peasantry. In hundreds of instances the
mayor and his colleagues could neither read nor write, spoke only their
own patois, and were incapable even of understanding the laws that
they were required to enforce. National guards, in place of protecting
the noble and his family from harm, took part with their neighbours
in destroying their dwelling, and in maltreating all whom interest or
prejudice incited them to regard as conspirators against the revolution.

♦Mutinies in the army.♦

Though troops of the line could be called out by municipalities to aid
in the enforcement of the Riot Act, their presence was in towns but an
additional cause of disorder. Class feeling was strongly pronounced
in the army, and the men turned upon their officers, accusing them of
extortion and oppression. All over the country, wherever regiments
were quartered, troops mutinied, demanding milder discipline and
higher pay, forming councils, seizing military chests, and compelling
officers to render account of the sums that passed through their hands.
These frequent mutinies alarmed men who closed their eyes to outrages
committed by peasants. Supported by a large majority in the Assembly,
the Marquis of Bouillé suppressed with heavy loss of life a serious
mutiny that broke out in a Swiss regiment, Châteauvieux, stationed at
Nancy (August 31). Reforms were afterwards effected both in army and
navy. The pay of the men was raised, and juries composed of both men
and officers instituted for the trial of military offences.

♦Schism in the Church.♦

The upper clergy, like the nobles, were alienated from the
revolution by the fusion of the three orders in one chamber, and by
the appropriation of Church property, and the civil constitution of
the clergy, were rendered irreconcilable enemies. They accused the
Assembly of seeking to destroy the Catholic religion, and denounced
the civil constitution as unlawful interference with matters of
Church government and discipline, which, as being matters of faith,
were beyond the cognisance of the state. But these attempts to excite
hostility against the Assembly had little success. The great body
of the nation had its interests far too closely bound up with the
revolution to be tempted into a crusade against it. The peasantry had
no quarrel with ecclesiastical changes which affected neither eyes nor
ears. The civil constitution itself did but reform the Church on the
basis laid down in the _cahiers_. It was only in the south where the
existence of Protestants excited religious rivalry, and the population
was most fanatic and intolerant, that the work of the Assembly met
with any serious resistance. At Perpignon, Tarn, Toulouse, and other
towns, the election of administrative bodies and the closing of the
monasteries gave rise to rioting and loss of life; while at Nimes,
where Protestants formed a third of the inhabitants, the streets for
three days ran with blood. Amongst the lower clergy there was small
disposition to follow the lead of their ecclesiastical superiors. The
state, which had appropriated church property, had improved their
material condition, and raised their position within the Church. Of
the monks, two-thirds elected to abandon monastic life. Nevertheless,
the arguments employed against recognition of the civil constitution
disturbed the minds of the curés, and the enforcement by the Assembly
of an oath as a condition for holding any benefice or office, placed
in the hands of the bishops, who had been driven by the loss of their
revenues into unappeasable hostility to the revolution, an arm of which
they were not slow to avail themselves, and by which they created a
schism within the Church (November 27). This oath engaged the taker
to be faithful to the nation, the law, and the King, and to maintain
the constitution. The object which the Assembly had in view was to
replace bishops who refused to take part in carrying out the new laws
by men attached to the revolution. The fact, however, that the oath
might be interpreted to imply acknowledgment of the lawfulness of
the Civil Constitution of the Clergy, the provisions of which were
inconsistent with the Papal system, was left out of account. The Pope
declared that those who had taken it were schismatics, and cut off from
communion with the Church. Passive acceptance of the civil constitution
was, therefore, no longer possible to the curés. Of 138 bishops and
archbishops only four took the oath, and two-thirds of the secular
clergy refused it. Many members of the regular orders, however, took
it, so that in the end about 60,000 ecclesiastics, or half of the
clergy of France, accepted the new arrangements.

By the imposition of this oath discord was aroused in every department.
The Assembly granted nonjurors a pension, and allowed them to
officiate in parish churches. The result was that in two-thirds of
the parishes of France there were two ministers, nominally of the
same persuasion, struggling, the one to gain, the other to maintain,
influence over the flock. The constitutional priest represented the
nonjuror, or former incumbent, as a plotter against the laws and the
constitution; the latter represented the intruder as a schismatic,
incapable of administering any sacrament, so that persons married or
children baptised by him were in reality neither married nor baptised.
Here nonjurors were regarded as enemies to the State; there the
constitutional clergy as enemies to religion; and whichever side
was the stronger proceeded to acts of violence against the other.
Generally, in the north of France, the nonjurors had comparatively
small influence; and it was only in certain provinces, where they had
the support of the peasantry--in Poitou, Auvergne, Alsace, and parts
of Artois, Franche-Comté, Champagne, Languedoc, and Bretagne--that any
large portion of the population exhibited zeal in their behalf.

Bold and radical reformers as the makers of the constitution proved
themselves, monarchical sentiment and distrust of the political
capacity of some million and a half of their countrymen had caused
them at times to shrink from carrying out fully Rousseau’s theory of
the sovereignty of the people. Hence, while their work was on one side
attacked by the party of reaction, on the other it was decried by the
extreme left, as being in contradiction to the principles which the
Assembly had itself proclaimed in the Declaration of Rights. Outside
the Assembly these views were even more strongly expressed. ♦Brissot.♦
One of the most noted journalists of the time, Brissot, combined
with ultra-democratic tendencies a firm belief in the advantages of
individual liberty, and was a zealous exponent of opinions subsequently
known as Girondist. His ideal form of government, which he aspired
to see established in France, was a democratic republic, where no
civil or political distinctions existed between man and man; where
habits of local government and obedience to the law allowed, without
detriment to public order, the action of the central government to
be barely visible; where principles of free trade, liberty of the
press, and religious toleration were carried systematically out; where
education, respect for labour, simple and virtuous habits of life
prevailed amongst all classes. On the ground that vice and corruption
readily found footing in large towns, Brissot was averse to the capital
exercising political ascendancy over the country. ‘Without private
morality,’ he said, ‘no public morality, no public spirit, and no
liberty.’ The goal here pointed out was truly Utopian as compared with
the actual condition of things in France. Nevertheless, Brissot was
credulous enough to believe that, owing to the beneficial influences
of general education and free institutions, its attainment would be
possible in the course of some twenty or thirty years.

♦Desmoulins.♦

In Camille Desmoulins the levelling principles of the revolution found
their ablest advocate. He belonged to the lower section of the middle
class; and, while speaking in the name of the people, gave expression
to the intense jealousy with which men in his position of life regarded
claims of property or of birth to political or social distinction.
Young, naive, and enthusiastic, Desmoulins was incapable of throwing
dust in his own eyes or in the eyes of others, and from the first
avowed that even the form of monarchical government was incompatible
with the principles that his party held. Since, however, the Assembly
ordained that France was to have a king, he expressed his readiness
to take off his hat when Louis passed by, but he refused to recognise
Marie Antoinette as Queen, and only made mention of her as the King’s
wife. Desmoulins was no precisian like Brissot, and did not concern
himself with the moral disposition of his fellow-countrymen. When
attacking men whom he designated as ‘reactionaries’ and ‘aristocrats,’
without heed of consequences, he made use of every arm which served
his end--irony, calumny, and gross exaggeration. The prevailing state
of anarchy he made light of. Rousseau had said that the people were by
nature merciful and forgiving, and his disciples palliated acts of
ferocity on the score of ignorance and misery. Was it to be expected,
Desmoulins asked, that after centuries of debasement liberty could be
obtained without a little blood-letting?

♦Marat.♦

Marat, a writer of a third type--called, after the title of his
journal, the ‘People’s Friend’--had no faith in any of the distinctive
principles of the time. He did not believe in the goodness of human
nature, nor in reason as the main lever by which to reconstitute
society and government, nor in the political capacity of his
countrymen, and was as ready to throw suspicion on the people’s
nominees as Brissot on the integrity of men put in office by the
King. He did not regard either commercial or individual liberty as
necessarily calculated to increase the happiness and prosperity of
the masses. The goal to which he pointed was a shadowy one of a
democratic state, where mediocrity ruled, and government provided that
the working-classes lacked neither labour nor bread. His means were
the re-establishment of absolute power and the use of force. Since
officials were corrupt, the upper classes seeking power merely for
selfish ends, the people ignorant and easily deceived, Marat proposed
to invest a dictator with authority to establish genuine equality by
crushing under foot the possessors of wealth and talent. As, however,
there appeared no probability of the adoption of this plan, he filled
the pages of his journal with incentives to murder and insurrection,
advising the people to secure their happiness by rising and killing
their enemies in a body. Some thousands of heads laid low, the true era
of freedom and prosperity would open.

♦Sources of influence of ultra-democrats.♦

Besides Brissot, Desmoulins, and Marat, there were a number of other
writers who in words declared their loyalty to the constitution,
while they excited discontent against it, called in question the
patriotism and good faith of all who did not agree with themselves,
and rendered harder the task of maintaining order. They had different
aims and different views of life, but on certain points they were
all agreed, and for the time the points of agreement alone came into
prominence. With one voice they cast bitter reproaches on the Assembly
for dividing Frenchmen into active and passive citizens, denying the
suffrage to the latter, and excluding them from the national guard.
So, again, they denounced the royal veto on decrees, on the ground
that it subjected the will of the sovereign people to the will of
the king. They condemned the Riot Act, and attacked the Assembly
whenever sanction was given to the employment of military force against
rioters. When the mutiny at Nancy was suppressed in blood, a loud
cry of indignation was raised against Lafayette and other deputies
who on that occasion abandoned the popular side. The ultra-democrats
formed undoubtedly but a minority of the population. The majority of
Frenchmen were content with the constitution, and had no desire to make
more radical changes than those already accomplished. Many causes,
however, enabled the ultra-democrats to exercise influence quite out
of proportion to their numerical strength. It was not merely that
the Government was weak, but also that there was no cohesion between
classes, and that there was no class capable of leading the nation by
obtaining its entire confidence. Suspicion of the nobles was so strong
that they were already nearly in the position of a proscribed class.
The bourgeoisie had not the habit even of administering local affairs,
and was itself regarded with suspicion by the class beneath it. The
people, both ignorant and discontented, regarded those men who were
for the time in office as responsible for their misery. If corn and
bread were dear, the municipal officer who would not lower their price
was denounced as an aristocrat, and his life was threatened. Men of
the middle class, engaged in professional and other pursuits, withdrew
in large numbers from political life. The ultra-democrats, active,
united, and unscrupulous, were therefore able, although a minority, to
put themselves forward as representatives of France, and gradually to
engross the direction of affairs in their own hands.

♦Influence exercised by Jacobin clubs.♦

In the National Assembly which represented France as it was in 1789,
the party did not, as has been seen, number more than from twenty to
thirty, but its weakness in the Assembly was fully atoned for by its
strength in the Jacobins. This society had developed into a political
organ which was none the less powerful because its authority was
not recognised by the laws. During 1790 and 1791 Jacobin clubs were
established in most provincial towns, and even in mere villages. They
were generally affiliated to the head or mother society at Paris, with
which they maintained a regular correspondence. Thus, at a time when
all other bonds of cohesion had been destroyed or had fallen away,
there was rising into existence over France, outside the constitution,
a network of authorities, directed from a common centre in Paris.
The clubs, in fact, perpetually interfered with the administrative
bodies, tendering advice which often assumed the form of dictation
or intimidation, and were always able, if they pleased, to get up
demonstrations in favour of their own views. They represented that
spirit of distrust which was everywhere felt and seemed to pervade the
very air men breathed; and if more moderate politicians disapproved
the violent language often used in them, and their assumptions of
administrative authority, they did not desire their suppression, for
the reason that their fear of danger from this source was less than
their fear of the triumph of reactionists and the undoing of the work
of the revolution.

In September 1790, the ministry had been dissolved in consequence of
attacks made on it by the Jacobins of Paris. Necker, painfully alive
to his loss of popularity, left the country unregretted (September),
and his colleagues, alarmed at the charges brought against them,
shortly afterwards resigned. Louis after this put men in office known
to be opposed to the restoration of the old order, but they possessed
as little influence on the Assembly as their predecessors. The right
refused them support, because they did not belong to the party of
reaction; and the left, because their attachment to the existing
constitution was called in question.

♦Commune of Paris.♦

Besides the Jacobin Club, other machinery existed at Paris by aid of
which the ultra-democrats were gradually paving the way for their
own advent to power. In September 1790, the commune of Paris was
reorganised in accordance with a special law, being divided into 48
sections, each of which had its primary assembly, composed of active
citizens. Out of a population of 800,000, 84,000 were entitled to vote.
Each of the 48 primary assemblies, commonly known as the sections, had
a permanent committee, whose business it was to execute the orders
of the municipality, and to carry out police regulations within the
section. The municipality itself, of which Bailly was re-elected mayor,
consisted of a general council of 96 and an executive of 44 members.
It did its best to maintain order and support the constitution. Its
position, however, was a difficult one. Work was scarce, crime rife,
the prisons crowded. Liberty of speech and of the press was on all
sides abused. There were no laws by which political agitation, though
it took the form of treason to the constitution, could be legally
suppressed. In the sections, owing to the withdrawal into private
life of men of moderate views, the ultra-democrats were often able to
obtain the upper hand. The permanent committees, in place of obeying
the municipality, sometimes disputed authority with it or took an
independent course of their own. All the 48 primary assemblies were
entitled to meet whenever eight of their number made the demand in
legal form. In the poorer sections agitators, by unceasing hostile
criticism, undermined amongst the lower classes the popularity of
the Assembly, of the municipality, of Lafayette, and of the national
guard. Amongst many popular clubs, founded in different parts of Paris,
the _Cordeliers_ south of the Seine acquired special notoriety. Here
presided Danton, an orator distinguished among his fellows by the zeal
and energy which he flung into the contest with the municipality.

♦Mirabeau’s policy and death.♦

As the revolution thus ran its course, and the ultra democratic
party, with the populace behind it, threatened by its activity and
unscrupulousness in time to make itself entire master of the political
arena, the stronger had become Mirabeau’s desire to enter the ministry
and direct the counsels of the King. From entrance into the council he
was, however, for the time hopelessly debarred. To nip his ambition in
the bud, Necker and his colleagues, shortly after the King’s arrival
in Paris, had instigated the Assembly to decree that no deputy should
be a minister. In the spring of 1790 the King and Queen were induced
to enter into secret communication with the great orator. He tendered
them advice in a written form, and the King in return for his services
made him monthly payments. But Mirabeau soon experienced that except in
trivial matters his advice was never followed. He demanded a far fuller
and more generous acceptance of the principles of the revolution than
it was possible for Louis to give. He accepted as absolute gain, both
for the King and the nation, the fall of the parliaments, the abolition
of privileges, the destruction of the orders of nobles and clergy,
and the freeing of land and labour. Unceasingly he urged and implored
Louis to win the confidence of the nation by turning his back wholly
on the past, and separating the cause of the crown from that of the
upper orders. ‘To accomplish a reaction,’ he wrote, ‘you must destroy
at a blow a whole generation or make blank the memories of twenty-five
millions of men.’ Mirabeau accepted also as the noblest fruits of the
revolution freedom of worship, freedom of the press, and the freedom
of the individual from arbitrary treatment in property and person. But
while detesting government that was arbitrary, or which went astray
through want of means to test public opinion, Mirabeau had little
faith in the wisdom of collective bodies of men, or in the political
intelligence of the middle and lower classes, of whom he believed that,
in the long run, the one would sell political liberty for order, the
other for bread. He, therefore, looked to the King to be the guide and
leader of the nation. His belief was that if only the existing barriers
of distrust were broken down, the middle-class, relieved from fear
of reaction in favour of the nobility and the Church, would readily
assent to the establishment of a strong executive and the repeal of
the decrees making administrative bodies independent of the central
government, and excluding ministers from the legislature. He had,
moreover, the penetration to see that the abolition of aristocratic
institutions, and the parcelling out of the country into equal
divisions, without historical traditions, were measures destructive of
variety and vigour in the national life, and thereby favourable to the
exercise of power by the crown. Unless the course that he advised were
followed he predicted the fall of the throne. ‘The mob,’ he repeatedly
said of the King and Queen, ‘will trample on their corpses.’ In despair
of getting the existing Assembly to repeal its decrees, Mirabeau
advised the King to quit Paris, and after doing all in his power to win
the middle-class to his side to make, if necessary, an appeal to arms.
While, however, he was urging such projects on Louis his naturally
strong constitution, overtaxed by his exertions, broke down, and he
died at the age of forty-two (April 2, 1791). It is wrong to regard
Mirabeau as having been false to his principles because he entered into
a pecuniary transaction with the King. He was a monarchist before 1789,
and he died one in 1791. But the low moral elevation of his character
vitiated his judgment, and increased the difficulties in his path.
By taking money of the King he was precluded from the possibility of
obtaining his confidence. Louis and Marie Antoinette never regarded him
otherwise than as a dangerous demagogue bought over. The distrust in
which his fellow deputies held him was not without justification. He
was quite unscrupulous as to what means he employed to gain his ends,
and did not hesitate to speak words in direct opposition to his real
opinion, nor to support measures which he deemed injurious, in order
to lower the Assembly in the opinion of the country, and increase the
possibility of bringing about a reaction in the royal favour. It is
difficult to doubt that his intense mortification at being excluded
from the ministry made him more ready to countenance the idea of civil
war.

Although long before his death ultra-democrats had accused Mirabeau of
playing a double game, they could not prove the truth of their words,
and to the last the great orator retained his popularity amongst the
people. His remains were interred in the Panthéon, a large church lately
built on the south side of the Seine, which the Assembly had reserved
for the special burial-place of Frenchmen who by their services had
won the honour and gratitude of their country. A vast crowd formed his
funeral procession. A lady, annoyed by the dust, complained of the
municipality for neglecting to water the boulevard. ‘Madam,’ replied a
fishwoman, ‘they reckoned on our tears.’ Whether true or not, the story
bears witness to the feelings of the time.

♦Position of Constitutionalists.♦

When Mirabeau died a significant change of temper was drawing over the
Assembly. As the framers of the constitution approached its completion
the truth began to press home on them that its stability was imperilled
by the continuance of disorder. They saw taxes refused, administrative
bodies pursuing whatever course was right in their own eyes, peasants
pillaging corn, street mobs persecuting nonjurors, soldiers refusing
obedience to officers, their own popularity waning, clubs usurping
authority, ultra-democratic journals discrediting the constitution,
and incessantly urging on the people the duty of insurrection. Now
that a free constitution was established, and reform effected in every
branch of the public service, justification for this state of things
from their point of view vanished. Lafayette, Barnave, the Lameths, and
other deputies of the left, who in 1790 had purposely sought to render
the executive weak, in 1791 began to fear lest they had overshot their
mark. Yet for them to change their course was no easy matter. They
still sought for popular support, and clung to the principles on which
the constitution of which they had themselves been the authors was
based. Fear of reaction, moreover, still weighed heavily on them. The
reactionary press, in coarse and violent language condemned the entire
work of the Assembly, and threatened with the axe or the gallows
all who from the opening of the States had at any time given support
to revolutionary principles. Such threats were not without meaning
at a time when emigrants were collecting in armed bands at Basel and
Coblentz, threatening invasion; and the King’s brother, the Count of
Artois, was calling on foreign powers to restore by force of arms the
authority of the throne.

The primary assemblies for the election of the constitutional
legislature were already meeting, when an event took place which
brought into clearer light the relations existing between all parties.




CHAPTER V.

THE FALL OF THE MONARCHY.


♦Flight of the Royal Family.♦

To the King and Queen their position had long since become intolerable.
They regarded the constitution as a monstrous work, based on principles
subversive of all good government. To the laws establishing the
Civil Constitution of the Clergy and imposing an oath on beneficed
ecclesiastics, Louis had given his official consent with reluctance,
but as he was unable to obtain the sanction of the Pope to what he had
done, his peace of conscience was gone. The Queen was greatly suspected
of using her influence to incite her husband against the revolution.
She was intensely unpopular. Up to the middle of the century France
had pursued a policy of opposition to Austria. In 1756 jealousy of
England, and of England’s ally, the rising state of Prussia, had
brought about an offensive and defensive alliance between France and
Austria. The national feeling of hostility had, however, not died out,
and the insignificant part that France took in foreign affairs was
ascribed not to the decadence of the monarchy, but to the Austrian
alliance. To make firm the bond, the partisans of the new system had
accomplished, in 1770, a marriage between Louis, then Dauphin, and
Marie Antoinette, daughter of the Empress Queen, Maria Theresa. Thus,
from her first entrance into the country, Marie Antoinette had been
regarded with disfavour, as the pledge of an unpopular alliance.
Courtiers and intriguers, opposed to the faction which had brought
about her marriage, had accused her of sacrificing French to Austrian
interests, and had bruited false and scandalous tales against her name.
By the revolutionary journalists she was now held up to execration
as the untrue wife and false Queen, the betrayer of France, who was
seeking by aid of Austrian troops to put down the revolution in blood.
Now that trouble had destroyed her love of dissipation and brought
into relief the strong side of her character, Marie Antoinette devoted
all the energy of which her mind was capable to the task of recovering
for her husband and bequeathing to her son the reins of government.
She found her chief pleasure in the fulfilment of her duties as wife
and mother, and by her dignified bearing impressed those who came into
contact with her with a high idea of her daring and intellect. Less
ready, however, than her husband to make concessions, and far more
so to practise deceit, she proved an evil councillor to Louis. Both
desired that the constitution should fail, and regarded the increase
of disorder with indifference, under the idea that suffering would
speedily recall their penitent subjects to the foot of the throne.
Meanwhile, Louis made repeated and public avowals of his satisfaction
with the constitution, intending hereafter to withdraw his words on
the plea that he was not at liberty to express his true opinion. Since
the winter a plan of flight to the eastern frontier was projected, but
its execution was delayed owing to want of money and troops. The Queen
relied on her brother, the Emperor Leopold, to place whatever Austrian
troops were in Luxemburg at her disposal in case of need. She thought
that if the King were once in safety on the frontier, and able to
protect his supporters, a large portion of the nation would rally round
him, and that it would be possible to make a settlement which, while
leaving to the country some form of constitutional government, would
set the royal authority above the heads of all subjects. Rumours that
the King intended flight had for months been floating about. In April,
the national guard, in spite of Lafayette’s remonstrances, detained by
force the royal carriages when on the point of starting for the Palace
of St. Cloud, a short distance outside the city.

The King and Queen had for some time been preparing for flight, though
the day of departure had been from various causes delayed. Servants
who could not be trusted had to be dismissed, and clothes and other
articles forwarded to the frontier ready for use. On the night of
June 20 the King, disguised as a valet, his sister, the Princess
Elizabeth, the Queen, the two children, and their governess, left the
Tuileries unobserved, and were driven in a hackney-carriage a short
distance outside Paris. Here they found ready waiting them a large
new travelling coach, built for the occasion, and three soldiers of
the bodyguard, dressed in yellow liveries, and prepared to act as
couriers. The destination of the royal party was Montmédy, close to
the Luxemburg frontier; and the Marquis of Bouillé, who commanded
in that quarter, had undertaken to station detachments of troops to
guard the way at all the chief towns and villages after Chalons. It
was already two o’clock at night when the coach left Paris behind.
The driver urged on his horses at a quick pace, some eight miles an
hour, and about five o’clock in the afternoon the travellers reached
Chalons-sur-Marne. At this point the most dangerous part of the journey
seemed over. At the next post-house, Pont Sommevesle, Louis expected to
see the first detachment of Bouillé’s troops. On his arrival, a little
after six, he was, however, disappointed. Bouillé had, indeed, with
considerable skill, ordered the passage of troops so that detachments
should be present at all the principal places on the road along which
the royal party was travelling; but unfortunately at each station
those in command lacked either zeal or capacity, or both. Because the
coach was three or four hours behind the time expected, the troops had
already withdrawn from Pont Sommevesle. At St. Menehould, Louis, who
incautiously put his head out of window, was recognised by the master
of the post, Drouet, who observed his likeness to the image of the King
on the assignats. Though not stopped, the coach was pursued by Drouet
and others, whilst the troops present in the town suffered themselves
to be disarmed. About midnight the coach safely reached Varennes, a
little town divided in two by the river Aire. While the bodyguards
were vainly seeking in the darkness a relay of horses, which was
waiting on the farther side of the bridge, Drouet and his companions
rode into the town, roused the mayor, and with whatever waggons and
barrels came first to hand, blocked the road over the bridge. The coach
was stopped, and the travellers compelled to alight and enter a house
belonging to a grocer, the procureur of the commune. This was close to
the bridge, beyond which were sixty hussars in their barracks. Their
officers, in place of calling them out on the first alarm, rode off to
seek instructions of Bouillé, who was miles away, at Stenay. Fifty or
sixty more troops arrived shortly afterwards, and during the night it
was still possible to disperse the opposers with a charge, and force a
way through the barricade. The officers, unwilling to do it on their
own responsibility, sought commands of Louis, who refused to take any
decisive action. The Queen, nearly on her knees, implored the wife of
the procureur, Madame Sauce, to let them proceed on their way. The
woman expressed sympathy for her, but said that she too had a husband
and children to care for. Meanwhile barricades were being strengthened,
the alarm-bells were ringing through all the countryside, and by the
morning the town was crowded with national guards, with whom the
troops were drinking. The return journey was therefore begun, and five
days after their departure the fugitives re-entered the Tuileries as
prisoners (June 25).

♦Split between constitutionalists and ultra-democrats.♦

When Louis’s flight was first reported, intense alarm prevailed at
Paris. It was expected that civil war, already organised, was on the
point of breaking out, and that the emigrants were about to cross the
frontier. The King’s capture brought a sense of relief, but did not
tend to lessen the difficulties of the situation. In justification
of his departure, Louis had left behind him a document, in which he
criticised the constitution from an unfavourable point of view, and
called in question all that had been done since October 1789. Thus
by act and word he had made known, without disguise, his intention
not to rule in accordance with the constitution, and henceforth
it was impossible that the country should have confidence in him.
Ultra-democrats with one voice wisely pronounced his protest and flight
a virtual abdication. Some, slow to take a decided part, amongst whom
Robespierre was prominent, or desirous of putting the Duke of Orleans
forward, demanded Louis’s deposition and a regency; others, as Brissot,
Desmoulins, and Danton, more sanguine and more outspoken, called
for the establishment of a republic. The Cordeliers, under Danton’s
guidance, covered the walls with placards in favour of a republic.
The Jacobins, following Robespierre, stopped short of this, and asked
only for the deposition of Louis. Closing their eyes, however, to the
undoubted fact of the King’s insincerity, the deputies of the left and
centre rallied together to support the tottering throne. They were
aware that the republican party was but a small minority. Lafayette and
Barnave, as well as other deputies, held themselves pledged in honour
to Louis to maintain his throne. In case of deposition, there was
increased danger of involving France in foreign war. Neither a change
of succession nor a regency appeared desirable. The King’s brothers
were emigrants, the Duke of Orleans a tool in the hands of Parisian
demagogues. Above all, there was fear that the deposition of Louis
would tend to undermine the constitution itself, and give increased
influence to the advocates of pure democracy. Under the influence of
such motives, the Assembly determined to restore the executive power
to Louis, should he accept the constitution when presented to him as
a completed whole. The republican party attempted a demonstration
against this decision. On Sunday, July 17, a large gathering of persons
assembled in the Champ de Mars, where a petition was signed asking
the Assembly to reconsider its decrees. The meeting itself was not
illegal, and in character perfectly peaceful. It was possible, however,
that within twenty-four hours the petition would be brought before the
Assembly supported by an armed and threatening mob. Urged on by the
monarchists, the municipal officers, accompanied by Lafayette and the
national guard, marched to the place of assemblage. Before the Riot Act
was read or dispersion possible, some companies fired, in irritation,
into the throng, killing and maiming several persons, men, women, and
children. General flight followed, and the petition was no more heard
of.

♦Attempt to revise the Constitution.♦

This event, known in the annals of the revolution as the massacre of
the Champ de Mars, caused complete severance between the men who were
bent on maintaining the constitution and the ultra-democratic party. A
schism took place in the Jacobins. The constitutionalists founded a new
club, the Feuillants, so called because it met in a convent formerly
belonging to monks of that name, while the ultra-democrats remained in
undisputed possession of the Jacobins. Amongst the constitutionalists
or Feuillants were Lafayette, Barnave, the Lameths, and all the most
prominent men of the centre and left. Could they have done their
work over again, they would have introduced material changes in the
constitution, with the double object of making it more acceptable
to the King, and enabling the ministry to exercise control over the
administrative bodies. Their main fear was that, after the dissolution
of the existing Assembly, new men would come into power who, having
had no hand in framing the constitution, would not have the same
interest as themselves in sustaining it. According to a constitutional
law, those who had been deputies could neither enter the ministry nor
hold any government appointment for a certain number of years; while
a special law forbade the election of men who had been members of the
present constituent Assembly to the ensuing Legislature. Robespierre
had proposed this latter law in April 1791, and to obtain its adoption
had appealed to the deputies to give proof of disinterestedness.
When the constitutional laws were adopted in a body, ready for final
presentation to Louis, some few amendments were made, but the attempt
of the constitutionalists to obtain the repeal of these important
disqualifications failed. The right voted with Robespierre and Pétion,
rejoicing over the falling out of their opponents.

♦Work of the Assembly.♦

Louis, when the constitution was presented to him, undertook to
govern in accordance with it, and the deputies then dispersed to give
place to their successors (September 30). Called upon to effect in
the course of a few months changes which could only be accomplished
without convulsions in the course of years, whatever their errors, they
had rendered France many and great services. By their legal reforms
alone they did away with an untold amount of mental and physical
suffering. By their economical and financial reforms they paved the
way for a new era in agriculture and industrialism. If, under passion
and prejudice, they had on occasions wantonly increased the number
and fury of opponents, yet much that they had been called on to do
remained still undone, and when they closed the sittings there was
small prospect that the tide of revolution would stop at the limit
which they had drawn. They had found neither time nor opportunity to
establish any general system of poor relief or any national system of
education. By their decrees dealing with proprietary rights they had
struck at the root of the old law, but the work of promulgating a new
code they left to those who came after them. With the fiefs had fallen
the law of primogeniture, but liberty of devise had been left in the
main unrestricted, though in default of a will all relations equal
in blood inherited equally. This principle of equal division was not
a speculative invention of the revolution, but as regards land held
by certain tenures, it had already existed in some parts of France.
The finances of the state had been restored only on paper. All the
expenses of government were regulated and the civil list fixed. Four
main branches of the revenue, tobacco and salt monopolies, excise
duties, and duties on wine had been abolished. The yearly expenditure,
including the expenses of the Established Church, was estimated at
27,900,000_l._, of which 21,350,000_l._ had to be raised by taxation.
In place of the _taille_ a tax of 13,125,000_l._, rated by local
boards, was imposed on lands and buildings. Taxes of 2,625,000_l._
were imposed on personal property. The remaining 6,000,000_l._ were
to be raised by various forms of indirect taxation, custom duties,
stamp taxes, and trade patents. The debt, however, during these two
and a half years of revolution had been greatly augmented, and the
deficit increased. The holders of the abolished offices had been
liberally indemnified, and the reforms effected in all departments
cost the nation no less than 61,200,000_l._, swelling the state debt
to more than 87,500,000_l._ Meanwhile the people had refused to pay
the old taxes long before their abolition by the Assembly, and it was
now only with difficulty that some portion of the new was collected.
Not only to pay state creditors, but also to cover the expenses of
government, resort had been had to new issues of assignats, and in
the spring of 1791 the paper money fell in value about ten per cent.
Metal money became scarce, being sent out of the kingdom or kept in
reserve. To supply the circulation, assignats of a few shillings value
had been created, and thus their fall in value affected all classes.
In September 1791 there were in circulation assignats to the value of
about 48,125,000_l._

♦Plans of the Queen.♦

Marie Antoinette and Louis had no other aim in accepting the
constitution than to deceive the nation until foreign powers were
ready to act in their behalf. After her return from Varennes the Queen
repeatedly urged on her brother, the Emperor Leopold, to effect the
meeting of a European congress for the settlement of French affairs.
This congress was to have at its disposition an army; but the Queen
wished that war should be avoided. Her expectation was that the
country, under terror of invasion, would gladly accept the mediation of
the King, and consent to a remodelling of the constitution according
to his wishes. She sought to separate the cause of the crown alike
from the cause of emigrants and of constitutionalists. She recalled
with bitterness the opposition of the nobles to the government
before 1789, and deeply resented their subsequent flight as a base
desertion of the royal cause. Their present conduct stood in the way
of the accomplishment of her own plans and heightened her feelings of
resentment. They refused to accept as sincere the King’s acceptance
of the constitution; they excited the country by threats of invasion
and vengeance; and, by representing themselves as defenders of the
monarchy, brought on Louis suspicion of being their accomplice. ‘The
cowards,’ she indignantly wrote, ‘first to abandon us, and then to
require that we should think only of them and their interests!’ To
alliance with the constitutionalists Marie Antoinette was as averse as
to alliance with the emigrants. Even were they willing and able to make
some modifications in the constitution, to rule on their terms was to
rule under their tutorship. Accordingly, while pretending to be acting
with them, she looked forward with impatience to the day when she might
with safety show her hand and prove them her tools and dupes.

♦State of Europe.♦

There was, however, small probability that a European congress would
meet; still less that the nation would, without resistance, submit
to foreign interference. Europe was in a disturbed condition. The
great powers had no confidence in one another, nor were they desirous
of acting in union. The empire of which the Queen’s brother was the
head was composed of more than 300 states, greatly varying in size.
The Peace of Westphalia, concluded at the end of the Thirty Years’
War (1648), had assured the princes all the rights of independent and
absolute rulers. Imperial institutions were in decay. The military
organisation of the empire was very defective and inefficient for its
defence. The Diet consisted merely of a few diplomatists, sitting
permanently at Ratisbon, who were representatives of the larger states,
and whom the smaller entrusted with their votes. Under Frederick the
Great (1740–1786) Prussia had developed into a strong power, which
acted as a rival to Austria within the empire. On all important
occasions the larger states followed the lead either of the Emperor
or of the King of Prussia, and between the cabinets of Vienna and
Berlin a bitter antagonism existed. Russia was another state which,
during the past hundred years, had risen into prominence. The Empress
Catherine II. was an able and ambitious woman, who had made use of the
rivalry existing between Prussia and Austria to interfere with effect
in the affairs of Central Europe. Throughout the century, all the great
powers, influenced by ambition and a desire for strengthening their
frontiers, had pursued a policy of territorial aggrandisement. Louis
XIV. had taken from the empire Alsace and Lorraine; Frederick the Great
had torn Silesia from Austria; in 1772, Catherine II., Frederick the
Great, and Maria Theresa together had deprived Poland of some of her
provinces; more recently the Emperor Joseph II., son of Maria Theresa,
had sought to incorporate Bavaria with the Austrian dominions, and
had formed an alliance with Catherine for the spoliation of Turkey.
In 1783 Catherine obtained the Crimea, thus extending her dominions
to the Black Sea. Under this condition of things, the main security
of the weaker states was found in the jealousy existing between the
more powerful. The principle of the balance of power required that
no large alterations should be made in the map of Europe, and that no
one power should make territorial acquisitions unless others obtained
an equivalent. Thus the opposition of Frederick the Great had foiled
Joseph’s project of incorporating Bavaria. It was the traditional
policy of France to support Sweden, Poland, and Turkey against
aggression, and the readiness with which the first partition of Poland
was carried out in 1772 was wholly owing to the decadence into which
the French monarchy had fallen under Louis XV.

♦Europe and the revolution.♦

In 1789, when the States-General met, Joseph and Catherine were engaged
in hostilities with Turkey, while England, Holland, and Prussia
threatened to take part in the conflict on behalf of the Porte. This
war in the east, and the possibility of a European conflict diverted
attention from affairs in France. In February 1790, however, the
enterprising and ambitious Joseph II. died; and his brother and
successor, Leopold II., a prince of cool and cautious temperament, made
it his chief object to restore order within his own dominions, more
especially in Hungary and Belgium, which were still in a disturbed
state owing to Joseph’s reforms. To insure Austria against being
attacked by Prussia, he made, in July 1790, a treaty with Frederick
William II., nephew of Frederick the Great, at Reichenbach, and,
to free his hands more completely, entered into negotiations with
Turkey. He had no disposition to attempt the restoration of absolute
monarchy in France. It was the belief of continental statesmen that
where, as in Poland or in England, a constitutional form of monarchy
existed, the executive was necessarily weak and precluded from acting
with vigour or decision in foreign affairs. Hence neither Leopold
nor his chancellor, Kaunitz, took exception to the establishment of
constitutional monarchy in France, which indeed they regarded as a pure
gain to Austria. But after the flight of the royal family to Varennes,
and the manifestation of republican opinions in Paris, foreign princes
began to look on Louis’s cause as the cause of kings, and to dread
lest revolutionary principles, spreading beyond France, should render
their own thrones insecure. Leopold, desirous to aid his sister, sought
the alliance of Frederick William, and made peace with the Porte at
Sistova. A meeting was held between the two allied princes at Pilnitz,
where they signed a declaration expressing their readiness to undertake
armed intervention in French affairs, if other European powers would
unite with them (August 27). Practically this declaration was no more
than a threat. Neither Leopold nor Frederick William contemplated
immediate resource to arms. The English cabinet, directed by Pitt, had
already refused to take part in common action. The alliance between
Austria and Prussia was as yet but loosely knit and was regarded with
distrust by the old school of both Austrian and Prussian statesmen.
Affairs in the east, moreover, called for unremitting attention.
Poland, situated between three powerful and grasping neighbours, was
a prey to perpetual anarchy. The monarchy was elective, and the king
was kept in check by the fierce and seditious nobility by whose votes
he was placed on the throne. The peasantry were downtrodden serfs, and
the middle class without political rights; king and nobles struggling
for power invited foreign interference, and Russia and Prussia by
turns exercised ascendancy at Warsaw. In May 1791, a patriotic party,
eager to secure national independence by the establishment of a strong
government, obtained the adoption of a new constitution, curtailing the
privileges of the nobles and making the crown hereditary. This measure
at once excited the hostility of Catherine. She gave support to its
opponents, and in order that she might carry out her designs in Poland
undisturbed made peace with Turkey, and sought to stir up a European
war in the west, encouraging the French emigrants, and instigating the
German powers to interfere in their behalf. Catherine’s zeal, however,
rendered Leopold the less willing to involve himself in hostilities,
since events on the Vistula were of much more moment to him than the
details of the French constitution. When, therefore, in September,
Louis agreed to rule in accordance with the constitution, he affected
to regard him as a free agent, and in the hope that the constitutional
party would maintain the upper hand, turned a deaf ear to his sister’s
entreaties that he would obtain the meeting of a European congress.
The King of Prussia entertained a violent hatred of the principles of
the revolution, but Polish affairs and distrust of Austria restrained
him from coming forward as a champion of Louis’s cause. Thus, while
continental princes agreed that the revolutionary tide must be stayed,
nothing was settled as to time and means.

♦The new Legislature.♦

In such a state of foreign affairs the new Legislative Assembly met
(October 1), the only one which ever came together in accordance
with that constitution which had cost so much labour to build up. It
consisted of 740 deputies, who represented exclusively revolutionary
France. There were in it no partisans of the old rule, and no reformers
with aristocratic tendencies. The right side was now composed of
constitutionalists, who held that only by close adherence to the
constitution could the country be safely guided between the double
perils of reaction and anarchy. Though without confidence in the King,
they regarded him as much less powerful for harm than the leaders of
the Parisian populace, and sought on all occasions to maintain him in
the unrestrained exercise of his constitutional prerogatives. The left
of the Assembly, though avowedly constitutionalist, at heart cherished
a desire for the establishment of a more democratic government, and
the abolition of monarchy. A group of men, remarkable for youth,
talent, and eloquence, sat on this side of the house. They were called
Girondists, because their chief orators--Vergniaud, Gensonné, Guadet,
and others who formerly belonged to the bar of Bordeaux--had been
returned by the department of the Gironde. These men were fervent
democrats and republicans, and at the same time defenders of the
principle of individual liberty. They were also sceptics and theists,
inheritors of Voltaire’s passionate scorn and hatred of Catholicism.
Brissot, who now had a seat in the house, belonged to them, and his
journal became the recognised organ of their party. Their policy was
mainly dictated by a theoretic aversion to monarchical government,
and nervous apprehension of the consequences of Louis’s treachery.
Alive, however, to the fact that public opinion was in favour of the
constitution, they formed no definite plans for its destruction, but
endeavoured to obtain the adoption of measures calculated to reveal the
King’s duplicity, and so to weaken the hold that the throne had upon
the affection of the nation. The body of deputies forming the centre
of the Assembly sincerely desired the maintenance of the constitution,
but had no reliance on the good faith of Louis, and hence oscillated
between the right and the left, being desirous of maintaining the
throne, and yet being afraid to give to the executive a hearty support
or to take strong measures for the suppression of insurrectionary
movements.

♦Ecclesiastical policy.♦

Important questions pressed upon the Legislature for solution. The
ecclesiastical settlement attempted by the constituent Assembly was
being daily proved impracticable. In many cases the administrative
bodies strove hard to preserve the peace and to keep the Churches
open, both to the nonjurors and their rivals; but their efforts were
hopeless. Without a military force always at command it was practically
impossible to maintain both parties in their legal rights. In some
departments the nonjurors set themselves at the head of insurgent
peasants. In others they were subjected to insult and outrage. At Paris
they could celebrate mass only under the protection of national guards.
During the summer of 1791 many administrative bodies, on the plea that
by no other means could order be preserved, prohibited nonjurors from
officiating in parish churches, and required them to reside in the
chief town of the department, away from their former parishioners. The
Legislature had no choice but either to abandon the imposition of the
oath or to follow it out to its logical consequences, and to regard
those who refused to take it as enemies to the existing order. The
last course accorded best with the prejudices of the majority, who
accused the nonjurors of being the sole authors of troubles to which
the situation itself could not fail to give rise. Some on the left
proposed to exile them in a body. The Girondists detested them as the
most bigoted of Catholics. The right weakly sought, on the ground of
religious liberty, to leave matters as they were; but the centre here
voted with the left, and a decree was passed depriving nonjurors of
their pensions, and preventing their officiating in public (November
25). Louis, however, refused his sanction, and the situation remained
unchanged.

♦Foreign policy.♦

A second and no less important question before the Assembly was the
policy to be pursued in relation to the emigrants and to foreign
powers. The Elector of Treves and other rulers of the small states, lay
and ecclesiastical, on the Rhine, gave encouragement and aid to the
emigrants in arming against France. These princes were eager to involve
the larger states of the Empire in hostilities. Their territories
were amongst the worst governed in Germany, and they feared lest
revolutionary principles should prove contagious, and affect their own
subjects. Many of them had, besides, a special ground of complaint. In
Alsace and Lorraine they possessed rights as seigneurs, secured to them
by the Treaty of Westphalia, and of which the decrees of August 4 (p.
50) had deprived them. This matter, however, might easily have been
arranged between France and the Empire had there been a disposition on
either side to maintain peace.

The principles of foreign policy pursued by the cabinets of Europe,
and the theories promulgated by the revolutionists, were in direct
opposition to one another. Statesmen took no account of national
forces or aspirations, but, intent on territorial acquisitions, were
ready to distribute populations of the same race and tongue among
different masters as suited diplomatic combinations. On the contrary,
the doctrine of the sovereignty of the people involved a right to
national independence. The constituent Assembly had publicly declared
the aversion of the French nation to offensive wars, and had given
proof of its pacific tendencies by limiting the army to 150,000
men. But the flight of the King and the drawing together of Austria
and Prussia gave rise to great uneasiness as to the intentions of
those powers, while the threat of interference in the Declaration of
Pilnitz gave deep offence to the national pride. Measures were taken
for increasing the army by an additional force of 97,000 volunteers.
The Legislative, like the constituent Assembly, repudiated ideas of
aggression and conquest, but became rapidly inflamed with warlike
zeal. It gave expression to the intense feelings of hatred existing
against the emigrants by a decree condemning to death as traitors all
Frenchmen who, after the end of the year, should still be beyond the
frontier in arms against their country (November 9). Louis refused to
sanction the decree, and thus increased the suspicion resting on him
of being the secret accomplice of those against whom it was aimed. The
Girondists desired war with Austria. They were aware that there was no
immediate danger of attack from the great powers, and that both the
emigrants and the princes who abetted them, unless supported by the
Emperor, were impotent; but they believed that, during war, the King’s
duplicity would be clearly revealed, and judged it the wiser course, in
place of waiting for attack, to begin hostilities, while Leopold still
sought to avoid them. Enthusiastic confidence in the national spirit
to fight to the last extremity in defence of its independence, and the
expectation that the principles of the revolution would spread rapidly
amongst other nations, and cause them to rise against their rulers,
led the Girondists to entertain no doubt of the success of their arms.
‘Let us tell Europe,’ exclaimed a fiery orator, Isnard, ‘that if
cabinets engage kings in a war against peoples, we will engage peoples
in a war against kings.’ Of the constitutionalists few cared to avoid
a rupture. The majority looked forward to war as a means of insuring
the ascendancy of their own party, and of bringing into existence
a powerful army under Lafayette’s command. There was no difficulty
in finding a ground of quarrel with Leopold either as Emperor or as
King of Hungary and Bohemia. The Assembly threatened to attack the
empire unless the bands of emigrants on the frontier were dispersed.
Afterwards, shifting its ground, it accused Leopold of having broken
the treaty of 1756 between France and Austria, and declared that a
refusal to renounce all treaties directed against the independence of
the French nation--in other words, his understanding with the King of
Prussia--would be held tantamount to a declaration of war (January 25,
1792). This hostile attitude of the Assembly hastened the conclusion of
a defensive alliance between Austria and Prussia; after which Leopold,
no longer caring to delay hostilities, added fuel to the flame by
claiming a right of interference in the internal affairs of France,
and by accusing the Assembly of being under the illegal ascendancy of
republicans and Jacobins.

The outbreak of war might probably have been postponed, but it could
hardly have been definitely averted. The doctrines of social and
political equality announced by the French revolutionists were not, as
were the arguments from law and precedent which had in the seventeenth
century risen to the surface in the English Long Parliament, adapted
merely to the country in which they arose. They were applicable to all
the states of Western Europe. Hence, they acquired all the force of a
religious propaganda. As in the sixteenth century men were not asked
whether they were Germans or Frenchmen, but whether they were Catholics
or Protestants, so now they would be first asked whether they were
on the side of the revolutionary opinions or not. Before that great
division of opinions all national antagonisms sank into comparative
insignificance. The French revolutionist could not long avoid being
carried away by a fierce desire to give effectual aid to his brother
revolutionist abroad, and the German or English anti-revolutionist
could not long keep his hands out of the fray whilst the classes in
France with whom he warmly sympathised were being borne down and
oppressed.

♦Declaration of War.♦

The ministry at this important crisis was disunited and without the
confidence of the Assembly. While the Assembly desired war, Delessart,
minister of foreign affairs, sought to maintain peace. The minister
of war, Narbonne, a friend of Lafayette, flung so much energy and
enthusiasm into the work of making preparations for hostilities that he
won support from both sides of the Assembly. Bertrand de Molleville,
minister of marine, was a reactionary. Louis through aversion to
Lafayette dismissed Narbonne from office. Brissot took advantage of
the discontent that this step excited amongst constitutionalists
to bring a charge of high treason against Delessart for betraying
the interests of France to Austria (March 10). This attack led to a
break-up of the cabinet, and Louis, whose one object now was to tide
with safety over the next few months, till the arrival of the allies at
Paris, put in office men who represented the opinions dominant in the
Assembly. Roland and Clavière, respectively ministers of the interior
and of finance, belonged to the Girondists. Dumouriez, minister of
foreign affairs, was an able, self-confident and unscrupulous soldier,
eager to obtain distinction and a career. On March 1, Leopold had
died. His son and successor, Francis, a young man of four-and-twenty,
who was some months later elected Emperor, cared less to avoid a
rupture than his father had done. The new French ministry was above
all a war ministry, and on the official proposition of the King, the
Assembly amid loud applause, declared war against Francis, as King of
Hungary and Bohemia (April 20). Wars have often been entered on with
as little ground of offence, but rarely with more rashness than when
the Assembly thus engaged France in hostilities with Austria, which
would necessarily involve a war also with her ally Prussia. The French
fortresses were out of repair and the army completely disorganised.
Since 1789 hundreds of officers had resigned, deserted, or had been
driven away by their men. According to the laws of the constituent
Assembly under officers were elected out of the ranks, and officers
generally advanced according to length of service. There were, however,
hundreds of vacancies still unfilled, and desertions both in army and
navy continued. Of the 150,000 troops of the line, 50,000 had yet to be
recruited. The 97,000 volunteers ordered to be raised were for the most
part unarmed and untrained.

♦Robespierre and the Jacobins.♦

The peril of the country excited on all sides suspicion and distrust,
increasing the bitterness of party strife and threatening to undermine
the standing ground alike of constitutionalists and Girondists.
Girondists as little as constitutionalists had an interest in making
further alterations in the bases of social order. If the Girondists
held more democratic notions of life and government, yet by equality
they understood equality of rights alone, and were to the full as
zealous defenders of the principles of internal free trade and
individual liberty. They were also political purists and precisians,
who, while decrying the aristocracies of birth and wealth, were intent
on founding one of talent and virtue. Hence no sooner had they obtained
possession of the ministries than they came into sharp collision with
whatever members of the ultra-democratic party did not share their
genuine devotion to impracticable ideals. A spirit different from
theirs was by this time rising into prominence amongst the Jacobins.
The saddest result of the long exercise of arbitrary authority is
that it renders mutual confidence impossible. The legacy of the old
system of government to the new France was distrust. Man distrusted
man, and class distrusted class. Thousands of persons who had embarked
in the revolution full of sentimental hope and confidence were now
rushing into the opposite extreme. They had known so little of their
fellow creatures as to imagine that the new equality would be received
with enthusiasm, even by those who had profited the most by the old
inequality; and they now fancied that under every reluctance to accept
the fullest results of the revolution was concealed a deep design
to betray it. A perfect self-confidence easily leads to the most
deep-rooted suspicion; and those who, after the long seclusion from
all participation in practical politics to which most Frenchmen had
been condemned for centuries, were inevitably ignorant how complicated
modern society is, readily imagined all who differed from them to
be traitors to their country. Not only was this suspicion directed
against the King and those of the once privileged orders who remained
in France, but it fastened upon all superiority of station or of
intellect. Many who had been educated in the theories of Rousseau to
believe unreasonably in the purity and intelligence of the masses,
learned no less unreasonably to distrust every man who in any way
rose above the common level, and offered himself with more or less
qualification as a rallying point to the disorganised society around
him.

The man who most represented this prevailing distrust of all
superiority would in the end gain for a time that very superiority
which he himself denied to be desirable, but which was required by
the very necessities of human nature. Such a man was Maximilien
Robespierre. A lawyer from Arras, he had been so far influenced by the
teaching of Rousseau as to throw up a lucrative judicial post, lest he
should be compelled to condemn a fellow-creature to death. From such
feelings of pity for the human race to cruelty towards individuals
there is in times of revolution, but a short step. The few who stood
in the way of the entrance of the people into the promised land, where
liberty, equality, and fraternity were to become the accepted rule of
life, soon came to be regarded as monsters of wickedness, whom it was
the duty of every good citizen to sweep away from the earth for very
kindness’ sake. The time for such a proscription had not yet come.
But Robespierre, though he was now excluded from the Legislature, as
having been a member of the last Assembly, was always on the alert in
the Jacobins, ready in dry and acrid tones to draw attention to every
delinquency of those who were struggling to build up authority. The
social and political formulas of Rousseau alone had taken root in his
mind. He cared for equality, and he cared for democracy. For individual
liberty he ceased to care as soon as he found himself in a position to
get the better of his adversaries by resorting to the arms of absolute
and despotic governments. He was certain to be a dangerous and a cruel
opponent. His mind was logical and narrow, he was ambitious and envious
of all above himself, cunning and hypocritical, yet earnest in pursuit
of his aims, incapable of strong affection, of a generous act or a
magnanimous resolution, and wholly devoid of moral sense. Whoever stood
in his light he regarded at once as a personal enemy and a traitor to
the people’s cause. By temperament he was nervous and cautious. He
never set himself at the head of popular movements, always guarded his
statements so as to mean much or little, according to circumstances;
and in case of danger, delayed till the last moment to take a decided
part. Robespierre opposed the war because he divined that both
constitutionalists and Girondists entered upon it with the aim of
obtaining for themselves mastery over France. While the Girondists
accused him of making himself the people’s idol, he accused them of
seeking power for party purposes. In the end he entirely destroyed the
popularity originally enjoyed by Brissot, Guadet, and others in the
Jacobins. The society had become even more democratic in character
since the constitutionalists abandoned it in July 1791. The galleries
were opened to the public, and were ordinarily filled by the most
ardent revolutionists belonging to the lower and lower middle classes.
Of this audience Robespierre won the entire confidence. He put himself
forward as the special representative of the people, whose wisdom
and goodness formed his constant theme. He personified the distrust
felt by the lower classes towards the possessors of rank, wealth, and
talent. He was himself indifferent to the enjoyments that wealth can
give, absolutely incorruptible, an orator without brilliant qualities
of any kind, but in appearance and language always respectable. Behind
Robespierre, frequenters of the Jacobins and joining in the attack on
the Girondists, were Desmoulins and others, to whom the preciseness and
exclusiveness of Roland and Brissot gave offence, besides adventurers
and agitators of the lowest type, whose sole object was to pave the way
for their own advent to power and office. Marat, in his journal, openly
accused the Girondists as well as the constitutionalists of being sold
to the court, and included both in the general proscription which he
unceasingly urged on the people of Paris.

♦Administrative anarchy.♦

The party conflicts waged in the capital were repeated in the
departments. The central government was powerless to impose uniform
action. Roland, the minister of the interior, issued circulars,
inculcating the duty of obedience to the laws, but words were powerless
to restrain the passions which the revolution had let loose. Each
administrative body followed its own course, according as it was
under the dominion of constitutionalist or Girondist opinions. In the
departments round Paris small armies of peasants and brigands, often
with municipal officers at their head, went about fixing a maximum
price of corn and other articles of food. In Languedoc and Guienne
insurgent bands extorted money and pillaged country houses. But nowhere
was administrative anarchy so great and crime so rife as in the four
departments of Gard, Bouches-du-Rhône, Vaucluse, and Lozère, where
reactionary and revolutionary elements came into violent collision.
In Lozère attempts were being made to excite amongst the peasantry
a Catholic reaction, and an armed camp, in communication with the
emigrants, was formed at Jalès. On the other hand, the municipality
at Marseilles, composed of violent ultra-democrats, raised a force
of 4,000 men, and disarmed a Swiss regiment at Aix, and the national
guard of Arles. Avignon, under mob rule, witnessed the commission of
horrible crimes. The Comtat Venaissin had belonged to the Pope since
1273, and Avignon, its chief town, since 1348. After the meeting of
the States-General civil war broke out within this small territory
between the supporters and opponents of revolutionary principles and of
union with France. The constituent Assembly sent mediators who patched
up a peace in January 1791. In September 1791 it at last decreed the
union of Avignon and the Comtat to France. But it had been too late to
prevent the perpetration of the most atrocious deeds. The force raised
by the French party, which had been recruited from the lowest sources,
quarrelled with its employers, the municipality of Avignon. A number
of persons were imprisoned without regard to age or sex. One of the
insurgent officers was in revenge brutally murdered in the streets.
His comrades, led by Jourdan, a brigand by profession, retaliated
by killing in cold blood sixty and more prisoners--men, women, and
children--whose bodies they flung into a dungeon beneath a tower of the
Papal palace (October, 1791). The assassins, though they were at first
imprisoned, afterwards obtained their release in right of an amnesty,
which the constituent Assembly before its dispersion had passed,
covering all crimes attaching to the revolution.

♦Position of Girondists.♦

The undisguised enmity of Robespierre, the cry raised for a maximum
price of corn, the tragedy of Avignon, the illegalities and crimes
incessantly committed, alarmed the Girondists, and tended to restrain
them from coming to open breach with the constitutionalists; but they
continued to regard domestic treason as far more dangerous than mob
violence, both to themselves and to France, and fearing to give the
executive the least vantage ground whence to facilitate the advance of
the Allies, opposed with vehemence the employment of coercive measures,
either to suppress political agitation on the part of the clubs, or
to restrain administrative bodies from passing beyond their legal
functions. They still entertained the belief that the people would be
brought to obey the voice of reason, and thought that were Louis’s
treachery once set in a clear light, the storm of revolution would pass
over with the establishment of a republican government, and the country
return without effort to paths of law and amity.

♦The 20th June.♦

Sense of danger made the Assembly the more eager to resort to
repressive measures against the emigrants and the nonjurors. The
property, real and personal, of the emigrants, was put under charge of
the administrative bodies, and their revenues confiscated by the state.
A decree, to which, however, the King refused his sanction, authorised
the directories of the departments to banish nonjurors who refused to
take an oath of fidelity to the nation, the law, and the King (May
27). Sanguine expectations of victory had been rapidly dissipated. In
April the Belgian frontier was crossed; but the troops on their first
meeting with the enemy fled in disorder, disobeying their officers,
whom they accused of treason. Servan, the minister of war, proposed the
formation of an armed camp for the protection of Paris. Much opposition
was however, raised to the project, and the Assembly decreed (June 6)
that 20,000 volunteers, recruited in the departments, should meet at
Paris to take part in the celebration of a federal festival on July
14, the third anniversary of the fall of the Bastille. The real object
of those who supported the decree was to have a force at Paris with
which to maintain mastery over the city should the Allies penetrate
into the interior. Louis left the decree unsanctioned, as he had the
one directed against nonjurors. The agitators of the sections sought
to get up an armed demonstration against this exercise of the King’s
constitutional prerogative. Though armed demonstrations were illegal,
the municipality offered but a perfunctory and half-hearted resistance.
Bailly had resigned office in the autumn of the preceding year. The
new mayor, Pétion, was a Girondist. During the winter half of the
municipal officers had been re-elected, and of the new members many
were ultra-democrats. Lafayette, no longer at the head of the national
guard, commanded on the eastern frontier. The officers of the guard
were mostly constitutionalists, but there was so little confidence in
the King that few were prepared to act with vigour or could answer
for the conduct of their men. Louis, irritated at the pressure put
on him by Roland, Clavière, and Servan to sanction the two decrees,
dismissed the three ministers from office (June 13). Dumouriez, who
had quarrelled with his colleagues, supported the King in taking this
step, but in face of the hostility of the Assembly himself resigned
office (June 15). Three days later a letter from Lafayette was read
in the Assembly. The general denounced the Jacobins as the authors of
all disorders, called on the Assembly to maintain the prerogatives
of the crown, and intimated that his army would not submit to see
the constitution violated (June 18). Possibly the dismissal of the
ministers and the writing of this letter were measures concerted
between the King and Lafayette. In any case the King’s motive was to
excite division between the constitutionalists and the Girondists, so
as to weaken the national defence. The dismissal of the ministers was,
however, regarded by the Girondists as a proof of the truth of their
worst suspicions, and no measures were taken to prevent an execution
of the project of making an armed, and therefore illegal demonstration
against the royal policy. On June 20, thousands of persons, carrying
pikes or whatever weapon came to hand, and accompanied by several
battalions of the national guard, marched from St. Antoine to the hall
of the Assembly. A deputation read an address demanding the recall of
the ministers. Afterwards the whole of the procession, men, women, and
children, dancing, singing, and carrying emblems, defiled through the
chamber. Instigated by their leaders they broke into the Tuileries. The
King, who took his stand on a window seat, was mobbed for four hours.
To please his unwelcome visitors, he put on his head a red cap, such
as was now commonly worn at the Jacobins as an emblem of liberty, in
imitation of that which was once worn by the emancipated Roman slave.
He declared his intention to observe the constitution, but neither
insult nor menace could prevail on him to promise his sanction to the
two decrees. The Queen, separated from the King, sat behind a table on
which she placed the Dauphin, exposed to the gaze and taunts of the
crowds which slowly traversed the palace apartments. At last, but not
before night, the mob left the Tuileries without doing further harm,
and order was again restored.

This insurrection and the slackness, if not connivance, of the
municipal authorities, excited a widespread feeling of indignation
amongst constitutionalists. Lafayette came to Paris, and at the bar of
the Assembly demanded in person what he had before demanded by letter
(June 28). With him, as with other former members of the constituent
Assembly, it was a point of honour to shield the persons of the King
and Queen from harm. Various projects for their removal from Paris were
formed, but policy and sentiment alike forbade Marie Antoinette to take
advantage of them. There was hazard in their execution, and the aims
of their authors were not hers. The one gleam of light on the horizon
of this unhappy Queen was the advance of the Allies. ‘Better die,’
she one day bitterly exclaimed, ‘than be saved by Lafayette and the
constitutionalists!’

♦Country declared in danger.♦

There was, no doubt, a possibility of the Allies reaching Paris that
summer, but this enormously increased the danger of the internal
situation. There were 80,000 Austrians and Prussians collecting on the
other side of the Rhine. To oppose their advance there were but 40,000
men stationed at Metz and Sedan, half of whom were recruits who had
never seen fire. The new ministers were constitutional monarchists
of weak type, who had neither energy nor a decided policy. It was
known that the army was not in a fit state to repel the enemy. The
Girondist orators unnerved the Assembly by asking whether the King
and his ministers desired that it should be in such a state? Both in
Paris and in the departments thousands of honest and patriotic men,
disgusted with party violence, and not knowing which side to take,
withdrew wholly into private life, or went to serve on the frontier.
To rouse the nation to a sense of peril the Assembly caused public
proclamation to be made in every municipality that the country was in
danger. The appeal was responded to with enthusiasm, and within six
weeks more than 60,000 volunteers enlisted. The Duke of Brunswick, the
commander-in-chief of the allied forces, published a manifesto, drawn
up by the emigrants. If the authors of this astounding proclamation had
deliberately intended to serve the purpose of those Frenchmen who were
bent on kindling zeal for the war, they could not have done anything
more likely to serve their purpose. The powers required the country to
submit unconditionally to Louis’s mercy. All who offered resistance
were to be treated as rebels to their King, and Paris was to suffer
military execution if any harm befell the royal family.

♦August 10.♦

The Jacobins openly proposed to depose the King. Those who shared
their views in the Assembly, however, consisted of but a small body
of members, who were called the Mountain, because they occupied the
topmost benches on the left. Unhappily the majority refused to take
into consideration a question the solution of which in the sense
indicated by the Jacobins would have spared much future misery to
both King and people. In the house of Roland, the dismissed Girondist
minister of the interior, projects were discussed of defending the
line of the Loire in case of the Allies reaching the capital. Madame
Roland, a talented, enthusiastic woman, who directed the actions of her
husband, was the centre of a small, and uncompromising circle, which
was ready to abet the destruction of the throne by violence. But the
leading Girondists--Vergniaud, Brissot, Guadet, and Gensonné--unwilling
that the republic should owe its origin to violence, were prepared to
give support to the throne had Louis assented to make the executive
dependent on the Legislature, and to restore the late ministers to
office. Their overtures to this effect were, however, rejected; and,
meanwhile, a second insurrection, which had for its object the King’s
deposition, was in preparation. The Assembly, after declaring the
country in danger, had authorised the sections of Paris, as well
as the administrative authorities throughout France, to meet at
any moment. The sections had, in consequence, been able to render
themselves entirely independent of the municipality. In each of the
sectional or primary assemblies from 700 to 3,000 active citizens had
the right to vote, but few cared to attend, and thus it constantly
happened that a small active minority spoke and acted in the name
of an apathetic constitutional majority. Thousands of volunteers
passed through Paris on their way to the frontier, some of whom were
purposely retained to take part in the insurrection. The municipality
of Marseilles, at the request of Barbaroux, a young friend of the
Rolands, sent up a band of 500 men, who first sung in Paris the verses
celebrated as the ‘Marseillaise.’ The danger was the greater since
every section had its own cannon and a special body of cannoneers, who
nearly to a man were on the side of the revolutionists. The terrified
and oscillating Assembly made no attempt to suppress agitation,
but acquitted (August 8) Lafayette, by 406 against 280 votes, of a
charge of treason made against him by the left, on the ground that
he had sought to intimidate the Legislature. This vote was regarded
as tantamount to a refusal to pass sentence of deposition on Louis.
On the following night the insurrection began. Its centre was in the
Faubourg of St. Antoine, and it was organised by but a small number
of men. Mandat, the commander-in-chief of the national guard, was an
energetic constitutionalist, who had taken well concerted measures
for the defence of the Tuileries. But the unscrupulousness of the
conspirators was more than a match for his zeal. Soon after midnight
commissioners from twenty-eight sections met together at the Hôtel de
Ville, and forced the Council-General of the Municipality to summon
Mandat before it, and to send out orders to the officers of the guard
in contradiction to those previously given. Mandat, unaware of what
was passing, obeyed the summons, and on his arrival was arrested and
murdered. After this the commissioners dispersed the lawful council
and usurped its place. At the Tuileries were about 950 Swiss and more
than 4,000 national guards. Early in the morning the first bands of
insurgents appeared. On the fidelity of the national guards it was
impossible to rely; and the royal family, attended by a small escort,
left the palace, and sought refuge with the Assembly. Before their
departure orders had been given to the Swiss to repel force by force,
and soon the sound of firing spread alarm through Paris. The King sent
the Swiss instructions to retire, which they punctually obeyed. One
column, passing through the Tuileries gardens, was shot down almost
to a man. The rest reached the Assembly in safety, but several were
afterwards massacred on their way to prison. For twenty-four hours
the most frightful anarchy prevailed. Numerous murders were committed
in the streets. The assailants, some hundreds of whom had perished,
sacked the palace, and killed all the men whom they found there. Of
the 749 deputies only 284 ventured to attend the sitting. The Assembly
was flooded by dense crowds calling for the deposition of the King.
A decree was passed pronouncing Louis provisionally suspended, and
summoning a National Convention to decide on the future form of
government. The distinction between active and passive citizens was
abolished, and manhood suffrage ordained. Roland, Clavière, and Servan
were restored to office, and the candidate of the Mountain, Danton,
appointed minister of justice.

The throne which had for so many centuries been the symbol of law and
order for the French nation, had fallen in a day before the attack of a
disorganised mob. Yet the very ease with which the insurgents succeeded
in their task carries conviction with it that the catastrophe was the
result of causes which had been long at work. In truth, the throne
of Louis had, since the meeting of the States-General, ceased to be
the symbol of law and order. Unable to guide the people whom he had
once called his subjects, Louis had become an obstacle in their path.
It was but natural that he should feel dissatisfied with the course
of events which had reduced him to that nullity for which alone his
character fitted him. Even in time of peace his existence in a place
of nominal authority would have been irritating alike to himself and
to those who still called him King. With the outbreak of war his
position became absolutely untenable. He could not but wish well to the
invaders, whose advent would free him from degradation and personal
constraint. The mere suspicion that such a wish was entertained by
him--and such a suspicion would be hard to silence--would arm against
him all who most prized the independence of their country, or would
make them indifferent to his fall. Even if he did nothing to assist the
invaders, his continuance on the throne would paralyse the national
defence. To remove the cause of that paralysis was the first step to
that reorganisation of anarchical France which the invasion had made
imperative. Though Louis had been struck down by a violent and unruly
mob, the submission of France to the act done in its name was more than
the outcome of that helplessness to which Frenchmen had been condemned
by centuries of despotic government. It was the silent acknowledgment
that Louis was out of place upon the throne.




CHAPTER VI.

THE FALL OF THE GIRONDISTS.


♦Submission of the country.♦

The departments accepted passively the results of the insurrection of
August 10. Men feared lest by offering opposition they might render
easier the advance of the allies. Lafayette, while he prepared to
defend the road to Paris, refused to recognise the validity of what had
been done. The Assembly declared him a traitor, his soldiers abandoned
him, and, in company with three other members of the late constituent
Assembly, he fled across the frontier, where all four were arrested and
imprisoned by the Austrians. The Assembly itself had lost all control
over the course of events. The men who had refused to take the right
step of deposing Louis had now to pay the penalty. That which might
have been effected without shock by the constituent or legislative
Assembly had been done by a violent explosion of popular wrath. The
Assembly had failed to take the lead, and after its flagrant subjection
to mob dictation, it was without moral energy or force. Yet a mob,
however powerful to destroy, is powerless to reconstruct. The one
organised force in Paris which could translate the feelings of the
populace into action was that of the sixty or seventy commissioners
who had dispersed the legal Municipal Council on the night before the
insurrection. A few days afterwards they raised their number by fresh
elections to 288. From henceforth this irregularly-elected body is
known to history as the Commune of Paris. With this new Commune supreme
power for the moment practically resided. It was strong because it
knew its own mind, and because it fully accepted the work of those of
its members who had swept away a king suspected of being in alliance
with a foreign enemy. Among the newly-chosen members was Robespierre,
the only one who had hitherto been of note. Other names, such as those
of Billaud-Varennes, Collot d’Herbois, Hébert and Chaumette now rose
first into prominence. Of the mass many were unprincipled adventurers,
others timid timeservers. ♦The insurrectionary Commune.♦ To a few the
holding of municipal office was merely a step in their career upwards.
The better men resigned office or kept out of sight, the more ruffianly
and unscrupulous came to the front. The ministers were thwarted and
disobeyed, the Assembly threatened, public property plundered, numbers
of arrests made, liberty of speech suppressed. Constitutionalists
for the most part kept away from the Assembly, and laws were passed
which before the insurrection had been rejected by large majorities.
Nonjurors were required to leave the country within fifteen days on
pain of ten years’ imprisonment; and unbeneficed ecclesiastics, on
whom the oath had never been imposed, were subjected to the same fate
whenever six citizens of their department joined in demanding their
exile. Emigrants’ property was confiscated and offered for sale.
Administrative bodies and municipalities were authorised to issue
warrants of arrest against persons suspected of political crime. This
law, which may be likened to a suspension of the Habeas Corpus Act in
England, destroyed at a blow the safeguards against arbitrary arrest
and imprisonment which the constituent Assembly had toiled to build up.

Yet, in spite of the terror that reigned, the position of the Commune
was insecure. In the departments it had no supporters. In Paris it
could only reckon on some hundreds of arms and votes. The artisans of
St. Antoine had taken part in the insurrection to destroy the throne,
not with the intention of placing power in the hands of the present
holders of office, most of whom were men entirely unknown to fame. The
Assembly resented their ascendancy, and there was no doubt that one of
the first acts of the Convention would be to attempt to establish its
own authority over the Commune.

♦The September massacres.♦

With the object of obtaining political supremacy an atrocious scheme
was devised, in the execution of which the advance of the enemy
assisted. The allies, marching from Coblentz, arrived before Longwy
on August 20. The place surrendered in four days. Verdun was next
besieged. Dumouriez, who commanded in Lafayette’s place, was at Sedan
with 20,000 men; Kellermann with another 20,000 at Metz. Unless these
forces should unite before Verdun surrendered, the way to Paris would
be open to the enemy. Strenuous exertions were being made by all
authorities to send men to the frontier, and Danton devoted to the
task unflagging vigour and energy. He dominated in the ministry over
his Girondist colleagues, and by his stirring appeals excited the
passion and enthusiasm of whatever audience he addressed. ‘The bells
that ring,’ he cried, as recruits hastened to the Champs de Mars,
‘are no signal of alarm. They sound the charge upon our country’s
enemies. To conquer them we need audacity, and again audacity, and
ever audacity, and France is saved.’ On his proposition the Assembly
decreed that commissioners should go from house to house and make an
inventory of arms, horses and carts. Of this decree the Commune took
advantage for its own purposes. For two days and nights the barriers
were closed, and many hundred persons arrested, principally nobles
and constitutionalists. Twenty-four hours later, while the church
bells were ringing and Danton exciting citizens to enlist, bands of
assassins, hired by the Commune, visited the prisons and massacred
their inmates. The work was carried out under the special direction
of a committee composed of the municipal officers at the head of the
police, to whom Marat and a few other persons, who, like himself,
were not members of the Commune, joined themselves. Besides political
prisoners, a number of ordinary criminals perished, including women
and boys, though in most cases the women were spared. At two of the
chief prisons, the Abbey and La Force, some show of judicial forms
was observed. At the Abbey a dozen individuals appointed themselves
judges with a president at their head. Each prisoner was called in turn
before them. He was asked one or two questions, and without further
discussion, either acquitted or ordered to be taken to the other
prison, La Force, a formula which meant death. As the condemned passed
through the prison gates, executioners stationed without rained blows
upon his back and head. The street became strewn with corpses and ran
with blood.

Similar scenes were enacted at La Force, where Hébert acted as
president of the tribunal. The massacres effected in eight prisons
went on continuously for five days and nights (September 2–7),
during which it is calculated that more than a thousand prisoners
were butchered. No action was taken to interfere with the murderers.
Ministers and deputies were afraid even to denounce the Commune in
vigorous language lest the weapons of the assassins should be turned
against themselves. They had no material force on which to rely.
Santerre, who commanded the national guard, obeyed the Commune. The
inhabitants of Paris remained perfectly passive, the violence of
party strife having destroyed enthusiasm for political ideals, and
the sense of common duty. In the midst of the butchery the news came
that Verdun had fallen, and the uncertainty of their own fate deadened
men’s sympathy for the fate of those charged justly or unjustly with
being in connivance with the enemy. So far as Paris was concerned the
contrivers of the massacres succeeded in their object. The elections
to the Convention were held while terror reigned over the city, and
twenty-four men, some of whom were partners in the crime, and none of
whom were prepared to denounce it, were returned for Paris. An attempt
was made to influence, by like means, the elections in the departments.
A circular, signed by Marat and his colleagues, was sent out inviting
the country to follow the example of the capital and to murder
traitors. This incitation to massacre, was, however, attended with
small success. In a few towns murders were committed at the instigation
of agents of the Commune; but generally the elections were conducted
without disturbance.

♦The Campaign of 1792.♦

When Verdun surrendered Dumouriez was still at Sedan, and Kellermann
at Metz. Between the allies and the plain of Champagne was only a
natural barrier, the forest of Argonnes, a range of wooded hills.
Fortunately for France the allies were dilatory in all their movements.
The campaign, instead of being commenced in the spring, had been
delayed till autumn, when the season was less favourable and France
better prepared to resist. The Duke of Brunswick was a cautious
commander, who had acquired his military reputation in the Seven Years’
War. With 80,000 men he did not believe it possible to maintain his
communications and occupy Paris in safety. His proposal, therefore, had
been to capture the fortresses on the Meuse, and to reserve operations
against the capital for the ensuing spring. But the King of Prussia,
who in person took part in the war, was eager to push on to Paris
and to release the royal family. After the fall of Verdun the Duke
assented, but advanced slowly and reluctantly. Meanwhile Dumouriez by
rapid marches got before him to the forest, and occupied the passes
leading through it. Driven from his positions as Brunswick advanced,
he rallied his men in the plain and made a stand near St. Menehould,
where he was joined by Kellermann. Recruits were incessantly pouring
in, so that the united French forces numbered 60,000 men. The allies
on their descent into the plain took up a position between the French
army and Paris. The weather was very wet, the roads nearly impassable,
and the invading army with difficulty supplied with bread. The placing
of garrisons in Longwy and Verdun, together with sickness, had reduced
the effective force under Brunswick’s command to 40,000 men, and he
could not push on to Paris leaving Dumouriez’ army unbeaten behind him.
The King was eager to fight, but Brunswick persuaded him, in place of
attempting to storm the French positions, merely to open a cannonade
on Kellermann’s forces, which were stationed in advance of Dumouriez’
men on some heights near the village of Valmy (September 20). This
cannonade was the turning point of the campaign. The young French
recruits stood fire so well that the allies determined on retreat. The
Austrian troops were afterwards called off for the defence of Belgium,
and thus Brunswick’s plan of holding the line of the Meuse was rendered
impracticable. Verdun and Longwy were evacuated, and the Prussians
retreated to Coblentz (October).

♦The Convention.♦

The Legislative Assembly gave place to the Convention on September
21, the day after the cannonade of Valmy. At once, the abolition of
monarchy was decreed, and the following day was henceforth accounted
as the first of the French Republic. The new Assembly consisted of
749 members, of whom 186 had belonged to the legislative, 77 to the
constituent Assembly, and 486 were new men. The constitutionalists,
through intimidation or want of public spirit, had kept away from the
poll, and among all the deputies were none who did not vote for the
abolition of monarchy with real or feigned enthusiasm. The Girondists
now sat on the right, forming the conservative side of the House.
Vergniaud, Brissot, Gensonné, and Guadet were all re-elected, and
around them gathered a knot of new comers, amongst whom were Buzot,
Pétion, Barbaroux, Louvet, and others who shared their views. The
deputation of Paris, together with about thirty deputies from the
departments, now formed the Mountain, sitting as in the last Assembly
on the topmost benches of the left. Here were Marat and other directors
of the massacres, several municipal officers, including Robespierre,
Billaud-Varennes, and Collot d’Herbois, the Duke of Orleans, who to
flatter the mob now called himself Philip Egalité, Desmoulins, and
Danton, who resigned the post of minister of justice in order to retain
his seat in the Assembly.

♦The Girondists and the Mountain.♦

From the opening of the Convention irreconcilable hostility was
declared between the Girondists and the Mountain. To secure the
independence of the Convention and supremacy for their own party, the
Girondists sought to bring to justice the contrivers of the massacres,
and to destroy the ascendancy of the Commune. They resented the stain
cast on the revolution, and were eager to prove to Europe that the
massacres were the work of a few hired assassins, and not, as the
deputies of Paris strove to represent, of the people of the capital
rising spontaneously to take vengeance on traitors. In appearance
their position was strong. Through their supporters, who occupied
the ministries, they directed the government and foreign relations.
They were enthusiastic, brilliant, eloquent; they had right on their
side, and both the country and the Convention shared their abhorrence
of the crimes committed. Yet the difficulties in their way were not
to be easily overcome. The Commune ruled the capital and had in
its pay bands of thieves and assassins, whose crimes bound them to
its support. The departments had taken no part in the insurrection
of August 10, yet had accepted without question the result, and the
predominance of Paris over them had thus acquired all the strength of
uncontested fact. Public spirit, moreover, no longer existed amongst
large masses of men. Primary assemblies were nearly deserted, and few
of the many thousands whose names were inscribed as national guards
rendered active service. Under such circumstances the task of crushing
the criminal band which, through the Commune and the sections, ruled
the city, was in any case difficult, and for the Girondists especially
impracticable. They were unversed in the conduct of affairs and were
strong party men, intensely credulous and suspicious in relation to all
that was outside their own circle. They stood on very narrow ground.
Republican fervour and hatred of Catholicism rendered them harsh and
intolerant towards whatever savoured of reaction. Abhorrence of crime
and pride in their own cause made them averse to compromise, and to
having dealings with men whose hands they believed to be soiled with
the blood of the September massacres. They had neither the traditions
of office nor the large capacity which creates a government by its
power of taking the lead in a distracted nation. Hence they did not
attempt to conciliate constitutionalists, nor yet to break the power
of the Commune by dividing its leaders, and bribing its followers with
money and office. As a party they did not inspire confidence. They were
without organisation or union, and being constantly divided in opinion
amongst themselves, they often voted on contrary sides. Their chief
orator, Vergniaud, possessed talent of a high order, and qualities
in which the party, as a body, was notably deficient--moderation
and foresight; but he was a man of retired habits and unassuming
disposition, who had neither taste nor inclination for the position of
a party leader. Hence the Girondists never brought forward any series
of well-concerted measures for gaining their objects, nor were they
ever able to obtain a working majority in the Convention. Impetuous
orators vaguely threatened to bring the Commune to justice, made
vehement attacks on the whole Paris deputation, and, singling out the
two most powerful men belonging to it, Robespierre and Danton, accused
them of aspiring, in conjunction with Marat, to form a triumvirate, and
Robespierre especially of aiming at a dictatorship. General charges of
this character could not be substantiated and were easily repelled.
Where, asked Robespierre, were the arms and the men by which he could
obtain a dictatorship, while he accused the Girondists of seeking to
sow disunion by calumniating Paris. It was no easy matter to fix even
on him the charge of being an author of the massacres. All members
of the Commune were, without doubt, immediately responsible for what
had taken place, but to allege mere inaction as proof of guilt was
hardly befitting to men who had formed part of the legislature at the
time Robespierre had been at the Hôtel de Ville, and had expressed
hostility towards the Girondists; but to this day it is a matter of
dispute how deeply he was implicated. Danton, though not a member of
the insurrectionary Commune, had been Minister of Justice. He, indeed,
had made no effort to stay the assassins’ hands, but there is no
proof whatever that it was he who gave the signal for the shedding of
blood, and officially he was no more responsible than Roland, who was
Minister of the Interior. It was, however, Danton whom the Girondists
regarded with most suspicion and distrust, whom they were readiest to
attack, and most eager to crush. To them he was vice personified. His
language was cynical; he affected to despise scruples of conscience
in action; crime could not revolt him; they believed him corrupt and
blood-stained, while he despised them as squeamish politicians, who
did not comprehend the conditions under which they worked, and who,
from being over-scrupulous in their choice of tools, let power slip
from their grasp. Nevertheless, he desired reconciliation with them.
He recognised the value of their disinterestedness and patriotism,
and was aware that the more narrow and criminal the base on which the
republic rested, the less would be its power of endurance, and the less
room would there be for himself to exert influence. Not easily moved by
petty considerations, and devoid of envy and resentment, Danton was the
one man on the left, as Vergniaud on the right, whose speeches bore no
trace of personal animosity.

♦Policy of the Centre.♦

The Centre of the Convention, often styled the Plain, consisted
mainly of new-comers from the departments, who abhorred Marat and his
doctrines, and resented the tyranny exercised by the Commune. But in
place of giving undisputed victory to the right, they followed the
safer course of a temporising policy between the two parties. They
feared to come into violent collision with the unscrupulous Commune,
and regarded the exaggerated charges brought against Robespierre and
Danton as what in fact they were--the fruits of violent party hate. It
was, indeed, no wonder that men who accepted the results of the last
insurrection should hesitate to send Danton to the scaffold, or should
doubt whether the revolution, having gone on thus far, could sustain
itself without him. The services that he had rendered in organising
the national defence were undoubted. There was no man so capable, with
his stentorian voice, his violent gesticulations, his abrupt vigorous
language, of rousing popular enthusiasm. The Girondists were no mob
orators, but Danton was at home alike in the Convention and in the
streets.

♦Re-election of the Commune.♦

The contest, incessantly renewed by the Girondists but never ending in
victory, resulted in strengthening the position of the Mountain. The
galleries of the House were ordinarily occupied by adherents of the
Jacobins, who applauded the deputies on the left and hooted those on
the right. Petitioners, often accompanied by armed mobs, invaded the
Convention, menacing insurrection unless their demands were complied
with. A project was brought forward by the Girondists for giving the
Convention a paid guard of 4,000 men, drawn in equal proportions
from the departments. But it never became law; and in case of a
breach with the Commune, the Convention had nothing to rely on except
recruits passing through Paris on their way to the frontier. A law was
finally carried for the re-election of the Commune. As, however, the
inhabitants of the city, through fear or indifference, did not attend
the sections, the result of the elections was merely to confirm the
existing party in power. Although since August 10 manhood suffrage had
prevailed, in many sections there were no more than 150 or 200 voters
present out of the many thousands who had the right to take part in
the elections. Chaumette and Hébert, as well as other members of the
revolutionary Commune, were re-elected. This new Commune was not fully
organised until July 1793. In the meantime its Council at the Hôtel de
Ville, often reduced to twenty members in place of its full complement
of ninety-six, ruled Paris under the guidance of Chaumette and Hébert.

♦Conquest of Savoy, Mainz, and Belgium.♦

The war increased the difficulties of the internal situation. Success
at first attended the French arms. During September French troops
occupied Nice and Savoy, part of the dominions of the King of
Sardinia, whose unconcealed hostility had given France a pretext for
a declaration of war. At the time when the Austrians and Prussians
invaded Lorraine, the French General Custine, with 18,000 men, marched
from Alsace against the smaller lay and ecclesiastical states on the
Rhine. Nowhere was serious opposition attempted. The petty rulers
proclaimed their neutrality, or fled to Coblentz. The important
fortress of Mainz surrendered. From this point it was open to Custine
to intercept the retreat of the Prussians from Lorraine; but, eager to
push his conquests further, he crossed the Rhine and took Frankfort,
whence he commanded the surrounding country (November). After the
retreat of the allied army through the Argonnes, Dumouriez hastened to
carry out the project of invading Belgium, where the fortresses were
out of repair, and little preparation for resistance had been made. A
battle was fought near the village of Jemmapes (November 6), in which
the Austrians were defeated. They retreated behind the Meuse, leaving
the French in undisputed possession of the country.

♦Foreign policy of the Convention.♦

The victory of Jemmapes, the first pitched battle fought, was greeted
with a burst of applause from one end of France to the other. When the
Legislative Assembly had declared war on Austria, it had represented
France as acting on a purely defensive policy, and had repudiated wars
of conquest as contrary to the right of each people to shape its own
destinies. Now that France was in possession of conquered territories,
the question of the manner in which they were to be dealt with
necessarily arose. The idea of making a merely diplomatic use of them,
and of restoring them in case of convenience to their former rulers
without regard to the wishes of the inhabitants, found no supporters.
The point at issue was whether the inhabitants were to be left really
free to select their own form of government, or whether France should
influence their decision.

Since the commencement of the war the Convention had become inflamed
with the desire of spreading the principles of the revolution far
beyond the frontiers of France. With the advance of French armies
it hoped that peoples would rise against their rulers, and that
not only the Continental countries in which the old aristocratic
institutions were in full play would willingly accept French aid for
the constitution of society and government upon a new basis, but
that even in constitutional England the people would insist upon the
establishment of the French system. Exultant in what they had already
achieved, French enthusiasts underestimated the strength of the forces
opposed to them, and overlooked the fact that a strong sense of
nationality was to be found in England; and that, under circumstances
favourable to its development, it might spring into activity even in
countries where it seemed most dead, as in Germany and in Italy. Under
the influence of such crude impulses the Convention gave wanton offence
to governments at peace with France by the issue of a proclamation,
proffering assistance to all peoples desirous of obtaining their
freedom (November 19).

[Illustration: BELGIUM

                                                          E. Weller.
]

♦Question of annexation of Belgium.♦

The wish to spread revolutionary principles operated strongly upon
the policy pursued by the Convention in relation to its conquests.
The annexation of conquered territories involved carrying out in them
the changes already effected in France. For smaller territories the
maintenance of political independence was in reality impracticable
amidst the clash of the great powers. Hence it came to pass that the
Convention rapidly gravitated towards a policy of forced annexation,
which they attempted to conceal by accepting the vote of their own
partisans as the expression of the popular will. Other motives also
existed. The ambition was roused of extending the French frontier
to the Alps and the Rhine. In case of annexations, the financial
difficulties of the government would be decreased. Church property in
the newly-acquired territory would become national property, and the
possession of new securities would raise the value of the assignats.
In Savoy and in Nice, as also in Liége and the small states near the
Rhine, much discontent prevailed, and no small part of the population
desired union with France. But in the Austrian Netherlands the case
was different. The clergy and feudal aristocracy possessed much
influence; the forms of constitutional government existed, and there
was a powerful party which sought to maintain political independence
of France while discarding connection with Austria. The Convention
accordingly decreed the union of Nice and Savoy with France, but
hesitated to annex the Austrian Netherlands. Its hesitation was not
due merely to the fact that only a minority of the population desired
union. Further consequences had to be taken into consideration. The
attempt to unite Belgium was certain to involve France in hostilities
with a fresh and formidable enemy. For centuries it had been a
cardinal point of English foreign policy that Belgium was to be in
possession of a power capable of resisting French aggression, and
the extension of the war was deprecated by all deputies who cared
for the restoration of internal order and settled government. A war
with England would seriously increase the expenses of government,
which were already only met by fresh issues of assignats, whilst the
rapid rise of prices which had ensued inflicted suffering on the
working-classes, and placed means at the command of the Commune of
exciting discontent against the Convention. An alternative plan of
creating an independent Belgian republic was desired by Dumouriez and
by some members of the Convention. Yet it was unlikely that this plan
would succeed in averting war with England. English statesmen were as
averse to the establishment of a Belgian republic as to the annexation
of the country to France. In fact, the Convention could only maintain
peace by abandoning the principles on which it was acting, and by
giving a pledge that Belgium should be restored to Austria. There was,
moreover, an immediate ground of quarrel. After the French armies
were in occupation of Belgium, the Convention had proclaimed the free
navigation of the Scheldt, which by an European arrangement, agreeable
to England and Holland, but ruinous to the trade of Antwerp, was closed
to commerce. This measure gave great offence to England as increasing
French influence, and was regarded in itself as sufficient ground for
a declaration of war. Though in accordance with the new principles
of the rights of nations not recognised by cabinets, but which were
no more than the principles of justice itself, the liberation of the
Scheldt was in the teeth of treaties to which both England and France
had been parties. The decree of November 19 (p. 131), which the French
government refused to withdraw, was regarded as a direct incitation to
subjects to revolt. The passing of a new decree (December 15), ordering
French generals to proclaim wherever they went the sovereignty of the
people, the suppression of the existing authorities, and the abolition
of feudal rights and privileges, was a second clear intimation to
Europe that France was intent on spreading revolutionary principles
beyond her own borders.

A portion of the Convention desired, at whatever hazard, to carry out
an immediate annexation of Belgium, and afterwards to invade Holland,
in accordance with a plan proposed by Dumouriez. Holland was at peace
with France, but there was no doubt whatever that in case of war
between England and France, the stadt-holder, who was maintained in
his seat by English and Prussian influence, would join the coalition.
The majority, however, led by the Girondists, hesitated to adopt
this course. Although their minds were inflated with the desire of
rousing revolutionary movements in other countries, including England
itself, they sought, from a sense of internal peril which every day
grew stronger, to circumscribe the field of war, and both to maintain
peace with England and to withdraw Prussia from the coalition. To
attain their ends the ministers were prepared to abandon the project
of invading Holland, to suffer the King and his family to quit France,
and to defer the final settlement of Belgium till the making of peace.
But neither the disposition of the King of Prussia nor of the English
people rendered it possible for any understanding to be arrived at on
these terms.

♦Austria and Prussia unwilling to make peace.♦

The allied princes had not entered into the war out of pure chivalry,
and did not intend to withdraw from it until they had obtained what
in diplomatic language they called an indemnity--in other words,
territorial acquisitions, either at the cost of France or of some
neutral state. Shortly before hostilities broke out Catherine II.
proposed to Frederick William a second partition of Poland. The King,
though bound by two treaties to maintain the integrity of Poland,
entered into the agreement. It was, therefore, to Poland that he looked
for his indemnity, and his assistance in the war against France was
the price he paid for the Emperor’s consent to his making acquisitions
in the east. Francis, on his side, looked for conquests in France,
and also had in his mind the revival of Joseph’s project of making
over Belgium to the Elector of Bavaria in exchange for that country.
A study of the map of Europe shows clearly what would have been the
advantage of the exchange to Austria in consolidating her dominions and
giving her increased predominance within the Empire.

♦England and the revolution.♦

While the personal feeling of Frederick William involved his subjects
in a war for which they had no enthusiasm, public opinion in England
compelled the Government to take a hostile attitude. William Pitt,
supported by the King, the country gentlemen, and the commercial middle
classes, had fought his way to power in 1783 in a sharp struggle in
which the Whig aristocracy was overthrown. As the head of the Tory
party he professed a toryism very different from the past toryism
of Harley and of St. John, which had battled against dissenters and
the mercantile class, and from the future toryism of Eldon, which
was to battle against improvement. In one sense he was the Turgot of
England. He was pre-eminently a peace minister, and he had taken the
lead, sometimes far in advance of the public opinion of his day, in
advocating projects of financial and economical reform. Those projects
he had viewed from the point of view of the highest statesmanship. He
had sought to bind England and Ireland together by a commercial union,
which he was unable to carry into effect. He had sought to bind England
and France together by a commercial treaty which had increased the
communications between the two countries. It was not his fault that
even a Parliament in which he counted so many supporters had rejected
a scheme of Parliamentary reform, which would have gone far to bind
class to class in England itself. Yet, even in his failures, his
efforts after good had made his government inapproachably strong. The
fallen Whig aristocracy, indeed, was very different from the effete
privileged orders of France. It counted amongst its members and its
followers high-spirited and large-minded politicians, such as Fox and
Burke. Its traditions were those of men brought up to combat for their
ideas in the open light of publicity, and to support their cause by
argument before their fellows. Yet there was something in it of the
faults which had made the continental nobilities unpopular. It was
narrow and exclusive, and was apt to regard office and emolument as
the special perquisite of its own members. Against such an aristocracy
Pitt stood as the champion of so much of equality as the conditions
of English society admitted of. Representing, as he did, the King and
the middle classes, he advocated a rational government, founded on
the best political science of the day. It was impossible that if war
broke out with France he should continue his work of internal reform.
Events happening in France were but superficially comprehended in
England. At first some of the Whigs, following Fox, extended sympathy
to a revolutionary movement which put forward as its object the
establishment of constitutional government. As soon as disorder and
violence showed themselves in France a large section of the Whigs,
including most of the great landowners, joined the Tories in viewing
the movement with distrust, though the latter had confidence in Pitt,
who sought to maintain friendship between the two governments. Neither
party had any clear perception of the fact that the revolution was
produced by social as well as political causes, and that its real aim
was to complete the destruction of the old feudal order long since in
slow process of decay. The special causes of discontent operating in
France were left unnoted. The comparative excellence of government in
England made Englishmen callous to the past misgovernment of France.
The fact was patent that the revolution declared war on established
institutions, and exhibited propagandist tendencies. Public opinion,
therefore, soon set strongly against it. Already, in 1790, Burke,
breaking loose from Fox, published his ‘Reflections on the French
Revolution,’ in which his eloquent declamations against men who were
destroying continuity between the past and the present, helped to
ripen the distrust that already existed in the minds of his countrymen
into fear and hatred. After the fall of the throne and the September
massacres, intense alarm prevailed lest the spread of democratic
principles should produce similar convulsions in England. In reality
there was no danger. The middle classes were not jealous of the upper;
the people were not starving. Societies established for the promotion
of French principles obtained but a few hundred supporters, a strong
proof of the unmoved disposition of the people at large. The panic,
however, if unfounded, was genuine. To secure themselves against danger
the governing classes desired to suppress the revolution by force
of arms, and loudly demanded the reclosing of the Scheldt and the
evacuation of Belgium as the price of peace.

While his supporters clamoured for war, Pitt still strove to avert a
breach. In the hope of effecting a European peace he made offers of
mediation at Berlin and Vienna. His offers were, however, but coldly
received, since both the Emperor and the King expected to gain from
the continuance of hostilities. War, therefore, became inevitable. The
French ministers went to the full length of their tether when, for
the sake of the neutrality of England, they left Holland untouched,
and offered to defer the settlement of Belgium till the making of
peace. To obtain more of the Convention was not in their power, nor
was it their wish. To satisfy the demands of England by reclosing
the Scheldt and re-establishing the old order of things in Belgium,
appeared to the mass of deputies, irrespective of party, as a base and
cowardly abandonment of principle. As the hostility of England grew
more manifest, the party in the Convention for immediate annexation
gained strength; and in the meantime an event happened which caused the
balance of power hitherto on the side of the Gironde to fall on the
side of the Mountain.

♦Trial and Death of the King.♦

Since the fall of the throne the King and his family had been kept
under harsh durance in the Temple, an old keep once belonging to the
Knights Templars. The Convention, after long and stormy debates,
decreed that Louis should be brought to trial before itself. The charge
that could justly be made against him was that, having undertaken to
govern in accordance with the constitution, he had sought foreign aid
to overthrow it. But for this he had been dethroned, and neither the
country nor the Convention had ground or right to take vengeance on
him for seeking to free himself from the untenable position which the
constituent Assembly had required him to accept. The deputies, however,
judged Louis’s conduct in the light of their own theories. They set
the nation in the place of the King, and then accused Louis of treason
because he had conspired against the will of the sovereign people. None
had any doubt of his guilt; few that its due penalty was death. Many,
however, even of those who thought his crime merited death, desired not
to shed his blood, but merely to give satisfaction to their pride as
republicans by passing sentence against him either of banishment or of
captivity till the end of the war. The ministers hoped by suspending
the sword over his head to put pressure on Prussia, and to induce
her to abandon her alliance with Austria, in return for the liberty
of the royal family. The Montagnards, or members of the Mountain,
however, sought Louis’s life. They were eager to defy the sovereigns
of Europe, and to give proof of their passion for equality by sending
Louis to the scaffold. ‘Let us,’ said Danton, ‘cast down before Europe,
as the gauntlet of battle, the head of a king.’ The Montagnards were
determined, moreover, to involve the majority of their fellow deputies
in an act that should unite them by an indissoluble bond to themselves.
The trial could be but a form; Louis’s guilt was a foregone conclusion.
The question what sentence should be passed upon him became the object
of a fierce party conflict. The Mountain set all the machinery at its
command in motion to intimidate the Convention. In the clubs and in the
sections a cry was raised for ‘the tyrant’s blood,’ and the ignorant
populace was taught to believe that the existing high prices were in
some occult manner connected with Louis’s existence as a captive. As
the trial dragged on, the Girondists became alarmed at the danger of
their own situation and the possibility of defeat; but not for the
sake of France, much less for the sake of Louis, were they prepared to
belie the past acts of their political life by declaring him innocent.
For, if Louis had not been in connivance with the enemy, where was the
justification for the insurrection of August 10? They, as well as he,
had sworn to maintain the constitution. Twice Louis was brought before
the Convention, once to hear his accusation read, a second time when
his counsel spoke in his defence. He did not dispute the authority of
the Convention, but denied the truth of the charges brought against
him. The Convention unanimously pronounced him guilty of treason
against the nation; 361 deputies voted for the penalty of death; 72
for death, but with a demand for delay of execution or for some other
restriction; 288 for imprisonment or banishment, thus leaving only
a majority of one for immediate death, though when a final vote was
taken two days later, on a fresh proposal to delay execution, the
majority for immediate death was swollen to 60 (January 17). Each
deputy voted aloud, and during the whole sitting, which lasted many
hours, the galleries and corridors of the house were occupied by armed
adherents of the Commune and the Jacobins.

Since his imprisonment Louis’s time had been spent in preparation for
death. Towards his enemies he entertained no feeling of resentment or
hatred, and received intelligence of the sentence passed against him
with calmness and resignation. On January 21, while the city maintained
a mournful silence, the King was guillotined on the great square, now
known as the Place de la Concorde, which since August 10 had borne the
name of the Place de la Révolution.

♦War with England.♦

The execution of the King hastened the rupture with England. Pitt sent
the French agent in London out of the country. The Convention adopted
a decree for effecting the union of Belgium with France, and without a
voice being raised in opposition declared war on England and Holland
(February 1). About this time Spain and Portugal, the Empire, and most
of the Italian states joined the coalition.

♦French driven from Belgium.♦

The French generals had owed their brilliant successes in part to the
speed of their movements, in part also to the defenceless state of the
countries invaded. During the winter Frankfort had been stormed by the
Prussians (December 2, 1792), and Custine had been driven back to the
Rhine. For the recovery of Belgium and the territory of the Empire on
the left bank of the river, Austria and Prussia brought together more
than 200,000 men, and these formed two armies. The northern, commanded
by an Austrian, Coburg, was to operate against Belgium; the southern,
commanded by the Duke of Brunswick, was to besiege Mainz, and to drive
Custine out of the Palatinate.

The French government authorised Dumouriez to invade Holland, though
the probabilities of success were now small. Coburg was advancing
towards the Meuse, and the Dutch were prepared to defend the passage of
their rivers. Dumouriez had only 100,000 men for purposes of defence
and invasion. He made a rapid march through the west of Flanders as far
as the arm of the sea which forms the mouth of the Meuse, where he was
checked by want of means of transport. Meanwhile one of his officers,
Miranda, guarded the line of the Meuse and besieged Maestricht. Coburg
advanced and relieved the town. The French troops, three-fourths of
whom were untrained volunteers, fled in disorder and deserted by
thousands. The pursuit, however, was not closely pressed, and Miranda,
rallying his scattered forces, took up a strong position near Louvain.

♦Revolutionary Court.♦

These disasters reacted on the situation in the capital. The hold
that the Girondists possessed on the Convention grew feebler every
day. They had failed in all they had attempted. Their foreign policy
had broken down, and the reproach fell heavily on the ministry of not
having suffered Dumouriez to invade Holland when the proposition was
first made. They had failed to save the King’s life, so that the whole
constitutional party outside the Assembly was as fully estranged from
them as from the Mountain. In spite of the fresh municipal elections
in Paris, which they had decreed in hope of changing the character
of the Commune (p. 128), it was the same criminal band that still
exercised authority. To provide for the war expenditure resort was had
to new issues of assignats. Prices incessantly rose, and discontent
spread rapidly amongst the working population, taught by agitators to
regard the right side of the Convention as the cause alike of the
prevailing destitution and of military disaster. The deputies of the
centre, in alarm for their own safety, and without confidence in the
Girondists as leaders, followed a vacillating course, accordingly as
they were actuated by their principles, their fears, or their regard
for the necessities of the situation. When Miranda’s retreat was known
an attempt was made to get up an insurrection directed against the
Girondists. It failed, from want of union and support. But the bands
at the service of the Jacobins and the Commune gathered round the
Convention, filling the galleries and menacing deputies. The Mountain
made use of the occasion to obtain the adoption of a law for the
creation of an extraordinary criminal court, to judge without appeal
conspirators against the state (March 9). The Girondists opposed the
measure, but in vain; and thus were Robespierre and Marat provided with
a ready weapon with which to strike at the heads of those who had so
long menaced their own.

♦Treason of Dumouriez.♦

Affairs in Belgium assumed a yet more alarming aspect. Dumouriez,
hastening back from Holland, rejoined Miranda near Louvain. He returned
resolved to break with the Convention. He had no enthusiasm for
democratic or republican ideals, and was excessively irritated because
the Convention had not pursued the policy advocated by himself, of
creating Belgium into a separate republic. He resolved to make a stand
and to fight the Austrians, expecting after victory to be able to
dictate his own terms to the Convention and to mediate between France
and the allies. But a long contested battle, which raged fiercely
round the village of Neerwinden, ended in the defeat and flight of the
French (March 18). Dumouriez, with a remnant of his army, effected a
retreat to the frontier, where he sought to make good his position by
opening negotiations with Coburg. He offered to march to Paris and
place the Dauphin on the throne if Coburg would undertake to give him
moral and, in case of need, material support. As a pledge of good faith
he was prepared to admit Austrian troops into Lille and Valenciennes,
on condition that the towns were restored to France on the making of
peace. It had long been suspected at Paris that Dumouriez was not to be
trusted; but neither Girondists nor Montagnards had dared to propose
his dismissal, because they had no general of talent to take his place.
After the battle of Neerwinden he made no concealment of his hostile
intentions; and on the arrival of four deputies sent by the Convention
to summon him to Paris, gave them up to Coburg as hostages for the
safety of the royal family. In the meantime every effort was made
by the agents of the government to secure the fidelity of the army,
and with success. The soldiers refused to betray France to Austria,
and Dumouriez, to save himself from arrest, took refuge in Coburg’s
quarters (April 3).

♦Party strife at Paris.♦

Dumouriez’ treachery increased the violence of the party struggle at
Paris, where Girondists and Montagnards strove to cast on each other
the odium of being the traitor’s accomplices. It was against Danton
that the Girondists directed their most vehement attacks. They made
charges in support of which they had no evidence to bring, and which
have never been proved. According to them Danton had been bribed by
Louis; he had misapplied public money; in Belgium he had plundered
state property. They even accused him of plotting with Dumouriez the
restoration of the throne, because he had praised that general’s
talent in the Convention. Danton turned fiercely on his assailants,
threatening irreconcilable war. Counter accusations and menaces
were hurled from right to left, from left to right. Robespierre
came forward to represent the entire public life of the Girondists
as forming a long series of crimes directed against liberty and the
republic, and concluded with a formal proposal to send Brissot,
Vergniaud, Gensonné and Guadet, along with Marie Antoinette and the
Duke of Orleans, as Dumouriez’ accomplices, before the new criminal
court (April 9).

♦Committee of Public Safety.♦

Though the ascendancy which the Girondists once held was lost, their
eloquence was still a power, and the first deputy who was sent before
the court was a Montagnard, Marat, on the charge of inciting the people
to insurrection (April 14). But this isolated party victory served only
to irritate without weakening their adversaries. The court, composed
of judges and jurymen, both elected in Paris, acquitted the accused,
and his partisans restored him in triumph to his seat. The direction
of the government, possessed by the Girondists at the opening of the
convention, passed into other hands. The ministry had been broken
up. Roland had resigned, complaining that he had not the support of
the Convention. The Mountain and the Gironde struggled to obtain
appointments for their own candidates, and the ministers, fearful of
having their acts misinterpreted, refused to take a step on their
own responsibility. Hence the wheels of government, when expedition
and secrecy were most requisite, threatened to come to a standstill.
Under the influence of the alarm excited by the treason of Dumouriez,
the Convention established a Committee of Public Safety, composed of
nine members, but subsequently enlarged to twelve, who were subject to
re-election every month, and were empowered to deliberate in secret,
to superintend the action of the ministry, and to take provisionally
whatever measures were requisite for the national defence (April 6).
The deputies entrusted with these large powers were Danton and eight
others belonging to the Mountain and the Plain. From this time the
ministers sank into the position of chief clerks of their respective
departments, while the Committee of Public Safety stood at the head of
the executive government.

♦Committee of General Security.♦

A second committee, which had been created earlier, acquired special
importance about the same time. This was a Committee of General
Security, which had under its superintendence the measures taken for
the detection of political crime. Originally the Girondists possessed
a majority in it, but shortly after the King’s death it had been
reorganised, and was now composed of twelve Montagnards.

♦Deputies in mission.♦

The immediate object of the Convention in instituting the Committee of
Public Safety was to have an executive sufficiently strong to bring
large armies rapidly into the field. About 200,000 men were now under
arms. For the ensuing campaign it was determined to raise the number
to 500,000; 300,000 had, therefore, to be found in the course of a
few weeks. All national guards between the ages of eighteen and forty
were put in requisition. Every department had to furnish a definite
contingent; if the voluntary system failed to make up the required
number, conscription was resorted to. In most departments the call
for soldiers was responded to with enthusiasm, but in a few zeal was
wanting, and there was great difficulty everywhere in obtaining money
and arms. In order to bring local authorities under the immediate
control of the Government, the Convention took direct part in the
administration, and sent deputies into every department, authorised
to take all measures necessary for hastening the levy of recruits and
for providing supplies for the armies. These men established special
committees to act as their agents, compelled the sale of corn, horses,
and arms, and dismissed administrative officers whose attachment
to the republic was held in question. When they had completed their
work they returned to Paris, but the Convention continued to pursue
the system of sending its members into the departments, invested with
arbitrary and absolute power for carrying out the work entrusted to
them. Deputies were always present with the armies, to superintend
commissariat arrangements and to keep a watchful eye on the conduct of
general officers. They were responsible only to the Convention and to
the Committee of Public Safety, under whose immediate direction they
acted. Agents of the central government were thus established by the
side of the independent local authorities, and the way was prepared for
the complete submission of the country to whichever party triumphed
at Paris. For the first time since the fall of the old system of the
monarchy there was a Government in France.

♦Laws against emigrants and nonjurors.♦

As the situation grew more perilous, legislation assumed an
increasingly harsh and tyrannical character. In March, at the very time
when the retreat of Dumouriez from Belgium offered an opportunity to
the allies of attempting a march on Paris, a dangerous insurrection,
excited by the forced recruitment, broke out amongst the peasants
of La Vendée. The Convention, enraged against its adversaries, and
frightened at the unexpected danger, struck at random, regardless of
the fact that it was crushing the innocent along with the guilty. Those
who instigated resistance to the recruitment of the army were punished
by death. Priests, subject to banishment, who had remained in the
country, were to be transported to French Guiana. Banished priests who
returned were to be executed within twenty-four hours. The Legislative
Assembly had made it a crime to quit the country, and had confiscated
the property of the emigrants. The Convention laid a firmer grip on
their property by banishing them for ever from the republic, and by
forbidding them to return under penalty of death. Although many of the
exiles had had no intention of fighting against their country, but had
merely quitted France because their lives were in danger, no exceptions
were made, and no account taken of sex or circumstance.

♦Policy of the Mountain.♦

In the midst of internal strife and preparation for defence the
Convention was engaged on the task of framing a new constitution. When
abstract questions were under discussion but little difference of
view arose. In fact, the contention between the two parties did not
concern principles, but their immediate application. The Girondists
were prepared, without heed of circumstances, to carry into action
principles of decentralisation, popular election, and free trade, and
contended that the republic must rest upon the political virtue and
public spirit of the mass of the population. The Montagnards regarded
facts only. They recognised that active support to the republic was to
be looked for from the mob alone; that attempts to enforce principles
of free trade against the will of their own supporters must lead to
the overthrow of the Convention; that under the circumstances popular
election was a farce, and that amid the strife of parties and factions
decentralisation meant, as the experience of the past two years had
shown, that France would be without an effective Government at a time
when a powerful coalition was formed against her. A far lower motive
impelled them in the same direction. The safety of their country
appeared to them dependent on the triumph of their own party, and to
secure this they were prepared to act in the teeth of their theoretical
opinions. They denied liberty to the press. They sacrificed freedom
of trade to the clamours of the populace. They not only maintained
the right of Paris to act for the whole of France, but, in order the
more effectually to secure submission, sought by the agency of clubs
and special committees to stamp out all vestiges of public spirit that
yet remained in the departments, and were indifferent to the character
of their instruments, or to the commission of acts of injustice and
cruelty, so long as their own ascendancy was secured.

♦Economical situation.♦

The Girondists denounced the policy of their adversaries with eloquence
and fervent indignation. But the issue of the struggle was dependent,
not on their power of speech, but on the support which they could
obtain in Paris. Affection for the Convention was nowhere to be found.
The middle classes were alienated by the death of the King, the lower
classes by the dearness of food, while large numbers were estranged
by the indifference manifested by the Convention towards the Catholic
faith. The actual hostility of the working classes was excited in
consequence of the strenuous opposition made by the Girondists to the
economic theories which found favour in the streets. In July 1792, the
nominal value of assignats in circulation was about 87,500,000_l._
In May 1793, it had risen, owing to the war expenditure, to about
131,250,000_l._ The Church lands, the security on which the assignats
were first issued, were already sold. A new security had been found in
the property of emigrants, which was now in course of sale. This was
conveniently estimated to be worth the exact amount of the assignats
in circulation, 131,250,000_l._ The Government, however, remained no
better off. It had no credit on which to borrow, and taxes were only
partially paid. All foresaw that, to cover the war expenses, it would
be necessary to have recourse to new issues of assignats, and hence in
spite of the large security offered the paper money fell rapidly in
value. In March 1793, assignats could be exchanged for silver at about
half their nominal value. To supply the deficiency of small change the
Legislative Assembly had created notes for very small sums. Hence the
depreciation of the paper money inflicted great suffering on men living
on wages, who had nothing but these small notes on their hands. Since
the autumn of 1791 prices had been rising rapidly all over France,
while special causes contributed to produce dearness and scarcity of
food in Paris. In proportion as assignats were multiplied all persons
disliked to hold them. While purchasers were eager to pay with them,
sellers pressed for coin in exchange for their wares. The consequence
was that trade deserted Paris, where paper money was most abundant,
and where it was more difficult to get payment in gold and silver
than in the country. Corn-growers kept their corn in store or sent it
elsewhere. Few cattle came to market. Bread, meat, fish, wine, wood--in
short, all articles rose in price, some trebling in cost in the course
of six months. In the spring of 1793 the drawing off of men to the
frontier caused a rapid rise in wages, which before had not advanced
in proportion to prices. Nevertheless, real want existed amongst the
lower classes, and a not unfounded fear of want even amongst the upper
classes. Those who had money laid in stores, thus increasing the
scarcity; while wholesale dealers held back supplies, either because
they were unwilling to take paper money, or calculated on an increased
rise in prices.

Under this condition of things, while there were many sufferers, some
made large gains, more especially capitalists, speculators, wholesale
dealers, and contractors engaged in large transactions with the
Government and foreign countries. The depreciation of the paper money
benefited also to a certain extent the taxpayer and the purchaser of
State lands. But in proportion as individuals gained the State lost,
for while its revenue was received in assignats at their nominal
value, when it made purchases it was compelled to find hard cash or
else to pay in assignats at their depreciated value.

How to raise the value of the paper money and to lower prices was the
question that pressed hardest on the Convention during the spring
of 1793. The people, accustomed under the monarchy to arbitrary
interference with trade, were now raising all through France a
clamorous cry for compelling farmers to bring corn to market, and for
fixing the prices of articles of ordinary use and consumption. In the
capital a draconian code was proposed as the best means of keeping
assignats at par and ensuring plenty. Persons who exchanged assignats
for money, who speculated on variations in price, who held back goods
from sale, were to suffer the penalty of death. A special tax was to be
imposed for the maintenance of the war, a special rate for supplying
Paris with cheap bread. Petition followed petition, from the sections,
the clubs, and the Commune, calling on the Convention, under the threat
of insurrection, to legislate to such effect.

♦Popular remedies opposed by Girondists.♦

These demands were in direct contradiction to the free trade principles
maintained by a large majority of deputies. Laws for the suppression of
speculation and for the regulation of the corn trade were held by the
Girondists as an unjustifiable interference with individual liberty,
and as calculated to produce the contrary effect to that which their
proposers intended. ‘Do you wish,’ said Vergniaud, ‘to decree famine?’
They ascribed the scarcity of corn solely to fear of pillage, and had
the temerity to denounce the system of supplying Paris with cheap bread
as demoralising the inhabitants of the city and as unjust to those of
the country, who received lower wages but had to pay the market price
of the commodity. To the demand for a maximum price and the punishment
of forestallers and speculators, there was added soon the demand for
sending the Girondists before the revolutionary court, as standing in
the way of the popular remedies becoming law. The Montagnards supported
a coercive policy. The large issue of assignats and the consequent
breakdown of ordinary commercial relations appeared to some to justify
exceptional legislation. But the preponderating motive, leading the
Mountain, as a body, to support propositions for maximum laws, was
the dread of an insurrection directed against the entire Convention,
and the desire of maintaining against the Commune the leadership of
the populace. Several members of the centre, under the influence of
fear, and regarding as impracticable the policy of the right, seceded
to the Mountain. The Girondists had eloquence and courage, but no
practical programme able to rally supporters round them. They had no
means of protecting the Convention, yet it was impossible to abandon
the existing system of supplying cheap bread to Paris without having
to face an immediate insurrection. They were unable to set a limit to
the issue of assignats, yet it was evident that if the notes went on
falling in value, there must before long be famine prices in Paris.
Most deputies of the centre, though they still held the same opinions
as the Girondists, dared not emulate their courage. The exchange of
assignats for silver at less than their nominal value was prohibited,
under penalty of six years’ imprisonment (April 11). Restrictions
upon the corn trade, which had been in force under the monarchy, were
revived, and a variable maximum for corn was fixed, to be regulated in
each department by the local authorities (May 3). To provide for the
war expenses, a forced loan was to be raised of more than forty-three
millions (May 20). These concessions, however, failed to satisfy the
populace, while on the point which the leaders of the agitation had
most in view, the expulsion of the Girondists, the Convention stood
firm, and refused to proscribe its members. Plotting went on openly.
The Convention had lately instituted special committees to put in
force police laws regarding foreigners residing in France (March
21). There was one in every section of Paris, and ultimately in
most municipalities in the country. These committees, which usurped
the functions of the ordinary or civil committees of the sections,
became agents for the execution of the police laws generally, and
soon acquired celebrity under the name of revolutionary committees.
Nobles and ecclesiastics were excluded from sitting on them, and they
were most often composed of ruffianly and dissolute adventurers.
One insurrectionary committee was now formed at Paris of delegates
from these revolutionary committees; a second of delegates from the
sections. The Commune, under the leadership of its mayor, Pache, and
its two law officers, Hébert and Chaumette, set itself at the head of
the movement. Some Montagnards, including Robespierre, Marat, Collot
d’Herbois, Chabot, Tallien, and Desmoulins gave it undisguised support.
But those whose hostility was less, hesitated. For if the Mountain had
to call in the aid of the Commune in order to obtain victory over the
Girondists, what security was there that after their expulsion it would
be able to maintain its own independence? And what influence could
Danton hope to exercise over a brow-beaten and intimidated body of men,
in fear for their lives? Compromise with the Girondists was, however,
impracticable, and the Committee of Public Safety, in place of taking
active measures against the conspirators, sought merely to moderate
their violence.

♦June 23.♦

While their enemies plotted the Girondists made no efforts to secure
the Convention against attack, or to form a party in Paris for its
defence. They relied on their eloquence and the goodness of their cause
to keep the centre true to them. They made the useless proposition that
the primary assemblies should meet and decide which deputies should
be ejected, and which keep their seats. They obtained addresses from
the departments promising armed intervention in their support, and in
case of insurrection threatened Paris with annihilation. ‘If ever,’
said the unrestrainable Isnard, when President of the Convention, to
a deputation from the Commune, ‘it should happen that violence were
offered to the national representatives, I declare to you, in the name
of the whole of France, that Paris would be destroyed, and grass would
grow on the banks of the Seine.’ Such words were far more hurtful to
the Girondists themselves than to those whom they threatened. They
sounded in men’s ears like an echo of Brunswick’s proclamation, and
made the inhabitants of Paris fear more the consequences of the success
of the Girondists, in case of a collision between the two parties, than
those of submission to the one which posed itself as the defender of
Paris from violence. Meanwhile the enemies of the Girondists lost no
opportunity of turning opinion against them. They accused them, not
only of seeking to excite civil war, but also of being Federalists,
and of plotting to destroy the unity of the republic by making the
departments independent of the capital. Marat and his murderous
followers were ready to execute a second massacre, whilst amongst the
people propositions were heard for a redistribution of property. Such
ideas were not countenanced either by the Jacobins or the Commune.
Bloodshed might lead the departments to rise, and it was possible
that the middle classes in Paris might move for the defence of the
Girondists if they thought the city was to be given over to assassins
and assailants of the rights of property. Meanwhile the Convention,
encouraged by some movements in the sections against the tyranny of
the Commune, assumed a bolder attitude, and appointed a commission of
twelve deputies to investigate the conspiracies (May 18). Hébert and
other agitators were arrested. But these acts of vigour hastened the
crisis. To quiet the apprehensions of the middle classes the Commune
and the Jacobins made public declaration of their respect for property
and of their intention to maintain order.

The Convention a few days previously had removed from the Riding School
to a spacious hall in the Palace of the Tuileries, capable of holding
more than a thousand persons. On May 31 armed bands streamed through
the streets to impose their will on the representatives of the nation.
The terrorised Convention decreed the suppression of the Commission of
Twelve, but refused to proscribe its members. It was not allowed to
escape without bending its neck yet more beneath the yoke. On June 2
many thousand insurgents flooded the Chamber, demanding, with threats,
the arrest of the leaders of the right. The alarmed and indignant
deputies, with the exception of some thirty on the left rose in a body
and left the hall. But all issues out of the palace courts and garden
were closely guarded, and passage refused with insult. They returned,
and while intruders sat on the benches and voted with them, a decree
was carried that thirty-one deputies, including Vergniaud, Gensonné,
Guadet, Brissot, and other leading Girondists, should be kept under
arrest at their own houses.




CHAPTER VII

THE COMMUNE AND THE TERROR.


The fall of the Girondists was the necessary result of their
unfitness to govern France in the midst of war and revolution.
The constitutionalists had been overthrown, because they refused
to recognise that Louis desired the triumph of the invaders. The
Girondists were overthrown because they refused to recognise the
insurrection of August 10 under its real aspect. After that event
it was inevitable that France should for a time be governed by the
minority which, aided by the populace, had swept away the throne
of the weak and incapable King. Not only had the people of France
no attachment to a republican form of government, and therefore no
readiness to move forward actively in support of the Girondists against
the Mountain; but also the great majority of the population, through
dread of reaction in favour of the privileged classes, had no will or
policy of their own. The Girondists had been incapable of evolving a
policy which could rouse enthusiasm in their cause or give confidence
in their guidance. Their ideal republic was fitted for some ideal
nation, not for the French people, torn by factions and involved in war
with half Europe. Yet it was all they had to offer to France, and hence
it happened that when the Commune of Paris rose against them, not an
arm had been raised in their behalf.

If, however, the Girondists had failed in solving the problem of giving
France a government, their ejection from the Convention was none the
less a catastrophe, fraught with most evil consequences. They had put
themselves forward as representatives not merely of the departments
against Paris, but also of principles of individual liberty, of
justice, and of humanity. The Montagnards used the same words, but
meant by them very different things. By the sovereignty of the people
they meant the domination of their own party; by justice and humanity
the sacrifice of the opponents of their own ideas. ‘Others have
sought,’ Vergniaud had said in one of his finest speeches, ‘to complete
the revolution by aid of terror; I would have wished to complete it by
aid of love.’

♦Submission of the Departments.♦

Though in the departments there was no popular movement in favour of
the Girondists, yet they had more supporters there than in the capital.
In Paris all authorities, with the exception of the Convention, were
on the side of the conspirators. In the departments the administrative
bodies, which had all been re-elected since the autumn, resembled
closely in constitution the Convention itself. As a rule, in these
bodies supporters of the Girondists were in a majority, supporters
of the Mountain in a minority. In more than sixty departments
administrative bodies contested the authority of the Convention, and
threatened to resort to arms in favour of the expelled deputies. The
chief centres of resistance were, in the north-west, Rennes and Caen;
in the south-west, Bordeaux. The danger of a general insurrection
seemed greater, owing to the fact that royalists at the same time
were raising the standard of revolt. In the important industrial town
of Lyons they gained the entire direction of affairs. The leaders
of the Jacobins were put to death, and active preparations were
taken to resist by force the authority of the Convention. At Toulon
like dispositions were manifested and the same course was pursued.
In the departments of Ardéche and Lozère royalist conspirators had
already been in arms before the expulsion of the Girondists; while
in La Vendée and Deux Sèvres the peasants since March were in open
rebellion. The task, however, of quelling resistance under these
circumstances was, in reality, less formidable than at first sight
appeared. There could be no alliance between royalist and Girondist
insurgents, and the mere fact that royalists were in arms increased
the reluctance of the population to dispute the authority of the
mutilated Convention. Hence the opposition raised by the supporters
of the Girondists was vacillating and weak. The administrative bodies
could not rely on any class for hearty support. Even amongst the
proscribed deputies themselves union was wanting. While some fled to
Normandy, others remained in Paris, prepared to suffer whatever fate
awaited them rather than bring upon themselves the guilt of exciting
civil war. On the other side, the party victorious in Paris was for
the time thoroughly united, and acted with caution and decision. The
Committee of Public Safety, under Danton’s guidance, sought to pursue
a policy of conciliation, and the supporters of the Commune, aware of
the insecurity of their position, held themselves under restraint.
The charge of socialism and tyranny made by the Girondists was
repudiated by the adoption of a new constitution, based upon individual
liberty and democratic principles. There was indeed not the smallest
intention of putting this constitution in force, but its promulgation
held out promise to the country of a speedy return to normal modes
of government. The phrase ‘The Republic, one and indivisible,’ was
adopted by the Montagnards to signify the national cause, while they
accused the Girondists of seeking to destroy the possibility of defence
against the foreigner by the establishment of a loosely organised
federal state, and even of being in alliance with the enemy, and of
seeking to betray France to England. In the course of a few weeks the
administrative authorities abandoned the attitude of even passive
resistance against the Convention. A few hundred men advancing from
Caen to Paris were defeated at Vernon on the Seine. Bordeaux, starved
out, surrendered at discretion, and thus before the end of August there
were none but royalists who continued to contest the authority of the
Convention.

♦War in La Vendée.♦

The danger of the situation, nevertheless, remained great. The
royalists, both in Lyons and Toulon, held out, and the rebellion in
La Vendée became more formidable every day. In this department the
destructive tendencies dominant in other parts of France were tempered
by strong conservative instincts. No violent feeling of antagonism
existed between nobles and peasants. The nobles lived at home and came
into personal contact with the tenant-farmers. The country was wholly
agricultural; there were few towns and no industries. The peasants,
excessively credulous and superstitious, were easily led by their
priests, and were ready to hazard the loss of whatever advantages the
revolution brought them for the sake of keeping their faith intact.
The attempt to deprive them of the priests to whom they were attached
first rendered them hostile to the revolution. The attempt to carry
out the forced levy of soldiers decreed in March was the immediate
cause of insurrection. For the republic they had no sympathy, and
refused to leave their homes to fight in its defence. A general rising
took place, extending over the whole of La Vendée and part of Deux
Sèvres. The Government, compelled to send every available soldier to
the frontier, was quite unable to cope with the insurgents. Raw and
undisciplined levies, hastily brought together in the neighbouring
departments, were no match for them. The character of the country
was that of an almost impregnable fortress. The interior, called the
Bocage, was hilly, thickly wooded, and intersected by small streams
flowing at the bottom of steep ravines. The villages lay far apart.
Roads and lanes, often impassable for wheels, ran a tortuous course up
and down-hill, between high hedges and forests of furze and broom. On
the sea-coast the country, though flat, was readily defended, being
marshy and cut up by wide ditches. A large portion of the population
were poachers and smugglers, who were skilled marksmen, and the very
men to carry on the guerilla warfare which now arose in every part of
a country so inaccessible to the regular soldier. Defeat told heavily
on the republicans, who lost stores and ammunition, missed their way in
flight, and were cut down one by one by the peasantry. The Vendeans, on
the other hand, if the enemy withstood their first onset, disappeared
by tracks known only to themselves, and returned to their farms and
ploughs, prepared to resume the contest on a more favourable occasion.

In the conduct of a war of this description there was naturally
little method. The insurgent bands sought out the nobles and put them
at their head. The stream of the Sèvre Nantaise divided the country
into two parts, and the leaders on the two sides of the river rarely
attempted concerted action. In the lower district Charette, a noble,
exercised the chief authority. In the upper, two nobles, De Lescure and
Bonchamps, and two peasants, Stofflet and Cathelineau, commanded.

Repeated successes were won by the Vendeans, who fought with all the
ardour inspired by religious enthusiasm, and were ready to follow
their leaders to the death. Priests, always present with the armies,
stimulated their courage, promising to those who fell immediate
entrance into Paradise. One after another the towns lying on the edge
of the disturbed country fell into the insurgents’ possession. In
June Saumur was captured, giving them the passage of a bridge across
the Loire. Cathelineau crossed to the right bank, entered Angers, and
marched against Nantes; while Charette, in Lower Vendée, agreed to
open an attack on the same place from the south. But the peasants,
whose custom it was to disperse after a few days’ service, had neither
inclination nor heart for an expedition directed against a distant
town. Many of those who followed Cathelineau deserted on the way.
Nantes was bravely defended, and the assault repelled (June 29).
Cathelineau received a mortal wound. Charette, south of the Loire,
failed to get possession of the bridge across the river, and the
Vendeans on the north bank dispersed, returning by boats to their own
country.

♦Objects pursued by the Allies.♦

While the Vendeans triumphed in the west, in the east the allies were
victorious. The armies of Coburg and Brunswick mustered 250,000 men.
After the re-conquest of Belgium, Coburg laid siege to the French
fortresses of Condé and Valenciennes. These surrendered in July. About
the same time Mainz was retaken by Brunswick, and had the two generals
advanced, the one from the Scheldt, the other from the Rhine, there was
every probability of their making themselves masters of the capital,
and with the capital, of France. The opportunity, however, was let
slip. The powers had their own separate objects in view, and cared more
for attaining them than for suppressing the revolution.

England designed to extend her maritime dominion and her trade by the
conquest of French colonies and the destruction of the French marine.
A body of English and Hanoverian troops was sent under the Duke of
York to help the Austrians to capture French border fortresses,
and especially to gain possession of the port of Dunkirk, where
the existence of a French naval station had always been an object
of jealousy to English statesmen. The alliance between Austria and
Prussia was fast breaking down. Austria had given her consent to the
acquisition of Polish provinces by Prussia. Prussia, on her side, had
undertaken to support the Austrian plan of exchanging Belgium for
Bavaria. Neither power, however, acted openly or honourably towards the
other. Prussia secretly encouraged opposition to the plan of exchange.
Austria urged Russia to cut Prussia’s share of Poland down to the
smallest possible portion, and to delay her entering into possession of
it. This state of tension was increased when the second partition of
Poland was actually carried out in March and April. In consequence a
change of ministry took place at Vienna. The supporters of the Prussian
alliance were dismissed from office, and Baron Thugut was entrusted
by the Emperor with the sole direction of foreign affairs. It was the
aim of Thugut’s ambition to give to Austria a dominant position on
the continent. The Prussian alliance he regarded in the light of an
impediment to the accomplishment of his schemes, since Prussia was
Austria’s rival in Germany and jealous of Austrian aggrandisement. For
the time he let drop the idea of exchanging Belgium for Bavaria. That
plan could not be carried out without the co-operation of Prussia, and
the chances of Prussia’s co-operation decreased in proportion as she
laid firmer hold on her new acquisitions in Poland. England, moreover,
was unwilling to see Belgium passing out of the Emperor’s possession,
and Thugut was eager to secure the friendship of England, in order
the more effectually to keep Prussia in check. He held it, therefore,
the surer policy to leave the plan in abeyance, and meanwhile to make
conquest of French territory, more especially of Alsace and Lorraine,
which provinces at the making of peace might be disposed of as appeared
most consonant to Austrian interests. The idea of attempting to reach
Paris was, accordingly, not entertained with favour by any of the
powers. England and Austria both wished to operate on the French
frontier, while Prussia did not care to engage deeply in hostilities in
the west while affairs in Poland remained unsettled. It was, besides,
the belief both of generals and diplomatists, that the strife of
factions within France must result in the collapse of all government,
and that in the following year a march to Paris could be effected
without difficulty.

♦Murder of Marat.♦

But while the allies besieged fortresses in Flanders, and operations
lagged on the Rhine, immense exertions were being made within France to
increase the size of the armies, and an iron despotism was established
which placed all the resources of the country at the disposition
of the Government. As the departments one after another submitted,
deputies from the Convention were sent into them to bring them the
more completely under the control of the party which had secured
ascendancy in Paris by the insurrection of June 2 (p. 155). Men who
had espoused the cause of the proscribed deputies were excluded from
office, and were expelled from the clubs, which from this time were
only frequented by ardent supporters of the Mountain. The body of the
population watched the establishment of a ruthless tyranny in their
midst without attempting resistance. The will and the union requisite
for action were both lacking, and the few who dared either by act or
word to venture opposition to the emissaries of the Mountain or of the
Commune of Paris, paid the penalty by loss of liberty if not of life.
Amongst those who had placed faith in the Girondists and their ideals
was a young woman of Normandy, Charlotte Corday. Like them, she had
dreamed of the establishment of a republic founded on the political
virtue and intelligence of the people; and when the mob of Paris rose
and drove with insult from the Convention those who in her eyes were
the heroic defenders of the universal principles of truth and justice,
she bitterly resented the wrong that had been done not only to the men
themselves, but to that France of which she regarded them as the true
representatives. Owing to Marat’s persistent cry for a dictatorship and
for shedding of blood, it was he who, in the departments, was accounted
especially responsible both for the expulsion of the Girondists and
for the tyranny which now began to weigh as heavily upon the whole
country as it had long weighed upon the capital. Incapable as all then
were of comprehending the causes which had brought about the fall of
the Girondists, Charlotte Corday imagined that by putting an end to
this man’s life, she could also put an end to the system of government
which he advocated. Informing her friends that she wished to visit
England, she left Caen and travelled in the diligence to Paris. On
her arrival she purchased a knife, and afterwards obtained entrance
into Marat’s house on the pretext that she brought news which she
desired to communicate to him. She knew that he would be eager to
obtain intelligence of the movements of the Girondist deputies still
in Normandy. Marat was ill at the time, and in a bath when Charlotte
Corday was admitted. She gave him the names of the deputies who were
at Caen. ‘In a few days,’ he said, as he wrote them hastily down, ‘I
will have them all guillotined in Paris.’ As she heard these words she
plunged the knife into his body and killed him on the spot (July 13).
The cry uttered by the murdered man was heard, and Charlotte, who did
not attempt to escape, was captured and conveyed to prison amid the
murmurs of an angry crowd. It had been from the first her intention to
sacrifice her life for the cause of her country, and glorying in her
deed, she met death with stoical indifference. ‘I killed one man,’ she
said, when brought before the revolutionary court, ‘in order to save
the lives of 100,000 others.’

♦Sanguinary tendencies of the Government.♦

Thus perished by the hands of an assassin the man who, since the
revolution began, had persistently maintained that assassination was
a justifiable mode for the accomplishment of political ends. His
murder brought about contrary results to those which the woman who
ignorantly and rashly had flung away her life, hoped by the sacrifice
to effect. Marat had not been the creator of the circumstances which
enabled him to exert influence, and there was no lack of men equally
sanguinary, and equally fanatic, ready to usurp the place left vacant
by his death. He was regarded as a martyr by no small portion of the
working population of Paris. The influence which he had exerted over
them was in reality due, not so much to his exhortations to massacre,
as to the fact that amongst the many writers who had put themselves
forward as the spokesmen of the lower orders, he alone had truly at
heart the destruction of the existing material misery. His murder
excited indignation beyond the comparatively narrow circle of those
who took an active part in political life, while at the same time it
added a new impulse to the growing cry for blood. After the expulsion
of the Girondists, power drifted more and more into the hands of those
who were most violent in language, and who were prepared to be most
violent in act. The more moderate section of the Mountain, composed of
Dantonists and seceders from the Plain, rapidly lost influence. They
were without means by which to exert control over their colleagues,
and were driven to use exaggerated and sanguinary language in order
to escape the charge of being themselves bad patriots and secret
supporters of royalists and federalists. The deputies forming the right
and centre of the Convention kept silence, or ceased to appear in their
seats. The nation remained passive, incapable of resistance. Every day
the Government displayed a more and more ferocious character. It was
cruel, because it was weak in the sense that it had little material
force on which it could rely for support, if its authority were once
disputed. It was cruel also, because it was resolute and fanatic,
determined to maintain itself at whatever cost, and at the same time
under the influence of theories and ideas which could not be carried
into practice except by resort to despotic means and by the destruction
of individual as well as of political liberty.

♦Disorganisation of Government.♦

Despotic as it was, the Government was also exceedingly disorganised,
and this cause rendered it the more sanguinary and aggressive. It
consisted of a number of separate and independent authorities, each
striving for mastery. They were composed in part of the same men, but
in part also of men whose characters, ideas, and aims were often at
variance with each other. The Convention, the Jacobins, the Deputies
in mission, the Committees of Public Safety and General Security,
now commonly called the two Committees of Government, and finally
the Commune of Paris, directed between them the affairs of France.
Of all these authorities the Convention, nominally representative
of France, was the weakest. It had lost the respect alike of the
country and of the populace of Paris, which had so often converted
it into its tool. The contempt in which it was held reacted on the
position of the Mountain, which after the expulsion of the Girondists
was powerless to adopt any measures that gave offence either to the
Commune of Paris or to the Committee of Public Safety, and was equally
powerless to reject measures which either of these bodies desired that
it should adopt. The authority once possessed by the Convention was
now transferred to the Committee of Public Safety, which continued
to gather strength in proportion as the Mountain grew weaker. At
first composed of Dantonists and seceders from the Plain, it became
converted into the organ of the extreme faction which had urged on
the insurrection against the Girondists. In July, Robespierre entered
it with two adherents--Couthon and St. Just. In September were added
Billaud-Varennes and Collot d’Herbois, who were allied with the leaders
of the Commune. On special occasions this Committee consulted in
common with the Committee of General Security, which, however, always
occupied a position subordinate to it. It was now composed of twelve
members, but the five men just named were those who directed the
general action of the Government. In the persons of Robespierre and his
supporters the Committee represented the Jacobins; in the persons of
Billaud and Collot it represented the Commune; and so complete did the
subserviency of the Montagnards become, that although the Committee was
legally subject to re-election every month, they never dared to avail
themselves of this opportunity for naming fresh members in the place of
those who had made themselves their masters.

♦The Commune of Paris.♦

By the side of the Committee of Public Safety, the Commune of Paris
occupied an independent position. Although nominally merely the body
administering the affairs of the capital, it in reality took the lead
in directing the general affairs of France. After it had accomplished
the insurrection against the Girondists, it was the strongest power
in Paris. It had armed bands of ruffians in its pay; the national
guard was under its orders; the revolutionary and civil committees of
the sections were its tools; and, for the time, it had the support of
the populace, which it supplied with bread. The Committee of Public
Safety dared as little as the Mountain risk collision with it. It
forced its supporters into the government offices; sent agents into the
departments; exerted influence over deputies in mission, and compelled
the Convention to appoint ministers and generals of its selection, and
to make laws in accordance with its wishes.

The action of the Commune had for long been mainly directed by two men,
Chaumette and Hébert. They had both been members of the insurrectionary
Commune which had driven Louis from the Tuileries in 1792, and after
its re-election had been ordered by the Convention in the autumn of
the same year, they had reappeared at the Hôtel de Ville, where they
filled the influential position of law officers to the new Commune,
which was made up in part of the same men, and was animated by the
same spirit as its predecessor. Their ascendancy was now signalised
by an extraordinary outburst of cruelty and fanaticism. Not content
with the abolition of political and civil distinctions between man and
man, they sought to destroy all superiorities and to put men socially
and intellectually on the same level. The superiority of wealth was
a special object of their attack. Capitalists, bankers, speculators,
large landowners, were by them and their followers classed along with
federalists, Girondists, nobles, priests, and royalists, as enemies to
the republic. Intellectual superiority and culture became a crime in
their possessors. Equality, in short, was to be produced not by the
raising of the lower, but by the degradation of the higher. If Hébert
demanded the establishment of a primary school in every village, he was
actuated not so much by a regard for the moral and intellectual results
of education as by the wish to make the working classes independent of
the upper. Higher education, more especially classical education, was
decried. Valuable books, statues, and works of art which bore trace
of having been produced under the monarchy, were wantonly destroyed.
Ignorance and rags were put forward as in themselves giving a claim to
respect, and the term ‘sans-culotte,’ ‘the breechless’ (applied to the
poor from their wearing trowsers in place of knee-breeches), was held
synonymous with that of ‘patriot.’ The words ‘Monsieur’ and ‘Madame’
were replaced by ‘citoyen’ and ‘citoyenne,’ and an untidy dress, a
rough manner, and rude language were adopted as symbols of a patriotic
spirit.

Despite the violence and brutality of which they were guilty, neither
the leaders of the Commune, nor yet many of those who followed in
their track or spurred them on, were without enlightened ideas. The
humane philosophy of the century had left its impression, though
it might be but a superficial one, on the hardest and most selfish
natures. Thus, while they sought by terror to destroy the existing
bases of society, Chaumette and Hébert sought also to figure in the
light of philanthropists and guardians of public morality. Acting under
their impulse, the Commune brought forward projects for the reform of
youthful criminals, and for the alleviation of the sufferings of the
sick in hospitals, as well as others of like character, and incessantly
urged on the Convention the suppression of state lotteries, by which
the poor were led to gamble away their sous. Even at their best,
however, the members of the Commune were mainly actuated by personal
motives. They sought to obtain some moral support to their position,
without which it would in the end be impossible for them to retain
power for long. Of their philanthropic schemes, moreover, very few
were carried out in practice. It was the inevitable result of the
conditions under which the Commune had grasped authority, that the
better men should be thrust into the background by the more selfish
and more unscrupulous. Thus Chaumette by the side of Hébert soon sank
into comparative insignificance. For while Chaumette cared for the
accomplishment of ideal aims, Hébert cared alone for the retention
of power by himself, and was entirely indifferent as to the means by
which he secured this end. He was a coarse and low-minded adventurer.
Before the revolution he had been dismissed from an inferior office at
a theatre for dishonest practices. After the revolution began, he had
sought notoriety by the publication of a paper, _Le Père Duchesne_,
written in language coarse even for that time, and advocating atheism.
Around him and the Commune now rallied all the worst ruffians and
scoundrels in Paris. Assassins were appointed to the command of armed
forces, and thieves and rogues were placed on civil and revolutionary
committees which had at their disposition the property and liberty
of their fellow-citizens. In short, so far as the administration was
concerned, the prevailing characteristics of the rule of the Commune
under Hébert’s leadership were anarchy and licence.

♦The Conscription.♦

All authorities were equally interested in preserving France from
invasion, and all concurred in making exertions to put soldiers in the
field, and to provide them with the necessary arms and supplies. The
Convention had at once to find forces to besiege the still revolted
towns of Lyons and Toulon, to suppress the rebellious Vendeans in
the east, to fight the Spaniards in the Pyrenees, the Piedmontese
in the Alps, the English and Austrians in the Netherlands, and the
Austrians and the Prussians on the Rhine. None of the usual motives
which cause men to shrink from adopting extraordinary measures were
felt by the existing rulers of France. To recruit the armies, they
resorted to a conscription. All citizens between the ages of eighteen
and twenty-five were called on to serve in person. Urged on by the
Commune, the Convention further decreed a levy of the whole male
population capable of bearing arms (August 23). Such a measure was of
course impracticable, but it enabled the deputies in mission to bring
together large bodies of men to act against Lyons and Toulon, and to
hold in check the insurgent Vendeans.

♦Maximum laws.♦

Between July and October laws were passed fixing prices and carrying
out the economical system long since demanded in the streets. A small
minority, however, alone of those who were willing to adopt them,
regarded them as economically good. Their framers had in reality
ulterior objects in view. The Hébertists desired to ruin the upper
commercial classes. The Montagnards, as a body, hoped to avert a State
bankruptcy by maintaining the value of the assignats in spite of new
issues, and to provide for the armies by putting at the disposition of
the Government the entire resources of the country--its revenue, its
capital, its stock, and its labour. In the spring a decree had been
passed fixing a maximum price for corn, but variable in the different
departments (p. 152). A maximum price for corn and meal was now fixed
without variation for the whole republic. Neither article might be
sold except at fairs and markets, and the trade in both was put under
the supervision of the municipal bodies. Nearly all articles of
consumption, many manufactured articles, and most raw materials, were
also subjected to a maximum price, which was fixed in each department
at the price that the article sold at in 1790, with the addition of a
third as much again (September 17). In order to prevent wholesale or
retail dealers from keeping back goods from sale, they were required
to expose over their shop doors a list of all articles that they had
in stock, and even private individuals were prohibited from laying in
stores. The practice of supplying the army through contractors was
entirely abandoned. Corn, cloth, butter, flour, meat, fodder, cattle,
carts, horses, vessels, and, in a word, all raw materials, manufactured
articles, or live stock immediately or remotely connected with the
service of the armies, were put in requisition, which meant that their
owners were compelled to sell to the Government at the maximum price,
and to take in payment assignats at their nominal value. Exactly the
same course was pursued with regard to labour. A maximum was fixed for
wages, the most the workman might demand being the wage he received in
1790, with the addition of half as much again. Workmen, like goods,
were then put in requisition, and employed by thousands in making of
arms, building of ships, repairing of roads, and other services of
the same character. In every transaction the State thus gained at the
expense of individuals, since the assignats, in which all payments were
made, were now worth only 33 per cent. of their nominal value.

Together with the requisition and maximum laws were passed others,
which had for their direct object the suppression of speculation on the
fluctuation in prices and in the value of the paper money. Capitalists,
bankers, merchants engaged in foreign commerce, and speculators of
every description, were denounced as aristocrats and enemies of
their country, and in order the more effectually to suppress their
transactions, the idea was entertained of breaking off commercial
and financial relations between France and foreign countries. It
was rendered a capital offence to refuse to accept assignats in
payment of goods, or to offer or accept a higher price in them than
in metal money. Financial and commercial companies were dissolved.
The investment of capital in foreign countries was prohibited, the
Exchange closed, the export of nearly all articles of French growth
and manufacture forbidden, and the mere possession of articles grown
or manufactured in Great Britain declared a crime. All the laws here
described were enforced by fines, confiscations, the prison, and the
guillotine. They succeeded in their immediate end. Wherever buying
and selling went on in public the paper money was taken at par, and
the Government was able to go on incessantly increasing the number of
notes in circulation without meeting a corresponding rise in prices.
But this result was only obtained at the cost of the destruction of
private enterprise, the ruin of hundreds of traders and manufacturers,
a lavish waste of the capital of the country, and the infliction of
an enormous amount of suffering. Little foreign trade remained except
what the Government itself carried on, and the only manufactures which
flourished were those of arms and war material. Trade and agriculture
became the most dangerous occupations in which it was possible to
engage.

From a variety of motives all who could pressed into the service of the
State. It was the one means of avoiding the proscription, the surest
means of avoiding imprisonment, the surest means of acquiring wealth.
The Government offices were flooded with incapable clerks. Municipal
officers and administrators, charged with the care and sale of national
property, had abundant opportunities of benefiting themselves and their
relatives at the expense of the State. The multitude of agents who
were employed in making requisitions for the army could, with small
danger of exposure, enrich themselves by extortion and by breach of the
maximum laws.

♦Formation of a revolutionary army.♦

The maximum laws prevented prices from rising in the open market,
but they could not assure abundance. It was possible to search a
tradesman’s cellars, and to force him to offer his existing stock of
goods for sale at a definite price; but it was impossible to make him
continue to carry on his trade at a loss to himself. It was easier
for the farmer than for the tradesman to break the law; but this did
not benefit the inhabitants of towns. The farmer would often choose
to risk his head by concealing his corn or by sending it out of the
country, sooner than send it to Paris or any other large town, where
the maximum law was most rigidly enforced, and its breach attended
with greatest danger to himself. Since the spring the Commune had
been compelled to take upon itself the entire task of providing for
the city’s consumption of bread. Its agents went into the surrounding
departments and purchased all the corn and meal they could obtain,
often giving a higher price than that prescribed by the law; but it was
nevertheless only with extreme difficulty that the necessary provision
was made. In order to maintain popularity with the working classes,
the Commune was, however, compelled to provide that the daily supply
of bread did not fail. It was compelled also to give satisfaction to
that idle and ruffianly portion of the population by aid of which it
was enabled to impose its will upon the Convention and the Committee
of Public Safety. At the demand of the Commune the Convention passed
a law declaring that Paris, like the armies, should be supplied by
requisitions, and ordering the formation of a special paid force, or
so-called ‘revolutionary army,’ of 7,000 men, which was to go into the
departments and compel farmers to part with their corn at the maximum
price. By these means the Commune obtained command of a new force, and
found means of living for the destitute thieves and beggars with whom
the city swarmed. This army was simply a horde of villains, let loose
upon the neighbouring departments, who went from village to village,
plundering, imprisoning, and torturing the inhabitants. Meanwhile,
scarcity increased at Paris to such an extent that to put an end to the
crowding at the bakers’ doors, the Commune ordered that tickets should
be issued by the sections, specifying the number of loaves that each
family in the city was to be suffered to have for its daily consumption.

♦Law of ‘suspected persons.’♦

The maximum laws increased the already large number of those placed
by the Mountain, the Jacobins, and the Commune outside the pale of
citizenship. The farmer, forced to part with his corn at the maximum
price, would henceforth be suspected of ill-will towards the republic,
as much as the speculator, the merchant, and the contractor for the
armies, who, while freedom of contract had prevailed, had made large
profits at the cost either of individuals or of the State. It was,
in fact, impossible that the economical system established by the
laws described should be accepted except through fear alone. The
self-interest of too many thousands operated in the contrary direction.
The very artisan, who thought it fair that the farmer should be forced
to sell his produce at maximum prices, strove, whenever opportunity
occurred, to obtain higher wages than those which the law allotted to
him. As the number of their enemies increased, the Hébertists, aware
of increased danger to themselves, grew fiercer and more sanguinary
in word and act. ‘To be safe,’ said Hébert, ‘you must kill all.’ If
once nobles, royalists, seigneurs, had been the enemies of France,
now Girondists, federalists, speculators, breakers of maximum laws
were placed in the same class. Urged on by the Commune, the Convention
passed a vaguely-worded law empowering the revolutionary committees
throughout France to imprison all nobles, relations of emigrants,
federalists, and other persons ‘suspected’ of ill-will towards the
Republic (September 17). To carry out literally Hébert’s advice, and
kill all such, was impracticable. But it was possible to diffuse
terror on every side, by casting into prison every man and woman who,
by their conduct or even by their looks, expressed disapproval of the
existing order, and by taking the lives of all those who bore names
in any way representative of the past. At the beginning of September
the number of prisoners in Paris was about 1,500; by the end of October
it had risen to 3,000. Deputies could neither be imprisoned nor be
sent before the revolutionary court without the authorisation of
the Convention. Their security was, however, slight. Ever since the
expulsion of the leading Girondists, the imprisonment, now of one,
now of another of their followers had been decreed, so that the right
side was gradually being destroyed. The final blow was given when, on
the demand of the Committee of General Security, the Convention sent
before the revolutionary court twenty-one deputies of the right, and
also the man who had once been known as the Duke of Orleans, but who
now sat in the ranks of the Mountain and styled himself Philip Egalité.
At the same time the Convention ordered the arrest of more than forty
other deputies who had signed protests against the proceedings of June
2 (October 3). The judges and jurymen of the revolutionary court, like
all authorities elected at Paris, were the tools or accomplices of the
Commune and of the Committees of Government. The public prosecutor,
Fouquier Tinville, acted under the instructions of the Committee
of Public Safety. Hitherto the Court had observed the forms of its
institution. Witnesses were called on both sides, and the defence was
fully heard. Between March and October the Court had sentenced to death
sixty-nine persons and acquitted ninety-two. But from this time forms
were less and less regarded, while the number of condemnations rose to
more than sixty a month. The guillotine stood permanently on the Place
de la Révolution.

♦Execution of the Queen.♦

The life of the captive Queen had long been sought for by the
Hébertists. Since the fall of the throne she had been shut off from
all communication with the outer world. She had seen her husband
leave her to die on the scaffold, and her young son had since been
torn from her arms, on the pretext that if he were left with her she
would bring him up to be a tyrant. Her gaolers, whatever their feelings
might be, dared not show her the smallest sign of sympathy. She was
informed of the fate that awaited her by her removal from the Temple
to the Conciergerie, a prison situated on the island in the Seine,
close to the Palais de Justice, where the Revolutionary Court, as
well as other Courts of Justice, sat. When brought before the Court
she replied with firmness to the accusations made against her, and by
her composed and dignified bearing won murmurs of applause from the
hostile crowd, which had gathered to witness how the once haughty Queen
would endure degradation and ignominy. Like other condemned persons,
Marie Antoinette was taken from the Conciergerie to the Place de la
Révolution, seated in a common cart with her arms tied behind her.
History can have little to say in praise of a Queen whose conduct,
during her years of prosperity, had done much to cause that general
disorganisation of society and government, in the midst of which she
perished amongst so many other victims, of whom many had striven for
higher objects, and of whom many were more innocent than herself. But
by her brave endurance of adversity, and the noble and resigned manner
in which she met death, she, like others, atoned for past errors, and
won for her memory respect and sympathy (October 16).

♦Execution of the Girondists.♦

Twenty-one deputies of the right soon followed the Queen to the
scaffold. Amongst them were nine of those deputies whose arrest had
been ordered on June 2, including Vergniaud, Brissot, and Gensonné.
Their trial was cut short through fear lest if they were allowed to
plead their cause they would gain the sympathy of the eager and
excited audience with which the Court was thronged. On their way from
the Conciergerie to the Place de la Révolution they sang together the
already famous song, the Marseillaise, beginning,--

    Allons, enfants de la patrie,
    Le jour de gloire est arrivé.

After their arrival at the scaffold the song was continued, while each
in turn received the blow of the fatal knife, and did not cease until
the head of the last had fallen.

From this time a number of victims, some distinguished, others obscure,
belonging to all parties, went every week to end their lives at the
Place de la Révolution. Amongst them were the late King’s sister,
the gentle and pious Madame Elizabeth; the former Mayor of Paris,
the grey-haired Bailly; the youthful Barnave, Mirabeau’s rival for
popularity in the Constituent Assembly; Philip Egalité, who could not
atone for the crime of his birth, although he had voted for the death
of Louis; and Madame Roland, the friend and inspirer of the Girondists,
condemned for plotting against the unity and indivisibility of the
republic. Her husband, the former Minister of the Interior, who had
been in hiding at Rouen, was found lying in a field, stabbed to death
by his own hand, soon after the news of her condemnation reached him.

♦Worship of Reason.♦

Those who were prepared to shed blood like water, and had, in their own
words, put terror on the order of the day, recognised no limitations to
their power. All, however, were not prepared to adopt the same course
of action. The Hébertists, following the atheistic and materialistic
doctrines which had been circulated by Diderot and other philosophers
of the same school, denied the existence of a personal God and the
immortality of the soul. Theists and sceptics, the followers of
Rousseau and of Voltaire, regarded the Catholic faith as pernicious
and degrading; but various reasons restrained them from attempting
its suppression. They held in theory the principles of religious
toleration; they believed that the Catholic faith would necessarily
lose influence as knowledge became more diffused; they were alive
to the danger of exciting the peasantry against the revolution by
depriving them of the rites to which they were accustomed. Hébert and
Chaumette entertained no such scruples. They were active propagandists,
eager to avail themselves of the power of the State in order to impose
a new form of worship on Catholic France. Unlike Marat and Robespierre,
Hébert from the beginning of the revolution had exhibited equal
hostility towards the hard-working and poorly-paid curé, whose parents
were peasants, as towards the titled and wealthy bishop who belonged to
the caste of the nobility; and he now exhibited equal hostility towards
the constitutional priest who had accepted the work of the revolution,
as towards the nonjuror who sought to excite reaction in favour of
royalty. Morality and reason as displayed by man were declared alone
fit for veneration, and the worship to take the place of the Catholic
ritual was to be one which, refusing to recognise a spiritual world
beyond the sphere of human knowledge, glorified human nature and
material objects. The people, said Chaumette, shall be our God; we need
no other. We want, said Hébert, no other religion than that of nature;
no other temple than that of reason; no other worship than that of
liberty, equality, and fraternity. By the orders of the Commune the
suppression of the Catholic worship was begun. Constitutional priests
were encouraged to marry and to abdicate their functions, and those who
refused were imprisoned. The exercise of the Catholic worship, either
in the streets or in the churches, was prohibited. Even burial rites
were changed. Every sign of mourning was abolished, and the black pall
was replaced by a tricolour cloth.

These things were done by the Commune on its sole authority, but the
Convention offered no opposition. The voices of Catholics were silent
through fear. Forty bishops and curés had seats in the House. But of
these the bravest had been proscribed with the Girondists. If few
deputies professed atheism, those who were theists and sceptics saw
not without gratification the suppression of the Catholic worship
by other hands than their own. Urged on by the Commune the Assembly
adopted a new calendar, which was in reality incompatible with the
maintenance of the Catholic Church as a State institution. The year
was divided into twelve months of thirty days each and five odd days;
each of the months into three weeks of ten days each. The months
were named after the seasons, the Frosty, the Rainy, and the like.
The year I. began on September 22, 1792, the day of the proclamation
of the republic. Hostility towards Catholicism was yet more plainly
evinced by the adoption of a new law, which treated the constitutional
clergy as enemies of the revolution. Not only were nonjurors to be
immediately transported to the West Coast of Africa, and if taken
in hiding in France to be put to death, but constitutional priests
were made subject to transportation to the same place at the pleasure
of the administrative authorities. Willingly or unwillingly the
Convention was dragged in the wake of the Commune, and had to give
official recognition to the new worship. Gobel, the Archbishop of
Paris, attended by his chaplains and curés, was brought before the
Assembly to make public resignation of his office. Several bishops
and curés, who were deputies, rose and followed his example. One man
alone, a Montagnard, Grégoire, the constitutional Bishop of Blois had
the courage to protest and to declare his intention of maintaining his
post (November 7). From day to day revellers, masquerading in priestly
vestments and laden with church plate, visited the Convention, there
to deposit their spoils and to denounce as impostors the maintainers
of Catholic doctrines. Finally, a festival in honour of Reason was
celebrated in the Church of Notre Dame. A mountain of painted wood was
erected in the choir, on which was seated a woman representing Reason,
dressed in white, with a pike in her hand and a red cap on her head.
All the civic authorities attended the ceremony. A procession, carrying
this representative of Reason in its midst, marched to the Convention
to the sound of music, and upon the demand of the municipal officers
it was decreed that the Church of Notre Dame should thenceforth be
converted into the Temple of Reason (November 10). From this time the
churches of Paris were either closed or used as meeting-places, where
disorderly crowds from time to time assembled to hear speeches made and
songs sung in honour of Liberty and of Reason.

♦Destruction of the Vendean army.♦

While these strange scenes were being enacted in Paris, war on the
frontiers, and war in the interior of France continued to be waged as
fiercely as before. The allies, when they deferred invasion till the
next campaign, had made the error of rendering no assistance to the
royalist insurgents within France. England sent no aid to the Vendeans;
Austria none to Lyons. Accordingly, in October, Lyons surrendered.
Toulon, by admitting an English and Spanish fleet into its harbour,
was enabled to lengthen out till the end of the year its isolated and
hopeless resistance. In La Vendée the war on both sides was conducted
with extreme ferocity. The Convention adopted a decree, brought in by
the Committee of Public Safety, which ordered the generals to burn the
forests and insurgent villages, to seize the corn and cattle, and to
make prisoners of the women and children (August 1). The intention was
to burn and starve the country out. But the undisciplined republican
levies were repelled whenever they sought to make their way into
the interior. The generals were incompetent and authority divided.
The Commune, the Committee of Public Safety, and the Mountain, were
severally represented by a number of agents and deputies in mission,
who contended with one another for the direction of the war and gave
support to different generals. The situation was at last changed by
the arrival at Nantes of several thousand troops of the line who had
formed the late garrison of Mainz, and who were bound by the terms of
their capitulation not to fight against the allies for a year, but
were not forbidden to fight against French insurgents. Led by one of
their own officers, Kléber, these troops penetrated to the heart of
Upper Vendée, driving before them the largest army the Vendeans ever
brought together. At the same time forces marched from Saumur and
other points to effect a junction with them. The retreating Vendeans
were accompanied by a host of non-combatants, old men, women, and
children, burnt out of their homes or flying for their lives. Forced
back on the Loire, they made a stand at Chollet, but only to experience
fresh defeat. A general flight was effected across the river in boats
(October 20). By this time most of the chiefs were either dead or
dying. La Rochejaquelein, a young noble, and Stofflet, a peasant,
took the command. Compelled always to move onwards through scarcity
of food, the fugitives made their way to Normandy, in the hope of
occupying Granville, a port town, and of receiving aid from England.
But they had no siege pieces, and their repeated attempts to storm the
fortifications failed. Then despair, long since felt by the chiefs,
overtook the whole body. The ranks of the fighting men, incessantly
called on to repel the attacks of the pursuing enemy, were gradually
thinned; there was dearth of food, and the sufferings of the wounded
were intense. The republicans massacred every man, woman, and child
left behind. The peasants forced their officers to lead them back to
their own country. Angers was reached, where was a bridge over the
Loire. But their attempt to force an entrance into the town failed. A
defeat took place outside Le Mans (December 12); the retreat became
a flight. Thousands were killed and made prisoners; a few escaped in
boats; the rest were hunted down and slaughtered on the banks of the
Loire.

♦The Terror in the departments.♦

While this civil war was continuing in the west, scenes similar to
those occurring in Paris occurred simultaneously throughout the
country. The will of the Commune was law in most of the departments of
France. Some of the deputies in mission joined the Hébertist faction,
and their colleagues followed in their train, not daring to venture
collision with them. Men, in fact, adopted the language then in vogue,
and acted cruelly, instigated by fear lest if they showed clemency
they would offer a handle which their enemies would use to compass the
ruin of themselves and their families. The deputies in mission, so
long as they found protection in Paris, exercised uncontrolled powers
over the properties and lives of their fellow-citizens. They imposed
fines and taxes, set aside laws, created criminal offences, and erected
criminal courts. Many decrees of the Convention merely extended to the
whole country measures already in force in different departments. As
instruments the deputies had at their service the municipalities, which
were reconstituted over and over again; the clubs, from which they
drove all who were not prepared slavishly to applaud their actions;
and, finally, the revolutionary committees, to which they delegated
the same arbitrary powers that they themselves exercised. These
committees, of which there was one established in every district and
every populous commune, were, as a rule, formed of the most fanatic,
the most cowardly, and the most worthless men whom the neighbourhood
produced. Many thousand persons were at their bidding flung into prison
on the merest pretext or without any motive at all being given. One
would be imprisoned because he was related to an emigrant, another
because he was a fanatic, a third because he was an egotist, a fourth
because he had done nothing for the revolution, a fifth because he had
100_l._ or 50_l._ a year. Persons of both sexes, of every age and rank,
were involved in the same proscription. Taxes were assessed at random.
Those who could not or would not pay the sum demanded were imprisoned
and their revenues confiscated. Persons in possession of metal money
were made to exchange it for assignats. In every third department at
least executions continually took place. There were no less than 178
extraordinary or revolutionary courts of one and another kind. Many
observed no forms whatever, and passed several hundred judgments in
a single sitting. So small was the control exercised by the central
Government, that the Committee of Public Safety was in ignorance of
the existence of some of these courts or of the number of persons
punished by their decrees. The Catholic religion was proscribed. Before
the worship of Reason was established at Paris, Hébertist deputies
were confiscating the plate of churches, prohibiting the exercise of
Catholic rites, and making bonfires of religious books and relics.
Constitutional priests were imprisoned and guillotined by the score.
Between one and two thousand married and abjured their faith. The
observance of Sunday was prohibited. On the first days of the new weeks
of ten days, feasts in honour of Reason, of Equality, of Liberty, and
the like, were held in the churches, from which none remained absent
without risk of being classed in the category of suspected persons.

In every department property was confiscated, many persons imprisoned,
and lives taken. But the amount of suffering inflicted and blood shed
in any one department, nevertheless, depended in some degree on the
character of the deputy in mission, and on the part that had been
taken by the department after the expulsion of the Girondists. The
Government had the support of a small number of men who, if fanatics,
were nevertheless honest in believing that, whatever its excesses, it
alone could save France from conquest, and who endeavoured to make
use of their authority, not for personal or selfish ends, but for the
public good, as they understood the term. Such men might be cruel;
but if so, it was with a motive, not through cowardice, or the mere
pleasure taken by the tyrant in making his power felt. St. Just, in
Alsace, took from the citizens of Strasburg their coats, their beds,
their boots, or whatever else he wanted to supply the wants of the
soldiers. The municipal officers were commanded to provide 10,000 pairs
of boots in the course of twenty-four hours. ‘Take,’ the youthful
dictator wrote to them, ‘the boots off the feet of the aristocrats.’
In Auvergne, Couthon, while he exercised a grinding tyranny, aspired
to win the attachment of the population. He obtained State grants
for the embellishment of Clermont, his native town, established a
manufactory of arms to give employment to destitute workmen, founded
a college in the interests of education, and let out of prison a
number of peasant farmers. But men of the description of St. Just and
Couthon were rare. Far more often deputies in mission sought to enrich
themselves, and closed their eyes to the greed and rapacity of their
agents. At Bordeaux, under the presidency of the cowardly Tallien,
the rich man who could offer a sufficiently large bribe to his judges
escaped with his life: the poor man went to the scaffold. In the
departments where the Hébertists ruled most licence and most shedding
of blood were invariably to be met with. Following the example set in
Paris, they established revolutionary armies, which were charged with
collecting taxes and bringing in corn, and which made havoc of the
country through which they passed. Men of weak and violent character,
suddenly risen to power, developed into tyrants capable of the most
atrocious crimes, and with hearts apparently destitute of all feelings
of justice and humanity. The prisons at Nantes were crowded with
persons dying from disease and starvation, the wrecks of the Vendean
army. In place of sending these victims of civil war back to their own
country, the deputy Carrier caused them to be placed on rafts, which
were afterwards sunk in the Loire, a process of execution twelve times
adopted. On the great industrial town of Lyons savage vengeance was
taken. Persons of every condition of life--manufacturers, shopkeepers,
and artisans--condemned by military commissioners, were shot in batches
of two or three hundred at a time. Whole streets and squares were
blown up by gunpowder; an immense amount of property was plundered and
destroyed. According to the reckoning of the two deputies on whom the
immediate responsibility rested, Collot and Fouché, in five months the
population was reduced from 130,000 to 80,000 souls. The punishment
inflicted on Toulon, when at last it surrendered in December, was
hardly less atrocious.

♦Terrorists few in number.♦

The men who approved these acts and took part in them formed but an
exceedingly small minority in the departments--in some districts
so small that they might be counted on the fingers. In parts of
Brittany fugitive Vendeans, in the neighbourhood of Bordeaux fugitive
Girondists, remained in safe hiding, because there was no one who
cared to betray them. In the Basses Pyrénées, up till the autumn of
1793, revolutionary laws had remained unenforced, and a noble, elected
in 1790, was still mayor of Pau. The judges of the ordinary courts,
though at peril of their lives, refused to condemn their neighbours
to death. The mass of municipal and administrative officers only
took part in revolutionary measures under compulsion. A small knot
of men, cowards, ruffians, fanatics, and fortune-hunters, gathered
round the deputy in mission, directed the action of the clubs, sat in
the revolutionary committees, and were judges in the revolutionary
courts. Peasants and artisans gave as little active support to the
Terror as the nobles or the bourgeoisie. The peasants, having freed
themselves from feudal duties, became conservative. The requisitions
for the armies and the corn maximum were incessant causes of irritation
to them. The maximum of wages irritated artisans. Both classes were
alienated by the suppression of the Catholic worship. The Hébertists
vainly strove to acquire support by holding up the rich to reprobation,
and by undertaking to give provision to the poor, and to provide
labour for them. They succeeded in ruining the rich, but failed to
benefit the poor. The main object, with a view to which their whole
conduct was regulated, was to lay hands on all the wealth which tyranny
and brutality could bring within their grasp; and of the spoils the
larger part stayed, if not in their own hands, in the hands of their
agents--the smaller was spent in the public service, and a bare
pittance was left for providing bread and alms for the destitute.
Thus, in 133 districts, where 1,400,000_l._ were admittedly raised in
revolutionary taxes, a year afterwards only 430,000_l._ were accounted
for. Material want was far greater than in the capital. In Lyons,
Bordeaux, and many other places the inhabitants were put on rations,
and a few ounces of bad bread were daily doled out per head.




CHAPTER VIII.

THE FALL OF THE HÉBERTISTS AND DANTONISTS.


♦The Army.♦

While the internal condition of France was such as has been described,
her enemies were being successfully held in check on the frontiers.
After the great conscription decreed by the Convention in August had
been effected, there were in all some million of men in arms. The
nation might hate and despise its fanatic, tyrannical, and cruel
Government, but it none the less remained proud of the changes which
the revolution had effected, and was ready to endure the heavy yoke
laid on it for the sake of defending France against interference from
abroad. The nation was in reality far more truly represented by the
army than by the Government. The soldiers, like the mass of those
who stayed at home, were intensely enthusiastic in defence of their
country, but took no part in the strife of internal factions. The
Government was fully alive to the fact that it had not, except in a
passive sense, the support of the large forces which necessity had
compelled it to bring together, and the leaders in Paris lived always
with the fear before them that some general would follow the example
of Dumouriez, and turn against his employers. The Hébertists sought
to weed out of the army all officers who by birth belonged to the old
nobility. Such were cashiered by hundreds, and their places given to
men from the ranks. Even these new officers, however, became objects of
suspicion if they displayed military capacity, and won the affection
of their men; and the generals were on the merest pretext condemned
of treachery or treason by the revolutionary court, and were sent to
the scaffold. Deputies in mission acted as spies on the conduct of all
superior officers, reported their words and actions to the Committee
of Public Safety, attended at military councils, and were held by
the soldiers in more awe than the commander-in-chief. All the more
important movements of the armies were directed from Paris, where the
plans of campaigns were laid down by Carnot, one of the members of the
Committee of Public Safety. Carnot had been educated as a military
engineer, and his considerable abilities were made available by his
indefatigable energy and his intense enthusiasm for his work. In the
face of the many obstacles which the disorganisation of the Government
presented, he devoted himself entirely to the task of organising the
armies, and of insuring that the war which extended over so wide a
field should be conducted with intelligence and method. The success
which the French attained was undoubtedly in great part owing to his
unremitting exertions. Hitherto the army had been divided into two
bodies, distinguished from one another by pay, uniform, and system of
advancement--namely, troops of the line which had formed the army of
the monarchy, and new battalions raised since the beginning of the war.
♦The French Army.♦ In February 1793, the Convention had determined
to abolish these distinctions, and to fuse in common regiments the
troops of the line and the new recruits, and the operation was actually
carried into effect during the following winter. Thus, in place of the
old royal army there had come into existence a wholly new army, the
creation of the revolution. The troops lacked training and discipline,
but were ready to fight continually against superior numbers, had
confidence in their officers, and were not easily shaken by reverses.
Many officers were unable to read and write, but against this defect
was to be set the advantage that military talent rapidly found its way
to the front. Two-thirds of the regimental officers were elected by
those whom they were to command, one-third was advanced by time of
service. The appointment of the generals the Government reserved to
itself.

[Illustration: THE RHINE

                                                          E. Weller.
]

♦Campaign in Belgium.♦

After the surrender of Condé and Valenciennes, the forces of the allies
in Flanders separated. The Duke of York, against Coburg’s desire, went
west to lay siege to Dunkirk, while Coburg himself invested Le Quesnoi.
The Duke’s forces were in two divisions. He himself with 20,000 men
besieged Dunkirk; 15,000 Hanoverians under Freitag remained a few miles
inland to watch the enemy. The commander of the garrison opened the
dykes and flooded the country, cutting off communication between the
two divisions, and confining the Duke’s retreat eastwards to Furnes,
along the sea coast. The French General Houchard, bringing together
50,000 men, overpowered Freitag’s 15,000 at the village of Hondschoote,
and drove them back on Furnes (September 8). The Duke of York, hastily
raising the siege, effected by a night march his retreat to Furnes, and
afterwards rejoined the Austrians. Houchard, accused of treason and
of neglecting to follow up his victory, was guillotined. In his place
was appointed General Jourdan, who in 1791 had entered the army as a
volunteer. Le Quesnoi surrendered to Coburg, and the allies next laid
siege to Maubeuge. Jourdan, bringing together a large force, defeated
at Wattignies 18,000 Austrians, stationed south of the river to guard
against his advance (October 16). Coburg in consequence raised the
siege, and the armies on both sides retired into winter quarters. The
allies during the campaign had won three French fortresses--Condé,
Valenciennes, and Le Quesnoi.

♦Campaign on the Rhine.♦

After the fall of Mainz the war on the Rhine had flagged. The Austrians
proposed to turn south and conquer Alsace, the Prussians to lay siege
to Saarlouis. The Austrian plan was adopted, but not vigorously
pursued. At Berlin the final settlement of affairs in Poland was
regarded as being of more importance to Prussia than anything that
might happen in France; and the advisers of Frederick William were
unwilling that Prussian troops should shed their blood in conquering
Alsace for the Emperor. The French occupied a strong position behind
the Lauter, called the lines of Weissenburg. After many weeks’ delay
these lines were stormed by a combined attack of the Austrian and
Prussian forces (October 11–13). The Austrian general Wurmser then
pressed on southwards, eager to reach Strasburg; while Brunswick, who
knew that he would give offence at Berlin if he engaged the Prussian
troops in a winter campaign in Alsace, blockaded Landau, and began
to take up winter quarters in the Vosges. The allied army in this
quarter was consequently spread out in a long thin line, extending
from Kaiserslautern to Hagenau and Dussenheim. The French forces,
divided into two armies, were commanded by two young and talented
generals--the Rhine army by Pichegru, the Moselle army by Hoche. Hoche
at first made ineffectual efforts to storm Brunswick’s positions round
Kaiserslautern, while Pichegru attacked the Austrians. Directed by
Carnot, Hoche then placed a portion of his army at Pichegru’s disposal,
after which a fierce and unremitting assault was opened on Wurmser’s
positions. The Austrian line, broken through and surrounded, gave
way on all sides. Wurmser, casting the blame of the disaster on the
Prussians, retreated across the Rhine, and Brunswick was compelled
to follow him. The siege of Landau was thus raised, and the French
reoccupied Spires and Worms (December).

The victory of Wattignies, and still more the expulsion of the allies
from Alsace, affected the relations of the factions which were
struggling for ascendancy in Paris. The Montagnards resented the
subserviency in which they were held by the Commune and by the two
Committees; and as the danger of invasion decreased, the stronger grew
their desire to shake off the oppressive yoke which they had laid
upon themselves by the expulsion of the Girondists. Only a very few
of their number really entertained the same ideas as the Hébertists;
whilst outside the Committees of Public Safety and General Security,
there was scarcely a deputy who did not resent the tyranny exercised by
these Committees. Yet the Montagnards could not regain independence.
They could not appeal to the deputies of the centre, who crouched in
subservience even greater than their own before the Committees and the
Commune. They were themselves without courage or union. All sense of
political honour was dead, and in order to avoid giving offence, where
to do so was dangerous, men were prepared to retract their own words,
and to sacrifice their fellows without compunction. Some Montagnards,
instigated by fear for their own lives, obtained the adoption of a
decree to the effect that the Convention would suffer its members to
speak in self-defence when charges were made against them (November
10). A few days afterwards, on the demand of the Committee of Public
Safety, the Convention repealed this decree, and ordered the arrest of
four deputies, including its proposers against whom a general charge of
conspiring against the Republic was laid by the Committee.

♦The work of the Convention.♦

Happily, this tale of crouching submission to tyranny does not fill
the whole of the annals of the Convention. Men ordinarily silent in
the Convention sought shelter in private committees appointed for the
preparation of special laws. In these, Montagnards and deputies of the
centre still worked side by side, elaborating legislative projects for
the advance of education, the reform of the civil law, the improvement
of agriculture, the draining of marshes, the suppression of mendicity
and the relief of the poor, and others of similar character. Although
much of their labour produced no results, still a considerable
amount of most important legislation was effected, which dated its
commencement from the times when the Girondists had been in power, and
which was far more truly characteristic of the Convention as a body
than the bloody laws which it passed at the dictation of the Committee
of Public Safety speaking in the name of the Jacobins and of the
Commune.

The Constituent Assembly had retained, until the proprietors could be
compensated, feudal duties presumed to be due for a grant of land. The
Legislative Assembly, following a theory which had been entertained by
many lawyers--that land was originally free--had decreed the abolition
of all duties without indemnity, except in cases where the proprietors
could prove the original title, showing that the duties were really
due for a grant of land. This as a rule was impossible, the duties
being due by prescription only. The new law gave rise to suits, and
the Convention destroyed the last vestiges of the feudal system by
decreeing the abolition without indemnity of all duties which bore a
feudal character. Before the ejection of the Girondists entails were
abolished, and parents were also prohibited from making wills favouring
one child more than another. Parents were now further prohibited from
giving more than a tenth of their property to strangers, or more than
a sixth to collateral relations. Illegitimate children were put on the
same footing as legitimate. The Legislative Assembly had instituted
civil marriages, and had permitted divorce, on the mere ground of
incompatibility of temper, with the consent of both parties. A new
civil code, clear and simple, and in accordance with the legislation
of the revolutionary Assemblies, was being prepared to take the place
of the chaos of old laws and customs. The work, however, was but in
progress, and the new code was not promulgated by the Convention. Negro
slavery was abolished, and men of colour in the colonies received the
rights of French citizens. A decree was passed for the establishment
of primary schools to be maintained by the State. Instruction was
to be gratuitous, attendance compulsory, and no religious teaching
allowed. Laws were also passed for the institution of three schools
of medicine and a school of natural history at Paris. But little was
in reality effected for the instruction of any class. Money and power
were both wanting. Instigated by its Committee of Public Instruction,
the Convention repeatedly ordered the preservation of the valuable
monastic libraries. None the less, the books were neglected, plundered,
and scattered. Primary schools, if opened, were, in the country,
unattended. Of higher education little was to be had. Suspected of
reactionary tendencies, all academies and learned societies had been
broken up. Most colleges had disappeared; a few dragged on a feeble
existence.

♦Cambon’s financial measures.♦

By the side of the two committees of Government, the Committee of
Finance occupied an important and, to some extent, an independent
position. The Committee of Public Safety possessed no member prepared
to undertake the direction of the finances, and it was therefore
obliged to leave the initiative to others. The deputy Cambon, who sat
on the confines of the Mountain, practically occupied the position of
Minister of Finance; and several laws introduced by him were adopted,
designed to restore equilibrium between expenditure and revenue, and
to prevent increase in the number of assignats in circulation. The
State possessed a large number of creditors, some lenders before the
revolution, others since; whilst to others compensation was due for
abolished offices. All these creditors were put on the same footing.
Capital, if due to them, was made irrecoverable, and in all cases five
per cent. interest given. The old titles were destroyed and the new
entered in a common book, called the Great Book of the Public Debt.
The State gained by the operation, more especially in the case of
loans contracted before the revolution, often on very onerous terms. A
new source of revenue was sought in the imposition of a forced loan,
according to the law passed in the spring. The lenders were to be
repaid in confiscated lands. This loan was expected to bring in the
large sum of 43,750,000_l._, and assignats to that amount were to be
withdrawn from circulation.

Efforts to restore the finances were, however, as fruitless as efforts
to advance education. While millions were being squandered in the
departments, taxes imposed by the Convention remained unpaid. The
forced loan never brought in more than eight millions. Cambon vainly
reiterated complaints that but little of the sums irregularly raised
in the departments ever reached the treasury. So long as the Commune
exercised power, it was impossible for the Convention to take any
effectual steps for the enforcement of its decrees.

Thus it came about from a variety of causes that the existing
Government gave dissatisfaction to many of those who took part in it.
Even the most cruel and unprincipled of the Montagnards resented their
subservient position. The institution of the Worship of Reason gave
offence to many of them. The wanton waste of property and destruction
of life going on in the chief commercial towns of France, in Lyons,
Toulon, Bordeaux, and Nantes, excited disgust if not pity. Now that the
country was no longer in any immediate danger of invasion, men, before
indifferent as to what was done so long as the enemy was repulsed,
awoke to the horror of the scenes that were being enacted round them.
The Dantonists sincerely desired to stay the action of the guillotine.
Having been pushed aside, since the reconstitution of the Committee
of Public Safety in July, by men more fanatic and sanguinary than
themselves, they were visited by remorse as they experienced their
powerlessness to hold in check passions which they had themselves
helped to unloose. ‘I cannot forget,’ wrote Desmoulins, warmly attached
to his own wife and child, ‘that the men they are killing by thousands
have also wives and children.’

♦The Hébertists attacked by Robespierre.♦

Besides creating discontent in the Mountain, the ascendancy of the
Commune gave dissatisfaction to the Committee of Public Safety, and in
particular to Robespierre. Robespierre was opposed to the principles of
which Hébert had declared himself the special champion. He put himself
forward, indeed, as being as well as Hébert the people’s friend, but
between neither the aims nor the characters of the two men did any real
similarity exist. Robespierre had no sympathy for a movement which
idolised ignorance, rags, and vice, and made the Republic the prey
of bands of rapacious and unscrupulous adventurers. While Hébert, by
the adoption of rude manners and coarse language, sought popularity,
Robespierre always maintained propriety both in language and in dress,
continuing even to wear his hair powdered, as had been the custom of
educated men under the monarchy. Further, the atheistic doctrines which
Hébert professed were to Robespierre essentially repugnant. Robespierre
was a theist of the school of Rousseau, and Rousseau had said that men
could not be good citizens who did not believe in a special providence
and in a future life, and that atheism was the one doctrine the public
profession of which no wise legislator would tolerate.

In the Jacobins Robespierre attacked Hébert and the Commune on the
ground of their intolerance. Those, he said, who persecute priests are
more fanatic than the priests themselves. Atheism is aristocratic.
The idea of a Supreme Being who watches over oppressed innocence and
punishes triumphant crime is wholly popular. If God did not exist, we
should have to invent him.

Thus, both by principle and ambition, Robespierre was urged on to seek
the destruction of the Hébertists and of the Commune. His colleagues
on the two committees, though most of them disliked him personally,
and were afraid of his gaining increased ascendancy for himself,
shared his desire to break the power of the Commune. As they grew more
accustomed to the exercise of authority, they became impatient at
having to share it with a body whose will had always to be taken into
consideration, and by whose action their own was often thwarted. The
Montagnards hated the tyranny of the two committees, but they hated
the tyranny of the Commune yet more, and were willing to take part in
overthrowing it, neglectful of the probability that by so doing they
would yet more securely rivet the chains in which the committees held
them. In the Convention the Hébertist generals and agents in La Vendée
were incessantly accused of misconduct and incapacity, and of being
responsible for whatever reverses had taken place. A law was passed
intended to centralise power in the hands of the two committees, and
to deprive the Commune of the instruments by means of which it secured
ascendancy in the departments. The revolutionary committees of Paris
were put under the supervision of the Committee of General Security.
The Commune was deprived of the right of sending agents into the
departments. The revolutionary army of Paris was for the time left in
existence, through fear lest if an attempt were made to disband it, it
might rise against the Convention, but the revolutionary armies in the
departments were to be suppressed. No taxes were to be imposed without
the sanction of the Convention. The law officers belonging to districts
and municipalities, hitherto elected, were made dependent on the
central Government, and received the name of national agents (December
4).

♦Struggle between Dantonists and Hébertists.♦

About the same time that this law was adopted, Desmoulins, encouraged
by Robespierre, began the publication of a paper, the _Old Cordelier_,
in which he first confined himself to denouncing the Hébertists, but
went on to denounce the Terror itself as a great deception, and to
compare the state of things in France to that which prevailed under
the worst of the Roman emperors. The law of treason, he said, was
extended to words; the inhabitants of towns were killed in masses.
Grief, pity, looks of disapprobation, silence itself, constituted State
crimes. It was a crime to be rich; a crime to give shelter to a friend.
Is it possible, he asked, that the state of things which constituted
despotism and the worst of governments when Tacitus wrote, constitutes
to-day liberty and the best of possible worlds? You wish to exterminate
your enemies by the guillotine. What folly! For every man you kill you
make ten new enemies. If we do not understand by liberty the carrying
out of principles, never was there an idolatry so stupid as ours, nor
one that costs more. Liberty is no operatic singer promenading in a red
cap. Liberty is happiness, equality, justice, the Declaration of Rights
itself. If I am to recognise her presence, open the prison doors to
those 200,000 citizens whom you call ‘suspected.’

Thus was the Commune attacked on three sides at once--by Montagnards,
who desired the independence of the Convention; by the Committee of
Public Safety, which sought the extension of its own authority; and by
Dantonists, who sought to hold in check the Terror. Hébert was afraid
to enter into contention with Robespierre. By the atheistic movement
he had sought and attained notoriety, but its active supporters were
few, and there was no probability that any considerable body of men
would rally round him in its defence. Chaumette, at the Commune, made
a speech on the folly of attempting to suppress religious opinions by
force. Hébert went further, and made a formal denial of atheism at the
Jacobins. But while seeking to curry favour with Robespierre, Hébert
and his followers opened the more vehement attack on the Dantonists.
Here they were surer of their ground, for all who had been actively
engaged in the work of destruction dreaded the first step of reaction,
lest vengeance should overtake themselves. The Cordeliers erased the
names of Danton and Desmoulins from their list of members. Collot,
the director of the atrocities committed at Lyons, who had returned
to Paris in December, expressed amazement that the first who spoke of
clemency had not been sent to the scaffold. Amongst the twelve men who
formed the Committee of Public Safety no good understanding existed.
Six concerned themselves with special branches of administration, but
took no part in directing the general action of the Government. The
remaining six were not all of one mind. Couthon and St. Just were
devoted adherents of Robespierre. Barère, originally a deputy of the
centre, and a temporiser between the Mountain and the Gironde, was
indifferent whether Robespierre or Hébert succumbed, so long as he
found himself on the winning side. Billaud and Collot, who acted
together, were the two most sanguinary men on the committee. They
were connected with the Hébertists. They had no quarrel with the
establishment of the Worship of Reason, and dreaded, by the destruction
of Hébert, to give Robespierre an opportunity of domineering over
themselves. As members of the committee, however, they disliked
the rivalry of the Commune, and they were besides afraid both of
Robespierre’s enmity and of the triumph of the Dantonists. Accordingly,
they were prepared to sacrifice Hébert, so long as they could secure
themselves against reaction by putting Danton to death as well. On
his side, Robespierre was prepared to sacrifice Danton. He could not
join the Dantonist reaction against the Terror without imperilling
his influence at the Jacobins, and forcing Collot and Billaud to make
common cause with Hébert. Moreover, were the Hébertists suppressed
by the triumph of the Dantonists, Robespierre would have to face
the contingency of the Mountain shaking off the control of the two
committees.

♦Robespierre and the Jacobins.♦

The Jacobin club was the field where the battle between Robespierre and
Hébert was first fought out. In this society, which was Robespierre’s
stronghold, Hébert was powerless to contend against him. Many of the
frequenters of the club were indeed Hébertists, but their influence
was small compared with that of Robespierre and his supporters. All
the small tradesmen and artisans who, uninfluenced by sordid motives,
still took interest in political affairs, idolised Robespierre. While
Hébert had the adherence of the unprincipled and vicious only, who were
sure to abandon him in time of peril, Robespierre had the affection of
partisans ready to stand by him, and in case of need to die for him.
His undoubted integrity, his constant talk of virtue and morality, the
reserve of his manner, the very dryness of his language, made a deep
impression upon sincere but narrow and fervent minds. The rough men
and women who frequented the galleries of the Jacobins listened to him
with rapt attention, and applauded his words with such hearty energy
that persons who ventured amongst them without imitating their conduct
became objects of remark. The society which Robespierre thus dominated
was a real political power, and had for long been the instrument by
aid of which he had been able to assume precedence of his colleagues
in the Committee of Public Safety. Every resolution the club adopted
the Convention had ultimately to adopt; and every individual whom the
club proscribed, were he a minister, a general, a deputy, or any other,
went in the course of a few days to prison and the guillotine. No man
was regarded as a good patriot who was not a Jacobin, and hundreds of
persons who never entered the place had, for the sake of security,
inscribed their names as members.

♦Fall of Hébertists and Dantonists.♦

Robespierre, as his habit was before he was sure of his path, adopted
an undecided attitude between the Hébertists and the Dantonists,
blaming the extreme, whether of excess or of moderation. The Hébertists
sought to strengthen their position in the club by attacking the
Dantonists; and it was only owing to Robespierre’s protection that
Desmoulins and others who had demanded the adoption of a more clement
policy, were able to maintain their footing in the society. Finally,
Robespierre secured his end by abandoning the Dantonists as victims to
the fanaticism and cruelty of his followers, whilst he openly sought
the proscription of the Hébertists. One after another, persons who had
either professed atheism or had displayed feelings of humanity, were
deprived of membership. The club became the tool of the Committee of
Public Safety, and none but the satellites of Robespierre and Collot
breathed freely in it. The Dantonists had no support to which to look
but the feeble and disunited Mountain. No one trusted his neighbour,
and each dreaded to oppose the will of the two committees, lest he
should afterwards be abandoned to their vengeance. Although the
Hébertists appeared more formidable, the danger of their being able
to overpower their adversaries was small. They could no longer rely
for support on the forces which had been at their disposal in July and
August. After the passing of the maximum laws they had played their
last card, and had no means left by which to move the populace to take
their side. On the contrary, it had become a constant effort on the
part of the Commune to prevent the gathering together of hungry crowds
in the streets, which might lead to a perfectly genuine explosion of
popular fury directed against itself. Every vestige of free political
life had been stamped out. The general assemblies of the sections only
met twice a week, and those attending them were paid. Clubs to which
many members belonged were viewed with suspicion and discountenanced.
The great maximum law of September, fixing prices at a third above what
they were in 1790, had ruined so many persons that it was abandoned as
untenable. A new law took as a basis the real cost of each article in
the place of production, allowed a certain percentage for carriage,
ten per cent. for the wholesale, and five per cent. for the retail
dealer. The tariff for Paris, which was published in March, excited
great discontent. Of the needier supporters of the Commune many had now
acquired booty or office, and hesitated to risk their lives by taking
up the cause of Hébert against Robespierre. The Committee of Public
Safety bid for the support of the idle and hungry by two laws, the one
(February 26) ordering the sequestration of property belonging to the
enemies of the revolution, the second (March 3) promising that means
should be taken to make provision for destitute patriots out of the
sequestered property. An attempt, headed by the Cordeliers, to get up
an insurrection against the Convention and the two committees failed.
Hébert and eighteen others were arrested and condemned to death by the
revolutionary court on the usual absurd charge of seeking to destroy
the Convention and to restore monarchy (March 24). A few days after
their execution came the turn of the Dantonists. Danton, Desmoulins,
and two other deputies were arrested in the night. The Convention
abandoned them on the demand of St. Just, without a voice speaking
in their defence (March 31). Danton, forewarned, had made no effort
to save himself. Can a man, he replied when urged to fly, take his
country with him on the soles of his shoes? By the court which he had
himself taken part in instituting, he and his friends were condemned as
monarchists and traitors to the Republic. No documents were produced,
and the accused were not suffered to make their defence. ‘On such a
day,’ said Danton in prison, ‘I caused to be erected the revolutionary
court. I ask pardon of God and man.’ Shortly afterwards a new batch
of victims was brought to the scaffold, some Hébertists, others
Dantonists. Amongst them was the widow of Hébert and the young widow
of Desmoulins, with whom, as well as with her husband, Robespierre had
lived on terms of close intimacy.




CHAPTER IX.

THE FALL OF ROBESPIERRE.


♦Dictatorship of the Committee of Public Safety.♦

The members of the Committee of Public Safety now concentrated all the
powers of government in their own hands. The Mountain was crushed
with Danton, the Commune with Hébert. The deputies in mission, who
before had joined the Hébertist party, now sought to guard their heads
by pursuing whatever line of action was indicated to them by the
committee. The Commune was reconstituted and placed under the direction
of two men devoted to Robespierre--its mayor, Fleuriot-Lescot, and
its national agent, Payan. The partisans of Hébert on civil and
revolutionary committees were replaced. The system of popular election
was abandoned even in form, and all reappointments were made either
by the committee itself, or by the Convention at its dictation. The
ministries were abolished, and the ministerial departments divided
between twelve commissions, on which new men were placed.

♦Aims of Robespierre.♦

Reports of the execution of the Hébertists penetrated the prison
walls, and aroused hope that the Terror itself was to come to an end.
Such hopes rapidly proved delusive. The dictatorship of the Committee
of Public Safety, founded by terror, rested on terror alone. Collot
and Billaud had no other thought than to perpetuate their rule by
continuing the system already in force. Robespierre was equally cruel,
not, as in their case, from mere disregard of the amount of blood
shed, but because he aimed at more, and regarded the guillotine as the
most facile instrument for the attainment of his ends. He could not be
satisfied with that which satisfied Billaud and Collot. Already the
most prominent man on the committee, he sought the first place in the
Republic, and to figure before Europe as the maintainer of virtue and
the regenerator of his country. He had learned of Rousseau to regard
as utterly hateful the state of society in the midst of which he had
grown up with its division of classes and glaring contrasts between
knowledge and ignorance, indolence and toil, luxury and squalor. Had
the power been his, he would have destroyed every vestige of it by
fusing all classes into one, abolishing vice and ignorance, with the
extremes of wealth and poverty, and giving to all citizens similar
interests, habits and pleasures. This ideal, which was Rousseau’s,
was always present in Robespierre’s mind, veiling from him his own
ambition; but it was vague, and he had no definite conception of
the manner in which its realisation should be attempted. He was not
a thinker or an organiser. Rousseau had suggested education and
legislation as possible means of regeneration. To these Robespierre
added nothing but the guillotine, the principle of extermination of
opponents. All who stood in his light he proscribed one after another,
as they appeared before him--the noble, the capitalist, the merchant,
the free-trader, the atheist, the fanatic, the merciful, the moderate,
the corrupt, the extortionate, and even the neutral man, until at last
the people whose praises were constantly on his lips dwindled down in
his mind to be no more than the Robespierrists, a few hundred ignorant
and credulous but fervent supporters and admirers.

♦St. Just.♦

Behind Robespierre was St. Just, a young man a little over twenty,
fanatic, self-confident and intolerant. In thought he was more
audacious than Robespierre, and his conceptions were more definite. He
was probably the most thorough-going disciple of Rousseau in France.
Like his master, he based his conceptions of what the government of
a great state ought to be on the institutions of the petty republics
of antiquity, and of all those republics the one which he selected
for imitation was, strangely enough, that of aristocratic Sparta.
But it was the despotism of Sparta, not its aristocracy, which he
admired. By means of Spartan institutions he thought to remould the
habits and customs of his countrymen. All boys were to be brought up
together in common schools. Every man was to marry, and every man to
work. Every man was to have friends, and to make every year a public
declaration of their names in the temple of the Supreme Being. If he
committed a crime, his friends were to be banished from the Republic.
In short, by aid of laws and state institutions of this character,
St. Just believed it possible to give to the French people simple,
frugal, and industrious habits. Circumstances, he said, were of
no importance, except to men who fear death. Meanwhile, until the
necessary institutions should be established and the habits and beliefs
of his countrymen transformed, St. Just, like Robespierre, fell back
on the guillotine in order to get rid of those who stood in the way of
the accomplishment of his ideal. Until men were virtuous in his sense
of the word, the Republic could rest upon terror alone. What, asked
this young, fanatical, and unscrupulous theorist, would those have who
reject alike as principles of government virtue and terror?

Besides fanaticism and love of power, there existed a material motive
for the continuance of the Terror. Resources were secured for the
service of the State. As soon as a person was imprisoned his capital
was sequestered and his revenue confiscated. When he was condemned
to die, the capital itself was confiscated. But the promise held out
before the arrest of the Hébertists, that provision should be made
for the indigent out of sequestered property, was never carried into
effect. Further, purchasers of state lands lost their lives by scores,
and thus national property came a second time into the market as
security for the paper money. Cynical words ascribed to Barère exactly
expressed the satisfaction felt by many at these financial results of
the guillotine. ‘We coin money,’ he was reported to have said, ‘on the
Place de la Révolution.’

The result of the dictatorship of the committee and of Robespierre’s
ascendancy was, therefore, that the Terror was reduced to a system.
Those who hoped for a return to a more clement policy were grievously
disappointed. The revolutionary army of Paris was disbanded. Special
courts in the departments, with the exception of some twenty, were
suppressed, and political prisoners sent to Paris for trial. Justice,
probity, and virtue were declared to be the order of the day, and the
penalties of imprisonment and death were suspended over the heads of
those who defrauded the Republic. The bands of villains, which, under
the name of revolutionary armies, were still the curse of several
departments, were broken up and their leaders sent to the scaffold.
Encouragement was promised to trade and agriculture, and the release
ordered of artisans and labourers in country districts against whom no
definite charges had been brought. The number of executions at Paris
rose in proportion as it decreased in the departments, from 60 to 155,
and then to 354 a month. In Bordeaux, Arras, and other towns where
special courts were retained, executions were recommenced. A new court
was established by the committee at Orange, which in forty-two sittings
condemned to death 331 persons, imprisoned 98, and acquitted 159. Five
Girondist outlaws still hiding in the Gironde were hunted out. Guadet
and Barbaroux were executed at Bordeaux, the bodies of Pétion and Buzot
were found dead in a field.

♦War in La Vendée.♦

In La Vendée a war of extermination was being carried on. After the
destruction of the great Vendean army in December, the country was
quiet through exhaustion, and by the adoption of a clement policy the
insurrection might have been brought to an end. But at the Commune,
where Hébert was still in power, the idea had been entertained of
annihilating the inhabitants and of confiscating their land. Under the
command-in-chief of Turreau, a man as brutal as Collot himself, twelve
columns marched into the interior from different points, killing all
living things that came in their way, and destroying villages, farms,
crops, ovens, and corn-mills. Even towns which they did not occupy
were pillaged and burnt, and those inhabitants who had throughout
supported the Republic were required to quit the country on pain of
being themselves treated as brigands. The war flared up again on all
sides. The population of entire villages, taking their goods and stock
with them, sought refuge in their forests, whence they carried on an
incessant guerilla warfare against the enemy. The isolated republican
posts were either stormed or starved out. If the soldiers had corn they
had no means of grinding it, because all the mills had been destroyed.
Supplies from Saumur and Nantes were cut off on the way. The men fell
ill by thousands, and the reduction of the country appeared less near
completion than when Turreau’s columns first began their work of
destruction.

♦The Hague Treaty.♦

After the disastrous ending of the Rhine campaign in December 1793,
the alliance between Austria and Prussia practically came to an end.
Prussia having acquired her so-called compensation in Poland, her
generals and diplomatists were desirous of bringing the war with France
to a speedy termination. The country was poor, and without interest in
its continuation. An important consideration, however, restrained the
Government from rashly entering on a peace policy. Prussia was bound,
for the sake of her headship in North Germany, to protect the northern
States against invasion. The King, moreover, had personally a strong
disinclination to desert the coalition before the existing government
in France was overthrown. A middle path was found. Prussia declared
her readiness to leave her army on the Rhine if the allies would bear
the cost of its maintenance. The lesser States of the Empire showed
no alacrity in responding to this appeal, while Austria refused to be
a party to any arrangement for the payment of a Prussian army. After
the experience of the last campaign, Thugut did not credit Prussia
with the intention of rendering any material assistance, and foresaw
that if Austria held back, England would undertake to bear the burden.
The ministers of George III. were making strenuous efforts to hold
the coalition together. They were intent on extending the colonial
empire of England, and while France was engaged in hostilities with
half the continent, it was impossible for her to defend her colonies.
Accordingly, a treaty was signed at the Hague between Malmesbury on the
English side and Haugwitz on the Prussian, by which England undertook,
together with Holland, to supply Prussia with a monthly sum for the
maintenance of 62,000 men (April 19).

♦Insurrection in Poland.♦

This treaty was hardly signed when news reached Berlin that the
Poles were in arms. The Polish Diet had been forced, at the time of
the second partition, not merely to relinquish provinces to Russia
and Prussia, but to sign a treaty which placed in subjection to
Russia that portion of the country still left nominally independent.
King Stanislaus was the tool of Catherine, and his Government was
supported by 40,000 Russians. Discontent permeated the country. The
inhabitants of the towns regretted the reformed constitution of May
1791, overthrown by the influence of Catherine (p. 98). The lesser
nobility was bitterly hostile to Russian domination; the army, still
30,000 strong, resented its degradation. The standard of revolt was
now raised on all sides. At Warsaw the populace, uniting with insurgent
Polish regiments, drove out the Russian garrison with heavy loss
of life (April 18). Yet, in spite of the enthusiasm with which the
insurrection was begun, and the patriotic spirit animating its leaders,
Potocki and Kosciusko, there was but little probability of final
success. The Poles, torn by internal faction, were unable to present
a united front against the common foe. Many of the upper nobility
were in Russian pay. Three powerful neighbours--Austria, Prussia,
and Russia--did but need a pretext for the accomplishment of a final
partition and the effacement of Poland from the map. Frederick William,
with 50,000 troops, at once marched into the country, and, joining with
the Russians, laid siege to Warsaw (July 13).

These events reacted sensibly on military operations in the West.
England and Prussia had had different objects in view when they entered
into the treaty of the Hague. The English Government expected that the
Prussian army would fight in Belgium; the King of Prussia intended
that it should merely secure the Empire against invasion by blocking
the passage of the Rhine. The Polish insurrection had heightened the
aversion of Prussian generals and ministers to the French war. They
refused to allow their army to leave the Rhine, urging the forcible
plea that the Empire would be exposed to invasion. They further made
the quarrel with England which broke out on this ground an excuse for
taking no active steps whatever to attack the enemy. In May, indeed,
their army had advanced in the direction of Alsace, and had driven the
French from Kaiserslautern and the neighbouring positions. But from
that time it remained inactive, and thus the French were able to send
large additional forces to combat the allies in Belgium.

♦Campaign in Belgium.♦

The Committee of Public Safety had abetted the insurrection of the
Poles, and had sought, though without result, to stir up war on the
Danube as well as on the Vistula, by subsidising the Porte to attack
Austria. Carnot, aware of the differences existing between Austria and
Prussia, arranged the campaign on the supposition that no vigorous
enemy would be found on the Rhine. He designed to confine offensive
operations to Belgium, where he hoped to overpower the allies by
superiority of numbers, and to threaten Holland and England with
invasion. The seat of war may be roughly divided into three divisions:
first, the country between the rivers Meuse and Sambre; secondly, the
country between the Sambre and the Scheldt; and thirdly, Flanders
between the Scheldt and the sea. This long line of territory the
allies had to defend with 160,000 against 300,000 men. Their generals
had no superior talents enabling them to contend with success against
such odds as these. The Duke of York, who had again been appointed to
command the English troops, because he was the son of George III.,
had neither military knowledge nor capacity. Coburg followed without
reserve the strategy of the day, which was to put an opposing body of
men opposite each body of the enemy, and to defend every locality which
had once been occupied. The idea of gaining victory by bringing an
overpowering force to bear upon a weak point of the enemy’s line did
not suggest itself to him or his staff, and his plan of operations was
confined to maintaining his positions and capturing French fortresses.

The allies were still in occupation of the three
fortresses--Valenciennes, Condé, and Le Quesnoi--which they had taken
in the preceding year. Between Valenciennes and Bavay was the Austrian
centre; their right wing occupied Flanders, their left guarded the
line of the Sambre. Carnot’s plan was to make use of his numerical
superiority, first to shatter the enemy’s wings, and then, attacking
his centre both in front and in flank, to drive him out of Belgium. The
Austrians began hostilities by laying siege to Landrecies. Pichegru,
with 100,000 men, advanced into Flanders, and defeated the allied right
wing at Turcoing (April 18). He next laid siege to Ypres, and the
allies, after an ineffectual attempt to relieve the town, retreated
behind the Scheldt. On the Sambre the allied forces were equal in
number to the French, both armies being about 50,000 strong; and here,
while Pichegru was conquering Flanders, an effectual stand was made
against the repeated efforts of the French generals to get a footing on
the north side of the river and to invest Charleroi. But the continued
inactivity of the Prussians enabled Carnot to send 50,000 men from the
Rhine to the Sambre, so as to outnumber the allies on this side also.
Charleroi was invested, and capitulated (June 25). The following day
Coburg, who had arrived from the centre with reinforcements and was
unaware of the surrender, attacked the French positions at Fleurus
and the neighbouring villages (June 26). The battle lasted the whole
day, without decided result; and Coburg, on hearing that Charleroi had
already surrendered, did not renew the struggle. The evacuation of
Belgium followed these disasters. Coburg withdrew behind the Meuse,
and the Duke of York, with the English and Dutch troops, retreated
into Brabant. The French laid siege to those fortresses in France and
Flanders in which the allies had left garrisons.

After the allies had been thus driven from Belgium, all danger of
invasion was over, and men would be more ready to call in question
the authority of a Government which it might soon be possible to
resist without rendering France weak in the presence of a dangerous
enemy. Robespierre had ever been keenly alive to the possibility of
the Government being overthrown by some victorious general, and he
followed the successes of the armies with an excessively jealous eye.
At this time, although he occupied the first place in the Committee of
Public Safety, he was not content with his position, but was seeking
to draw the reins of government more closely into his own grasp, and
to make himself independent of his colleagues. They had no means of
combating him. The Commune and the Jacobins, the two main wheels by
which the revolutionary Government was kept in action, were now under
his control. He established a special police office, which encroached
on the functions of the Committee of General Security. He sent special
agents into the departments as spies on the conduct of the deputies in
mission, who were to make private reports to himself. Above all, he
sought to obtain a basis to his authority wanting to his rivals, by
asserting the necessity of laying the foundations of morality and duty
in spiritual beliefs. In thus acting, if Robespierre was instigated by
personal ambition, he was instigated also by the desire to put into
practice, at whatever risk to himself, the principles which he had
learned of Rousseau. ♦The worship of the Supreme Being.♦ Under his
inspiration the Convention decreed that the French people recognised
a Supreme Being and the immortality of the soul. A new worship was
inaugurated by a festival in honour of the Supreme Being, held in the
Champ de Mars. The Convention took part in the ceremonies. Robespierre,
at the time president, walked first, dressed in a sky-blue coat, and
holding in his hand a large bunch of flowers, fruits, and corn. Arrived
at the Champ de Mars he set fire to figures representing atheism and
egoism. As they burnt, the figure of wisdom rose out of the flames.
Hymns were sung, and the ground strewn with flowers by children (June
8).

♦Revolutionary Court reorganised.♦

For a moment expectation prevailed that this recognition of a Supreme
Being would be followed by a revival of sentiments of humanity.
The case proved otherwise. The festival was barely over when the
Convention, in accordance with a project drawn up by Robespierre,
reorganised the revolutionary court (June 10). The calling of
witnesses, hearing of counsel, and other forms long since only
partially observed, were formally abolished. The prisoners were brought
before the court in batches of twenty, thirty, or fifty at a time.
A short vaguely-worded charge was read. The president asked each
person his or her name and one or two questions. No evidence on either
side was heard. The jury condemned the accused in a body. To make as
quick as possible the work of judicial massacre, Robespierre’s agents
invented a story that the prisoners were conspiring to save themselves
by assassinating the members of the Convention, and on this charge
persons belonging to every condition of life, brought together from all
quarters of France, were sent pell mell to the scaffold. From the time
of its institution in March 1793 to the passing of this law on June 10,
1794, the court had condemned to death 1,259 persons; after June 18, in
less than seven weeks, it caused the execution of 1,368 persons.

The reorganisation of this court, which Robespierre, by the
reappointment of judges and jurymen, endeavoured to convert into his
special instrument, spread alarm on every side. At this time, indeed,
terror prevailed in official circles to an extent that it would be
difficult to exaggerate. There was no opposition to the Government.
In the Jacobins, the Commune, the Convention, the Sections, no
propositions were made that did not accord with the views of the two
committees. In the Commune, the National agent Payan travestied the
language of Robespierre, as Robespierre in the Convention the language
of Rousseau. In the departments party strife was suppressed as it was
in Paris. The clubs, few of which now numbered more than forty or fifty
members, followed without a will of their own the cue given them from
Paris. All over the country festivals in honour of the Supreme Being
took the place of festivals in honour of Reason. Although Robespierre
proclaimed principles of religious toleration, he neither desired nor
suffered their observance. It is possible that he would never have
ventured, as Hébert had done, to proscribe the Catholic worship, but
the work having been done for him, circumstances would not permit him
to seek supporters by again allowing the celebration of those rites
which still had the affection of the nation. He was at the head of a
Government which could not retrace a step without extreme danger of
weakening its own authority, and it was only by continuing the system
already in force that it was possible for him, as he could not fail
to be aware, to carry his social ideas into practice. Hence the feast
of the Supreme Being, in place of leading to a revival of principles
of humanity, had been followed by a sharpening of the Terror. On the
pretext of maintaining public order, the Catholic worship remained
prohibited. The tyranny weighed down the oppressors along with the
oppressed. Men were imprisoned and sent to the scaffold indifferently
for acts of mercy, knavery, or extravagance. The denouncer of to-day
was the denounced of to-morrow. Municipalities and administrative
bodies trembled before clubs and revolutionary committees; these, in
turn, before deputies in mission; deputies in mission before the two
committees; and the members of the committees before one another.
However high a man’s place in the revolutionary hierarchy, he could not
shelter his best friends or nearest relatives without risking his own
head.

♦Insurrection of Thermidor 10.♦

Violent discords broke out within the Committee of Public Safety.
Robespierre’s efforts to raise himself excited the indignation of his
colleagues; for the more powerful he became, the more insecure was the
tenure on which their own lives rested. On the other hand, Robespierre
was nervous, envious, and suspicious, and the higher he rose the more
eager he became to shed the blood of his enemies, and of those who
stood in the way of his rising higher still. The Montagnards hated him.
Those who had walked behind him at the feast of the Supreme Being had
not been able to restrain themselves from uttering insulting words.
‘Formerly he was master’, one was heard to say, ‘and now he must be God
as well.’ Some, aware that they were objects of his special enmity,
were plotting obscurely against him. Of the twelve members of the
Committee of General Security all but two were his enemies. Supported
by Couthon and St. Just, Robespierre proposed in the Committee of
Public Safety a proscription of several members of the Mountain and of
the Committee of General Security. Billaud and Collot opposed. Consent
would have been suicidal, since they were called on to sacrifice their
own supporters. The cowardly Barère hesitated which side to join. One
member of the Committee of Public Safety had been guillotined with the
Dantonists. The remaining five, though it was not their desire to shed
blood, were accustomed to give their signatures without questioning on
the demand of the governing members, and thus incurred responsibility
for all that took place. They had more in common with Robespierre than
with Collot, since they too cared for order as well as power; but,
while submitting to his ascendancy, they loathed and despised him.
Carnot, who was one of these, and whose success at the head of the war
administration made Robespierre envious, and who could not conceal his
antipathy for Robespierre and St. Just, was marked out for destruction.
The threatened members of the Committee of General Security, afraid
that Billaud and Collot would sacrifice them sooner than come to an
open breach with Robespierre, sought to defend themselves by combining
with the threatened Montagnards. Within the Committee of Public Safety
efforts were made to come to an understanding, but without success.
Robespierre, aware that his enemies were conspiring against him,
determined to strike first, and to secure dictatorship for himself by
replacing his opponents on the two committees by partisans of his own.
There appeared to be little doubt of the result. The Convention had
less reason to support Billaud and Collot than himself. They had been
fully as sanguinary as he; and when Collot in the Convention had once
proposed to send to the scaffold seventy-three deputies of the right
who had been imprisoned for signing protests against the ejection of
the Girondists, he had opposed and saved their lives. In case of a
struggle he had material force at his command, his opponents none.
The Jacobins and the Commune were both his; the national guard, now
called the armed force, was under the command of Henriot, a partisan
of his own. The cannoniers of each section formed a paid force, of
which every man had been selected by the Commune. Robespierre opened
the attack by a long speech in the Convention, in which he complained
of the traitors who spread calumnies against himself (July 26). He
threatened many, but named none. It was a fatal mistake, for each man
in the Convention fancied it possible that his name might be on the
list of proscription. Despair gave courage to the plotters to struggle
for their lives. They belonged to all parties. Some were Hébertists,
others Dantonists, others independent Montagnards. Most were inferior
in character to the man who attacked them. Amongst them were members of
the Committee of General Security, such as the cowardly and ferocious
Vadier and Amar, and the most brutal members of the Convention--Fouché,
who had slaughtered at Lyons, Tallien at Bordeaux, Fréron at
Marseilles, Carrier at Nantes.

When, on the following day, Thermidor 10 (July 27), St. Just ascended
the tribune, he was interrupted almost before he opened his lips.
Shouts were raised of ‘Down, down with the tyrant!’ as Robespierre,
gesticulating and menacing, strove to make himself heard above the
din. The President, a Dantonist, Thuriot, incessantly rang his bell.
The struggle went on for hours. ‘President of assassins’, cried
Robespierre, sinking under exhaustion, ‘for the last time I demand the
right of speech.’ He appealed to the Plain, the members who had been
mere tools in the hands of the strongest party, and who had been mute
against the Mountain since the ejection of the Girondists. But the
Plain, seeing that he was no longer powerful, joined his enemies; and
when it was proposed to arrest himself, his brother, Couthon, and St.
Just, its members rose in a body to confirm the condemnation of the man
before whom they had so long trembled.

All four were conducted to prison. Yet victory so far was merely a
parliamentary one. An attempt to arrest Henriot gave warning of danger
to Robespierre’s partisans outside the Convention. The Municipality
summoned the armed force to the Hôtel de Ville, and sent agents into
the sections to stir up an insurrection. The two Robespierres, St.
Just, and Couthon were released from prison and taken to the Hôtel
de Ville. But excess of tyranny had left isolated those by whom it
had been exercised. The Robespierrists were ardent in the defence
of their leader; but they were but a mere handful, even amidst the
Terrorists. The members of the civil and revolutionary committees,
wishing to secure their heads, waited to declare for the Commune
until they had assurance that the Commune would win. The Convention
outlawed Henriot, Robespierre, and his companions, and sent deputies
into the sections to gain their support. The few who still attended
the assemblies of the sections were eager to fling off the yoke with
which they were oppressed. When they understood that the quarrel was
between Robespierre and the Convention, they sent messengers to recall
the battalions of national guards already at the Hôtel de Ville. The
deputy Barras, appointed by the Convention to command in Henriot’s
place, invested, about two at night, the nearly-deserted building
without encountering opposition. Those within were surprised where
they sat. Robespierre, with his jaw painfully fractured by a pistol
shot--it is uncertain whether the wound was inflicted by his own or by
the hand of another--was taken to the Committee of Public Safety, and
left lying upon a table, exposed to the taunts of every gazer. Being
already outlawed, Robespierre, his brother, Couthon, and St. Just, with
eighteen other persons, were executed as soon as day arrived, without
form of trial. During the two following days more than eighty of
Robespierre’s followers, including a large number of the members of the
Commune, were sent to the scaffold.




CHAPTER X.

FALL OF THE MONTAGNARDS.


♦Reaction.♦

It is calculated that during the fourteen months which had elapsed
since the ejection of the Girondists, about 16,000 persons had perished
throughout France by the sentence of revolutionary courts. With the
proscription of the Robespierrists the Terror as a system of government
came to an end. Collot and Billaud, in overthrowing Robespierre, had
deprived themselves of the two main engines by which the machinery of
the Terror had been kept in motion. After the execution of its members
the Commune had been broken up, and the Jacobins were enfeebled. The
Mountain at once asserted its independence of the two committees; the
Plain, in turn, asserted its independence of the Mountain. From this
time the committees were renewed by a fourth every month, and the
outgoing members rendered incapable of immediate re-election. Within a
few weeks all the men who conducted the Government during the Terror
had resigned or had been deprived of office.

The fall of Robespierre and of the committees was felt as much in
Paris as it was in the Convention. No sooner did the incessant action
of the guillotine cease than the revolutionary authorities fell into
contempt, and the revolutionary laws, which the Terror alone had
sustained, ceased to be observed. There was again freedom of action, of
speech, and of the press. Hundreds and thousands of young men collected
in the sections and public places, declaring war on the Jacobins,
and demanding the release of friends and relations, the abolition
of revolutionary committees, the imprisonment and trial of their
late oppressors. They belonged to all ranks of life, but were mostly
skilled artisans, clerks in offices, shopmen, tradesmen, and sons of
nobles and capitalists. As in 1789, the agitation had its centre in
the Palais Royal, and, as then, found its leaders in young authors
and journalists. In the departments the reaction proceeded with equal
rapidity. Nowhere was any attempt made to resist the new revolution.
The names of Robespierre and Couthon were given over to execration by
the same men who a week before had made a show of delight in honouring
them. The petty tyrant of yesterday, ejected from office, went to join
his victims in prison; and, as in Paris, all classes of the population
speedily took advantage of the relaxation of the Terror to slip their
necks free of the yoke of the revolutionary laws.

Upon the destruction of the dictatorship of the committees, supreme
power reverted to the Convention. That body, however, had as little
coherence now as it had had in the first months of its existence. The
restitution of its liberty split it into numerous sections. It was
torn by violent party spirit, and had no determinate policy or aim,
but drifted onwards, following not directing the course of events.
All agreed in condemnation of Robespierre, but in that alone. The
Montagnards were divided amongst themselves. Only a small minority
was prepared to maintain in its entirety the Terror as a system
of government--Billaud and Collot and their companions in office,
who feared for their own lives. A few, such as Romme and Soubrany,
resolutely opposed social and economical changes which would, in the
end, lead to the return of the middle-class to power. Others again,
as the financier Cambon and the Dantonist Thuriot, struggled to
maintain the ascendancy of the Mountain over the Plain, but declared
war on Billaud and Collot, who, following in the course of Hébert and
Robespierre, sought, by aid of clubs and revolutionary committees,
to tyrannise over the Mountain. The Thermidorians, so-called from the
name of the revolutionary month in which the new revolution had been
effected, Tallien, Fréron, and others of the men who had conspired to
destroy Robespierre, took up a position between the Mountain and the
Plain, and for the time possessed the leadership of the Convention;
but they had no policy except that of yielding sufficiently to public
opinion to maintain ascendancy, and at the same time of holding in
check the reaction so as to prevent its reaching themselves. One after
another demands made by the anti-Terrorist press and by gatherings
in the Palais Royal were complied with. The Jacobin Club, the resort
of Collot, Billaud, and their partisans, was closed (November 12).
The Revolutionary Committees were reduced in number and shorn of
their powers. Thousands of prisoners were released and their property
restored to them. Throughout the country new men were placed in office,
while members of revolutionary committees and other inferior tools of
the Terror were imprisoned by hundreds. A trial going on before the
Revolutionary Court at Paris revealed in all their horrible details the
massacres committed at Nantes, and raised a cry for vengeance against
Carrier. Abandoned by the Thermidorians and almost the entire Mountain,
Carrier was sent before the court for trial, and thence in his turn to
the scaffold (December). Billaud, Collot, and other marked Terrorists,
already denounced in the Convention by Danton’s friends, felt that
danger was every day drawing nearer to themselves. Their fate was to
all appearance sealed by the readmission to the Convention (December 8)
of seventy-three deputies of the right, imprisoned in 1793 for signing
protests against the expulsion of the Girondists.

By the return of these deputies the complexion of the Assembly was
entirely altered. It was they who had formed the phalanx which had
supported the Gironde, and they now sought to undo the work of the
Convention since the insurrection by which their party had been
overwhelmed. They demanded that confiscated property should be restored
to the relatives of persons condemned by the revolutionary courts; that
emigrants who had fled in consequence of Terrorist persecutions should
be allowed to return; that those deputies proscribed on June 2, 1793,
who yet survived, should be recalled to their seats. The Mountain,
as a body, violently opposed even the discussion of such questions.
The Thermidorians split into two divisions. Some in alarm rejoined
the Mountain; while others, headed by Tallien and Fréron, sought
their safety by coalescing with the returned members of the right.
A committee was appointed to report on accusations brought against
Collot, Billaud, Barère, and Vadier (December 27, 1794). In a few weeks
the survivors of the proscribed deputies entered the Convention amidst
applause (March 8, 1795), and it was clear that, in spite of every
effort made by the left to delay a decision, the four accused men would
be called upon to account for the tyranny that had been exercised by
the two committees unless the Convention were overpowered by force.

♦The revolt of Germinal 12.♦

There was at this time great misery prevalent in Paris, and imminent
peril of insurrection. After Robespierre’s fall, maximum prices were
no longer observed, and assignats were only accepted in payment
of goods at their real value compared with coin. The result was a
rapid rise in prices, so that in December prices were double what
they had been in July, and were continuing to rise in proportion as
assignats decreased in value. The policy pursued by the Convention
tended of necessity to hasten the depreciation of the paper money.
Girondists, Thermidorians, and a portion of the Mountain concurred in
denouncing the economic system imposed on the Convention by Hébert and
Robespierre. The system of requisitions was gradually abandoned, the
armies were again supplied by contract, and the maximum laws, already
a dead letter, were repealed (December 24). The abolition of maximum
prices and requisitions increased the already lavish expenditure of the
Government, which, to meet the deficit in its revenues, had no resource
but to create more assignats, and the faster these were issued the
faster they fell in value and the higher prices rose. In July 1794,
they had been worth 34 per cent. of their nominal value. In December
they were worth 22 per cent., and in May 1795, they were worth only 7
per cent. Want of food was the more acutely felt owing to the winter
having been one of great severity. The Seine was covered for weeks with
ice, and wood and coal were, like other articles, dear and scarce. All
persons living on fixed incomes suffered intensely. Even those who
lived on wages were seriously affected. Wages had indeed risen, but not
in proportion to prices. Starvation prices prevailed. Workmen earned
from five to eleven shillings a day in paper money, while a multitude
of State officials, pensioners and creditors, received no more than
from three to six shillings a day. Yet at this time a pound of bread
cost eight shillings, of rice thirteen, of sugar seventeen, and other
articles were all proportionately dear. It is literally true that more
than half the population of Paris was only kept alive by occasional
distributions of meat and other articles at low prices, and the daily
distribution of bread at three-halfpence a pound. In February, however,
this source of relief threatened to fail. Farmers preferred to send
their corn anywhere else than to Paris, where only paper money was
to be had. It was only with extreme difficulty that the Government,
which since the annihilation of the Commune had supplied Paris with
bread, performed its task. The rations fell from one pound to half a
pound, and soon to a few ounces per head. Numerous deaths took place,
the result of destitution or actual starvation. An insurrection,
however, though constantly threatened, for weeks failed to break out.
One cause was that the people had grown hopeless of improving their
condition by insurrection; another, that those journalists, clerks,
and others, who at the opening of the revolution had incited popular
movements, were now, although suffering themselves, found on the
other side, and were prepared to fight in defence of the Convention,
which they none the less detested, sooner than endure a revival of
the Terror. Material suffering offered, however, a ready handle for
Terrorist agitators; and as the peril of insurrection increased, so
too, within the Convention, did the violence of party strife. The
Mountain, threatened with proscription, sought to turn the position of
the right and to obtain credit outside, by demanding the immediate end
of provisional government and the putting in force of the democratic
constitution promulgated by the Convention in 1793, after the ejection
of the Girondists. On April 1, or Germinal 12, bread riots, begun by
women, broke out in every section. Bands collected and forced their
way into the Convention, shouting for bread, but offering no violence
to the deputies. Occasionally the demand was made for the release of
imprisoned patriots and for the Constitution of 1793. The crowd was
already dispersing when forces arrived from the sections and cleared
the House. The insurrection was a spontaneous rising for bread, without
method or combination. The Terrorists had sought, but vainly, to obtain
direction of it. Had they succeeded, the Mountain would have had an
opportunity of proscribing the right. Their failure gave the right
the opportunity of proscribing the left. The transportation to Cayenne
of Billaud, Collot, Barère, and Vadier was decreed, and the arrest of
fifteen other Montagnards, accused without proof, in several cases
without probability, of having been accomplices of the insurgents. The
Thermidorians showed themselves more vindictive than the Girondists,
and it was on the proposition of Tallien that amongst those proscribed
were included Thuriot and Cambon, men whose hands, compared with his
own, were clear of blood.

The insurrection of Germinal 12 gave increased strength to the party
of reaction. The Convention, in dread of the Terrorists, was compelled
to look to it for support. The bands of young men who assembled in the
Palais Royal, called ‘Fréron’s army,’ often rendered useful service by
clearing the Tuileries Gardens of discontented and threatening groups.
Already the dress, language, and manners in vogue during the Terror
were laid aside. Red caps gave place to hats. The habit of addressing
strangers by the familiar ‘thou,’ and the use of the word ‘citizen,’
were dropped in drawing-rooms. No Jacobin could set foot in the Palais
Royal without experiencing insults and blows. Busts of Marat, which had
been set up in every public building, were pulled down and broken, and
both theatres and streets became the scene of incessant riots.

♦Reaction in the Departments.♦

In the departments famine, disorder, and crime prevailed, as well as
in Paris. In all towns a large portion of the population was kept
alive by daily distributions of bread. The country was exhausted
by the war burdens laid on it. Requisitions for the armies had
drained one department after another of horses, carts, corn, and
men. Nevertheless, destitution was not so great in rural districts
as in towns. Corn growers, since the fall of Robespierre, had made
large profits, while every peasant sold his wine or other produce at
prices as high in proportion as the price of bread. From the first
the reaction proceeded in the departments with a more rapid step and
in bolder form than in Paris which was subjected to the restraining
influences exercised by the presence of the Convention. Everywhere,
except in Paris, municipal bodies had, as early as in January, suffered
churches to be reopened and Mass again to be celebrated. Without
the Terror it was as impossible to maintain the proscription of the
Catholic worship as it was to enforce the observance of maximum laws.
A minority in the Convention, composed of Catholics and Liberals,
desired to carry into practice those principles of religious toleration
which the Convention in theory had always maintained and had publicly
announced in opposition to Hébert, but which for so many months it had
neglected to put in practice. The majority, whatever their repugnance
to a revival of sacerdotal influence, recognised the hopelessness of
resisting the popular movement. Since the beginning of the Revolution
the idea of the separation of Church and State had gained ground. The
constitutional clergy desired to be allowed to reorganise the Church
without any interference by the State. The mass of deputies were
unwilling to recognise the Catholic as the national religion, lest
by so doing they should enable the Church the more readily to regain
ascendency. A compromise was arrived at. The Convention declared that
the public exercise of all forms of worship was permissible, but that
henceforth the State would provide neither buildings nor funds for
any religious body. Small pensions, however, varying from 35_l._ to
52_l._, which under the Terror had been accorded to bishops and priests
who had resigned their offices were granted to the whole body of the
Constitutional clergy. Further, various restrictions were laid on the
public exercise of religion. No ceremonies might be performed outside
the building set apart for worship, whether in streets, burial grounds,
hospitals, or prisons. Ecclesiastics might not wear a special dress out
of doors, and even the ringing of bells was prohibited (February 22).

♦The White Terror.♦

Though their position was far more precarious--for none of the
laws against them had been repealed--nonjurors, as well as the
Constitutional clergy, resumed their functions. With the connivance of
municipal bodies they had come in numbers out of their hiding-places,
or had returned to France from abroad. In the departments of the
south-east, where the Royalists had always possessed a strong
following, emigrants of all descriptions readily made their way back;
and here the opponents of the Republic, instigated by a desire for
vengeance or merely by party spirit, commenced a reaction stained
by crimes as atrocious as any committed during the course of the
revolution. Young men belonging to the upper and middle classes were
organised in bands bearing the name of companies of Jesus and companies
of the Sun, and first at Lyons, then at Aix, Toulon, Marseilles, and
other towns, they broke into the prisons and murdered their inmates
without distinction of age or sex. Besides the Terrorist and the
Jacobin, neither the Republican nor the purchaser of State lands was
safe from their knives; and in the country numerous isolated murders
were committed. This lawless and brutal movement, called the White
Terror in distinction to the Red Terror preceding Thermidor 9, was
suffered for weeks to run its course unchecked, and counted its victims
by many hundreds, spreading over the whole of Provence, besides the
departments of Rhône, Gard, Loire, Ain, and Jura.

♦Insurrection of Prairial.♦

Neither deputies in mission nor administrative officers attempted
to arrest the assassins or to bring them to justice. The Convention
expressed indignation, but took no active measures for the maintenance
of law and order. In fact, men still lived in incessant fear of a
revival of the Terror, and hence for the time they regarded with
indifference the reaction in the south, in spite of its Royalist
tendencies. After the insurrection of Germinal, the condition of the
people at Paris remained unchanged. The rations of bread on occasions
fell as low as a couple of ounces. Jacobins and other agents of
the Terror did their utmost to direct the ever-swelling flood of
discontent against the Convention. On May 20, or Prairial 1, a second
insurrection broke out, fiercer, more extended, and more persistent
than the preceding one. The insurgents, men and women, broke into
the Convention clamouring for bread, and insulting and reproaching
the deputies without distinction of party. With cries for bread were
joined cries for the Constitution of 1793, but the crowd was without
leaders, and barely knew its own ends, still less by what means to
seek their realisation. On the arrival of battalions of the national
guard in support of the Convention, a general combat took place
within the Chamber, in which the defenders of the Convention were at
first worsted. A deputy, Feraud, who sought to protect the President,
Boissy d’Anglas, from insult, was wounded by the populace and dragged
outside, his head cut off and paraded on a pike through the streets.
Many deputies fled. A few Montagnards, threatened by the mob and urged
by the frightened deputies on the right, put to the vote the demands
raised by voices in the crowd, such as the release of imprisoned
patriots and the reconstitution of the Committees of Government. The
insurgents, who were now appeased, began to disperse, when more
national guards arrived and drove away those who still remained.
Victory, however, was not secured. The Faubourg St. Antoine remained
in insurrection, and the next day directed the mouths of its cannon
upon the Tuileries. The Convention only secured its safety by promising
to provide bread, and to put in force the Constitution of 1793. In
the meantime, however, 4,000 troops of the line were being brought to
Paris. These, with a selected force of national guards, surrounded
the insurgent faubourg. To a population supported upon rations, there
was no choice between yielding or starving. They yielded, giving up
arms and cannon (May 23). The Convention made use of its triumph to
destroy the Mountain and to secure itself against a repetition of the
late scenes. A decree for the disarmament of agents of the Terror
furnished a pretext for taking pikes and guns from the hands of the
people, and the national guard was reorganised so as to exclude from
active service the poorer sections of the population. Many hundred
persons were imprisoned. The revolutionary court had already been
dissolved. For the sake of summary procedure a military commission was
instituted, which sat for more than two months, and condemned to death
between thirty and forty persons, and as many more to imprisonment or
transportation. The proscription of the Mountain comprised in all more
than sixty deputies. Of those who formed the Committees of Government
during the Terror, Carnot and one other alone were spared. ‘Carnot,’
said a voice, when his arrest was proposed, ‘has organised victory.’
Many of the proscribed effected their escape. A few committed suicide.
The remainder suffered transportation or death.




CHAPTER XI.

THE TREATY OF BASEL AND THE CONSTITUTION OF 1795.


♦Conquest of Holland.♦

While internally France was a prey to bankruptcy, hunger, crime, and
civil strife, the triumph of her armies continued uninterruptedly.
After the evacuation of Belgium by the English and Austrians, in June
1794, the Prussians, in danger of being outnumbered and isolated,
abandoned their positions round Kaiserslautern and fell back on the
Rhine. The Austrians retreated to the same river, while the English
and Hanoverians, under the Duke of York’s command, withdrew behind the
Lower Meuse. One French army invested the great fortress of Mainz,
while Pichegru pressed on into North Brabant. Little defence was made.
The Dutch army was small, and there was no probability that the country
would rise. Not only had the French numerous and influential partisans
amongst the political opponents of the House of Orange, but the
peasantry, alienated by the brutal and plundering habits of the allied
troops, were eager to be relieved of their presence. The invaders were,
however, not above 46,000 strong, and short of clothes, arms, and
munition for besieging purposes; so that the English army of 30,000
men, competently led, would have been sufficiently strong to hold them
in check. But the Duke was a bad general, and his men were demoralised
by their retreat. He remained helplessly on the north side of the
Meuse, while the fortresses in North Brabant fell one after another.
The French, after effecting the passage of the Meuse by a bridge of
boats (October 19), found their further advance barred by the mouths of
the Rhine, the broad and rapid rivers Waal and Leck. Here, however,
the inclement winter came to their aid. By the middle of January
1795, the rivers were covered with ice which bore the passage of men,
horses, and cannon. The English forces retreated eastwards, leaving
the French masters of the country. The Stadtholder fled to England. A
revolutionary movement broke out in the principal towns, and the French
were everywhere accepted as friends. The fleet, which was frozen up
in the harbours of the Texel, was prevailed on to capitulate by an
attack of a body of French cavalry advancing on the ice. The English
and Hanoverians finally abandoned the country, and the conquerors left
the seven united provinces in possession of nominal independence and
their federal form of government; but forced them to conclude a treaty
of alliance which reduced the country to the position of a satellite of
France, and put its resources at her disposition (May 12).

♦Foreign policy of the Convention.♦

The brilliant achievements of her armies had revived in France the old
passion for military glory and conquest which had been distinctive of
the reign of Louis XIV. The war, begun with the object of securing
France against invasion, was being pursued with the object of extending
the frontiers of the Republic. The national triumph over foreign foes
became the one point in respect to which there existed a strong bond of
sympathy between France and the Convention. Girondists, Thermidorians,
and Montagnards, if only for the sake of winning popularity, vied with
each other in seeking to gratify the national pride and ambition;
and the point of view of the Republican Government was practically
identical with that of the Emperor, or of the King of Prussia,
namely, that there must be no laying down of arms without acquisition
of territory. A small minority of deputies would have restored the
conquered Rhine lands to the Empire and constituted Belgium into an
independent republic, if they could on such terms have obtained a
European peace. But the majority, including all the more prominent men
who by turns sat on the Committee of Public Safety and directed foreign
affairs, to whatever party they belonged--Boissy d’Anglas, Thibaudeau,
Merlin of Thionville, Merlin of Douai, Carnot, Siéyès, Cambacérès,
Rewbel, Larevellière-Lépeaux--aspired to incorporate Belgium with
France, and on the side of the Empire to extend the frontier, if not to
the Rhine, at least to the Meuse.

If, however, the country, proud of its conquests, desired to retain
them, its exhaustion made it eager for the conclusion of hostilities,
and the necessity of at least confining the field of war to narrower
limits was recognised even by those deputies whose policy was most
aggressive and ambitious. As in France, so also in Spain, in Prussia,
throughout Italy, the Austrian dominions, and the Empire, a general
desire for peace existed. In none of these countries had there been
from the first any national enthusiasm for the war, while the large
expectations with which governments began hostilities had been blown
to the winds. There was no longer any thought of restoring the Bourbon
monarchy in France, nor probability of making conquests at her expense;
and, in fact, those continental Princes alone cared to continue the
struggle who looked forward to effecting, at the cost of third and
weaker States, the enlargement of their own dominions.

♦Policy of Thugut.♦

As yet Austria had, during the course of the war, made no territorial
acquisition. In the second division of Poland, Russia and Prussia
alone shared. The chancellor, Thugut, the director of Austrian foreign
policy, and the one statesman of mark whom Austria possessed, was
a continuator of the schemes formerly entertained by Joseph II.
for the extension and consolidation of the Austrian dominions. He
possessed the entire confidence of his master, Francis II., but the
position which he held was isolated, and his authority limited. Had
he attempted to draw upon the resources of the various kingdoms and
duchies subject to the Emperor, as the Convention had drawn upon the
resources of France, he would have incited disturbance and revolt on
every side. The administration, more especially of the war department,
was inefficient and lax, and the public service suffered in consequence
of the negligence or wilfulness of officials high in place. Thugut was
the son of a poor boatbuilder, and the court nobility never forgot his
origin, and thwarted him on every opportunity. Thugut, however, proud,
despotic, and ambitious, would not be diverted from his course by
misfortune in war, by the factious opposition of a court nobility, or
by the ill-will and discontent of subject populations. On the retention
of Belgium he laid no great stress. Belgium lay far from the seat of
government, and though wealthy, its wealth was not at the arbitrary
disposition of the Emperor. If, however, he were to resign Belgium,
Thugut required an ample equivalent for the loss elsewhere, and before
bringing to a close the French war, designed further to acquire an
indemnity equal to that which Prussia had obtained by the second
partition of Poland. There were three courses by which Thugut saw
possible opportunities of making acquisitions. He might make Austrian
influence supreme in Germany by the annexation of Bavaria, or he might
extend the Austrian dominions in Italy, or, again, he might acquire new
possessions in the East, at the expense of Poland and of the Porte.
For the time he had no thought of entering into negotiation with the
Republic, because he expected best to gain his ends by making common
cause with England and Russia, which two Powers were both urgent for
the continuation of the war.

♦Alliances between Austria and Russia.♦

The third partition of Poland was at this time at the point of
accomplishment. The insurrection which broke out in the Spring of 1794
had been suppressed by Russian troops, under the command of Suwaroff,
the famous conqueror of the Crimea. The Poles had received two crushing
defeats. The national hero, Kosciusko, had been wounded and made
prisoner. Warsaw, the capital, had surrendered (November 8) after the
storm of its suburb Praga, when, for a long time, no quarter was given,
and, as it was said, 10,000 persons, including many non-combatants,
were either drowned in the Vistula or perished by the sword. Poland,
having thus been obliterated from the list of independent kingdoms,
Catherine II. again turned her attention to the destruction of the
empire of the Porte. She sought to secure the good-will of Austria,
and by insuring the continuance of war in the West, to avert the
possibility of interference on the part either of England or of France.
The evident reluctance with which the Prussian Government continued
to take part in the French war was sufficient cause for Catherine to
favour Austria in dividing the remains of Poland. But, on the other
hand, she could not exclude Frederick William II. from all share in
the partition without incurring risk of driving him to take up arms
against herself. A treaty was concluded between Russia and Austria,
determining the partition that was to be made between the three
Powers, which the Emperor and the Czarina undertook to carry into
effect, whether the King of Prussia were content or not with the share
allotted to him (January 3, 1795). At the same time they entered into
an alliance directed against Turkey, and agreed that in case of war
Moldavia, Wallachia, and Bessarabia should be converted into a Russian
dependency, and that Servia and Bosnia should pass to Austria. The plan
of exchanging Belgium for Bavaria was revived, and Catherine further
engaged to support the Emperor in making acquisition of Venetian or
other territory.

♦England’s foreign policy.♦

Between France and England the strong sense of national hostility
which existed when the war first broke out had increased in intensity.
There was no name so hated in France as the name of Pitt. The English
statesman, who by his gold sustained the arms of the Coalition, had
also, according to popular report, by his bribes and emissaries been
the author of the Terror, and was held responsible for all the internal
ills under which France suffered. In England, the feeling of hatred
was fully reciprocated. The ideas of the Revolution were regarded
with abhorrence, the Convention with loathing, and the triumph of
the French armies did but excite the stronger determination to go on
fighting until both Holland and Belgium were wrested from the grasp
of the atheistic and regicide Republic. If England had ignominiously
been beaten on the Continent, she had been victorious at sea. Corsica
had been occupied, and George III. proclaimed (February, 1794). A
naval battle had been fought, commonly called the battle of June 1,
when the French fleet, sailing out of Brest, had been defeated by
Lord Howe, and driven back shattered to the coast (1794). Tobago, St.
Martinique, Guadaloupe, and other French West Indian islands were
already in English possession, and St. Domingo, the most important of
French colonies, threatened with conquest. If now the Dutch fleet was
pressed into the service of France, on the other hand the rich Dutch
colonies, possessions coveted by England, such as Ceylon and the Cape,
were open to seizure. The Cabinet was indeed intensely eager that the
Continental war should continue, and was making every exertion to fan
the zeal of Austria, and to draw Russia on to render active assistance.
Instead of subsidising Prussia, England now subsidised Austria. In
return for a loan of 4,600,000_l._ the Emperor undertook to put 200,000
men in the field (May 4, 1795). A treaty was, at the same time, entered
into between England and Russia, in which Catherine agreed to send
12,000 men to fight against France. Subsequently, in the autumn, a
Triple Alliance was concluded between the three Powers, and separate
negotiations renounced (September 28).

♦Treaty of Basel.♦

While thus Austria, Russia, and England were drawing closer together,
Prussia was fast backing out of the war. Both military and official
circles were thoroughly weary of it. The country had no interests
peculiar to itself to defend, and the Government no acquisitions in
view, beyond what had already been obtained in Poland. It was, however,
but with reluctance that the King, who had lost none of his repugnance
to the Revolution, consented to the opening of the negotiations held
with Barthélemy, the French Ambassador at Basel. The main difficulty
in coming to terms was the disposition of Prussian possessions on the
left bank of the Rhine, of which the cession would imply readiness on
the King’s part to resign to France all the territory of the Empire
on that side. The Committee of Public Safety demanded absolutely
whatever belonged to Prussia on the left bank. But Frederick William
was unwilling formally to abandon the cause of the Empire, and the
Committee was too desirous of concluding peace to refuse a compromise
which, in reality, yielded to France the point required. In the public
articles of the treaty it was merely stated that French troops should
remain in occupation of Prussian territory on the left bank until the
making of peace between France and the Empire; but in a secret article
the King declared his readiness to abandon his territory on the left
bank in return for an equivalent on the right, if France kept the
Rhine as her boundary when she made peace with the Empire. A second
matter of difficulty was the question whether the Empire was to obtain
the benefits of peace. The King could not leave the Northern States to
be overrun by French armies without lowering the position of Prussia
within the Empire. He accordingly proposed that France should agree to
a truce with the Empire, and afterwards accept Prussian mediation. The
Committee refused these demands, but consented to a line of demarcation
being drawn across Germany, and to regard as neutrals the States lying
to the north of it. It was also agreed that the Committee should accept
the services of the King in treating with the separate States of the
Empire. On these terms peace was concluded at Basel (April 5), and
ratified with applause by the Convention. The Empire was henceforth
torn in half. The Northern States under the wing of Prussia enjoyed
neutrality, while the Southern remained subjected to the miseries of
war.

♦Treaty with Spain.♦

Spain, shortly after Prussia, made her peace with France. Before the
revolution the two countries had been united by a treaty, entitled the
Family Compact (1761), which placed Spain, ruled by a younger branch
of the House of Bourbon, in political dependence on France. Dynastic
reasons had therefore had a large share in causing Spain to join the
coalition. No desire existed in the country for the triumph of the
allies. In possession of a large colonial empire, at the expense of
which she lived, Spain was intensely jealous of England’s superiority
at sea, and feared, in case of the ruin of the French navy, only to
retain her colonies at the good-will of her too powerful ally, and to
be forced to throw open their trade to English vessels. The war was
conducted without vigour. Nearly the whole of the revenue was absorbed
in the maintenance of the fleet, and the army did not consist of
35,000 men. During 1793 the French, however, had not been able to
muster at the Pyrenees an equally strong force. The Spaniards had
crossed the mountains and had occupied French territory. But in 1794
the tide of success had turned. The French armies were reinforced,
and drove the Spaniards back over the frontier (October-November). At
Madrid reigned confusion, alarm, and incapacity. The country was taxed
to the utmost extent it could bear. The Government had not credit
to borrow. Insurrectionary movements were feared in the towns. The
peasants of Catalonia, Navarre, and Biscay were warlike, and ready
to rise against the invaders; but the Government dared not give them
encouragement, through fear lest they should seize the occasion to
demand the re-establishment of provincial rights.

The weak and incapable king, Charles IV., was led by his wife, Marie
Louise of Parma, whose favourite, Godoy, was the real ruler of Spain.
This man, whose object was whether by war or peace to maintain himself
in power, after much vacillation opened negotiations with the French
Government. The Committee of Public Safety was eager to bring the
war to a close, but still persisted in demanding in return for the
evacuation of Spanish territory, the cession of the Spanish part of the
island of St. Domingo. The advance of the army of the Western Pyrenees
to the Ebro created a panic, which induced Godoy to yield the point,
and in July peace between France and Spain was on such terms made at
Basel.

♦Expedition to Quibéron.♦

[Illustration: QUIBERON BAY

                                                           E. Weller
]

Siéyès, Rewbel, and the other members of the Committee of Public
Safety, regarded these treaties with Prussia and Spain merely as
steps towards the final goal they had in view, namely, the conclusion
of a European peace ceding to France the Alps and the Rhine as her
boundaries. After making peace with Prussia and Spain, they hoped to
obtain the alliance of Prussia to aid them in crushing Austria in
Germany, and the alliance of Spain to aid them in crushing England at
sea. For the time, want of resources caused a practical cessation of
hostilities on the Upper Rhine. The Austrian armies on the right bank,
short of money and food, remained on the defensive. The French armies
on the left bank lived with difficulty at the cost of the conquered
territories, which, having long been the seat of war, were suffering
extreme misery. Meanwhile, the attention of the Government was drawn
towards the west, where war still smouldered in La Vendée, and where
a new war had broken out north of the Loire. In the large forests
and uncultivated tracts in which the provinces of Brittany, Maine,
and Anjou abounded, many bands of insurgents appeared, composed of
brigands, deserters from the armies, fugitive Vendeans, and returned
emigrants. They were called ‘Chouans,’ after one of their leaders,
a smuggler, who had himself received the nickname--derived from
‘chouette,’ a small owl--either from his surly, morose habits, or from
his using the owl’s cry as a signal. Though without organisation, and
under the conduct of a number of independent chiefs, the war proved
as difficult to suppress as the war in La Vendée. In the autumn of
1794 it spread into Normandy, and threatened to assume the form of a
general insurrection. The peasants, who resented the suppression of
their religion and the persecution of their priests, when they did
not join the marauders were in connivance with them. Raids were made
on republican posts, supplies cut off from towns, and many isolated
murders committed. In support of the movement, emigrants and priests
came from England, bringing with them munitions of war, and money both
in coin and forged assignats. So serious did the danger become, that
the Committee appointed Hoche, at this time the most distinguished
general whom the Republic possessed, to the command-in-chief of the
forces north of the Loire. During the Terror, his services to his
country had been requited by imprisonment, and but for Robespierre’s
sudden destruction, he would have fallen a victim to the guillotine.
Besides being an able soldier, Hoche was a sincere and patriotic man in
both public and private life, single-minded, straightforward, and pure.
The irksome and inglorious task now entrusted to him he carried out
with characteristic firmness and moderation, and while taking severe
measures for the repression of rebellion, he did all in his power to
win the good-will of the inhabitants, by treating them justly and
restoring discipline amongst his troops. He allowed the churches to be
reopened, and by leaving the clergy unharassed, sought to destroy their
enmity towards the Republic. Both the Convention and the insurgents
desired a breathing time in which to recruit their forces. Charette,
and other Vendean leaders, made an engagement to lay down arms and
recognise the authority of the Republic, on condition that indemnity
should be granted to themselves, that liberty of worship should be
allowed, and that the national guard should be under their command
(February 17). Many Chouan chiefs recognised the Republic on the same
terms (April 20). These agreements were merely armed truces. The
insurgent leaders retained their authority, and were but waiting the
arrival of means from England to resume their arms.

Fortunately for the Republic, its enemies were unready and disunited.
The concurrence of a general conflagration in the West, and of the
advance of 200,000 men across the Rhine, would have called to mind
the hazards run in 1793. Hostilities, however, still flagged on the
Rhine, while in the West jealousy and discord destroyed the chances
of successful resistance to the Republican armies. Amongst the
emigrants no union existed. Those who had fled in 1790 regarded with
contempt and aversion those who fled at a later date, and confounded
Constitutionalists with Robespierrists and Terrorists under the common
name of Jacobins. The leader of the expedition from England, Count
Joseph of Puisaye, was in ill-favour with the supporters of the Count
of Provence, because in 1789 he had been on the popular side. Hoche,
aware of their designs, arrested the Baron of Cormaton, the most
able of the Chouan chiefs, and seven other leading conspirators (May
15). The war in consequence was renewed in Brittany, but Charette,
who did not care to act as second to Puisaye, remained quiet in
La Vendée. The expedition from England disembarked at Carnac, the
little town at the head of the peninsula which encloses on one side
the Bay of Quibéron. Pitt had forborne to risk the lives of English
troops until assured that the emigrants were able, in accordance
with their representations, to acquire a firm footing in the country.
The force consisted of about 5,000 emigrants and between 1,000 and
2,000 French prisoners of war. Large bodies of Chouans came to the
commander and joined the invaders, and Fort Penthièvre, guarding the
connection between the peninsula and the mainland, was besieged and
taken. Meanwhile, however, quarrels broke out between the leaders
of the expedition and between the emigrants and the Chouans. Hoche,
having brought together 12,000 men at Auray, defeated the rebels, and
forced them back from their position at Carnac on to the peninsula
of Quibéron, where, with women and children, 20,000 persons were
collected. By aid of French prisoners of war who deserted, Fort
Penthièvre was, at the dead of night, surprised and captured (July 20).
The crowded peninsula lay open to the Republican army. Amid scenes
of utter confusion and distress an effort to reach the English ships
was made. Some succeeded in escaping, but several thousands were left
behind and made prisoners. The lives of the Chouans were spared, but
there remained more than a thousand emigrants. The Convention refused
mercy to emigrants, and all of them were shot in accordance with the
law.

♦Death of the Dauphin.♦

In dealing thus harshly with the captured emigrants, the Convention
was actuated by fear of danger to itself from the classes by which
it had recently been supported. After the insurrection of Prairial,
the working classes of Paris, defeated and leaderless, disappeared
for the time from the scene of political action. The Convention found
itself left face to face with its late ally, the middle classes, which
had taken part against the insurgents through dread of a Terrorist
reaction, but which now sought to turn the victory to their own
account. To the rule of the Convention intense aversion was felt and
freely expressed. There were in Paris concealed Royalists, most of
them persons belonging to the old privileged orders, who sought by
intrigue and conspiracy to effect a reaction in favour of the emigrant
Bourbon Princes. But such were comparatively few in number. The
middle classes desired merely complete liberty of worship and return
to constitutional forms of government. Though the Republic did not
possess their confidence or affection, they did not avow themselves
Monarchists nor aim definitely at the re-establishment of monarchy.
The formation of a strong united monarchical party was prevented both
by the conduct of the emigrants and by the want of a name to which
constitutional monarchists could rally. The late King’s brothers, the
Counts of Provence and Artois, as well as his more distant relations,
were emigrants. The young Dauphin, his only son, died at this time in
the Temple (June 8). In the summer of 1793 the child had been parted
from his mother, and placed under the charge of a shoemaker, Simon,
who treated him with roughness, if not brutality. In January 1794 he
was confined in a small dark room, of which the door was barred up,
and communication between him and his keepers maintained by means of
a grating, through which was passed daily a little bread, meat, and
water. Here he remained till after the fall of the Robespierrists in
July. When again brought into the light he was found covered with dirt,
apathetic, and diseased. His material condition was from this time
improved, but none of the care necessary to revive his spirits and to
save his life was given. The companionship of his sister, imprisoned
in the same building, was refused, and it was not until he was visibly
dying that resort was had to medical advice. Of the thousands who
perished in the course of the revolution none suffered so cruel or so
unmerited a fate as this innocent child, separated from every friend,
and slowly killed by misusage and neglect.

The death of the young Prince was a subject of rejoicing to
Republicans, but served as an additional cause of indignation against
the Convention. The probability of a Royalist insurrection in Paris
was increased by the landing of the emigrants at Quibéron. The
Thermidorians became alarmed for their own safety, and denounced as
Royalists the same journalists and national guards, whose action they
had before the insurrection of Prairial abetted and applauded. But,
since the proscription of the Mountain, they had lost the power of
controlling the Assembly, and the reaction, though impeded by their
resistance, still continued its course.

♦State of the Church.♦

Accepting what had already been done in many parts of the country,
the Convention passed a law sanctioning the provisionary use of
churches for the exercise of worship, but prohibiting any persons from
officiating in them before making a promise of submission to the laws
of the Republic (May 30). At Paris twelve, and subsequently fifteen,
churches were reopened. The oath imposed by the civil constitution of
the clergy was thus abandoned, and, in fact, the civil constitution
itself. Within the limits assigned by this law and the law which had
been passed in February (p. 227), the Church was left at liberty
to effect its own reorganisation. The constitutional Bishops, of
whom the majority had not abdicated, headed by Grégoire, Bishop of
Blois, made every endeavour to recover for the Church its former
influence. The work was accomplished with rapidity. The religious
persecution in itself had tended to destroy the sceptical spirit
which had prevailed amongst the middle classes in 1789, while the
mass of the constitutional clergy were men who had proved themselves
worthy of respect by remaining throughout the Terror faithful to their
convictions. Within a few months the clergy were again exercising
their former functions without obstruction. Internal divisions,
however, remained unhealed. Some of the nonjurors, who had never
taken the oath imposed by the civil constitution, made the promise
of submission to the laws of the Republic, and officiated in public
buildings, but refused to recognise the authority of the former
constitutional Bishops. Others of the nonjurors refused even to promise
submission to the laws, and officiated in secret in barns and private
houses, under constant fear of proscription and death. There were thus
three classes of priests, all at enmity with each other: (1) those who
had taken the oath required in 1790; (2) those who had refused this
oath, but had since promised submission to the laws; (3) the so-called
refractory priests, who had not taken the oath required in 1790, and
now refused submission to the laws. As a rule the lower and middle
classes were attached to the constitutional clergy, while nobles and
Royalists followed the nonjurors. It was in the East, the South, and
the West that the refractory priests had most influence.

♦Constitution of 1795.♦

The re-establishment of constitutional government, loudly demanded
by public opinion, was held by the majority in the Convention
itself necessary for the security of the Republic. On one side the
Constitution of 1791 was lauded by the Monarchists; on the other side
the Constitution of 1793, framed by the Mountain after the ejection
of the Girondists, but never put into force, was demanded by the
Jacobins. To the Convention both were unacceptable; the first because
it admitted a king, the second because it appeared impracticable. The
Terror had dissipated faith in the political virtue and intelligence of
the people, and the same men who in 1791 had been the warmest advocates
of decentralization and extreme forms of democratic government, were
now opposed to manhood suffrage, or to giving to local authorities
the opportunity of usurping sovereign powers. The appointment of a
committee to revise the Constitution of 1793 led to the adoption of
what was in reality a new form of government. The Constitution of
the year III., or 1795, was based on the liberal principles of 1789.
It guaranteed individual liberty, liberty of worship, liberty of the
press, and security of property and of person. As in the Constitution
of 1791, a low property qualification was required for voting in
primary assemblies, a higher one for voting in secondary assemblies.
Primary assemblies elected, as hitherto, justices of the peace for
the canton and municipal officers; secondary assemblies elected the
judges of the higher courts, the upper administrative bodies, and
the deputies to the Legislature. The number of administrative and
municipal bodies was greatly reduced. The administration of districts
was entirely abolished. Only communes with a population of over 5,000
retained separate municipalities. Communes of which the population
was below this number, included in any one canton, had a municipality
common to all. To every administrative and municipal body was added a
commissioner, nominated by the Government, whose duty was to see that
the laws were executed. Precaution was taken against the revival of an
authority at Paris rival to the Legislature. Communes of over 100,000
inhabitants were divided into districts, each with a municipality of
its own. Paris had thus twelve municipalities. The Legislative body
was formed of two Houses, a council of five hundred, and a council of
250 Ancients. Both Houses were elected on the same principle, but the
Ancients had to be forty years of age. Both were renewed by a third
of their number yearly. To the five hundred belonged the introduction
of laws; the Ancients had the right of rejecting them. At the head
of the executive was a Directory of five members, selected by the
Ancients out of a list drawn up by the five hundred. These Directors
appointed the ministers, in number six, and ordered the disposition of
the armed forces. They had no veto on legislation, and neither they nor
the ministers might sit in either council. One Director had to retire
yearly, so that the whole body would be renewed in the course of five
years.

♦Vendémiaire 13.♦

This Constitution, put in force as it stood, would have given France
a government formed of new men. But the members of the Convention,
long accustomed to the exercise of power, were unwilling to resign it,
or to hazard the maintenance of the Republic by allowing Royalists
and Monarchists an opportunity of obtaining a majority in the new
Legislature. It was determined to apply at once the principle of
renewing the Legislature by a third of its number every year. A
special law bound the secondary assemblies to elect two-thirds of
their deputies out of the Convention, so that only a single third in
either council would be formed of new men (August 22, Fructidor 5).
There were further to be no new elections till the spring of 1797,
so that for a year and a half the domination of the republican party
was secured. A second law required that if, in consequence of double
elections, all the seats reserved for members of its own body were not
filled, the Convention should elect the deputies required to make up
the number wanting (August 31, Fructidor 13). The new constitution was
submitted to the primary assemblies, and accepted by large majorities,
but with it were coupled these two accessory laws. At Paris popular
indignation was fanned into revolt by the emigrants and royalists. The
Convention depended for its safety on 4,000 troops of the line, and a
few hundred Jacobins and workmen hastily armed for its defence. On the
other side were 20,000 national guards. These, however, were under
two great disadvantages. They had no competent general, and they had
no artillery, all the sections having been deprived of their cannon
after the insurrection of Prairial. The forces of the Convention were
commanded by the deputy Barras, who entrusted the organisation of
resistance to Napoleon Bonaparte, a young general, who was the ablest
man in the service of the Republic, but whose name as yet was hardly
known beyond military circles, where his reputation stood high as the
officer to whose genius was owing the capture of Toulon in 1793. In all
haste a strong force of artillery was brought from a camp at Grenelle,
a few miles from Paris, and stationed round the Tuileries, so as to
command the approaches from the Rue St. Honoré and the Church of St.
Roch, which the insurrectionists occupied. The combat was sharp, but
soon decided. Before nightfall the insurgents were on all sides in
flight and dispersed (October 5, Vendémiaire 13).

The insurrection, thus quelled, strengthened the Thermidorians and
more violent party in the Convention. New laws were passed, designed
to keep the defeated party down and to insure that power should remain
in the hands of its actual possessors. Deported priests, returned to
France, were ordered to quit the country on pain of suffering, in
accordance with the laws, death as emigrants. Relations of emigrants,
in the first or second degree, such as fathers, brothers, sons, uncles
and nephews, were prohibited from holding any office, judicial,
legislative, or administrative (October 25). This measure, known as the
law of Brumaire 3, was of great political importance. It deprived a
very large number of persons of rights, guaranteed by the Constitution,
and was calculated to prevent the new Government rising above the
character of a purely party Government. Before the arrival of the new
deputies, those of the old members who retained their seats elected to
be Directors five men, all bound by interest to support the Republic,
since all had voted for the death of Louis XVI.

The new Government was therefore formed only in an insensible degree
of new men. The five Directors--Larevellière-Lépeaux, Rewbel, Carnot,
Letourneur, and Barras--the six ministers, and the two councils, stood
in the place of the Committee of Public Safety and the Convention;
but the change was one of name and form, not of system. There was
no change, either in the internal or in the foreign policy of the
Government.

As the Government remained practically unchanged, it could not, by
any possibility, be strong. It had none of that authority which comes
from representing the national will. What that will might be, it was
at the time hard to say. The nation itself had given up the task of
impressing its mind upon its rulers, and contented itself with private
disapprobation of their conduct. In Paris, where that disapprobation
had been expressed in action, it had been promptly silenced by military
intervention, and it was by no means unlikely that the army, which
was now the only strong organisation remaining in the country, might
hereafter intervene against the Directory as it had lately intervened
in its favour.

It was the more likely that this would happen because the army did not
owe its strength to its organisation alone. As far as it is possible
to judge, it fairly represented, for the time, the popular sentiment
of the nation. At the outset of the revolution, zeal for improvement
and change had seized upon every variety of mind and upon every class
of the community. The higher minds looked forward to liberty of speech
and thought, and through them to the raising of mankind in the scale of
human progress. The masses looked forward to material equality, to the
removal of the load of outrage and oppression under which they groaned.
For some time it seemed as if these objects could be achieved together.
It was not long before the attempt to grasp too much at a time brought
failure with it. Liberty was trodden down in practice, whilst it
was adored in word. Fraternity became but an excuse for fratricide.
Equality remained as the one aim to be pursued at all hazards, and
the equality which was most in favour was the lower and more material
equality which appealed to the masses of unlettered peasants. For one
man who cared about moral and spiritual advancement there were at least
a hundred who cared only to have a guarantee for their purchases of
confiscated property, and an assurance that they should be under no
disadvantages because they were not of noble birth. Such feelings,
strong in the nation, were strong in the army. The soldier has never
much sympathy for the machinery of a free government. It is his duty
in life to obey orders, not to impose them on his superiors. But the
soldier of revolutionary France was the champion of material equality.
He had offered it to the peoples which he had invaded. It had given to
him that which he prized most, the right of promotion to the superior
ranks of the service, irrespective of birth.

A body which is thoroughly organised, and which represents the
dominant ideas of a people, is, in reality, irresistible. For the
perfect organisation of the army one thing was wanting--a general
who could inspire it with confidence. That general would be found in
the young chief who had fought the battle of the Convention against
the insurgents of Vendémiaire. Because the nation itself was as yet
unprepared to appear upon the scene, the revolutionary epoch was
followed not by the Constitutional but by the Napoleonic age.

Yet the striving of the political revolutionists had not been in vain.
The time would come when the pursuit of merely material gains would
bring ruin and desolation with it, and the old ideals of the thinkers
of the eighteenth century would again be welcomed by a generation
wearied by military despotism, and which would therefore seek to
establish social and political institutions on a safer basis than
Mirabeau or Vergniaud had been able to do. Nor do even the wild schemes
of Chaumette and St. Just form a mere episode in French history, though
wisely to lighten the load which inevitably falls on the shoulders of
the poor and unfortunate, and thus to diminish the amount of human
suffering, is a work which opens up problems which these men attempted
rashly to cut with the axe of the executioner, but which are now
understood to be amongst the most complicated subjects of political
thought. To trace the fate of the ideas which were thrown up in the
course of the French Revolution would require many volumes. It is
because these ideas were so many sided and so powerful that the French
nation accepts the Revolution, in spite of the errors and crimes of the
revolutionists, as the source of its mental as well as of its political
life.




INDEX.


  America, assisted by France, 25;
    declaration of Independence by, 26

  Army, the French, mutinies in, 73;
    disorderly condition of, 105;
    extraordinary measures for the enlistment of, 146;
    conscription introduced for, 170;
    treatment of, by the Hébertists, 188;
    reorganisation of, 189

  Artois, the Count of, emigrates, 63;
    appeals to foreign Powers, 86

  Assignats, first issue of, 68;
    fresh issues of, 94;
    continued issue and depreciation of, 149, 172, 224, 225

  Austria, relations of, with Prussia and Turkey, 97, 98;
    forms a defensive alliance with Prussia, 104;
    war declared by France against, 105;
    ill-feeling towards Prussia of, 161;
    Thugut, minister of, 162

  Avignon, massacre at, 110


  Bailly, is chosen mayor of Paris, 47;
    addresses the King on his visit to Paris, 48;
    execution of, 178

  Barbaroux, asks Marseilles to send men to Paris, 116;
    execution of, 208

  Barère, selfish indifference of, 200;
    applauds the financial results of the Terror, 207

  Barnave, is a leader of the Centre and Left, 53;
    is a rival of Mirabeau, 57;
    is popular in the Jacobin Club, 65;
    supports the King after the flight to Varennes, 90;
    joins the Feuillants, 92;
    execution of, 178

  Basel, peace of, 238

  Bastille, the attack upon, 45;
    capture of, 46

  Belgium, invaded by the French, 111;
    invaded by Dumouriez, 130;
    question of the annexation of, 131;
    its annexation decreed, 141;
    is reconquered by the allies, 161;
    is again conquered by the French, 213

  Berthier, murder of, 48

  Billaud-Varennes, elected to the commune of Paris, 120;
    is placed on the Committee of Public Safety, 167;
    sanguinary character of, 200;
    opposes Robespierre, 217

  Bonaparte, Napoleon, suppresses the insurrection of Vendémiaire, 250

  Bordeaux, Girondist sentiments of, 157

  Bouillé, suppresses a mutiny at Nancy, 73;
    supports the flight to Varennes, 89

  Brienne, ministry of, 27

  Brissot, political opinions of, 76;
    calls for a republic, 90;
    trial and execution of, 177

  Brunswick, the Duke of, publishes a manifesto, 114;
    conducts the invasion, 123;
    retreats from Valmy, 124;
    commands one of the armies of the coalition, 141;
    takes Mainz, 161;
    is obliged to retreat, 192

  Burke, his Reflections on the French Revolution, 138


  Caen, Girondist sentiments prevail at, 157

  Cahiers, the, 29

  Calendar, the republican, 180

  Calonne, ministry of, 27

  Cambon, financial measures of, 195

  Carnot, directs the movements of the armies, 189;
    arranges the campaign of 1794, 212;
    escapes from prosecution after the insurrection of Prairial, 231

  Carrier, conduct of, at Nantes, 186;
    execution of, 223

  Cathelineau, crosses the Loire, 160;
    is killed, 161

  Catherine II., patronises French philosophers, 22;
    extends her dominions in Poland and the Crimea, 96;
    proposes a second partition of Poland, 135

  Cazalès, defends the monarchy, 51

  Champ de Mars, the, massacre of, 91

  Charette, commands part of the Vendean army, 160;
    fails to cross the Loire, 161

  Chaumette, elected to the commune of Paris, 120;
    his position in the commune, 169;
    attacks religion, 179

  Chollet, defeat of the Vendeans at, 182

  Chouans, the, insurrection of, 241

  Church, the French, position of, before the revolution, 6, 15;
    demands of the Cahiers respecting, 31;
    its property appropriated by the Constituent Assembly, 67;
    the civil constitution provokes a schism in, 74;
    schism continued in, 101;
    treatment of, by the Hébertists, 179;
    Robespierre’s behaviour towards, 216;
    improvement in the condition of, 228;
    condition of, after the Terror, 246

  Civil constitution of the clergy, the, enacted, 69;
    position of the Legislative Assembly towards, 101

  Clavière, minister of Finance, 105;
    is dismissed, 112;
    is restored to office, 117

  Clermont-Tonnerre, 52

  Coburg, commands one of the armies of the coalition, 141;
    relieves Maestricht, 142;
    takes Condé and Valenciennes, 161;
    evacuates Belgium, 213

  Collot d’Herbois, elected to the commune of Paris, 120;
    becomes a member of the Committee of Public Safety, 167;
    sanguinary character of, 200;
    opposes Robespierre, 217

  Committee of General Security instituted, 146

  Committee of Public Safety, instituted, 145;
    acquires power over the Convention, 166;
    does not dare to risk a collision with the Commune, 167;
    composition of, 200;
    gains over the mob, 203;
    dictatorship of, 204;
    dissatisfaction of Robespierre with, 205;
    extension of the Terror by, 208;
    Robespierre’s management of, 214;
    discord in, 217;
    reorganisation of, after the Terror, 221

  Commune of Paris, the, first organisation of, 81;
    dispersion of the municipal council of, 116;
    reconstruction of, 119;
    organises the September massacres, 121;
    re-election of, 129;
    heads the movement for the proscription of the Girondists, 153;
    its power independent of the Convention, 167;
    controls the revolutionary army, 174;
    is attacked by Robespierre, 198;
    is reconstituted by Robespierre, 205;
    is broken up, 221

  Condé surrenders, 161

  Conscription, the, resorted to, 170

  Constituent Assembly, the, fusion of the orders in, 38;
    its dissolution desired by the Queen, 43;
    abolishes feudal services, 49;
    formation of parties in, 51;
    wishes to establish constitutional government, 55;
    constitutional provisions of, 58;
    annuls regulations impeding the circulation of corn, 59;
    removes to Paris, 62;
    completes the constitution, 65;
    appropriates Church property, 67;
    enacts the civil constitution of the clergy, 69;
    increase of party spirit in, 70;
    abolishes titles of nobility, 71;
    leaves the King without authority, 72;
    presents the constitution to the King, and dissolves itself, 93

  Constitution, of 1791, 65, 92;
    of 1793, 158;
    of 1795, 247

  Convention, the National, summoned, 117;
    elected, 123;
    parties in, 124;
    its galleries occupied by Jacobins, 129;
    offers to help all peoples desirous of freedom, 131;
    decrees the union of Nice and Savoy, 133;
    decrees the opening of the Scheldt, and orders the generals to
        proclaim the sovereignty of the people, 134;
    condemns the King, 140;
    decrees the annexation of Belgium, and declares war against
        England, 141;
    institutes the Committee of Public Safety, 145;
    orders the transportation of priests, 147;
    forbids the emigrants to return on pain of death, 148;
    refuses to proscribe the Girondists, 153;
    is compelled to order the arrest of the Girondists, 155;
    resistance in the departments to, 157;
    falls into the hands of the extreme party in the Mountain, 165;
    its comparative weakness, 166;
    orders a levy _en masse_, 170;
    orders requisitions to supply Paris, and institutes a revolutionary
        army, 174;
    passes the law of suspected persons, 175;
    sends twenty-one deputies before the Revolution Court, 176;
    submits to the Commune, 180;
    accepts the Worship of Reason, 181;
    Reorganises the army, 189;
    its legislative work, 193;
    reorganises the Revolutionary Court, 215;
    overthrows Robespierre, 219;
    parties in, after the fall of Robespierre, 222;
    restoration of Girondist deputies to, 223;
    reaction in, 224;
    looks for the support to the party of reaction, 227;
    foreign policy of, 233;
    becomes unpopular with the middle classes, 244

  Cordeliers, the Club of the, presided over by Danton, 82;
    demands a republic, 91

  Corday, Charlotte, admires the Girondists, 163;
    assassinates Marat, 164

  Couthon, is placed on the Committee of Public Safety, 167;
    his conduct in Auvergne, 185;
    supports Robespierre, 200;
    arrest of, 219;
    execution of, 220

  Custine, takes Frankfort, 130;
    is driven out of Frankfort, 141


  D’Alembert, writings of, 14;

  Danton, presides over the Cordeliers, 82;
    calls for a republic, 90;
    becomes Minister of Justice, 117;
    stirs up resistance against invasion, 121;
    resigns his ministry, 125;
    is attacked by the Girondists, 127;
    advocates the condemnation of the King, 140;
    breaks with the Girondists, 144;
    loses authority in the Convention, 165;
    wishes to stop the Reign of Terror, 197;
    is executed, 204

  Dauphin, the, death of, 245

  De Launay, murder of, 46

  Delessart, advocates peace, 104;
    is charged with treason, 105

  Departments, France divided into, 65

  Desmoulins, Camille, urges the Parisians to take arms, 44;
    political opinions of, 77;
    advocates a republic, 90;
    supports Robespierre, 109;
    wishes to stop the Reign of Terror, 197;
    publishes _The Old Cordelier_, 199;
    execution of, 204

  D’Espréménil, defends the old system, 51

  Diderot, writings of, 14

  Directors, appointment of, 251

  Dumouriez, minister of foreign affairs, 105;
    resigns, 112;
    commands the army, 121;
    occupied the Argonnes, 123;
    gains a victory at Jemmapes, 130;
    proposes the invasion of Holland, 135;
    fails in an invasion of Holland, 142;
    is defeated at Neerwinden, 143;
    takes refuge with the Austrians, 144


  Economists, the, 16

  Egalité, Philip. _See_ Orleans, Duke of

  Elizabeth, Madame, execution of, 178

  Emigrants, the, begin to leave France, 63;
    increasing numbers of, 71;
    are encouraged by the princes on the Rhine, 101;
    confiscation of the revenues of, 111;
    are forbidden to return on pain of death, 148

  Empire, the defective organisation of, 96;
    anti-French feeling in, 102;
    joins the coalition against France, 141

  Encyclopædia, the, 14

  England, political condition of, 23;
    dislikes the annexation of Belgium by France, 133;
    opposes the opening of the Scheldt, 134;
    state of political opinion in, 136;
    war declared by France against, 141

  Europe, prevalence of Voltairian ideas in, 21


  Federation, Feasts of the, 70

  Feraud, murder of, 230

  Feudal nobility, privileges of, under the monarchy, 1–5;
    abolition of, 49

  Feuillants, the club of the, foundation of, 92

  Fleurus, battle of, 213

  Foulon, murder of, 48

  Fouquier Tinville, public prosecutor, 176

  France before the revolution, political condition of, 1;
    economical condition of, 8;
    progress of reforming ideas in, 22

  Francis II., the Emperor, war declared by France against, 105;
    hopes to make conquests in France, 135

  Frankfort, occupied by Custine, 130;
    stormed by the Prussians, 141

  Frederick II., patronises French philosophers, 22;
    extends his territories, 97

  Frederick William II., concludes the treaty of Reichenbach, 97;
    is prevented from helping Louis, 99;
    urges a march to Paris, 123;
    agrees to the second partition of Poland, 135


  Gensonné, sits in the Legislative Assembly, 100;
    trial and execution of, 177

  Germany. _See_ Empire, the

  Germinal, insurrection of, 226

  Girondists, the principles of, 100;
    ecclesiastical policy of, 101;
    warlike tendencies of, 102;
    enter the ministry, 105;
    opposition aroused against, 106;
    hope for the establishment of a republic, 111;
    dismissal of their ministers, 112;
    make overtures to the King, 115;
    form the right of the Convention, 125;
    weakness of, 126;
    attack Robespierre and Danton, 127;
    increasing weakness of, 142;
    break with Danton, 144;
    attacked by Robespierre, 145;
    economical doctrines of, 149;
    movement for the proscription of, 153;
    arrest of the leaders of, 155;
    causes of the failure of, 156;
    feeling in the departments in favour of, 157;
    suppression of the movement in favour of, 158;
    trial and execution of the leaders of, 177;
    restoration of the survivors of, 224

  Gobel, Archbishop, resigns office, 180

  Grégoire, Bishop, refuses to resign office, 180

  Guadet, sits in the Legislative Assembly, 100


  Hague, the, the treaty of, 210

  Hébert, elected to the Commune of Paris, 120;
    his position in the Commune, 169;
    his character and aims, 170;
    calls for a reign of terror, 175;
    attacks Christianity, 179;
    supports the system of terror, 183;
    is opposed by Robespierre, 197;
    execution of, 204

  Hoche, commands the army on the Moselle, 192;
    is sent to command in the west, 242;
    defeats the Chouans at Quiberon, 244

  Holland, proposed invasion of, 135;
    failure of Dumouriez in an attack upon, 142;
    is conquered by Pichegru, 232

  Hondschoote, battle of, 191

  Houchard, defeats the enemy and is guillotined, 191


  Isnard, desires war with Austria, 103;
    threatens that Paris shall be destroyed, 154


  Jacobins, the club of, formation of, 64;
    affiliation of provincial clubs to, 80;
    asks for the King’s deposition after the flight to Varennes, 91;
    opposition to the Girondists in, 106;
    gives its confidence to Robespierre, 109;
    proposes to dethrone the King, 115;
    takes part against the Girondists, 129;
    Robespierre’s influence at, 201;
    closure of, 223

  Jalès, camp of, 110

  Jemmapes, battle of, 130

  Joseph II., the Emperor, reforms attempted by, 23;
    wishes to incorporate Bavaria, 97

  Jourdan, gains the victory of Wattignies, 191

  June, battle of the first of, 237


  Kaunitz, is indifferent to the progress of the revolution, 98

  Kellermann, commands at Metz, 121

  Kléber, commands against the Vendeans, 182


  Lafayette, proposes the adoption of the tricolour, 47;
    is a leader of the Centre and Left, 53;
    supports the system of two chambers, 54;
    refuses to support Mirabeau, 57;
    extent of the influence of, 60;
    arrives at Versailles, 61;
    guards the King, 63;
    supports the King after the flight to Varennes, 91;
    joins the Feuillants, 92;
    commands on the Eastern frontier, and denounces the Jacobins, 112;
    appears at the bar of the Assembly, 113;
    support of, rejected by the Queen, 114;
    is acquitted by the Assembly, 116;
    flies from the country and is imprisoned by the Austrians, 119

  Lally-Tollendal, 52, 63

  Lameth, the brothers, are amongst the leaders of the Centre and Left,
        53;
    distrust Mirabeau, 57;
    join the Feuillants, 92

  La Vendée. _See_ Vendeans, the

  Legislative Assembly, the, composition of, 99;
    ecclesiastical policy of, 101;
    growth of warlike tendencies in, 102;
    declares war against the King of Hungary, 105;
    decrees that Volunteers shall come to Paris, 112;
    proclaims the country to be in danger, 114;
    suspends the King, and summons a National Convention, 117;
    last sitting of, 124

  Le Mans, defeat of the Vendeans at, 183

  Leopold II. the Emperor, is urged by the Queen to intervene in
        France, 94;
    concludes the treaty of Reichenbach, 97;
    concludes the treaty of Sistova, 98;
    refuses to help Louis, 99;
    seeks to avoid war, 103;
    claims a right of interference in France, 104;
    death of, 105

  Levy _en masse_, 170

  Longwy, siege of, 121

  Louis XIV., monarchy of, 2

  Louis XV., misgovernment of, 3

  Louis XVI., accession of, 18;
    character of, 19;
    takes part in the American war, 25;
    design of, in summoning the States General, 32;
    opens the States General, 33;
    weakness of his position, 34;
    attempts to hinder the fusion of the orders, 39;
    dismisses Necker, 44;
    visits Paris after the capture of the Bastille, 47;
    idea of retreating to Metz, considered by, 60;
    is brought to Paris, 62;
    swears to maintain the Constitution, 70;
    appoints reactionary ministers, 81;
    refuses to be guided by Mirabeau, 83;
    dislikes the civil constitution of the clergy, 86;
    desires that the constitution may fail, 87;
    attempts flight, 88;
    is stopped at Varennes, 89;
    his deposition proposed and rejected, 90;
    accepts the constitution, 93;
    deception practised by him, 93;
    hopes that the allies will reach Paris, 105;
    refuses to sanction a decree against the nonjurors, 111;
    refuses to sanction a decree for the meeting of Volunteers at
        Paris, and dismisses the Girondist ministers, 112;
    is visited by the mob, 113;
    is driven from the Tuileries and suspended, 117;
    causes of the fall of, 118;
    trial of, 139

  Lyons, royalist insurrection at, 157;
    surrender of, 181;
    vengeance taken on, 186


  Mainz, surrender to the French, 130;
    is retaken by Brunswick, 161

  Malouet, 52

  Marat, political opinions of, 78;
    attacks the Girondists, 109;
    takes part in the September massacres, 122;
    acquittal of, 145;
    assassination of, 163

  Marie Antoinette, character of, 20;
    urges the King to hinder the fusion of the orders, 39;
    distrusts Mirabeau, 57;
    appears at a military banquet at Versailles, 61;
    is brought to Paris, 62;
    becomes unpopular, 86;
    effect of her counsels on her husband, 87;
    urges the King to fly, 88;
    is arrested at Varennes, 89;
    urges the Emperor to intervene, 94;
    refuses the help of the constitutionalists and the emigrants, 95;
    is threatened by the mob, 113;
    refuses to be saved by Lafayette, 114;
    execution of, 177

  Marseillaise, the, 116

  Maury, the Abbé, defends the clergy, 51

  Maximum laws, the, enacted, 171;
    difficulty of enforcing, 175;
    re-enacted in a new form, 203;
    cease to be observed, 224;
    are repealed, 225

  Merlin of Douai, 53

  Mirabeau, character and policy of, 35;
    is chosen as a representative of the Third Estate, 37;
    is a leader of the Centre and Left, 53;
    opposes Necker, 55;
    statesmanlike policy of, 56;
    difficulties in the way of, 57;
    attacks Necker, 58;
    close of the career of, 82;
    death of, 84

  Miranda, fails to take Maestricht, 147

  Molleville, reactionary opinions of, 105

  Monarchy, the French, rise of, 1;
    centralisation of the government of, 7

  Mounier, 52, 63

  Mountain, the, proposes the deposition of the King, 115;
    struggles with the Girondists, 125;
    urges the condemnation of the King, 140;
    obtains the creation of the Revolutionary Court, 143;
    obtains the command of the Committee of Public Safety, 146;
    principles of, 148;
    supports a coercive economical policy, 152;
    fills the clubs with its supporters, 162;
    is held in subserviency by the committees and the commune, 192;
    is divided in opinion after Robespierre’s fall, 222;
    asks for the constitution of 1793, 226;
    transportation of the leaders of, 227

  Municipality of Paris. _See_ Commune of Paris


  Nancy, mutiny at, 73

  Narbonne, conduct of, a minister of war, 105

  National Assembly, the title of adopted by the Third Estate, 38.
    _See_ Constituent Assembly

  Necker, first ministry of, 25;
    second ministry of, 29;
    gives advice to the States General, 33;
    weakness of policy, 34;
    is opposed to the dissolution of the Assembly, 43;
    dismissal of, 44;
    recalled to office, 47;
    fails to guide the Assembly, 55;
    finally resigns office, 81

  Neerwinden, battle of, 143

  Nice, occupied by the French, 129;
    annexed, 133

  Nonjurors, the, refuse to swear to the civil constitution of the
        clergy, 75;
    are deprived of their pensions, 101;
    are threatened with banishment, 111;
    transportation of, 180

  Notables, the, meeting of, 27


  Orders, the privileged, exempted from taxation, 8

  Orleans, Duke of, takes the popular side, 42;
    is said to have aimed at the throne, 63;
    sits with the Montagnards, 125;
    trial of, 176;
    is executed, 178


  Paris, anarchy in, 42;
    assault upon the Bastille in, 45;
    establishment of a municipality and a national guard in, 47;
    difficulty of provisioning, 59;
    the King brought to, 62;
    organisation of, 81;
    proposed formation of an armed camp for the defence of, 111;
    preparations for insurrection in, 116;
    election of a new commune of, 119;
    massacres in, 121;
    predominates over the departments, 126;
    is ruled by the new commune, 120

  Parliaments, the, oppose the King, 25, 28

  Pétion, sits on the extreme left in the Constituent Assembly, 53;
    becomes Mayor of Paris, 112;
    death of, 208

  Pichegru, defeats the allies on the Rhine, 192;
    conquers Flanders, 213;
    conquers Holland, 232

  Pilnitz, conference at, 98

  Pitt, internal policy of, 24;
    refuses to join foreign powers against France, 98;
    character of the statesmanship of, 136;
    strives to maintain peace, 138

  Plain, the, position of, in the convention, 128

  Poland, first partition of, 96;
    establishment of a new constitution in, 98;
    hostility of Catherine II. to, 99;
    proposed second partition of, 135;
    insurrection of, 210;
    second partition of, 211;
    third partition of, 236

  Portugal, joins the coalition against France, 141

  Prairial, insurrection of, 231

  Privileged orders, the, position of, 8;
    aims of, 29

  Provinces, the, insurrections in, 48;
    anarchy in, 109

  Prussia, its relations with Austria, 97;
    forms a defensive alliance with Austria, 104;
    is drawn into a war with France, 105;
    its jealousy of Austria, 161;
    concludes peace with France, 238


  Quiberon, peninsular of Hoche’s victory at, 244


  Reason, the worship of, 181

  Reichenbach, treaty of, 97

  Rennes, Girondist sentiments of, 157

  Revolutionary army, the formation of, 173

  Revolutionary Court, the, establishment of, 143;
    deputies first sent before, 176

  Rights of Man, declaration of the, 58

  Robespierre, sits on the extreme Left in the Constituent Assembly, 53;
    is applauded by the Jacobins, 65;
    hesitates to decide for the King’s deposition, 90;
    proposes a law forbidding re-election, 92;
    leads the opposition against the Girondists, 107;
    opposes the war, 108;
    is elected to the Commune, 120;
    is attacked by the Girondists, 127;
    proposes the imprisonment of the leading Girondists, 145;
    supports the insurrection against the Girondists, 153;
    becomes a leading member of the Committee of Public Safety, 167;
    attacks the Hébertists, 197;
    causes of the influence of, 201;
    procures the destruction of the Hébertists by abandoning Danton,
        202;
    is dissatisfied with the Committee of Public Safety, 205;
    reduces the Terror to a system, 208;
    inaugurates the worship of the Supreme Being, 214;
    reorganises the Revolutionary Court, 215;
    comes into collision with the Committee of Public Safety, 217;
    his imprisonment, 219;
    execution of, 220

  Roland, is minister of the interior, 105;
    attempts in vain to restore order, 109;
    is dismissed, 112;
    projects of a retreat to the Loire discussed in the house of, 115;
    is restored to office, 117;
    resignation of, 145;
    death of, 178

  Roland, Madame, directs the actions of her husband, 115;
    execution of, 178

  Rousseau, doctrines of, 16


  St. Just, is placed on the Committee of Public Safety, 167;
    makes requisitions at Strasburg, 185;
    character and aims of, 206;
    arrest of, 219;
    execution of, 220

  Santerre, commands the national guard, 122

  Sardinia, the King of, war declared against, 130

  Saumur, is taken by the Vendeans, 160

  Savoy, occupied by the French, 129;
    annexed, 133

  Scheldt, the opening of, 134

  September massacres, the, 121

  Servan, is minister of war, 111;
    is dismissed, 112;
    is restored to office, 117

  Siéyès, writes a pamphlet, 30;
    is a leader of the Centre and Left, 53

  Sistova, the treaty of, 98

  Smith, Adam, publishes the ‘Wealth of Nations,’ 24

  Spain, joins the coalition against France, 141;
    concludes peace with France, 239

  States-General, the, summoned, 28;
    discussions on the constitution of, 31;
    meeting of, 33;
    fusion of the orders in, 38.
    _See_ Constituent Assembly

  Supreme Being, the, worship of, 214


  Tallien, conduct of, at Bordeaux, 185;
    his position after the revolution of Thermidor, 223

  Taxation, exemption of the privileged orders from, 8;
    character of, under the monarchy, 9;
    system of, established by the Constituent Assembly, 94

  Tennis Court Oath, the, 40

  Terror, the Reign of, commencement of, 165

  Thermidor, revolution of, 219

  Thermidorians, the, party of, 222

  Third Estate, double representation of, 31;
    adopts the title of the National Assembly, 38

  Thouret, 53

  Thugut, becomes foreign minister of Austria, 162;
    foreign policy of, 234

  Tories, the English, 136

  Toulon, resists the Convention, 157;
    capture of, 181;
    vengeance taken on, 186

  Turcoing, Pichegru’s victory at, 213

  Turgot, ministry of, 18

  Turreau, devastates La Vendée, 209


  Valenciennes, surrenders, 161

  Valmy, cannonade of, 124

  Varennes, the flight to, 88

  Vendeans, the, rise in insurrection, 147;
    mode of fighting of, 159;
    first successes of, 160;
    are driven back into their own country, 161;
    destruction of the army of, 182;
    continuance of the war against, 208

  Vendémiaire, insurrection of, 249

  Verdun, siege of, 121

  Vergnaud, sits in the Legislative Assembly, 100;
    qualities of, 126;
    trial and execution of, 177

  Versailles, arrival of the mob at, 61;
    the King removed from, 62

  Veto, given to the King, 58

  Voltaire, opinions and influence of, 14, 21


  Wattignies, Battle of, 193

  Weissenburg, the lines of, 192

  Whigs, the English, 136

  White Terror, the, 229

  Wurmser, commands the Austrians on the Rhine, 192


  York, the Duke of, commands the English Army in the Netherlands, 161;
    is driven from Dunkirk, 191;
    commands the English forces in the campaign of 1794, 212;
    fails to defend Holland, 232

  Young, Arthur, describes the economical condition of France, 11




                   _Printed at_ THE BALLANTYNE PRESS
                  SPOTTISWOODE, BALLANTYNE & CO. LTD.
                  _Colchester, London & Eton, England_




Transcriber’s Notes


Punctuation, hyphenation, and spelling were made consistent when a
predominant preference was found in the original book; otherwise they
were not changed.

Simple typographical errors were corrected; unbalanced quotation
marks were remedied when the change was obvious, and otherwise left
unbalanced.

Illustrations in this eBook have been positioned between paragraphs
and outside quotations. In versions of this eBook that support
hyperlinks, the page references in the List of Illustrations lead to
the corresponding illustrations.

The index was not checked for proper alphabetization or correct page
references.



        
            *** END OF THE PROJECT GUTENBERG EBOOK THE FRENCH REVOLUTION 1789-1795 ***
        

    

Updated editions will replace the previous one—the old editions will
be renamed.

Creating the works from print editions not protected by U.S. copyright
law means that no one owns a United States copyright in these works,
so the Foundation (and you!) can copy and distribute it in the United
States without permission and without paying copyright
royalties. Special rules, set forth in the General Terms of Use part
of this license, apply to copying and distributing Project
Gutenberg™ electronic works to protect the PROJECT GUTENBERG™
concept and trademark. Project Gutenberg is a registered trademark,
and may not be used if you charge for an eBook, except by following
the terms of the trademark license, including paying royalties for use
of the Project Gutenberg trademark. If you do not charge anything for
copies of this eBook, complying with the trademark license is very
easy. You may use this eBook for nearly any purpose such as creation
of derivative works, reports, performances and research. Project
Gutenberg eBooks may be modified and printed and given away—you may
do practically ANYTHING in the United States with eBooks not protected
by U.S. copyright law. Redistribution is subject to the trademark
license, especially commercial redistribution.


START: FULL LICENSE

THE FULL PROJECT GUTENBERG LICENSE

PLEASE READ THIS BEFORE YOU DISTRIBUTE OR USE THIS WORK

To protect the Project Gutenberg™ mission of promoting the free
distribution of electronic works, by using or distributing this work
(or any other work associated in any way with the phrase “Project
Gutenberg”), you agree to comply with all the terms of the Full
Project Gutenberg™ License available with this file or online at
www.gutenberg.org/license.

Section 1. General Terms of Use and Redistributing Project Gutenberg™
electronic works

1.A. By reading or using any part of this Project Gutenberg™
electronic work, you indicate that you have read, understand, agree to
and accept all the terms of this license and intellectual property
(trademark/copyright) agreement. If you do not agree to abide by all
the terms of this agreement, you must cease using and return or
destroy all copies of Project Gutenberg™ electronic works in your
possession. If you paid a fee for obtaining a copy of or access to a
Project Gutenberg™ electronic work and you do not agree to be bound
by the terms of this agreement, you may obtain a refund from the person
or entity to whom you paid the fee as set forth in paragraph 1.E.8.

1.B. “Project Gutenberg” is a registered trademark. It may only be
used on or associated in any way with an electronic work by people who
agree to be bound by the terms of this agreement. There are a few
things that you can do with most Project Gutenberg™ electronic works
even without complying with the full terms of this agreement. See
paragraph 1.C below. There are a lot of things you can do with Project
Gutenberg™ electronic works if you follow the terms of this
agreement and help preserve free future access to Project Gutenberg™
electronic works. See paragraph 1.E below.

1.C. The Project Gutenberg Literary Archive Foundation (“the
Foundation” or PGLAF), owns a compilation copyright in the collection
of Project Gutenberg™ electronic works. Nearly all the individual
works in the collection are in the public domain in the United
States. If an individual work is unprotected by copyright law in the
United States and you are located in the United States, we do not
claim a right to prevent you from copying, distributing, performing,
displaying or creating derivative works based on the work as long as
all references to Project Gutenberg are removed. Of course, we hope
that you will support the Project Gutenberg™ mission of promoting
free access to electronic works by freely sharing Project Gutenberg™
works in compliance with the terms of this agreement for keeping the
Project Gutenberg™ name associated with the work. You can easily
comply with the terms of this agreement by keeping this work in the
same format with its attached full Project Gutenberg™ License when
you share it without charge with others.

1.D. The copyright laws of the place where you are located also govern
what you can do with this work. Copyright laws in most countries are
in a constant state of change. If you are outside the United States,
check the laws of your country in addition to the terms of this
agreement before downloading, copying, displaying, performing,
distributing or creating derivative works based on this work or any
other Project Gutenberg™ work. The Foundation makes no
representations concerning the copyright status of any work in any
country other than the United States.

1.E. Unless you have removed all references to Project Gutenberg:

1.E.1. The following sentence, with active links to, or other
immediate access to, the full Project Gutenberg™ License must appear
prominently whenever any copy of a Project Gutenberg™ work (any work
on which the phrase “Project Gutenberg” appears, or with which the
phrase “Project Gutenberg” is associated) is accessed, displayed,
performed, viewed, copied or distributed:

    This eBook is for the use of anyone anywhere in the United States and most
    other parts of the world at no cost and with almost no restrictions
    whatsoever. You may copy it, give it away or re-use it under the terms
    of the Project Gutenberg License included with this eBook or online
    at www.gutenberg.org. If you
    are not located in the United States, you will have to check the laws
    of the country where you are located before using this eBook.
  
1.E.2. If an individual Project Gutenberg™ electronic work is
derived from texts not protected by U.S. copyright law (does not
contain a notice indicating that it is posted with permission of the
copyright holder), the work can be copied and distributed to anyone in
the United States without paying any fees or charges. If you are
redistributing or providing access to a work with the phrase “Project
Gutenberg” associated with or appearing on the work, you must comply
either with the requirements of paragraphs 1.E.1 through 1.E.7 or
obtain permission for the use of the work and the Project Gutenberg™
trademark as set forth in paragraphs 1.E.8 or 1.E.9.

1.E.3. If an individual Project Gutenberg™ electronic work is posted
with the permission of the copyright holder, your use and distribution
must comply with both paragraphs 1.E.1 through 1.E.7 and any
additional terms imposed by the copyright holder. Additional terms
will be linked to the Project Gutenberg™ License for all works
posted with the permission of the copyright holder found at the
beginning of this work.

1.E.4. Do not unlink or detach or remove the full Project Gutenberg™
License terms from this work, or any files containing a part of this
work or any other work associated with Project Gutenberg™.

1.E.5. Do not copy, display, perform, distribute or redistribute this
electronic work, or any part of this electronic work, without
prominently displaying the sentence set forth in paragraph 1.E.1 with
active links or immediate access to the full terms of the Project
Gutenberg™ License.

1.E.6. You may convert to and distribute this work in any binary,
compressed, marked up, nonproprietary or proprietary form, including
any word processing or hypertext form. However, if you provide access
to or distribute copies of a Project Gutenberg™ work in a format
other than “Plain Vanilla ASCII” or other format used in the official
version posted on the official Project Gutenberg™ website
(www.gutenberg.org), you must, at no additional cost, fee or expense
to the user, provide a copy, a means of exporting a copy, or a means
of obtaining a copy upon request, of the work in its original “Plain
Vanilla ASCII” or other form. Any alternate format must include the
full Project Gutenberg™ License as specified in paragraph 1.E.1.

1.E.7. Do not charge a fee for access to, viewing, displaying,
performing, copying or distributing any Project Gutenberg™ works
unless you comply with paragraph 1.E.8 or 1.E.9.

1.E.8. You may charge a reasonable fee for copies of or providing
access to or distributing Project Gutenberg™ electronic works
provided that:

    • You pay a royalty fee of 20% of the gross profits you derive from
        the use of Project Gutenberg™ works calculated using the method
        you already use to calculate your applicable taxes. The fee is owed
        to the owner of the Project Gutenberg™ trademark, but he has
        agreed to donate royalties under this paragraph to the Project
        Gutenberg Literary Archive Foundation. Royalty payments must be paid
        within 60 days following each date on which you prepare (or are
        legally required to prepare) your periodic tax returns. Royalty
        payments should be clearly marked as such and sent to the Project
        Gutenberg Literary Archive Foundation at the address specified in
        Section 4, “Information about donations to the Project Gutenberg
        Literary Archive Foundation.”
    
    • You provide a full refund of any money paid by a user who notifies
        you in writing (or by e-mail) within 30 days of receipt that s/he
        does not agree to the terms of the full Project Gutenberg™
        License. You must require such a user to return or destroy all
        copies of the works possessed in a physical medium and discontinue
        all use of and all access to other copies of Project Gutenberg™
        works.
    
    • You provide, in accordance with paragraph 1.F.3, a full refund of
        any money paid for a work or a replacement copy, if a defect in the
        electronic work is discovered and reported to you within 90 days of
        receipt of the work.
    
    • You comply with all other terms of this agreement for free
        distribution of Project Gutenberg™ works.
    

1.E.9. If you wish to charge a fee or distribute a Project
Gutenberg™ electronic work or group of works on different terms than
are set forth in this agreement, you must obtain permission in writing
from the Project Gutenberg Literary Archive Foundation, the manager of
the Project Gutenberg™ trademark. Contact the Foundation as set
forth in Section 3 below.

1.F.

1.F.1. Project Gutenberg volunteers and employees expend considerable
effort to identify, do copyright research on, transcribe and proofread
works not protected by U.S. copyright law in creating the Project
Gutenberg™ collection. Despite these efforts, Project Gutenberg™
electronic works, and the medium on which they may be stored, may
contain “Defects,” such as, but not limited to, incomplete, inaccurate
or corrupt data, transcription errors, a copyright or other
intellectual property infringement, a defective or damaged disk or
other medium, a computer virus, or computer codes that damage or
cannot be read by your equipment.

1.F.2. LIMITED WARRANTY, DISCLAIMER OF DAMAGES - Except for the “Right
of Replacement or Refund” described in paragraph 1.F.3, the Project
Gutenberg Literary Archive Foundation, the owner of the Project
Gutenberg™ trademark, and any other party distributing a Project
Gutenberg™ electronic work under this agreement, disclaim all
liability to you for damages, costs and expenses, including legal
fees. YOU AGREE THAT YOU HAVE NO REMEDIES FOR NEGLIGENCE, STRICT
LIABILITY, BREACH OF WARRANTY OR BREACH OF CONTRACT EXCEPT THOSE
PROVIDED IN PARAGRAPH 1.F.3. YOU AGREE THAT THE FOUNDATION, THE
TRADEMARK OWNER, AND ANY DISTRIBUTOR UNDER THIS AGREEMENT WILL NOT BE
LIABLE TO YOU FOR ACTUAL, DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE OR
INCIDENTAL DAMAGES EVEN IF YOU GIVE NOTICE OF THE POSSIBILITY OF SUCH
DAMAGE.

1.F.3. LIMITED RIGHT OF REPLACEMENT OR REFUND - If you discover a
defect in this electronic work within 90 days of receiving it, you can
receive a refund of the money (if any) you paid for it by sending a
written explanation to the person you received the work from. If you
received the work on a physical medium, you must return the medium
with your written explanation. The person or entity that provided you
with the defective work may elect to provide a replacement copy in
lieu of a refund. If you received the work electronically, the person
or entity providing it to you may choose to give you a second
opportunity to receive the work electronically in lieu of a refund. If
the second copy is also defective, you may demand a refund in writing
without further opportunities to fix the problem.

1.F.4. Except for the limited right of replacement or refund set forth
in paragraph 1.F.3, this work is provided to you ‘AS-IS’, WITH NO
OTHER WARRANTIES OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO WARRANTIES OF MERCHANTABILITY OR FITNESS FOR ANY PURPOSE.

1.F.5. Some states do not allow disclaimers of certain implied
warranties or the exclusion or limitation of certain types of
damages. If any disclaimer or limitation set forth in this agreement
violates the law of the state applicable to this agreement, the
agreement shall be interpreted to make the maximum disclaimer or
limitation permitted by the applicable state law. The invalidity or
unenforceability of any provision of this agreement shall not void the
remaining provisions.

1.F.6. INDEMNITY - You agree to indemnify and hold the Foundation, the
trademark owner, any agent or employee of the Foundation, anyone
providing copies of Project Gutenberg™ electronic works in
accordance with this agreement, and any volunteers associated with the
production, promotion and distribution of Project Gutenberg™
electronic works, harmless from all liability, costs and expenses,
including legal fees, that arise directly or indirectly from any of
the following which you do or cause to occur: (a) distribution of this
or any Project Gutenberg™ work, (b) alteration, modification, or
additions or deletions to any Project Gutenberg™ work, and (c) any
Defect you cause.

Section 2. Information about the Mission of Project Gutenberg™

Project Gutenberg™ is synonymous with the free distribution of
electronic works in formats readable by the widest variety of
computers including obsolete, old, middle-aged and new computers. It
exists because of the efforts of hundreds of volunteers and donations
from people in all walks of life.

Volunteers and financial support to provide volunteers with the
assistance they need are critical to reaching Project Gutenberg™’s
goals and ensuring that the Project Gutenberg™ collection will
remain freely available for generations to come. In 2001, the Project
Gutenberg Literary Archive Foundation was created to provide a secure
and permanent future for Project Gutenberg™ and future
generations. To learn more about the Project Gutenberg Literary
Archive Foundation and how your efforts and donations can help, see
Sections 3 and 4 and the Foundation information page at www.gutenberg.org.

Section 3. Information about the Project Gutenberg Literary Archive Foundation

The Project Gutenberg Literary Archive Foundation is a non-profit
501(c)(3) educational corporation organized under the laws of the
state of Mississippi and granted tax exempt status by the Internal
Revenue Service. The Foundation’s EIN or federal tax identification
number is 64-6221541. Contributions to the Project Gutenberg Literary
Archive Foundation are tax deductible to the full extent permitted by
U.S. federal laws and your state’s laws.

The Foundation’s business office is located at 809 North 1500 West,
Salt Lake City, UT 84116, (801) 596-1887. Email contact links and up
to date contact information can be found at the Foundation’s website
and official page at www.gutenberg.org/contact

Section 4. Information about Donations to the Project Gutenberg
Literary Archive Foundation

Project Gutenberg™ depends upon and cannot survive without widespread
public support and donations to carry out its mission of
increasing the number of public domain and licensed works that can be
freely distributed in machine-readable form accessible by the widest
array of equipment including outdated equipment. Many small donations
($1 to $5,000) are particularly important to maintaining tax exempt
status with the IRS.

The Foundation is committed to complying with the laws regulating
charities and charitable donations in all 50 states of the United
States. Compliance requirements are not uniform and it takes a
considerable effort, much paperwork and many fees to meet and keep up
with these requirements. We do not solicit donations in locations
where we have not received written confirmation of compliance. To SEND
DONATIONS or determine the status of compliance for any particular state
visit www.gutenberg.org/donate.

While we cannot and do not solicit contributions from states where we
have not met the solicitation requirements, we know of no prohibition
against accepting unsolicited donations from donors in such states who
approach us with offers to donate.

International donations are gratefully accepted, but we cannot make
any statements concerning tax treatment of donations received from
outside the United States. U.S. laws alone swamp our small staff.

Please check the Project Gutenberg web pages for current donation
methods and addresses. Donations are accepted in a number of other
ways including checks, online payments and credit card donations. To
donate, please visit: www.gutenberg.org/donate.

Section 5. General Information About Project Gutenberg™ electronic works

Professor Michael S. Hart was the originator of the Project
Gutenberg™ concept of a library of electronic works that could be
freely shared with anyone. For forty years, he produced and
distributed Project Gutenberg™ eBooks with only a loose network of
volunteer support.

Project Gutenberg™ eBooks are often created from several printed
editions, all of which are confirmed as not protected by copyright in
the U.S. unless a copyright notice is included. Thus, we do not
necessarily keep eBooks in compliance with any particular paper
edition.

Most people start at our website which has the main PG search
facility: www.gutenberg.org.

This website includes information about Project Gutenberg™,
including how to make donations to the Project Gutenberg Literary
Archive Foundation, how to help produce our new eBooks, and how to
subscribe to our email newsletter to hear about new eBooks.
"""


#8.1

print(book.count('the')) # 9681 times
print(book.count('science')) # 5 times

#8.2

print(book.count('q')) # 389 times
print(book.count('s')) # 26348 times

#8.3

print(len(book)) # 550429 	

#8.4

# What is the index of the first character 'Q' in the book?
print(book.index('q')) # 1063
# What are the last 5 characters of the book?
print(book[-5:]) # oks.