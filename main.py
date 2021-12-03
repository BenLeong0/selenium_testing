from enum import Enum
import os
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

os.environ['PATH'] += r";C:/Users/benle/SeleniumDrivers"

def main():
    driver = webdriver.Chrome()
    driver.get("https://home-journey.comparethemarket.com")

    cookies_popup(driver)

    page_1(driver)
    go_to_next_page(driver)

    page_2(driver)
    go_to_next_page(driver)

    page_3(driver)
    go_to_next_page(driver)

    page_4(driver)
    go_to_next_page(driver)

    page_5(driver)
    go_to_next_page(driver)

    page_6(driver)
    go_to_next_page(driver)

    page_7(driver)
    driver.find_element(By.ID, "getYourQuotes").click()

    results_page(driver)


def cookies_popup(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "consent-preferences")))
    driver.find_element(By.CLASS_NAME, "btn-manage-prefs").click()


def go_to_next_page(driver: webdriver.Chrome):
    driver.find_element(By.ID, "next").click()


def page_1(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Questions_PolicyDetails")))

    # Title
    class TITLE_DICT(Enum):
        MR = "HomeInsurance_Questions_PolicyDetails_Policyholder_Title_MR"
        MRS = "HomeInsurance_Questions_PolicyDetails_Policyholder_Title_MRS"
        MS = "HomeInsurance_Questions_PolicyDetails_Policyholder_Title_MS"
        MISS = "HomeInsurance_Questions_PolicyDetails_Policyholder_Title_MISS"
    driver.find_element(By.ID, TITLE_DICT.MR.value).click()

    # Name
    first_name, last_name = ("Bobby", "Fucko")
    driver.find_element(By.ID, "HomeInsurance_Questions_PolicyDetails_Policyholder_FirstName").send_keys(first_name)
    driver.find_element(By.ID, "HomeInsurance_Questions_PolicyDetails_Policyholder_LastName").send_keys(last_name)

    # Address
    house_number, post_code = ("1", "CM12 0XP")
    driver.find_element(By.ID, "HomeInsurance_Questions_PolicyDetails_YourAddress_HouseNumberOrName").send_keys(house_number)
    driver.find_element(By.ID, "HomeInsurance_Questions_PolicyDetails_YourAddress_Postcode").send_keys(post_code)
    driver.find_element(By.ID, "YourAddress_FindMyAddress").click()

    # Ownership
    class OWNERSHIP_DICT(Enum):
        MORTGAGED = "HomeInsurance_Questions_PolicyDetails_OwnershipCategory_03"
        OWNED_OUTRIGHT = "HomeInsurance_Questions_PolicyDetails_OwnershipCategory_08"
        RENTED = "HomeInsurance_Questions_PolicyDetails_OwnershipCategory_rented"
    driver.find_element(By.ID, OWNERSHIP_DICT.MORTGAGED.value).click()

    # Policy Type
    class POLICY_TYPE_DICT(Enum):
        BUILDINGS_AND_CONTENTS = "HomeInsurance_Questions_PolicyDetails_CoverType_BC"
        BUILDINGS = "HomeInsurance_Questions_PolicyDetails_CoverType_BO"
        CONTENTS = "HomeInsurance_Questions_PolicyDetails_CoverType_CO"
    driver.find_element(By.ID, POLICY_TYPE_DICT.BUILDINGS_AND_CONTENTS.value).click()

    # Start Date
    Select(driver.find_element(By.ID, "HomeInsurance_Questions_PolicyDetails_PolicyStartDate")).select_by_index(1)


def page_2(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Questions_Buildings")))

    # Home type
    class HOME_TYPE(Enum):
        HOUSE = "HomeInsurance_Questions_Buildings_YourHouse_house"
        BUNGALOW = "HomeInsurance_Questions_Buildings_YourHouse_bungalow"
        TOWNHOUSE = "HomeInsurance_Questions_Buildings_YourHouse_townhouse"
        FLAT = "HomeInsurance_Questions_Buildings_YourHouse_flat"
        MAISONETTE = "HomeInsurance_Questions_Buildings_YourHouse_maisonette"
        ROOM_ONLY_OR_BEDSIT = "HomeInsurance_Questions_Buildings_YourHouse_room"
    driver.find_element(By.ID, HOME_TYPE.HOUSE.value).click()

    # House type
    class HOUSE_TYPE(Enum):
        MID_TERRACED = "HomeInsurance_Questions_Buildings_YourHouse_House_19"
        END_TERRACED = "HomeInsurance_Questions_Buildings_YourHouse_House_18"
        SEMI_DETACHED = "HomeInsurance_Questions_Buildings_YourHouse_House_10"
        DETACHED = "HomeInsurance_Questions_Buildings_YourHouse_House_02"
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "YourHouse_House")))
    driver.find_element(By.ID, HOUSE_TYPE.MID_TERRACED.value).click()

    # Build year
    build_year = 1930
    driver.find_element(By.ID, "HomeInsurance_Questions_Buildings_YearBuilt").send_keys(build_year)

    # Smoke detectors
    class SMOKE_DETECTORS(Enum):
        YES = "HomeInsurance_Questions_Buildings_HasSmokeDetectors_yes"
        NO = "HomeInsurance_Questions_Buildings_HasSmokeDetectors_no"
    driver.find_element(By.ID, SMOKE_DETECTORS.YES.value).click()

    # Rooms
    num_bedrooms = ["1","2","3","4","5","More"]
    num_living_rooms = ["0", "1","2","3","4","More"]
    num_bathrooms = ["0", "1","2","3","4","More"]
    num_other_rooms = ["0", "1","2","3","4","More"]
    driver.find_element(By.ID, "HomeInsurance_Questions_Buildings_NumOfBedrooms_" + num_bedrooms[1]).click()
    driver.find_element(By.ID, "HomeInsurance_Questions_Buildings_NumOfReceptions_" + num_living_rooms[1]).click()
    driver.find_element(By.ID, "HomeInsurance_Questions_Buildings_NumOfBathrooms_" + num_bathrooms[2]).click()
    driver.find_element(By.ID, "HomeInsurance_Questions_Buildings_NumOfOtherRooms_" + num_other_rooms[1]).click()

    # Walls
    class WALLS(Enum):
        STONE = "HomeInsurance_Questions_Buildings_ConstructionWalls_16"
        BRICK = "HomeInsurance_Questions_Buildings_ConstructionWalls_02"
        CONCRETE = "HomeInsurance_Questions_Buildings_ConstructionWalls_05"
        OTHER = "HomeInsurance_Questions_Buildings_ConstructionWalls_Other"
    driver.find_element(By.ID, WALLS.STONE.value).click()

    # Roof material
    class ROOF_MATERIAL(Enum):
        SLATE = "HomeInsurance_Questions_Buildings_ConstructionRoof_10"
        TILE = "HomeInsurance_Questions_Buildings_ConstructionRoof_15"
        CONCRETE = "HomeInsurance_Questions_Buildings_ConstructionRoof_02"
        OTHER = "HomeInsurance_Questions_Buildings_ConstructionRoof_Other"
    driver.find_element(By.ID, ROOF_MATERIAL.SLATE.value).click()

    # Roof flatness
    ROOF_FLATNESS = {
        "None": "HomeInsurance_Questions_Buildings_FlatRoofCoverage_none",
        "10%": "HomeInsurance_Questions_Buildings_FlatRoofCoverage_10",
        "20%": "HomeInsurance_Questions_Buildings_FlatRoofCoverage_20",
        "30%": "HomeInsurance_Questions_Buildings_FlatRoofCoverage_30",
        "40%": "HomeInsurance_Questions_Buildings_FlatRoofCoverage_40",
        "50%": "HomeInsurance_Questions_Buildings_FlatRoofCoverage_50",
        "More": "HomeInsurance_Questions_Buildings_FlatRoofCoverage_over 50",
    }
    driver.find_element(By.ID, ROOF_FLATNESS['None']).click()

    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "RICSLogo")))

    # Tall trees
    class TALL_TREES(Enum):
        YES = "HomeInsurance_Questions_Buildings_TallTrees_yes"
        NO = "HomeInsurance_Questions_Buildings_TallTrees_no"
    driver.find_element(By.ID, TALL_TREES.YES.value).click()

    # Near water
    class NEAR_WATER(Enum):
        YES = "HomeInsurance_Questions_Buildings_Water_yes"
        NO = "HomeInsurance_Questions_Buildings_Water_no"
    driver.find_element(By.ID, NEAR_WATER.NO.value).click()

    # Ongoing building work
    class ONGOING_BUILDING_WORK(Enum):
        YES = "HomeInsurance_Questions_Buildings_HasOngoingBuildingWork_yes"
        NO = "HomeInsurance_Questions_Buildings_HasOngoingBuildingWork_no"
    driver.find_element(By.ID, ONGOING_BUILDING_WORK.NO.value).click()

    # Buildings excess
    EXCESS_OPTIONS = ["0","50","100","150","200","250","300","350","400","450","500"]
    excess = EXCESS_OPTIONS[4]
    excess_select = Select(driver.find_element(By.ID, "HomeInsurance_Questions_Buildings_BuildingsVoluntaryExcess"))
    excess_select.select_by_value(excess)

    # Buildings AD
    class BUILDINGS_AD(Enum):
        YES = "HomeInsurance_Questions_Buildings_AccidentalDamage_yes"
        NO = "HomeInsurance_Questions_Buildings_AccidentalDamage_no"
    driver.find_element(By.ID, BUILDINGS_AD.YES.value).click()

    # Home emergency
    class HOME_EMERGENCY(Enum):
        YES = "HomeInsurance_Questions_Buildings_HomeEmergency_yes"
        NO = "HomeInsurance_Questions_Buildings_HomeEmergency_no"
    driver.find_element(By.ID, HOME_EMERGENCY.YES.value).click()

    # Legal assistance
    class LEGAL_ASSISTANCE(Enum):
        YES = "HomeInsurance_Questions_Buildings_LegalAssistance_yes"
        NO = "HomeInsurance_Questions_Buildings_LegalAssistance_no"
    driver.find_element(By.ID, LEGAL_ASSISTANCE.YES.value).click()

    # Replacement Locks and Keys
    class REPLACEMENT_LOCKS_AND_KEYS(Enum):
        YES = "HomeInsurance_Questions_Buildings_ReplacementLocks_yes"
        NO = "HomeInsurance_Questions_Buildings_ReplacementLocks_no"
    driver.find_element(By.ID, REPLACEMENT_LOCKS_AND_KEYS.NO.value).click()


def page_3(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Questions_Locks")))

    # Lock type
    class LOCK_TYPE(Enum):
        RIM_AUTO_DEADLATCH = "HomeInsurance_Questions_Locks_MainLockTypes_RimAutoDeadLatch"
        MULTI_POINT_SYSTEM = "HomeInsurance_Questions_Locks_MainLockTypes_MultiPointSystem"
        FIVE_LEVER = "HomeInsurance_Questions_Locks_MainLockTypes_FiveLever"
        OTHER = "HomeInsurance_Questions_Locks_MainLockTypes_OtherLock"
    driver.find_element(By.ID, LOCK_TYPE.RIM_AUTO_DEADLATCH.value).click()

    # Sliding lock doors
    class SLIDING_LOCK_DOORS(Enum):
        YES = "HomeInsurance_Questions_Locks_HasSlidingLock_true"
        NO = "HomeInsurance_Questions_Locks_HasSlidingLock_false"
    driver.find_element(By.ID, SLIDING_LOCK_DOORS.NO.value).click()

    # Other doors
    class OTHER_DOORS(Enum):
        YES = "HomeInsurance_Questions_Locks_HasOtherLocks_other-true"
        NO = "HomeInsurance_Questions_Locks_HasOtherLocks_other-false"
    driver.find_element(By.ID, OTHER_DOORS.NO.value).click()

    # Window locks
    class WINDOW_LOCKS(Enum):
        YES = "HomeInsurance_Questions_Locks_HasWindowLocks_yes"
        NO = "HomeInsurance_Questions_Locks_HasWindowLocks_no"
    driver.find_element(By.ID, WINDOW_LOCKS.YES.value).click()

    # Neighbourhood watch
    class NEIGHBOURHOOD_WATCH(Enum):
        YES = "HomeInsurance_Questions_Locks_HasNeighbourhoodWatch_yes"
        NO = "HomeInsurance_Questions_Locks_HasNeighbourhoodWatch_no"
    driver.find_element(By.ID, NEIGHBOURHOOD_WATCH.YES.value).click()

    # Burglar alarm
    class BURGLAR_ALARM(Enum):
        YES = "HomeInsurance_Questions_Locks_AlarmFitted_yes"
        NO = "HomeInsurance_Questions_Locks_AlarmFitted_no"
    driver.find_element(By.ID, BURGLAR_ALARM.YES.value).click()

    class BURGLAR_ALARM_PROFESSIONALLY_FITTED(Enum):
        YES = "HomeInsurance_Questions_Locks_AlarmProfessionalFittedAndApproved_YES"
        YES_PROFESSIONALLY = "HomeInsurance_Questions_Locks_AlarmProfessionalFittedAndApproved_YES_PROFESSIONALLY"
        NO = "HomeInsurance_Questions_Locks_AlarmProfessionalFittedAndApproved_NO"
    driver.find_element(By.ID, BURGLAR_ALARM_PROFESSIONALLY_FITTED.YES_PROFESSIONALLY.value).click()


def page_4(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Questions_Contents")))

    # Contents cover
    # CONTENTS_COVER_OPTIONS = range(15000, 201000, 1000)
    contents_cover = 20000        # Between 15000 and 200000
    contents_cover_select = Select(driver.find_element(By.ID, "HomeInsurance_Questions_Contents_ReplacementCost"))
    contents_cover_select.select_by_value(str(contents_cover))

    # High risk items cover
    HIGH_RISK_COVER_LEVELS = [int(contents_cover * x/100) for x in range(10,51,5)]
    high_risk_cover = HIGH_RISK_COVER_LEVELS[2]
    high_risk_cover_select = Select(driver.find_element(By.ID, "HomeInsurance_Questions_Contents_TotalValueHighRiskItems"))
    high_risk_cover_select.select_by_value(str(high_risk_cover))

    # Valuable items
    class VALUABLE_ITEMS(Enum):
        YES = "HomeInsurance_Questions_Contents_SpecifiedItems_yes"
        NO = "HomeInsurance_Questions_Contents_SpecifiedItems_no"
    driver.find_element(By.ID, VALUABLE_ITEMS.NO.value).click()

    # Bicycles
    class BICYCLES(Enum):
        YES = "HomeInsurance_Questions_Contents_CoverBicycles_yes"
        NO = "HomeInsurance_Questions_Contents_CoverBicycles_no"
    driver.find_element(By.ID, BICYCLES.NO.value).click()

    # Contents excess
    EXCESS_OPTIONS = ["0","50","100","150","200","250","300","350","400","450","500"]
    excess = EXCESS_OPTIONS[4]
    excess_select = Select(driver.find_element(By.ID, "HomeInsurance_Questions_Contents_ContentsVoluntaryExcess"))
    excess_select.select_by_value(excess)

    # Out of home
    class OUT_OF_HOME(Enum):
        YES = "HomeInsurance_Questions_Contents_CoverPersonalPossessions_yes"
        NO = "HomeInsurance_Questions_Contents_CoverPersonalPossessions_no"
    driver.find_element(By.ID, OUT_OF_HOME.NO.value).click()

    # Contents AD
    class CONTENTS_AD(Enum):
        YES = "HomeInsurance_Questions_Contents_CoverAccidentalDamage_yes"
        NO = "HomeInsurance_Questions_Contents_CoverAccidentalDamage_no"
    driver.find_element(By.ID, CONTENTS_AD.YES.value).click()

    # Freezer cover
    class FREEZER_COVER(Enum):
        YES = "HomeInsurance_Questions_Contents_FreezerCover_yes"
        NO = "HomeInsurance_Questions_Contents_FreezerCover_no"
    driver.find_element(By.ID, FREEZER_COVER.NO.value).click()


def page_5(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Questions_PersonalDetails")))

    # Date of birth
    day, month, year = 1, 0, 1980
    Select(driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_PriPolholdDateOfBirth_Day")).select_by_value(str(day))
    Select(driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_PriPolholdDateOfBirth_Month")).select_by_value(str(month))
    Select(driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_PriPolholdDateOfBirth_Year")).select_by_value(str(year))

    # Marital status
    class MARITAL_STATUS(Enum):
        MARRIED = "M"
        CIVIL_PARTNERED = "B"
        SINGLE = "S"
        COMMON_LAW_PARTNERED_COHABITING = "P"
        DIVORCED_DISSOLVED = "D"
        SEPARATED = "A"
        WIDOWED_SURVIVING_CIVIL_PARTNER = "W"
    Select(driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_PriPolholdMaritalStatus")).select_by_value(MARITAL_STATUS.SINGLE.value)

    # Employment status
    class EMPLOYMENT_STATUS(Enum):
        EMPLOYED_FULLTIME = "EF"
        EMPLOYED_PARTTIME = "EP"
        UNEMPLOYED = "U"
        SELF_EMPLOYED = "S"
        HOUSEPERSON = "H"
        IN_EDUCATION = "F"
        RETIRED = "R"
        DISABLED_OR_ILL = "N"
    Select(driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_PriPolholdEmploymentStatus")).select_by_value(EMPLOYMENT_STATUS.EMPLOYED_FULLTIME.value)

    # Job title
    job_title = "Software Engineer"
    driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_PriPolholdMainJobInfo_Title").send_keys(job_title, Keys.ENTER)

    # Industry
    industry = "Insurance"
    driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_PriPolholdMainJobInfo_Industry").send_keys(industry, Keys.ENTER)

    # Secondary employment
    class SECONDARY_EMPLOYMENT(Enum):
        YES = "HomeInsurance_Questions_PersonalDetails_PriPolholdHasSecondaryEmployment_yes"
        NO = "HomeInsurance_Questions_PersonalDetails_PriPolholdHasSecondaryEmployment_no"
    driver.find_element(By.ID, SECONDARY_EMPLOYMENT.NO.value).click()

    # Joint policy holder
    class JOINT_POLICY_HOLDER(Enum):
        NO = "HomeInsurance_Questions_PersonalDetails_JointPolicyholderType_JustMyself"
        YES = "HomeInsurance_Questions_PersonalDetails_JointPolicyholderType_MyselfAndAnother"
    driver.find_element(By.ID, JOINT_POLICY_HOLDER.NO.value).click()

    # Is main home
    class IS_MAIN_HOME(Enum):
        PERMANENT_HOME = "HomeInsurance_Questions_PersonalDetails_Occupancy_PH"
        WEEKEND_ONLY = "HomeInsurance_Questions_PersonalDetails_Occupancy_WE"
        WEEKDAY_ONLY = "HomeInsurance_Questions_PersonalDetails_Occupancy_WD"
        HOLIDAY_HOME = "HomeInsurance_Questions_PersonalDetails_Occupancy_HH"
        UNOCCUPIED = "HomeInsurance_Questions_PersonalDetails_Occupancy_UN"
    driver.find_element(By.ID, IS_MAIN_HOME.PERMANENT_HOME.value).click()

    # Empty for 30 days
    class EMPTY_FOR_THIRTY_DAYS(Enum):
        YES = "HomeInsurance_Questions_PersonalDetails_MoreThan30Days_YES"
        NO = "HomeInsurance_Questions_PersonalDetails_MoreThan30Days_no"
    driver.find_element(By.ID, EMPTY_FOR_THIRTY_DAYS.NO.value).click()

    # When at home
    class WHEN_AT_HOME(Enum):
        NIGHT_AND_DAY = "HomeInsurance_Questions_PersonalDetails_HomeOccupancyType_DayAndNight"
        DAY = "HomeInsurance_Questions_PersonalDetails_HomeOccupancyType_Day"
        NIGHT = "HomeInsurance_Questions_PersonalDetails_HomeOccupancyType_Night"
    driver.find_element(By.ID, WHEN_AT_HOME.NIGHT_AND_DAY.value).click()

    # How long lived
    lived_here_for = 2
    driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_YearsOccupied").send_keys(str(lived_here_for))

    # Housemates
    class HOUSEMATES(Enum):
        POLICYHOLDER = "HomeInsurance_Questions_PersonalDetails_HomeResidentsGroup_H"
        POLICYHOLDER_AND_FAMILY = "HomeInsurance_Questions_PersonalDetails_HomeResidentsGroup_Y"
        POLICYHOLDER_AND_OTHER = "HomeInsurance_Questions_PersonalDetails_HomeResidentsGroup_other"
    housemates = HOUSEMATES.POLICYHOLDER_AND_FAMILY
    driver.find_element(By.ID, housemates.value).click()

    if housemates != HOUSEMATES.POLICYHOLDER:
        num_adults = ["1","2","3","4","5","More"]
        num_children = ["0", "1","2","3","4","More"]
        driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_Adults_" + num_adults[1]).click()
        driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_Children_" + num_children[0]).click()

    # Any cats or dogs
    class CATS_OR_DOGS(Enum):
        YES = "HomeInsurance_Questions_PersonalDetails_CatsAndDogs_yes"
        NO = "HomeInsurance_Questions_PersonalDetails_CatsAndDogs_no"
    driver.find_element(By.ID, CATS_OR_DOGS.NO.value).click()

    # Any smokers
    class SMOKERS(Enum):
        YES = "HomeInsurance_Questions_PersonalDetails_AnySmokers_yes"
        NO = "HomeInsurance_Questions_PersonalDetails_AnySmokers_no"
    driver.find_element(By.ID, SMOKERS.NO.value).click()

    # Business purposes
    class BUSINESS_PURPOSES(Enum):
        NONE = "HomeInsurance_Questions_PersonalDetails_BuildingUsage_N"
        REGULAR = "HomeInsurance_Questions_PersonalDetails_BuildingUsage_V"
        CLERICAL = "HomeInsurance_Questions_PersonalDetails_BuildingUsage_C"
        OTHER = "HomeInsurance_Questions_PersonalDetails_BuildingUsage_O"
    driver.find_element(By.ID, BUSINESS_PURPOSES.NONE.value).click()

    # Claims in past five years
    class MADE_CLAIM(Enum):
        YES = "HomeInsurance_Questions_PersonalDetails_NoClaims_yes"
        NO = "HomeInsurance_Questions_PersonalDetails_NoClaims_no"
    driver.find_element(By.ID, MADE_CLAIM.NO.value).click()

    ncb_buildings = ["0","1","2","3","4","More"]
    ncb_contents = ["0","1","2","3","4","More"]
    driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_BuildingsNoClaims_" + ncb_buildings[2]).click()
    driver.find_element(By.ID, "HomeInsurance_Questions_PersonalDetails_ContentsNoClaims_" + ncb_contents[3]).click()


def page_6(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Questions_Contact")))

    # Contact email
    contact_email = "bobby@fucko.com"
    driver.find_element(By.ID, "HomeInsurance_Questions_Contact_EmailQuestion").send_keys(contact_email)

    # Phone number
    phone_number = "07777777777"
    driver.find_element(By.ID, "HomeInsurance_Questions_Contact_Telephone").send_keys(phone_number)

    # Payment frequency
    class PAYMENT_FREQUENCY(Enum):
        MONTHLY = "HomeInsurance_Questions_Contact_PaymentFrequency_M"
        ANNUAL = "HomeInsurance_Questions_Contact_PaymentFrequency_A"
    driver.find_element(By.ID, PAYMENT_FREQUENCY.ANNUAL.value).click()

    # Happy to be contacted
    class CONTACT_ME(Enum):
        YES = "HomeInsurance_Questions_Contact_PartnerContact_yes"
        NO = "HomeInsurance_Questions_Contact_PartnerContact_no"
    driver.find_element(By.ID, CONTACT_ME.NO.value).click()


def page_7(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "HomeInsurance_Summary")))

    # Confirm details
    driver.find_element(By.ID, "HomeInsurance_Summary_TermsQuestion").click()


def results_page(driver: webdriver.Chrome):
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "Interstitial")))
    WebDriverWait(driver, 30).until(EC.invisibility_of_element((By.ID, "Interstitial")))

    # Get prices
    quotes: WebElement = driver.find_element(By.CLASS_NAME, "_1fZCO2opVDhd5gTHBgqf8y")
    cards: List[WebElement] = quotes.find_elements(By.CLASS_NAME, "Card")
    with open("latest_prices.csv", "w") as f:
        for card in cards:
            pounds = card.find_element(By.CLASS_NAME, "_1iLOZyp3tWfBXAl1TUwuOB").text
            pennies = card.find_element(By.CLASS_NAME, "_1cagmbrfcpQJ55dkTgABS").text

            provider_image: WebElement = card.find_element(By.CLASS_NAME, "BrandLogo__image")
            provider_name = provider_image.get_property("alt")

            print(pounds + pennies, "-", provider_name)
            f.write(pounds+pennies + "\t" + provider_name + "\n")




if __name__ == "__main__":
    main()
