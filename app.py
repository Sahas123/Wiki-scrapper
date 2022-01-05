import random
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from flask import Flask
from flask import Flask, render_template, request, jsonify

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def root():

        return render_template('root.html')

@app.route('/result', methods=['POST','GET'])
def result():

            link=request.form['num1']
            #link1="/https://en.wikipedia.org/wiki/KL_Rahul"



            browser=webdriver.Chrome(executable_path=ChromeDriverManager().install())
            #browser.openUrl("https://www.flipkart.com/")
            (browser.get(link))

            #print(browser.find_elements_by_xpath("/html/body/div[4]/div[3]/div[5]/div[1]/p[9]/text()[1]"))
            text1=browser.find_elements_by_class_name("mw-parser-output")
            #print(len(text1))
            #print(type(text1))
           # wikicontent=[]
            for d in text1:
                data=d.text
                file = pd.read_csv(data)
                #wikicontent.append(data)
                return render_template("results.html",result=file)
if __name__ == '__main__':
    app.run(debug=True,port=8003)









