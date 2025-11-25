it('Written with DeploySentinel Recorder', () => {
  // Load "https://www.amazon.com/"
  cy.visit('https://www.amazon.com/');

  // Resize window to 1347 x 715
  cy.viewport(1347, 715);

  // Click on <a> "Sign in"
  cy.get('[href="https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"]').click();

  // Click on <input> #ap_email_login
  cy.get('#ap_email_login').click();

  // Fill "bidemi007@gmail... on <input> #ap_email_login
  cy.get('#ap_email_login').type("bidemi007@gmail.com");

  // Click on <input> .a-button-input
  cy.get('.a-button-input').click();

  // Resize window to 1040 x 715
  cy.viewport(1040, 715);

  // Fill "b3Vw4R^dwvb(cJU... on <input> #ap_password
  cy.get('#ap_password').type("b3Vw4R^dwvb(cJU");

  // Click on <input> #signInSubmit
  cy.get('#signInSubmit').click();

  // Click on <input> #twotabsearchtextbox
  cy.get('#twotabsearchtextbox').click();

  // Fill "tesla car charg... on <input> #twotabsearchtextbox
  cy.get('#twotabsearchtextbox').type("tesla car charger");

  // Press Enter on input
  cy.get('#twotabsearchtextbox').type('{Enter}');

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1);

  // Scroll wheel by X:1, Y:25
  cy.scrollTo(0, 26);

  // Scroll wheel by X:-31, Y:156
  cy.scrollTo(0, 182);

  // Scroll wheel by X:0, Y:21
  cy.scrollTo(0, 203);

  // Scroll wheel by X:10, Y:21
  cy.scrollTo(0, 224);

  // Scroll wheel by X:0, Y:14
  cy.scrollTo(0, 238);

  // Scroll wheel by X:9, Y:23
  cy.scrollTo(0, 261);

  // Scroll wheel by X:-1, Y:6
  cy.scrollTo(0, 267);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 267);

  // Scroll wheel by X:-16, Y:114
  cy.scrollTo(0, 382);

  // Scroll wheel by X:0, Y:14
  cy.scrollTo(0, 396);

  // Scroll wheel by X:1, Y:2
  cy.scrollTo(0, 398);

  // Scroll wheel by X:0, Y:20
  cy.scrollTo(0, 418);

  // Scroll wheel by X:-13, Y:105
  cy.scrollTo(0, 523);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 525);

  // Scroll wheel by X:7, Y:18
  cy.scrollTo(0, 543);

  // Scroll wheel by X:0, Y:4
  cy.scrollTo(0, 547);

  // Scroll wheel by X:0, Y:-4
  cy.scrollTo(0, 543);

  // Scroll wheel by X:6, Y:-28
  cy.scrollTo(0, 515);

  // Scroll wheel by X:0, Y:-25
  cy.scrollTo(0, 490);

  // Scroll wheel by X:9, Y:-23
  cy.scrollTo(0, 467);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 465);

  // Scroll wheel by X:1, Y:-2
  cy.scrollTo(0, 463);

  // Scroll wheel by X:0, Y:-6
  cy.scrollTo(0, 457);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 456);

  // Scroll wheel by X:0, Y:-4
  cy.scrollTo(0, 452);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 451);

  // Scroll wheel by X:0, Y:-4
  cy.scrollTo(0, 447);

  // Scroll wheel by X:2, Y:-2
  cy.scrollTo(0, 445);

  // Scroll wheel by X:0, Y:-4
  cy.scrollTo(0, 441);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 444);

  // Scroll wheel by X:-16, Y:83
  cy.scrollTo(0, 527);

  // Scroll wheel by X:0, Y:166
  cy.scrollTo(0, 693);

  // Scroll wheel by X:-20, Y:182
  cy.scrollTo(0, 875);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 878);

  // Scroll wheel by X:6, Y:10
  cy.scrollTo(0, 888);

  // Scroll wheel by X:0, Y:9
  cy.scrollTo(0, 897);

  // Scroll wheel by X:-7, Y:109
  cy.scrollTo(0, 1006);

  // Scroll wheel by X:0, Y:380
  cy.scrollTo(0, 1386);

  // Scroll wheel by X:-13, Y:79
  cy.scrollTo(0, 1465);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 1468);

  // Scroll wheel by X:-43, Y:123
  cy.scrollTo(0, 1591);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1592);

  // Click on <span> "Tesla Universal Wall Conn..."
  cy.get('#\33 5705ba2-b1bc-4383-a6c6-2cdf95349f26 .a-size-base-plus:nth-child(1) > span:nth-child(1)').click();

  // Scroll wheel by X:0, Y:50
  cy.scrollTo(0, 331);

  // Scroll wheel by X:-1, Y:10
  cy.scrollTo(0, 341);

  // Scroll wheel by X:0, Y:38
  cy.scrollTo(0, 379);

  // Scroll wheel by X:1, Y:21
  cy.scrollTo(0, 400);

  // Scroll wheel by X:-14, Y:124
  cy.scrollTo(0, 533);

  // Scroll wheel by X:0, Y:138
  cy.scrollTo(0, 662);

  // Scroll wheel by X:4, Y:66
  cy.scrollTo(0, 728);

  // Scroll wheel by X:-14, Y:115
  cy.scrollTo(0, 843);

  // Scroll wheel by X:0, Y:74
  cy.scrollTo(0, 917);

  // Scroll wheel by X:-16, Y:102
  cy.scrollTo(0, 1019);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 1021);

  // Scroll wheel by X:-1, Y:2
  cy.scrollTo(0, 1023);

  // Scroll wheel by X:0, Y:8
  cy.scrollTo(0, 1031);

  // Scroll wheel by X:-2, Y:4
  cy.scrollTo(0, 1035);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 1037);

  // Scroll wheel by X:-19, Y:65
  cy.scrollTo(0, 1102);

  // Scroll wheel by X:0, Y:75
  cy.scrollTo(0, 1177);

  // Scroll wheel by X:-18, Y:198
  cy.scrollTo(0, 1385);

  // Scroll wheel by X:0, Y:151
  cy.scrollTo(0, 1528);

  // Scroll wheel by X:-24, Y:186
  cy.scrollTo(0, 1712);

  // Scroll wheel by X:0, Y:240
  cy.scrollTo(0, 1952);

  // Scroll wheel by X:-4, Y:37
  cy.scrollTo(0, 1989);

  // Scroll wheel by X:0, Y:76
  cy.scrollTo(0, 2065);

  // Scroll wheel by X:2, Y:7
  cy.scrollTo(0, 2072);

  // Scroll wheel by X:0, Y:31
  cy.scrollTo(0, 2103);

  // Scroll wheel by X:-5, Y:28
  cy.scrollTo(0, 2131);

  // Scroll wheel by X:0, Y:117
  cy.scrollTo(0, 2248);

  // Scroll wheel by X:-7, Y:130
  cy.scrollTo(0, 2378);

  // Scroll wheel by X:0, Y:484
  cy.scrollTo(0, 2862);

  // Scroll wheel by X:-7, Y:138
  cy.scrollTo(0, 3000);

  // Scroll wheel by X:0, Y:1464
  cy.scrollTo(0, 4464);

  // Scroll wheel by X:-7, Y:154
  cy.scrollTo(0, 4685);

  // Scroll wheel by X:0, Y:1397
  cy.scrollTo(0, 6015);

  // Scroll wheel by X:-2, Y:12
  cy.scrollTo(0, 6033);

  // Scroll wheel by X:0, Y:5
  cy.scrollTo(0, 6038);

  // Scroll wheel by X:3, Y:9
  cy.scrollTo(0, 6047);

  // Scroll wheel by X:0, Y:8
  cy.scrollTo(0, 6055);

  // Scroll wheel by X:-17, Y:76
  cy.scrollTo(0, 6131);

  // Scroll wheel by X:0, Y:151
  cy.scrollTo(0, 6282);

  // Scroll wheel by X:-14, Y:116
  cy.scrollTo(0, 6398);

  // Scroll wheel by X:0, Y:4
  cy.scrollTo(0, 6402);

  // Scroll wheel by X:4, Y:7
  cy.scrollTo(0, 6409);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 6412);

  // Scroll wheel by X:1, Y:1
  cy.scrollTo(0, 6412);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 6416);

  // Scroll wheel by X:-2, Y:-1
  cy.scrollTo(0, 6416);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 6412);

  // Scroll wheel by X:-20, Y:-230
  cy.scrollTo(0, 6182);

  // Scroll wheel by X:3, Y:-23
  cy.scrollTo(0, 6159);

  // Scroll wheel by X:0, Y:-16
  cy.scrollTo(0, 6143);

  // Scroll wheel by X:-3, Y:-19
  cy.scrollTo(0, 6124);

  // Scroll wheel by X:0, Y:-97
  cy.scrollTo(0, 6028);

  // Scroll wheel by X:-43, Y:-109
  cy.scrollTo(0, 5918);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 5916);

  // Scroll wheel by X:-5, Y:-10
  cy.scrollTo(0, 5906);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 5904);

  // Scroll wheel by X:-1, Y:-2
  cy.scrollTo(0, 5902);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 5900);

  // Scroll wheel by X:-2, Y:-4
  cy.scrollTo(0, 5896);

  // Scroll wheel by X:0, Y:-5
  cy.scrollTo(0, 5891);

  // Scroll wheel by X:-2, Y:-6
  cy.scrollTo(0, 5885);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 5882);

  // Scroll wheel by X:-1, Y:-3
  cy.scrollTo(0, 5879);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 5877);

  // Scroll wheel by X:-1, Y:-2
  cy.scrollTo(0, 5875);

  // Scroll wheel by X:0, Y:-15
  cy.scrollTo(0, 5860);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 5859);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 5856);

  // Scroll wheel by X:0, Y:6
  cy.scrollTo(0, 5862);

  // Scroll wheel by X:-15, Y:288
  cy.scrollTo(0, 6150);

  // Scroll wheel by X:0, Y:582
  cy.scrollTo(0, 6732);

  // Scroll wheel by X:-3, Y:40
  cy.scrollTo(0, 6772);

  // Scroll wheel by X:4, Y:113
  cy.scrollTo(0, 6885);

  // Scroll wheel by X:-12, Y:136
  cy.scrollTo(0, 7021);

  // Scroll wheel by X:0, Y:198
  cy.scrollTo(0, 7219);

  // Scroll wheel by X:3, Y:99
  cy.scrollTo(0, 7318);

  // Scroll wheel by X:-4, Y:80
  cy.scrollTo(0, 7398);

  // Scroll wheel by X:0, Y:592
  cy.scrollTo(0, 7990);

  // Scroll wheel by X:-21, Y:194
  cy.scrollTo(0, 8184);

  // Scroll wheel by X:0, Y:4
  cy.scrollTo(0, 8188);

  // Scroll wheel by X:-29, Y:219
  cy.scrollTo(0, 8407);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 8409);

  // Resize window to 1372 x 715
  cy.viewport(1372, 715);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 8174);

  // Scroll wheel by X:-29, Y:212
  cy.scrollTo(0, 8386);

  // Scroll wheel by X:0, Y:10
  cy.scrollTo(0, 8396);

  // Scroll wheel by X:-16, Y:184
  cy.scrollTo(0, 8580);

  // Scroll wheel by X:0, Y:135
  cy.scrollTo(0, 8715);

  // Scroll wheel by X:-3, Y:23
  cy.scrollTo(0, 8738);

  // Scroll wheel by X:0, Y:12
  cy.scrollTo(0, 8750);

  // Scroll wheel by X:-2, Y:21
  cy.scrollTo(0, 8771);

  // Scroll wheel by X:0, Y:7
  cy.scrollTo(0, 8778);

  // Scroll wheel by X:-10, Y:29
  cy.scrollTo(0, 8807);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 8808);

  // Scroll wheel by X:-7, Y:7
  cy.scrollTo(0, 8815);

  // Scroll wheel by X:0, Y:5
  cy.scrollTo(0, 8820);

  // Scroll wheel by X:-9, Y:19
  cy.scrollTo(0, 8839);

  // Scroll wheel by X:0, Y:14
  cy.scrollTo(0, 8853);

  // Scroll wheel by X:1, Y:3
  cy.scrollTo(0, 8856);

  // Scroll wheel by X:0, Y:6
  cy.scrollTo(0, 8861);

  // Scroll wheel by X:-7, Y:76
  cy.scrollTo(0, 8938);

  // Scroll wheel by X:0, Y:8
  cy.scrollTo(0, 8946);

  // Scroll wheel by X:-3, Y:15
  cy.scrollTo(0, 8961);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 8964);

  // Scroll wheel by X:2, Y:3
  cy.scrollTo(0, 8967);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 8968);

  // Click on <a> "Read more"
  cy.get('.a-section:nth-child(3) .review:nth-child(2) [href="javascript:void(0)"]:nth-child(2)').click();

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 8968);

  // Scroll wheel by X:-7, Y:99
  cy.scrollTo(0, 9068);

  // Scroll wheel by X:0, Y:14
  cy.scrollTo(0, 9082);

  // Scroll wheel by X:-1, Y:10
  cy.scrollTo(0, 9092);

  // Scroll wheel by X:0, Y:299
  cy.scrollTo(0, 9391);

  // Scroll wheel by X:2, Y:3
  cy.scrollTo(0, 9394);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 9396);

  // Scroll wheel by X:1, Y:1
  cy.scrollTo(0, 9397);

  // Scroll wheel by X:0, Y:12
  cy.scrollTo(0, 9409);

  // Scroll wheel by X:2, Y:2
  cy.scrollTo(0, 9411);

  // Scroll wheel by X:0, Y:18
  cy.scrollTo(0, 9429);

  // Scroll wheel by X:-2, Y:7
  cy.scrollTo(0, 9436);

  // Scroll wheel by X:0, Y:5
  cy.scrollTo(0, 9441);

  // Scroll wheel by X:3, Y:22
  cy.scrollTo(0, 9463);

  // Scroll wheel by X:0, Y:21
  cy.scrollTo(0, 9484);

  // Scroll wheel by X:-2, Y:16
  cy.scrollTo(0, 9500);

  // Scroll wheel by X:0, Y:123
  cy.scrollTo(0, 9623);

  // Scroll wheel by X:5, Y:20
  cy.scrollTo(0, 9643);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 9645);

  // Scroll wheel by X:2, Y:3
  cy.scrollTo(0, 9648);

  // Scroll wheel by X:0, Y:4
  cy.scrollTo(0, 9652);

  // Scroll wheel by X:2, Y:2
  cy.scrollTo(0, 9654);

  // Scroll wheel by X:0, Y:7
  cy.scrollTo(0, 9661);

  // Scroll wheel by X:-2, Y:6
  cy.scrollTo(0, 9667);

  // Scroll wheel by X:0, Y:18
  cy.scrollTo(0, 9685);

  // Scroll wheel by X:-5, Y:41
  cy.scrollTo(0, 9734);

  // Scroll wheel by X:0, Y:155
  cy.scrollTo(0, 9881);

  // Scroll wheel by X:-1, Y:14
  cy.scrollTo(0, 9895);

  // Scroll wheel by X:0, Y:41
  cy.scrollTo(0, 9936);

  // Scroll wheel by X:-3, Y:34
  cy.scrollTo(0, 9970);

  // Scroll wheel by X:0, Y:207
  cy.scrollTo(0, 10173);

  // Scroll wheel by X:-3, Y:24
  cy.scrollTo(0, 10201);

  // Scroll wheel by X:0, Y:11
  cy.scrollTo(0, 10212);

  // Scroll wheel by X:3, Y:36
  cy.scrollTo(0, 10248);

  // Scroll wheel by X:0, Y:13
  cy.scrollTo(0, 10261);

  // Scroll wheel by X:-4, Y:45
  cy.scrollTo(0, 10319);

  // Scroll wheel by X:0, Y:213
  cy.scrollTo(0, 10519);

  // Scroll wheel by X:-8, Y:45
  cy.scrollTo(0, 10564);

  // Scroll wheel by X:0, Y:6
  cy.scrollTo(0, 10570);

  // Scroll wheel by X:-7, Y:57
  cy.scrollTo(0, 10639);

  // Scroll wheel by X:0, Y:199
  cy.scrollTo(0, 10826);

  // Scroll wheel by X:-9, Y:86
  cy.scrollTo(0, 10912);

  // Scroll wheel by X:0, Y:262
  cy.scrollTo(0, 11174);

  // Scroll wheel by X:-5, Y:25
  cy.scrollTo(0, 11199);

  // Scroll wheel by X:0, Y:9
  cy.scrollTo(0, 11208);

  // Scroll wheel by X:-1, Y:4
  cy.scrollTo(0, 11212);

  // Scroll wheel by X:0, Y:6
  cy.scrollTo(0, 11218);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 11215);

  // Scroll wheel by X:-5, Y:-55
  cy.scrollTo(0, 11160);

  // Scroll wheel by X:0, Y:-12
  cy.scrollTo(0, 11148);

  // Scroll wheel by X:-1, Y:-11
  cy.scrollTo(0, 11137);

  // Scroll wheel by X:1, Y:-10
  cy.scrollTo(0, 11127);

  // Scroll wheel by X:0, Y:-233
  cy.scrollTo(0, 10894);

  // Scroll wheel by X:-21, Y:-120
  cy.scrollTo(0, 10774);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 10771);

  // Scroll wheel by X:1, Y:-2
  cy.scrollTo(0, 10769);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 10767);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 10766);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 10765);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 10764);

  // Scroll wheel by X:0, Y:-6
  cy.scrollTo(0, 10758);

  // Click on <a> "Read more"
  cy.get('.a-section:nth-child(3) .review:nth-child(6) [href="javascript:void(0)"]:nth-child(2)').click();

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 10858);

  // Scroll wheel by X:-7, Y:98
  cy.scrollTo(0, 10956);

  // Scroll wheel by X:0, Y:351
  cy.scrollTo(0, 11307);

  // Scroll wheel by X:3, Y:12
  cy.scrollTo(0, 11319);

  // Scroll wheel by X:0, Y:8
  cy.scrollTo(0, 11327);

  // Scroll wheel by X:-3, Y:4
  cy.scrollTo(0, 11331);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 11333);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 11334);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 11335);

  // Scroll wheel by X:-12, Y:60
  cy.scrollTo(0, 11395);

  // Scroll wheel by X:0, Y:135
  cy.scrollTo(0, 11530);

  // Scroll wheel by X:-8, Y:48
  cy.scrollTo(0, 11578);

  // Scroll wheel by X:0, Y:9
  cy.scrollTo(0, 11587);

  // Scroll wheel by X:-2, Y:11
  cy.scrollTo(0, 11598);

  // Scroll wheel by X:0, Y:6
  cy.scrollTo(0, 11604);

  // Scroll wheel by X:-9, Y:45
  cy.scrollTo(0, 11649);

  // Scroll wheel by X:0, Y:110
  cy.scrollTo(0, 11759);

  // Scroll wheel by X:-16, Y:164
  cy.scrollTo(0, 11923);

  // Scroll wheel by X:0, Y:123
  cy.scrollTo(0, 12046);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 12047);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 12048);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 12049);

  // Scroll wheel by X:0, Y:-10
  cy.scrollTo(0, 12039);

  // Scroll wheel by X:9, Y:-33
  cy.scrollTo(0, 12006);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 12003);

  // Scroll wheel by X:1, Y:-3
  cy.scrollTo(0, 12000);

  // Scroll wheel by X:0, Y:-52
  cy.scrollTo(0, 11948);

  // Scroll wheel by X:10, Y:-24
  cy.scrollTo(0, 11924);

  // Click on <a> "See more reviews"
  cy.get('.a-row > [href="/product-reviews/B0CNJH667W/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"]').click();

  // Scroll wheel by X:0, Y:12
  cy.scrollTo(0, 12);

  // Scroll wheel by X:6, Y:19
  cy.scrollTo(0, 31);

  // Scroll wheel by X:0, Y:20
  cy.scrollTo(0, 51);

  // Scroll wheel by X:-18, Y:128
  cy.scrollTo(0, 187);

  // Scroll wheel by X:0, Y:106
  cy.scrollTo(0, 284);

  // Scroll wheel by X:-3, Y:20
  cy.scrollTo(0, 305);

  // Scroll wheel by X:0, Y:17
  cy.scrollTo(0, 322);

  // Scroll wheel by X:4, Y:37
  cy.scrollTo(0, 359);

  // Scroll wheel by X:0, Y:9
  cy.scrollTo(0, 368);

  // Scroll wheel by X:-6, Y:53
  cy.scrollTo(0, 421);

  // Scroll wheel by X:0, Y:128
  cy.scrollTo(0, 549);

  // Scroll wheel by X:-10, Y:144
  cy.scrollTo(0, 708);

  // Scroll wheel by X:0, Y:263
  cy.scrollTo(0, 956);

  // Scroll wheel by X:-4, Y:26
  cy.scrollTo(0, 982);

  // Scroll wheel by X:0, Y:50
  cy.scrollTo(0, 1032);

  // Scroll wheel by X:-2, Y:17
  cy.scrollTo(0, 1049);

  // Scroll wheel by X:0, Y:205
  cy.scrollTo(0, 1254);

  // Scroll wheel by X:-3, Y:29
  cy.scrollTo(0, 1283);

  // Scroll wheel by X:4, Y:65
  cy.scrollTo(0, 1348);

  // Scroll wheel by X:0, Y:297
  cy.scrollTo(0, 1645);

  // Scroll wheel by X:-1, Y:7
  cy.scrollTo(0, 1652);

  // Scroll wheel by X:5, Y:54
  cy.scrollTo(0, 1706);

  // Scroll wheel by X:0, Y:376
  cy.scrollTo(0, 2082);

  // Scroll wheel by X:5, Y:77
  cy.scrollTo(0, 2159);

  // Scroll wheel by X:0, Y:456
  cy.scrollTo(0, 2615);

  // Scroll wheel by X:5, Y:82
  cy.scrollTo(0, 2725);

  // Scroll wheel by X:0, Y:576
  cy.scrollTo(0, 3273);

  // Scroll wheel by X:11, Y:17
  cy.scrollTo(0, 3290);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 3292);

  // Scroll wheel by X:0, Y:-4
  cy.scrollTo(0, 3288);

  // Scroll wheel by X:2, Y:-2
  cy.scrollTo(0, 3286);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 3284);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 3283);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 3282);

  // Scroll wheel by X:2, Y:-2
  cy.scrollTo(0, 3280);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 3277);

  // Scroll wheel by X:2, Y:-1
  cy.scrollTo(0, 3277);

  // Scroll wheel by X:0, Y:-4
  cy.scrollTo(0, 3272);

  // Scroll wheel by X:1, Y:0
  cy.scrollTo(0, 3272);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 3271);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 3270);

  // Scroll wheel by X:0, Y:4
  cy.scrollTo(0, 3274);

  // Scroll wheel by X:-20, Y:170
  cy.scrollTo(0, 3444);

  // Scroll wheel by X:0, Y:129
  cy.scrollTo(0, 3573);

  // Scroll wheel by X:-11, Y:149
  cy.scrollTo(0, 3750);

  // Scroll wheel by X:0, Y:421
  cy.scrollTo(0, 4143);

  // Scroll wheel by X:-1, Y:6
  cy.scrollTo(0, 4149);

  // Scroll wheel by X:0, Y:21
  cy.scrollTo(0, 4170);

  // Scroll wheel by X:-18, Y:126
  cy.scrollTo(0, 4306);

  // Scroll wheel by X:0, Y:140
  cy.scrollTo(0, 4436);

  // Scroll wheel by X:-13, Y:103
  cy.scrollTo(0, 4539);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 4539);

  // Scroll wheel by X:0, Y:-10
  cy.scrollTo(0, 4528);

  // Scroll wheel by X:-3, Y:-6
  cy.scrollTo(0, 4522);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 4520);

  // Scroll wheel by X:-2, Y:-2
  cy.scrollTo(0, 4518);

  // Scroll wheel by X:0, Y:-6
  cy.scrollTo(0, 4512);

  // Scroll wheel by X:2, Y:-2
  cy.scrollTo(0, 4510);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 4508);

  // Scroll wheel by X:1, Y:-1
  cy.scrollTo(0, 4507);

  // Scroll wheel by X:0, Y:-10
  cy.scrollTo(0, 4497);

  // Scroll wheel by X:1, Y:-2
  cy.scrollTo(0, 4495);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 4493);

  // Scroll wheel by X:1, Y:-2
  cy.scrollTo(0, 4491);

  // Scroll wheel by X:0, Y:-9
  cy.scrollTo(0, 4482);

  // Scroll wheel by X:-14, Y:-135
  cy.scrollTo(0, 4347);

  // Scroll wheel by X:0, Y:-555
  cy.scrollTo(0, 3791);

  // Scroll wheel by X:-35, Y:-196
  cy.scrollTo(0, 3596);

  // Scroll wheel by X:2, Y:-9
  cy.scrollTo(0, 3587);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 3584);

  // Scroll wheel by X:2, Y:-2
  cy.scrollTo(0, 3582);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 3585);

  // Scroll wheel by X:-5, Y:9
  cy.scrollTo(0, 3594);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 3594);

  // Scroll wheel by X:-2, Y:-9
  cy.scrollTo(0, 3583);

  // Scroll wheel by X:6, Y:-21
  cy.scrollTo(0, 3562);

  // Scroll wheel by X:3, Y:15
  cy.scrollTo(0, 3577);

  // Scroll wheel by X:-20, Y:222
  cy.scrollTo(0, 3799);

  // Scroll wheel by X:0, Y:413
  cy.scrollTo(0, 4210);

  // Scroll wheel by X:-3, Y:19
  cy.scrollTo(0, 4231);

  // Scroll wheel by X:0, Y:7
  cy.scrollTo(0, 4238);

  // Scroll wheel by X:-1, Y:6
  cy.scrollTo(0, 4244);

  // Scroll wheel by X:0, Y:11
  cy.scrollTo(0, 4255);

  // Scroll wheel by X:8, Y:29
  cy.scrollTo(0, 4284);

  // Scroll wheel by X:-7, Y:24
  cy.scrollTo(0, 4308);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 4309);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 4306);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 4305);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 4304);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 4303);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 4302);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 4301);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 4300);

  // Scroll wheel by X:-3, Y:-5
  cy.scrollTo(0, 4295);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 4293);

  // Scroll wheel by X:-3, Y:-6
  cy.scrollTo(0, 4287);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 4286);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 4285);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 4284);

  // Scroll wheel by X:-4, Y:-4
  cy.scrollTo(0, 4280);

  // Scroll wheel by X:0, Y:-5
  cy.scrollTo(0, 4275);

  // Scroll wheel by X:-2, Y:-2
  cy.scrollTo(0, 4273);

  // Scroll wheel by X:0, Y:-5
  cy.scrollTo(0, 4268);

  // Scroll wheel by X:-18, Y:-146
  cy.scrollTo(0, 4122);

  // Scroll wheel by X:0, Y:-384
  cy.scrollTo(0, 3738);

  // Scroll wheel by X:-35, Y:-205
  cy.scrollTo(0, 3533);

  // Scroll wheel by X:0, Y:-12
  cy.scrollTo(0, 3521);

  // Scroll wheel by X:8, Y:-19
  cy.scrollTo(0, 3502);

  // Scroll wheel by X:0, Y:-6
  cy.scrollTo(0, 3496);

  // Scroll wheel by X:-29, Y:-98
  cy.scrollTo(0, 3398);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 3396);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 3395);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 3393);

  // Scroll wheel by X:-15, Y:-25
  cy.scrollTo(0, 3368);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 3365);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 3364);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 3363);

  // Scroll wheel by X:-2, Y:-2
  cy.scrollTo(0, 3361);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 3360);

  // Scroll wheel by X:-2, Y:-2
  cy.scrollTo(0, 3358);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 3357);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 3356);

  // Scroll wheel by X:0, Y:-4
  cy.scrollTo(0, 3352);

  // Scroll wheel by X:-2, Y:-2
  cy.scrollTo(0, 3350);

  // Scroll wheel by X:0, Y:-3
  cy.scrollTo(0, 3347);

  // Scroll wheel by X:-2, Y:-2
  cy.scrollTo(0, 3345);

  // Scroll wheel by X:0, Y:-12
  cy.scrollTo(0, 3333);

  // Scroll wheel by X:-9, Y:-100
  cy.scrollTo(0, 3209);

  // Scroll wheel by X:0, Y:-456
  cy.scrollTo(0, 2776);

  // Scroll wheel by X:-17, Y:-115
  cy.scrollTo(0, 2662);

  // Scroll wheel by X:0, Y:-420
  cy.scrollTo(0, 2242);

  // Scroll wheel by X:-12, Y:-109
  cy.scrollTo(0, 2133);

  // Scroll wheel by X:0, Y:-674
  cy.scrollTo(0, 1459);

  // Scroll wheel by X:-10, Y:-84
  cy.scrollTo(0, 1375);

  // Scroll wheel by X:0, Y:-632
  cy.scrollTo(0, 743);

  // Scroll wheel by X:-9, Y:-90
  cy.scrollTo(0, 653);

  // Scroll wheel by X:0, Y:-852
  cy.scrollTo(0, 0);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 0);

  // Scroll wheel by X:-15, Y:50
  cy.scrollTo(0, 51);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 52);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 53);

  // Scroll wheel by X:0, Y:4
  cy.scrollTo(0, 57);

  // Scroll wheel by X:-2, Y:1
  cy.scrollTo(0, 57);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 60);

  // Scroll wheel by X:-21, Y:58
  cy.scrollTo(0, 119);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 120);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 121);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 122);

  // Scroll wheel by X:-13, Y:22
  cy.scrollTo(0, 144);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 146);

  // Scroll wheel by X:-2, Y:4
  cy.scrollTo(0, 150);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 152);

  // Scroll wheel by X:-10, Y:20
  cy.scrollTo(0, 172);

  // Scroll wheel by X:0, Y:6
  cy.scrollTo(0, 178);

  // Scroll wheel by X:6, Y:66
  cy.scrollTo(0, 244);

  // Scroll wheel by X:0, Y:12
  cy.scrollTo(0, 256);

  // Scroll wheel by X:-8, Y:38
  cy.scrollTo(0, 294);

  // Scroll wheel by X:0, Y:5
  cy.scrollTo(0, 299);

  // Scroll wheel by X:-2, Y:4
  cy.scrollTo(0, 303);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 304);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 305);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 306);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 307);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 309);

  // Scroll wheel by X:-2, Y:0
  cy.scrollTo(0, 309);

  // Scroll wheel by X:0, Y:9
  cy.scrollTo(0, 318);

  // Scroll wheel by X:4, Y:12
  cy.scrollTo(0, 330);

  // Scroll wheel by X:0, Y:14
  cy.scrollTo(0, 344);

  // Scroll wheel by X:-2, Y:2
  cy.scrollTo(0, 346);

  // Scroll wheel by X:0, Y:8
  cy.scrollTo(0, 354);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 355);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 356);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 357);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 358);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 359);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 360);

  // Scroll wheel by X:-9, Y:13
  cy.scrollTo(0, 373);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 376);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 377);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 379);

  // Scroll wheel by X:-2, Y:2
  cy.scrollTo(0, 381);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 383);

  // Scroll wheel by X:-2, Y:2
  cy.scrollTo(0, 385);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 387);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 388);

  // Scroll wheel by X:0, Y:5
  cy.scrollTo(0, 392);

  // Scroll wheel by X:-4, Y:4
  cy.scrollTo(0, 397);

  // Scroll wheel by X:0, Y:13
  cy.scrollTo(0, 410);

  // Scroll wheel by X:-13, Y:64
  cy.scrollTo(0, 474);

  // Scroll wheel by X:0, Y:144
  cy.scrollTo(0, 618);

  // Scroll wheel by X:-13, Y:136
  cy.scrollTo(0, 754);

  // Scroll wheel by X:0, Y:282
  cy.scrollTo(0, 1036);

  // Scroll wheel by X:2, Y:4
  cy.scrollTo(0, 1040);

  // Scroll wheel by X:0, Y:10
  cy.scrollTo(0, 1050);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1051);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1052);

  // Scroll wheel by X:-3, Y:3
  cy.scrollTo(0, 1055);

  // Scroll wheel by X:0, Y:10
  cy.scrollTo(0, 1065);

  // Scroll wheel by X:-2, Y:3
  cy.scrollTo(0, 1068);

  // Scroll wheel by X:0, Y:13
  cy.scrollTo(0, 1081);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1082);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1083);

  // Scroll wheel by X:-2, Y:2
  cy.scrollTo(0, 1085);

  // Scroll wheel by X:0, Y:4
  cy.scrollTo(0, 1089);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1090);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 1092);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1093);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 1095);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1096);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 1098);

  // Scroll wheel by X:-3, Y:6
  cy.scrollTo(0, 1104);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 1106);

  // Scroll wheel by X:-2, Y:2
  cy.scrollTo(0, 1108);

  // Scroll wheel by X:0, Y:2
  cy.scrollTo(0, 1110);

  // Scroll wheel by X:-2, Y:2
  cy.scrollTo(0, 1112);

  // Scroll wheel by X:0, Y:7
  cy.scrollTo(0, 1119);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1120);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1121);

  // Scroll wheel by X:-5, Y:7
  cy.scrollTo(0, 1128);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1129);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1130);

  // Scroll wheel by X:0, Y:7
  cy.scrollTo(0, 1137);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1138);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1139);

  // Scroll wheel by X:-1, Y:1
  cy.scrollTo(0, 1140);

  // Scroll wheel by X:0, Y:1
  cy.scrollTo(0, 1141);

  // Scroll wheel by X:-4, Y:4
  cy.scrollTo(0, 1145);

  // Scroll wheel by X:0, Y:3
  cy.scrollTo(0, 1148);

  // Scroll wheel by X:-2, Y:2
  cy.scrollTo(0, 1150);

  // Scroll wheel by X:0, Y:5
  cy.scrollTo(0, 1155);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 1155);

  // Scroll wheel by X:-18, Y:-34
  cy.scrollTo(0, 1120);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 1119);

  // Scroll wheel by X:-2, Y:-2
  cy.scrollTo(0, 1117);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 1116);

  // Scroll wheel by X:-11, Y:-14
  cy.scrollTo(0, 1102);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 1101);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 1100);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 1098);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 1097);

  // Scroll wheel by X:-1, Y:0
  cy.scrollTo(0, 1097);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 1096);

  // Scroll wheel by X:-10, Y:-10
  cy.scrollTo(0, 1086);

  // Scroll wheel by X:0, Y:-1
  cy.scrollTo(0, 1085);

  // Scroll wheel by X:-1, Y:0
  cy.scrollTo(0, 1085);

  // Scroll wheel by X:-1, Y:-1
  cy.scrollTo(0, 1085);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 1083);

  // Scroll wheel by X:-16, Y:-142
  cy.scrollTo(0, 941);

  // Scroll wheel by X:0, Y:-813
  cy.scrollTo(0, 128);

  // Scroll wheel by X:-31, Y:-76
  cy.scrollTo(0, 52);

  // Scroll wheel by X:0, Y:-2
  cy.scrollTo(0, 50);

  // Scroll wheel by X:-10, Y:-100
  cy.scrollTo(0, 0);

  // Scroll wheel by X:0, Y:-496
  cy.scrollTo(0, 0);
});