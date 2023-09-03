from main import webDriver
import pandas

if __name__ == "__main__":
    func = webDriver()
    func.startDriver()
    func.Browser()
    func.searchBar()
    dataLine1 = func.actions1()
    dataLine2 = func.actions2()
    jsonData = pandas.concat(dataLine1 + dataLine2, axis=1)
    jsonData.to_json("Wiki_Data.json")
    func.closeBrowser()