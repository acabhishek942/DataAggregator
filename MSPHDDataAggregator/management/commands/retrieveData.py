from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from django.core.management.base import BaseCommand, CommandError

from MSPHDDataAggregator.models import Applicant, ApplicationStatusDetails

# create a new chrome session
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.implicitly_wait(10)


class Command(BaseCommand):

	def handle(self, *args, **kwargs):
		# navigate to the application home page
		driver.get("https://engineering.academickeys.com")


		link = driver.find_element_by_link_text('Who\'s Who')
		link.click()




		driver.find_element_by_xpath("//select[@name='form[category_IDXs][]']/option[text()='Graduate Student']").click()
		driver.find_element_by_xpath("//select[@name='form[field_IDXs][]']/option[text()='Engineering - Other']").click()

		driver.find_element_by_xpath("//input[@value='Search Database']").click()

		nameList=driver.find_elements_by_xpath("//div[@id='layout_main']/div/table/tbody/tr/td/table[2]/tbody/tr/td[2]/strong[1]")
		positionList = driver.find_elements_by_xpath("//div[@id='layout_main']/div/table/tbody/tr/td/table[2]/tbody/tr/td[2]/strong[2]")
		universityList = driver.find_elements_by_xpath("//div[@id='layout_main']/div/table/tbody/tr/td/table[2]/tbody/tr/td[2]/strong[3]")
		for webelement in nameList:
			studentCandidate = Applicant(studentName=webelement.text, slug=webelement.text, undergradInstittute="DUmmyValue",
				undergradDegree="B.S.", undergradBranch="foo Branch", undergradGPA=3.4, GREScore=320, GMATScore=123,
				email="lorna@dummy.com")
			studentCandidate.save()
			applicationStatus = ApplicationStatusDetails(applicant_id=studentCandidate.id, applicationUniversity="Juni", applicationStatus="Applied")
			
			applicationStatus.save()

# driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr/td/table[2]/tbody/tr[1]/td[2]/strong[1]/a").click()
# academic_title=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[2]").text
# personalwebsite=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[4]/a").text
# current_dept=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[6]").text
# current_insitution=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[8]").text
# highest_degree=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[12]").text
# degree_year=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[13]").text
# degree_insti=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[14]").text
# expertise=driver.find_element_by_xpath("//div[@id='layout_main']/div/table/tbody/tr[1]/td/ul/div/li[18]").text

# print("NAME : ",name)
# print("Acadamic title : ",academic_title)
# print("Department name : ",current_dept)
# print("Institution Name : ",current_insitution)
# print("Expertise : ", expertise)