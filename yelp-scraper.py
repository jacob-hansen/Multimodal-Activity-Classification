import requests
from csv import writer
from bs4 import BeautifulSoup
# from MostPopulatedCitiesInEachStateRetriever import getMostPopulatedCities

# 1. Separate list of abbreviations from cities
def YelpDatasetGetter():
    citiesList = [["MA", "Boston"]]#, ["MA", "Cambridge"]]# getMostPopulatedCities()
    maxListings = 10 # takes approximatly the top 10*(maxListings//10) listings
    maxReviewNum = 10 # takes approximatly the top 10*(maxReviewNum//10) reviews
    tempReview = []  # temporarily stores review data

    with open("yelpReviewsDataset.csv", "w") as csv_file:
        csv_writer = writer(csv_file)

        headerrow = ["placeName", "rating", "reviewText"]
        csv_writer.writerow(headerrow)

        for row in citiesList:
            currentState = row[0]
            for currentCity in row[1:]:
                searchURL = (
                    "https://www.yelp.com/search?find_desc=activities&find_loc="
                    + currentCity
                    + "%2C+"
                    + currentState
                    + "&ns=1&sortby=review_count&start="
                )
                placeList = []
                i = 0
                while i < maxListings:
                    """Pull All the objects of the right class from each page"""
                    restaurantSearchPage = requests.get(searchURL)
                    restaurantSearchPageSoup = BeautifulSoup(
                        restaurantSearchPage.text, "html.parser")
                    newData = restaurantSearchPageSoup.findAll(class_="css-1uq0cfn")

                    """Pull URL extentions for objects of interest"""
                    noValidData = True
                    for data in newData:
                        try:
                            if not data.find("a")["href"]:
                                continue
                            else:
                                placeURLEnding = data.find("a")["href"]
                                placeList.append(placeURLEnding[1:])
                                noValidData = False
                        except TypeError:
                            continue
                    if noValidData: # Page has no more listings
                        break
                    else: # Up the count and keep searching
                        i += 10

                # gets URL for each restaurant listing
                for urlExt in placeList:
                    i = 0
                    print("Scraping ", "https://yelp.com", urlExt)

                    placeURL = "https://yelp.com" + urlExt
                    placeName = ((urlExt.split("/")[-1]).split("?"))[0].replace("-", " ")

                    while i < maxReviewNum:
                        placeURL = "https://yelp.com" + urlExt + "&start=" + str(i)
                        placePage = requests.get(placeURL)
                        placePageSoup = BeautifulSoup(
                            placePage.text, "html.parser"
                        )

                        reviewsRawList = placePageSoup.findAll(
                            "div", class_="review__09f24__oHr9V border-color--default__09f24__NPAKY",)

                            #class_="review__09f24__oHr9V border-color--default__09f24__NPAKY"
                        #)
                        print(reviewsRawList)
                        for review in reviewsRawList:
                            testing = review.find("aria-label")
                            print(testing)
                        sysbreak()


                        for review in reviewsRawList:
                            tempReview.append(placeName)
                            reviewRating = review.find("aria-label")
                            print(reviewRating)
                            sysbreak()

                             # gets the number of stars in the rating (1-5)
                            tempReview.append(reviewRating)
                            reviewText = review.find("span", {"lang": "en"}).getText()
                            tempReview.append(reviewText)
                            csv_writer.writerow(tempReview)
                            tempReview = []
                        i += 10
                    # break  # testing
                # break  # testing
            # break  # testing


if __name__ == "__main__":
    YelpDatasetGetter()
