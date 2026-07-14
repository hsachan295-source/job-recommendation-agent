#!/usr/bin/env python3
import os
import json
from datetime import datetime

DB_PATH = os.path.join("tools", "applied_jobs.json")

# List of 100 top companies with roles & career links in India
COMPANIES_100 = [
    {"company": "Google India", "role": "AI Engineer Intern", "category": "AI", "url": "https://careers.google.com/"},
    {"company": "Microsoft India", "role": "Data Scientist I", "category": "DS", "url": "https://careers.microsoft.com/"},
    {"company": "Amazon India", "role": "Applied Scientist - Machine Learning", "category": "ML", "url": "https://www.amazon.jobs/"},
    {"company": "Meta India", "role": "Machine Learning Engineer", "category": "ML", "url": "https://www.metacareers.com/"},
    {"company": "Apple India", "role": "Data Analyst (App Store)", "category": "DA", "url": "https://www.apple.com/careers/"},
    {"company": "Netflix India", "role": "Analytics Engineer", "category": "DA", "url": "https://jobs.netflix.com/"},
    {"company": "Uber India", "role": "Data Scientist (Rides)", "category": "DS", "url": "https://www.uber.com/careers/"},
    {"company": "Ola Cabs", "role": "Data Analyst (Operations)", "category": "DA", "url": "https://www.olacabs.com/careers"},
    {"company": "Paytm", "role": "Data Scientist (Fraud Analytics)", "category": "DS", "url": "https://careers.paytm.com/"},
    {"company": "PhonePe", "role": "Data Analyst (Merchant Payments)", "category": "DA", "url": "https://www.phonepe.com/careers/"},
    {"company": "CRED", "role": "Data Scientist (Risk & Underwriting)", "category": "DS", "url": "https://careers.cred.club/"},
    {"company": "Razorpay", "role": "Data Analyst (Treasury)", "category": "DA", "url": "https://razorpay.com/jobs/"},
    {"company": "Flipkart", "role": "Data Scientist (Recommendation Systems)", "category": "DS", "url": "https://www.flipkartcareers.com/"},
    {"company": "Myntra", "role": "Data Analyst (Fashion Trends)", "category": "DA", "url": "https://careers.myntra.com/"},
    {"company": "Swiggy", "role": "Data Scientist (Delivery Optimization)", "category": "DS", "url": "https://careers.swiggy.com/"},
    {"company": "Zomato", "role": "Data Analyst (Customer Insights)", "category": "DA", "url": "https://www.zomato.com/careers"},
    {"company": "InMobi", "role": "Machine Learning Engineer (AdTech)", "category": "ML", "url": "https://www.inmobi.com/company/careers"},
    {"company": "ShareChat", "role": "ML Engineer (Recommendation)", "category": "ML", "url": "https://sharechat.com/careers"},
    {"company": "Zepto", "role": "Data Analyst (Supply Chain)", "category": "DA", "url": "https://www.zepto.com/careers"},
    {"company": "Blinkit", "role": "Data Analyst (Dark Store Metrics)", "category": "DA", "url": "https://blinkit.com/careers"},
    {"company": "Nykaa", "role": "Data Analyst (Marketing)", "category": "DA", "url": "https://www.nykaa.com/careers"},
    {"company": "Reliance Jio", "role": "AI Engineer (JioGenAI)", "category": "AI", "url": "https://careers.jio.com/"},
    {"company": "Bharti Airtel", "role": "Data Scientist (Network Churn)", "category": "DS", "url": "https://www.airtel.in/careers"},
    {"company": "Tata 1mg", "role": "Data Scientist (Healthcare Analytics)", "category": "DS", "url": "https://www.1mg.com/careers"},
    {"company": "PharmEasy", "role": "Data Analyst", "category": "DA", "url": "https://pharmeasy.in/careers"},
    {"company": "Groww", "role": "Data Scientist (Investment Products)", "category": "DS", "url": "https://groww.in/careers"},
    {"company": "Zerodha", "role": "Data Analyst (Trading Systems)", "category": "DA", "url": "https://zerodha.tech/careers/"},
    {"company": "Upstox", "role": "Data Scientist", "category": "DS", "url": "https://upstox.com/careers/"},
    {"company": "CoinDCX", "role": "Data Analyst (Crypto Compliance)", "category": "DA", "url": "https://coindcx.com/careers"},
    {"company": "Wipro", "role": "Data Analyst Graduate Trainee", "category": "DA", "url": "https://careers.wipro.com/"},
    {"company": "Infosys", "role": "Junior Machine Learning Engineer", "category": "ML", "url": "https://careers.infosys.com/"},
    {"company": "TCS", "role": "Data Science Associate", "category": "DS", "url": "https://www.tcs.com/careers"},
    {"company": "Cognizant", "role": "Data Analyst (SQL & Power BI)", "category": "DA", "url": "https://careers.cognizant.com/"},
    {"company": "Accenture", "role": "Data Analyst Trainee", "category": "DA", "url": "https://www.accenture.com/careers"},
    {"company": "Capgemini", "role": "Data Analyst (Business Intelligence)", "category": "DA", "url": "https://www.capgemini.com/careers/"},
    {"company": "Tech Mahindra", "role": "Data Analyst", "category": "DA", "url": "https://careers.techmahindra.com/"},
    {"company": "HCLTech", "role": "Machine Learning Associate", "category": "ML", "url": "https://www.hcltech.com/careers"},
    {"company": "LTIMindtree", "role": "Data Scientist", "category": "DS", "url": "https://www.ltimindtree.com/careers/"},
    {"company": "Genpact", "role": "Data Analyst (Operations)", "category": "DA", "url": "https://www.genpact.com/careers"},
    {"company": "EXL Service", "role": "Data Analyst (Decision Science)", "category": "DA", "url": "https://www.exlservice.com/careers"},
    {"company": "Mu Sigma", "role": "Decision Scientist Trainee", "category": "DS", "url": "https://www.mu-sigma.com/careers"},
    {"company": "Fractal Analytics", "role": "Junior Data Scientist", "category": "DS", "url": "https://fractal.ai/careers/"},
    {"company": "Tiger Analytics", "role": "Data Scientist", "category": "DS", "url": "https://www.tigeranalytics.com/careers/"},
    {"company": "LatentView Analytics", "role": "Data Analyst (Marketing)", "category": "DA", "url": "https://www.latentview.com/careers/"},
    {"company": "Quantiphi", "role": "Machine Learning Engineer", "category": "ML", "url": "https://careers.quantiphi.com/"},
    {"company": "Sigmoid", "role": "Data Engineer / Analyst", "category": "DA", "url": "https://www.sigmoid.com/careers/"},
    {"company": "Absolutdata", "role": "Data Scientist", "category": "DS", "url": "https://www.absolutdata.com/careers/"},
    {"company": "Bridgei2i", "role": "Data Analyst", "category": "DA", "url": "https://bridgei2i.com/careers/"},
    {"company": "Gramener", "role": "Data Analyst / Visualizer", "category": "DA", "url": "https://gramener.com/careers/"},
    {"company": "Decision Point", "role": "Data Analyst", "category": "DA", "url": "https://decisionpoint.in/careers"},
    {"company": "IBM India", "role": "Associate Data Scientist", "category": "DS", "url": "https://www.ibm.com/careers/in-en"},
    {"company": "Oracle India", "role": "Data Analyst", "category": "DA", "url": "https://careers.oracle.com/"},
    {"company": "SAP Labs India", "role": "Machine Learning Developer", "category": "ML", "url": "https://www.sap.com/about/careers.html"},
    {"company": "Cisco India", "role": "Data Scientist", "category": "DS", "url": "https://jobs.cisco.com/"},
    {"company": "Intel India", "role": "AI Engineer Intern", "category": "AI", "url": "https://www.intel.com/content/www/us/en/jobs/locations/india.html"},
    {"company": "Nvidia India", "role": "AI Engineer (Deep Learning)", "category": "AI", "url": "https://www.nvidia.com/en-us/about-nvidia/careers/"},
    {"company": "Qualcomm India", "role": "Machine Learning Engineer", "category": "ML", "url": "https://www.qualcomm.com/company/careers"},
    {"company": "AMD India", "role": "ML Software Engineer", "category": "ML", "url": "https://careers.amd.com/"},
    {"company": "Samsung R&D", "role": "AI Engineer (Vision/NLP)", "category": "AI", "url": "https://www.samsung.com/in/about-us/careers/"},
    {"company": "Adobe India", "role": "Machine Learning Engineer", "category": "ML", "url": "https://www.adobe.com/careers.html"},
    {"company": "Salesforce India", "role": "Data Scientist", "category": "DS", "url": "https://www.salesforce.com/company/careers/"},
    {"company": "VMware India", "role": "Data Scientist", "category": "DS", "url": "https://careers.vmware.com/"},
    {"company": "Dell India", "role": "Data Analyst", "category": "DA", "url": "https://jobs.dell.com/"},
    {"company": "HP India", "role": "Data Analyst", "category": "DA", "url": "https://jobs.hp.com/"},
    {"company": "Lenovo India", "role": "Data Analyst", "category": "DA", "url": "https://jobs.lenovo.com/"},
    {"company": "Sony India", "role": "AI Engineer", "category": "AI", "url": "https://www.sony.co.in/section/careers"},
    {"company": "Panasonic India", "role": "Data Analyst", "category": "DA", "url": "https://www.panasonic.com/in/corporate/careers.html"},
    {"company": "LG India", "role": "Data Analyst", "category": "DA", "url": "https://www.lg.com/in/about-lg/careers"},
    {"company": "Bosch India", "role": "AI Engineer", "category": "AI", "url": "https://careers.bosch.com/en/"},
    {"company": "Siemens India", "role": "Data Scientist", "category": "DS", "url": "https://new.siemens.com/in/en/company/jobs.html"},
    {"company": "GE India", "role": "Data Scientist", "category": "DS", "url": "https://www.ge.com/careers"},
    {"company": "Philips India", "role": "Data Scientist", "category": "DS", "url": "https://www.careers.philips.com/global/en"},
    {"company": "Abbott India", "role": "Data Analyst", "category": "DA", "url": "https://www.abbott.in/careers.html"},
    {"company": "Pfizer India", "role": "Data Analyst", "category": "DA", "url": "https://www.pfizer.com/careers"},
    {"company": "Novartis India", "role": "Data Scientist", "category": "DS", "url": "https://www.novartis.com/careers"},
    {"company": "Roche India", "role": "Data Scientist", "category": "DS", "url": "https://www.roche.com/careers"},
    {"company": "McKinsey India", "role": "Data Analyst", "category": "DA", "url": "https://www.mckinsey.com/careers"},
    {"company": "BCG India", "role": "Data Analyst", "category": "DA", "url": "https://careers.bcg.com/"},
    {"company": "Bain & Company", "role": "Data Analyst", "category": "DA", "url": "https://www.bain.com/careers/"},
    {"company": "Deloitte India", "role": "Data Analyst", "category": "DA", "url": "https://www.deloitte.com/in/en/careers"},
    {"company": "EY India", "role": "Data Analyst", "category": "DA", "url": "https://www.ey.com/en_in/careers"},
    {"company": "KPMG India", "role": "Data Analyst", "category": "DA", "url": "https://home.kpmg/in/en/home/careers.html"},
    {"company": "PwC India", "role": "Data Analyst", "category": "DA", "url": "https://www.pwc.in/careers.html"},
    {"company": "Goldman Sachs", "role": "Data Scientist", "category": "DS", "url": "https://www.goldmansachs.com/careers/"},
    {"company": "Morgan Stanley", "role": "Data Scientist", "category": "DS", "url": "https://www.morganstanley.com/about-us/careers"},
    {"company": "J.P. Morgan", "role": "Data Scientist", "category": "DS", "url": "https://careers.jpmorgan.com/"},
    {"company": "HSBC India", "role": "Data Analyst", "category": "DA", "url": "https://www.hsbc.com/careers"},
    {"company": "Citi India", "role": "Data Analyst", "category": "DA", "url": "https://careers.citigroup.com/"},
    {"company": "Standard Chartered", "role": "Data Analyst", "category": "DA", "url": "https://www.sc.com/en/careers/"},
    {"company": "ICICI Bank", "role": "Data Analyst", "category": "DA", "url": "https://www.icicibankcareers.com/"},
    {"company": "HDFC Bank", "role": "Data Analyst", "category": "DA", "url": "https://careers.hdfcbank.com/"},
    {"company": "Axis Bank", "role": "Data Analyst", "category": "DA", "url": "https://www.axisbank.com/careers"},
    {"company": "SBI", "role": "Data Analyst", "category": "DA", "url": "https://sbi.co.in/web/careers"},
    {"company": "Kotak Bank", "role": "Data Analyst", "category": "DA", "url": "https://www.kotak.com/en/careers.html"},
    {"company": "Bajaj Finserv", "role": "Data Analyst", "category": "DA", "url": "https://www.bajajfinserv.in/careers"},
    {"company": "Muthoot Finance", "role": "Data Analyst", "category": "DA", "url": "https://www.muthootfinance.com/careers"},
    {"company": "Aditya Birla", "role": "Data Analyst", "category": "DA", "url": "https://careers.adityabirla.com/"},
    {"company": "Reliance Industries", "role": "Data Analyst", "category": "DA", "url": "https://relianceindustries.careers/"},
    {"company": "Adani Group", "role": "Data Analyst", "category": "DA", "url": "https://www.adani.com/careers"},
    {"company": "Mahindra Group", "role": "Data Analyst", "category": "DA", "url": "https://www.mahindra.com/careers"}
]

def populate():
    # If file exists, read existing data
    if os.path.exists(DB_PATH):
        try:
            with open(DB_PATH, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []
    else:
        data = []

    # Exclude duplicates based on company name
    existing_companies = {app["company"].lower() for app in data}
    
    added_count = 0
    for job in COMPANIES_100:
        if job["company"].lower() not in existing_companies:
            clean_company = "".join(c for c in job["company"] if c.isalnum()).lower()
            cv_filename = f"cv/main_{clean_company}.pdf"
            
            new_app = {
                "id": len(data) + 1,
                "role": job["role"],
                "company": job["company"],
                "url": job["url"],
                "category": job["category"],
                "cv_path": cv_filename,
                "date": datetime.now().strftime("%Y-%m-%d"),
                "status": "Applied"
            }
            data.append(new_app)
            added_count += 1

    # Save data back to json
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"[Agent] Database populated! Added {added_count} new job records to {DB_PATH}.")

if __name__ == "__main__":
    populate()
