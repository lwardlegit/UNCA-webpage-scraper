import scrapy
import smtplib 
from email.mime.text import MIMEText


class Jobe_Scraper(scrapy.Spider):
    name = "Jobe"
    jobs = ''
    start_urls = ['https://jobs.unca.edu/postings/search?utf8=%E2%9C%93&query=&query_v0_posted_at_date=&2414%5B%5D=1&commit=Search']
    def parse(self, response):
        SET_SELECTOR = '.job-title'
	stringJobs=''
#need to get joblist out of a function
	
	
        for index in response.css(SET_SELECTOR):
            NAME_SELECTOR = 'a ::text'
            yield {
                'Job title': index.css(NAME_SELECTOR).extract_first(),
            }
	    jobList={'*': index.css(NAME_SELECTOR).extract_first()}
	    stringJobs+=(str(jobList))
	print(stringJobs)
	stringJobs.split("*")
	print(stringJobs)
	sender = 'lwardle@unca.edu'
	receivers = 'lwardle@unca.edu'
	body_of_email = 'Here are the Current UNCA Job Listings:'+stringJobs+''
	msg = MIMEText(body_of_email, 'html')
	msg['Subject'] = 'New Job Updates'
	msg['From'] = sender
	msg['To'] = receivers

	s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
	s.login(user = 'lwardle@unca.edu', password = 'Evaricky0')
	s.sendmail(sender, receivers, msg.as_string())
	s.quit()
