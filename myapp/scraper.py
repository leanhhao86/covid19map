import requests
from bs4 import BeautifulSoup

def scrape_all():
	# Not a good source though
	URL = "https://vi.wikipedia.org/wiki/Bản_mẫu:Dữ_liệu_đại_dịch_COVID-19/Số_ca_nhiễm_theo_tỉnh_thành_tại_Việt_Nam"
	page = requests.get(URL)

	soup = BeautifulSoup(page.content, "html.parser")

	# table body that contains real data
	tbody = soup.find_all("tbody")[0]

	# omitting the headers
	trs = tbody.find_all("tr")[1:]

	# get sum data (number of regions, number of cases, hospitalized, others, cured, deaths)
	headers = trs[0].find_all("th")

	head = dict()
	head["allregions"] = headers[0].text.strip()
	head["allinfected"] = headers[1].text.strip()
	head["allhospitalized"] = headers[2].text.strip()
	head["allother"] = headers[3].text.strip()
	head["allcured"] = headers[4].text.strip()
	head["alldeaths"] = headers[5].text.strip()
	# print(head)

	region_tr = trs[1:]
	figures = []
	for tr in region_tr:
		tds = tr.find_all("td")
		if len(tds) == 6:
			body = dict()
			body["name"] = tds[0].text.strip()
			body["infected"] = int(tds[1].text.strip().replace(".",""))
			body["hospitalized"] = int(tds[1].text.strip().replace(".",""))
			body["other"] = int(tds[3].text.strip().replace(".",""))
			body["cured"] = int(tds[4].text.strip().replace(".", ""))
			body["deaths"] = int(tds[5].text.strip().replace(".",""))

			head[tds[0].text.strip()] = body

	return head



if __name__ == "__main__":
	scrape_all()

