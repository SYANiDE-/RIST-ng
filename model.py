#!/usr/bin/env python3
from inspect import getmembers
import webbrowser as WB
from selenium.webdriver.common.by import By
from selenium import webdriver
# import mechanize

NOTES="""\
Good dummy IP:              14.232.1.237
Good dummy domain:          www.yesterdazelolz.com
Good dummy url:             http://www.yesterdazelolz.com/
                            https://swatblog.rtgp.xyz/?
                            http://ourworldofpixels.com/piano/
                            http://gifdanceparty.giphy.com/
                            http://www.dogbreedchart.com/
                            http://roxik.com/require.html
                            http://penisland.net/index.html
                            http://stuffonmycat.com/
                            https://www.hectorsalamanca.com/
"""

class methods():
    def __init__(self, WORKING_SET, WORKING_OPT, BR, SE):
        self.BrowserDict = {
            0:'mozilla', 1:'firefox', 2:'netscape', 3:'galeon', 4:'epiphany',
            5:'skipstone', 6:'kfmclient', 7:'konqueror', 8:'kfm', 9:'mosaic',
            10:'opera', 11:'grail', 12:'links', 13:'elinks', 14:'lynx',
            15:'w3m', 16:'windows-default', 17:'macosx', 18:'safari', 19:'google-chrome',
            20:'chrome', 21:'chromium', 22:'chromium-browser'
        }       
        SELENIUMS = {
            0:'Chrome', 1:'Edge', 2:'Firefox', 3:'Ie', 4:'Opera', 5:'Safari'
        }
        self.WORKING_SET = WORKING_SET
        self.WORKING_OPT = WORKING_OPT
        self.BR = BR
        self.SE = SE


    def _return(self):
        return [ (item, 0) for item, func in getmembers(self) if not item.startswith("_") ]

    def _simple(self, IoC, loc, postfix=""):   #for simple concatenation and spawn
        url = loc+ IoC + postfix
        self.__spawn__(url)

    def __spawn__(self, url):                  #launches URL in new tab
        # self.BR = WB.get(self.BrowserDict[int(self.WORKING_OPT['browser'])])
        self.BR.open_new_tab(url)
    #
    #
    ###  Drop-ins below this line  ####################################################



    def i_Robtex(self, IoC):
        self._simple(IoC.replace(".", "/", 3), "http://www.robtex.com/en/advisory/ip/", "/")

    def i_DNSlytics(self, IoC):
        self._simple(IoC, "https://dnslytics.com/ip/")

    def i_whois(self, IoC):
        self._simple(IoC, "https://www.whois.com/whois/")

    def i_MultiRBL(self, IoC):
        self._simple(IoC, "http://multirbl.valli.org/lookup/", ".html")

    def d_MultiRBL(self, IoC):
        self._simple(IoC, "http://multirbl.valli.org/lookup/", ".html")

    def i_MXtoolbox(self, IoC):
        self._simple(IoC, "http://mxtoolbox.com/SuperTool.aspx?action=blacklist:", "&run=toolspage")

    def i_Hetrix(self, IoC):
        self._simple(IoC, "https://hetrixtools.com/blacklist-check/")

    def i_Virustotal(self, IoC):
        self._simple(IoC, "https://www.virustotal.com/#/search/", "/information/")

    def u_Virustotal(self, IoC):
        self._simple(IoC, "https://www.virustotal.com/#/search/", "/information/")
 
    def d_Virustotal(self, IoC):
        self._simple(IoC, "https://www.virustotal.com/#/search/", "/information/")

    def i_AntiAbuseProject(self, IoC):
        self._simple(IoC, "http://www.anti-abuse.org/multi-rbl-check-results/?host=")

    def i_AbuseIPDB(self, IoC):
        self._simple(IoC, "https://www.abuseipdb.com/report-history/")

    def i_ProjectHoneypot(self, IoC):
        self._simple(IoC,"https://www.projecthoneypot.org/ip_")

    def i_Deepviz(self, IoC):
        self._simple(IoC, "https://search.deepviz.com/?s=")

    def d_Deepviz(self, IoC):
        self._simple(IoC, "https://search.deepviz.com/?s=")

    def i_AlienVaultOTX(self, IoC):
        self._simple(IoC, "https://otx.alienvault.com/browse/pulses/?q=", "&type=all")

    def i_IBM_XForce(self, IoC):
        self._simple(IoC, "https://exchange.xforce.ibmcloud.com/search/")

    def d_IBM_XForce(self, IoC):
        self._simple(IoC, "https://exchange.xforce.ibmcloud.com/search/")

    def i_ThreatMiner(self, IoC):
        self._simple(IoC, "https://www.threatminer.org/host.php?q=")

    def d_ThreatMiner(self, IoC):
        self._simple(IoC, "https://www.threatminer.org/host.php?q=")

    def i_ThreatCrowd(self, IoC):
        self._simple(IoC, "https://www.threatcrowd.org/ip.php?ip=")

    def d_ThreatCrowd(self, IoC):
        self._simple(IoC, "https://www.threatcrowd.org/domain.php?domain=")

    def i_ShodanIO(self, IoC):
        self._simple(IoC, "https://www.shodan.io/search?query=")

    def d_ShodanIO(self, IoC):
        self._simple(IoC, "https://www.shodan.io/search?query=")
    
    def i_CiscoTalos(self, IoC):
        self._simple(IoC, "https://talosintelligence.com/reputation_center/lookup?search=")

    def d_CiscoTalos(self, IoC):
        self._simple(IoC, "https://talosintelligence.com/reputation_center/lookup?search=")

    def i_Hashdd(self, IoC):
        self._simple(IoC, "https://hashdd.com/i/")

    def d_Hashdd(self, IoC):
        self._simple(IoC, "https://hashdd.com/i/")
 
    def d_DNSspy(self, IoC):
        self._simple(IoC, "https://dnsspy.io/scan/")

    def d_DNSDumpster(self, IoC):
        SE = self.SE()      #webdriver.[selenium browser]()
        SE.get("https://dnsdumpster.com")
        textbox = SE.find_element_by_name('targetip')
        textbox.send_keys(IoC)
        textbox.submit()
    
    def u_JoeSandbox(self, IoC):
        SE = self.SE()      #webdriver.[selenium browser]()
        SE.get("https://www.joesandbox.com/#windows")
        cookie_policy = SE.find_element_by_class_name("cc-btn")
        cookie_policy.click()
        textbox = BR.find_element_by_name("url")
        textbox.send_keys(IoC)
        checkbox = BR.find_element_by_name("tandc")
        checkbox.send_keys(" ")
        textbox.submit()
        
    def u_URLscanIO(self, IoC):
        SE = self.SE()
        SE.get("https://urlscan.io")
        textbox = SE.find_element_by_id("url")
        textbox.send_keys(IoC)
        textbox.submit()

    def d_MalwareDomainList(self, IoC):
        SE = self.SE()
        SE.get("http://www.malwaredomainlist.com/mdl.php")
        A = SE.find_element_by_css_selector("table tbody tr td input")
        A.send_keys(IoC)
        A.submit()

    def u_PhishTank(self, IoC):
        SE = self.SE()
        textbox = SE.find_element_by_name("isaphishurl")
        textbox.clear()
        textbox.send_keys(IoC)
        textbox.submit()

    def i_RiskIQ(self, IoC):
        self._simple(IoC, "https://community.riskiq.com/search/")

    def u_RiskIQ(self, IoC):
        self._simple(IoC, "https://community.riskiq.com/search/")

    def d_RiskIQ(self, IoC):
        self._simple(IoC, "https://community.riskiq.com/search/")

    def u_TrendMicro(self, IoC):
        SE = self.SE()
        SE.get("https://global.sitesafety.trendmicro.com/")
        textbox = SE.find_element_by_id("urlname")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_URLVoid(self, IoC):
        SE = self.SE()
        SE.get("http://www.urlvoid.com/")
        textbox = SE.find_element_by_tag_name("input")
        textbox.send_keys(IoC)
        textbox.submit()

    def i_IPVoid(self, IoC):
        SE = self.SE()
        SE.get("http://www.ipvoid.com/ip-blacklist-check/")
        textbox = SE.find_element_by_css_selector("div input")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_IsItHacked(self, IoC):
        SE = self.SE()
        SE.get("http://www.isithacked.com/")
        textbox = SE.find_elelement_by_css_selector("div input")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_ZScalerZulu(self, IoC):
        SE = self.SE()
        SE.get("https://zulu.zscaler.com/")
        textbox = SE.find_element_by_css_selector("div #url")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_URLqueryNET(self, IoC):
        SE = self.SE()
        SE.get("http://onlinelinkscan.com")
        textbox = SE.find_element_by_css_selector("table tbody tr td input")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_OnlineLinkScan(self, IoC):
        SE = self.SE()
        SE.get("http://onlinelinkscan.com")
        textbox = SE.find_element_by_name("lookup")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_UnmaskParasites(self, IoC):
        SE = self.SE()
        SE.get("http://www.unmaskparasites.com/security-report/")
        toolbox = SE.find_element_by_id("id_siteUrl")
        toolbox.send_keys(IoC)
        textbox.submit()

    def u_BuiltWith(self, IoC):
        SE = self.SE()
        SE.get("https://builtwith.com")
        textbox = SE.find_element_by_css_selector("form div div input")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_WebInspector(self, IoC):
        SE = self.SE()
        SE.get("https://app.webinspector.com/")
        textbox = SE.find_element_by_id("url")
        textbox.clear()
        textbox.send_keys(IoC)
        textbox.submit()

    def u_ReScanPro(self, IoC):
        SE = self.SE()
        SE.get("https://rescan.pro/")
        textbox = SE.find_element_by_id("input_url")
        textbox.clear()
        textbox.send_keys(IoC)
        textbox.submit()

    def u_PCRisk(self, IoC):
        SE = self.SE()
        SE.get("https://scanner.pcrisk.com/")
        textbox = SE.find_element_by_id("url_input_field")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_SiteGuarding(self, IoC):
        SE = self.SE()
        SE.get("https://www.siteguarding.com/en/sitecheck")
        textbox = SE.find_element_by_id("website_url")
        textbox.send_keys(IoC)
        textbox.submit()

    def u_NetCraft(self, IoC):
        SE = self.SE()
        SE.get("https://searchdns.netcraft.com/")
        textbox = SE.find_element_by_name("host")
        textbox.send_keys(IoC)
        textbox.submit()

    def d_Quttera(self, IoC):
        SE = self.SE()
        SE.get("https://quttera.com/website-malware-scanner")
        textbox = SE.find_element_by_id("url_input_field")
        textbox.send_keys(IoC)
        textbox.submit()
        
    def u_KasperskyVirusDesk(self, IoC):
        SE = self.SE()
        SE.get("https://virusdesk.kaspersky.com/")
        textbox = SE.find_element_by_id("txt-input-01")
        textbox.send_keys(IoC)
        textbox.submit()

    def d_HackerCombat(self, IoC):
        SE = self.SE()
        SE.get("https://hackercombat.com/website-malware-scanner/")
        textbox = SE.find_element_by_name("site")
        textbox.send_keys(IoC)
        textbox.submit()

    def i_OPSWAT(self, IoC):
        SE = self.SE()
        SE.get("https://metadefender.opswat.com/#!/")
        textbox = SE.find_element_by_id("homepage_search_box")
        textbox.send_keys(IoC)
        submit = SE.find_element_by_id("analyze_btn")
        submit.click()

